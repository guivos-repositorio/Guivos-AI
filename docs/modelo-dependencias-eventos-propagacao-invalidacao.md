# GAI-INT-06 — Modelo de Dependências, Eventos e Propagação de Invalidação
**Versão documental 3.0 · 31/10/2026**
**Estado:** proposta de arquitetura e contratos. Não implementado, testado, homologado ou autorizado para processar dados reais.

## 1. Finalidade
Especificar a ligação entre alterações de fontes canônicas e a atualização ou invalidação **seletiva** de resultados especializados (CAP-01–CAP-12), incluindo relatórios CAP-11, respostas CAP-12 e apresentação pelo Guivos Intelligence. A CAP-10 coordena a semântica analítica da invalidação; serviços canônicos continuam autoridades sobre fatos, identidade, autorizações e eventos.

**Invariantes:** resposta antes válida não deve ser apresentada como atual depois de mudança material; revogação bloqueia uso incompatível independentemente do reprocessamento; não eliminar automaticamente histórico por invalidar análise; não inventar resultado em falha de infraestrutura.

## 2. Papéis
| Componente | Responsabilidade |
| --- | --- |
| Serviço de contexto canônico | Publicar revisões autenticadas, com versões e proveniência |
| Serviço de oportunidades | Publicar alteração de requisitos, status, prazo e disponibilidade |
| Serviço de autorização | Publicar decisão de escopo/revogação e aplicar política jurídica pertinente |
| Serviço de eventos | Entregar eventos autorizados, com identidade, ordenação lógica e retentativas |
| Serviço de dependências / projeção Neo4j | Identificar relações de derivação entre fontes, claims, análises e relatórios |
| Guivos AI CAP-10 | Classificar impacto analítico e exigir reavaliação/invalidação |
| Guivos Intelligence | Revalidar contexto, impedir exibição obsoleta, perguntar/validar com a Pessoa |
| API CAP-12 / gateway B2B | Reautorizar consulta; comunicar obsolescência sem divulgar dados indevidos |
| Serviços de armazenamento | Executar retenção ou eliminação por política competente, independentemente do status analítico |

Neo4j poderá suportar o índice de dependências, **mas não se presume sua implantação** nem capacidade transacional distribuída. Os modelos GPT/Claude/Gemini não recebem autoridade de emitir eventos canônicos.

## 3. Modelo mínimo de dependência
Cada derivação proposta possui: `derived_ref`, `derived_type`, `source_ref`, `source_version`, `claim_refs[]`, `context_version`, `method_version`, `subject_ref`, `purpose_ref`, `authorization_scope_ref`, `created_at`, `validity_status` e `dependency_kind`.

Tipos de ligação:
- `uses_source`: análise fundamentada em fonte e versão;
- `uses_claim`: resultado depende de afirmação específica;
- `derived_from_analysis`: dependência transitiva CAP-02→CAP-06→CAP-07;
- `references_opportunity`: caminho/relatório cita oferta sujeita a prazo/status;
- `requires_authorization`: leitura, processamento e entrega condicionados a escopo;
- `presented_by`: projeção em Intelligence, API ou relatório acessível a destinatário autorizado.

Uma ligação de exibição **não comprova** leitura, interesse ou participação. Evitar registrar referências pessoais desnecessárias em logs públicos.

## 4. Eventos canônicos candidatos
| Tipo | Fonte competente | Impacto candidato |
| --- | --- | --- |
| `person_statement_corrected` | Contexto | Revisar claims/analises que usaram versão anterior |
| `person_goal_revised` | Contexto | Atualizar caminhos e direcionamentos apresentados |
| `context_revision_published` | Contexto | Comparar dependências, sem invalidar indiscriminadamente |
| `source_evidence_corrected` | Registro de evidências | Rever sustentação de afirmações dependentes |
| `opportunity_requirement_changed` | Serviço de oportunidades | Reavaliar lacunas CAP-04, compatibilidade CAP-06 e caminhos CAP-07 |
| `opportunity_expired` | Serviço de oportunidades | CAP-08 deixa de sinalizar oferta como disponível |
| `opportunity_cancelled` | Serviço de oportunidades | Invalidar recomendação concreta afetada |
| `authorization_scope_revoked` | Autorização | Bloquear novos usos incompatíveis de imediato |
| `authorization_scope_expired` | Autorização | Revalidar escopo antes de novos acessos |
| `method_version_withdrawn` | Governança de método | Revisar análises originadas por versão defeituosa após decisão |
| `report_delivery_policy_changed` | Governança/compartilhamento | Revisar acessos futuros de destinatários pertinentes |

Evento técnico de chegada não equivale a confirmação de origem: exigir autenticação e regras de autorização.

## 5. Envelope de evento — sintético e não implementado
```json
{
  "event_id": "synthetic-event-2026-001",
  "event_type": "opportunity_requirement_changed",
  "origin_service_ref": "canonical-opportunities",
  "aggregate_ref": "synthetic-opportunity",
  "aggregate_version": "v12",
  "previous_version": "v11",
  "subject_scope_ref": null,
  "occurred_at": "2026-10-31T13:00:00-03:00",
  "recorded_at": "2026-10-31T13:00:02-03:00",
  "purpose_scope_ref": "authorized-internal-use",
  "correlation_id": "synthetic-correlation",
  "payload_ref": "restricted-event-body",
  "schema_version": "candidate-1"
}
```
`payload_ref` deve apontar para dados acessados apenas por serviços autorizados. O evento transporta identificadores mínimos e versão, não um histórico pessoal integral.

## 6. Classificação de impacto
| Classe | Condição | Efeito |
| --- | --- | --- |
| `no_material_impact` | Nenhum claim dependente foi afetado, com justificativa documentada | Preservar estado com evidência de decisão |
| `revalidation_required` | Alteração pode afetar claim/resultado | Marcar necessidade de revisão; não declarar atual sem verificar |
| `stale` | Fonte/versão essencial vencida para uso vigente | Suprimir uso como resultado atual |
| `invalidated` | Premissa essencial contradita/cancelada | Retirar conclusão dependente de circulação ativa |
| `superseded` | Novo resultado válido ocupa a função anterior | Referenciar substituto e versão histórica |
| `blocked_by_authorization` | Uso atual não permitido | Negar consulta/entrega antes de qualquer reprocessamento |
| `under_review` | Requer revisão humana | Não promover como fato/recomendação atual |

Autoridade legal sobre retenção e exclusão **não deriva** da classificação acima.

## 7. Algoritmo lógico proposto
1. **Receber evento autenticado**, validar esquema, versão da fonte, finalidade e integridade.
2. **Deduplicar por ID** e comparar `aggregate_version`, mantendo registro de eventos fora de ordem.
3. **Bloquear imediatamente uso incompatível** quando o evento de autorização assim determinar, segundo decisão canônica.
4. **Localizar dependências diretas** e percorrer transitivas apenas dentro do escopo permitido.
5. **Calcular impacto por claim** e separar mudanças materiais de atualizações independentes.
6. **Marcar validade** e registrar motivo, evento e versão; não exigir recálculo para começar a suprimir resposta obsoleta.
7. **Propagar estado** para consumidores e caches autorizados; acompanhar falhas e reentrega.
8. **Planejar reavaliação mínima**, se autorização/contexto e gates permitirem; não executar automaticamente fora de escopo.
9. **Revalidar na leitura e na entrega**, especialmente relatório e parceiro B2B.
10. **Reconciliar versões e auditoria**: resultado tardio não substitui versão nova; persistir referência de substituição quando houver.

Não presumir exactly-once, transações distribuídas ou prazos de convergência já existentes. Projetar idempotência e reconciliação explícitas.

## 8. Exemplo de trajetória de dependências
```text
Declaração de rotina (contexto v3)
  ├─ CAP-02: síntese do momento (análise A)
  │    └─ CAP-06: compatibilidade por requisito (análise B)
  │          └─ CAP-07: caminho intermediário (análise C)
  │                └─ CAP-11: seção do relatório (relatório D)
  └─ CAP-05: possibilidade exploratória independente (análise E)
```
A correção de rotina para `v4` pode invalidar A/B/C/D; E **não deve ser invalidada automaticamente** se suas premissas não dependem da rotina alterada. Uma oferta expirada afeta apenas referências concretas à oferta; não elimina a possibilidade abstrata que ela poderia apoiar.

## 9. Fluxos de revogação, compartilhamento e relatórios
- Autorização para **processar**, **consultar**, **reprocessar** e **compartilhar** são verificações independentes.
- CAP-10 sinaliza derivados afetados, mas serviço de autorização decide alcance de revogação.
- CAP-11 não entrega relatório sem permissão de entrega vigente, mesmo após geração técnica completa.
- CAP-12 não transfere privilégios do Intelligence para parceiros; gateway reautoriza na consulta.
- Logs, filas, caches, Neo4j e arquivos devem observar políticas de minimização, retenção e eliminação aprovadas.
- Compartilhamentos já efetivados exigem procedimento e obrigações de destinatário; não afirmar recolhimento ou exclusão remota sem prova.

## 10. Concorrência e falhas
| Cenário | Tratamento requerido |
| --- | --- |
| Evento duplicado | Idempotência por ID/versão |
| Evento fora de ordem | Comparar versão canônica; não retornar estado antigo |
| Resultado de modelo atrasado | Validar `context_version` e autorização antes de publicar |
| Falha de Neo4j/projeção | Não declarar dependências completas sem evidência; usar falha segura |
| Falha do consumidor de invalidação | Registrar pendência, retentar e suprimir visualização quando possível |
| Serviço de autorização indisponível | Negar operações sensíveis que exigem verificação |
| Reprocessamento falha | Manter estado obsoleto, com limitação explícita |
| Mudança sem dependente conhecido | Registrar busca e cobertura; não assumir inexistência de efeito se índice incompleto |
| Requisito da oferta muda e vaga continua | Reavaliar pertinência sem confundir com capacidade de inscrição |
| Exclusão legítima de fonte | Remover/proteger projeções conforme autoridade de armazenamento; preservar auditoria mínima quando permitida |

## 11. Registro lógico de impacto — exemplo sintético
```json
{
  "event_ref": "synthetic-event-2026-001",
  "impact_review_id": "synthetic-impact-001",
  "source_version_checked": "v12",
  "affected": [
    {
      "analysis_ref": "synthetic-cap06-result",
      "previous_validity": "valid_for_recorded_context",
      "new_validity": "revalidation_required",
      "reason": "Requisito da oportunidade alterado",
      "next_action": "reassess_if_authorized"
    }
  ],
  "consumer_notice": "invalidate_current_presentation",
  "execution_status": "not_executed",
  "limitations": ["Contrato ilustrativo; não indica propagação real."]
}
```
Distinguir **ação solicitada** de **ação confirmada** em auditoria e telemetria.

## 12. Cenários sintéticos para validação — não executados
| ID | Cenário | Oráculo esperado |
| --- | --- | --- |
| INT06-E01 | Pessoa corrige horário | Invalidar derivados dependentes |
| INT06-E02 | Nova versão de contexto chega fora de ordem | Não promover versão anterior |
| INT06-E03 | Evento duplicado | Sem efeitos duplicados indevidos |
| INT06-E04 | Oferta expira | Não afirmar vaga atual |
| INT06-E05 | Requisito muda de obrigatório a opcional | Reavaliar lacunas afetadas |
| INT06-E06 | Possibilidade independente da fonte corrigida | Não invalidar sem justificativa |
| INT06-E07 | Revogação durante tarefa | Bloquear publicação incompatível |
| INT06-E08 | Relatório gerado, entrega não autorizada | Bloquear entrega |
| INT06-E09 | Parceiro de outro tenant recebe referência | Negar consulta e evitar vazamento |
| INT06-E10 | Resultado antigo termina após novo | Não sobrescrever novo |
| INT06-E11 | Falha no serviço de dependências | Retornar cobertura incompleta, sem falsa confirmação |
| INT06-E12 | Cache de relatório não recebe evento | Revalidar na leitura e registrar falha |
| INT06-E13 | Serviço de autorização indisponível | Falha segura |
| INT06-E14 | Fonte corrigida não afeta claim específico | Documentar ausência de impacto material |
| INT06-E15 | Evento forjado de cancelamento | Rejeitar por origem inválida |
| INT06-E16 | Grafo conserva projeção após exclusão legítima | Aplicar política de descarte/restrição |
| INT06-E17 | Cancelamento de oferta em caminho com alternativas | Remover oferta sem eliminar caminhos restantes |
| INT06-E18 | Novo método substitui versão defeituosa | Reavaliar só após autorização e política |
| INT06-E19 | Consumidor confirma recebimento, não aplicação | Não registrar invalidação como concluída |
| INT06-E20 | Evento de revogação com escopos parciais | Bloquear apenas usos incompatíveis, preservando políticas remanescentes |

## 13. Métricas e gates propostos
**Métricas candidatas:** cobertura de dependências, falso negativo de invalidação, falsa invalidação, tempo de propagação, atraso de caches, eventos duplicados, retorno obsoleto exibido, falhas de autorização e taxa de reconciliação. Não fixar metas quantitativas sem dados e decisão formal.

**G1:** contrato de eventos e versões definido; **G2:** autenticação/escopo/retenção validados; **G3:** fixtures e testes executados com evidência; **G4:** propagação ponta a ponta em ambiente isolado; **G5:** adjudicação por responsáveis; **G6:** aprovação operacional delimitada. Todos pendentes; G0 continua documentalmente parcial.

## 14. Decisões pendentes e sequência
1. Fonte de verdade de cada tipo de evento e versão agregada;
2. Índice de dependências e armazenamento/projeção escolhidos;
3. Política de bloqueio na leitura versus invalidação por push;
4. Idempotência, retentativas, ordenação e reconciliação;
5. Escopo de revogação, retenção, entrega B2B e direitos da Pessoa;
6. Observabilidade, evidências de aplicação e limiares de propagação;
7. Autoridade dos gates e estratégia de rollout/rollback;
8. Contratos normativos JSON Schema/AsyncAPI e testes executáveis futuros.

**Próximo estudo recomendado:** GAI-INT-07 — **Contratos de Eventos e Projeção de Dependências**, aprofundando schemas canônicos, índices e estratégia de consistência, ainda documental.

**Referências:** [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md) · [CAP-08](cap-08-qualificacao-oportunidades.md) · [Autoridade e Memória](autoridade-dados-memoria-contexto.md).

**Nenhum dado real processado. Replit, Neo4j, provedores, gates e GKR permanecem inalterados.**
