# GAI-CAP-10 — Reavaliação e Invalidação de Análises
**Especificação de capacidade · Versão documental 2.2 · 31/10/2026**
**Estado:** conceituada. Contratos, mecanismos e cenários são propostas; nada foi implementado, homologado ou autorizado para produção.

## 1. Propósito
Garantir que conclusões, sínteses, possibilidades, lacunas, caminhos, oportunidades e relatórios **não continuem apresentados como atuais** quando suas premissas forem alteradas, corrigidas, expirarem ou deixarem de estar autorizadas.

A CAP-10 administra o **ciclo de validade das análises derivadas**, não substitui os sistemas canônicos de fatos, identidade, autorização ou publicação de oportunidades. Ela não modifica o histórico original da Pessoa, não elimina automaticamente registros legais sujeitos à retenção e não decide se o objetivo da Pessoa é correto.

**Princípio:** uma análise válida para determinado contexto, método e data não é necessariamente válida após uma mudança. A mudança deve ser rastreada até os resultados que dela dependem.

## 2. Autoridades e responsabilidades
| Componente | Papel |
| --- | --- |
| Serviços canônicos do ecossistema | Origem autorizada de registros, correções, revisões, revogações e eventos |
| Guivos AI — CAP-10 | Identifica dependências, classifica impacto, sinaliza obsolescência e solicita reavaliação analítica |
| Guivos AI — CAP-03/09 | Fundamentação por afirmação; reconhecimento de conflito e obsolescência epistêmica |
| Guivos Intelligence | Orquestra nova análise, impede exibição de resultado vencido e solicita validação humana |
| Serviço de autorização | Decide o acesso vigente, finalidade, retenção e efeitos de revogação |
| Neo4j/memória contextual | Pode projetar relações de dependência, sem ser autoridade universal dos dados |
| GPT/Claude/Gemini | Executam tarefas sob adaptadores; não autorizam acesso nem modificam fatos canônicos |

A Guivos AI não deve reexecutar modelos automaticamente com dados pessoais se a finalidade ou autorização não permitir.

## 3. Objeto versionável da análise
Cada resultado derivado precisará carregar, no contrato definitivo:
- `analysis_id`, `capability_id`, `method_version`, `analysis_version`;
- `subject_ref`, `purpose`, `authorized_scope_ref` e destinatários permitidos;
- `context_version`, `source_refs`, `source_versions` e claims dependentes;
- `as_of`, `generated_at`, `valid_until` quando aplicável;
- estados de validade e motivo da alteração;
- dependências de requisitos, ofertas, possibilidades e eventuais outros resultados;
- referências de substituição, revisão humana e evidência de reavaliação;
- regra de retenção/eliminação, sem inserir informações sensíveis no log público.

**Graus de dependência:** direta (a conclusão usa uma fonte), transitiva (usa outra análise), temporal (exige atualização), de autorização (requer escopo válido) e de método (depende de versão de processamento).

## 4. Eventos que podem disparar revisão
| Evento | Exemplo | Efeito candidato |
| --- | --- | --- |
| Correção de fato | Pessoa corrige o horário informado | Invalidar claims e caminhos afetados |
| Nova versão contextual | Rotina, disponibilidade ou preferência mudou | Reavaliar análise do momento e dependentes |
| Alteração de objetivo | Pessoa suspende uma possibilidade | Não continuar apresentando roteiro antigo como escolha atual |
| Revisão de fonte | Certificado ou documento foi atualizado | Reexaminar afirmações que usavam a versão anterior |
| Expiração de oportunidade | Prazo terminou ou oferta foi cancelada | Retirar status de disponibilidade e requalificar caminhos |
| Mudança de requisito | Pré-requisito passou de obrigatório a opcional | Recalcular lacuna contextual sem preservar falso bloqueio |
| Contradição relevante | Fontes contemporâneas se tornam incompatíveis | Sinalizar análise dependente como pendente |
| Revogação de autorização | Pessoa restringe acesso profissional | Bloquear leitura/reutilização e aplicar política competente |
| Mudança de método | Nova versão do algoritmo corrige defeito factual | Programar reavaliação controlada, se legitimamente permitida |
| Contaminação/erro de isolamento | Análise contém dados de outro sujeito | Bloqueio crítico e resposta de segurança |

**Não executar todas as análises em resposta a qualquer evento.** Determinar o conjunto mínimo afetado com base nas dependências.

## 5. Estados de validade
- `valid_for_recorded_context`: resultado íntegro dentro de versão, finalidade e período explicitados.
- `revalidation_required`: possível impacto, precisa verificar dependências.
- `stale`: evidência atualizada ou vencida; não apresentar como situação atual.
- `superseded`: substituído por análise mais recente válida.
- `blocked_by_authorization`: acesso/uso corrente não autorizado.
- `under_review`: revisão humana ou técnica pendente.
- `invalidated`: premissas essenciais deixaram de sustentar o resultado.
- `failed`: reprocessamento falhou; não usar como se tivesse sido atualizado.

**Validade histórica ≠ validade presente.** Um registro anterior pode ser preservado de forma autorizada para auditoria, mas não apresentado como a recomendação atual. `superseded` e `invalidated` não significam exclusão física automática.

## 6. Processo de propagação
1. Receber evento canônico autenticado e autorizado contendo referência à origem, versão e natureza da mudança.
2. Verificar integridade, ordem lógica, duplicidade e escopo; eventos desconhecidos ou não verificáveis não devem ser tratados como fato.
3. Consultar dependências diretas e transitivas da fonte/claim/resultado.
4. Classificar o impacto por capacidade: informativo, revisão necessária, invalidação obrigatória ou bloqueio de autorização.
5. **Marcar imediatamente resultados afetados como não atuais** antes de disponibilizar uma nova conclusão quando o risco exigir.
6. Propagar o estado aos consumidores e caches autorizados (Intelligence, relatório, API), observando falhas e confirmações.
7. Reprocessar apenas com autorização atual, contexto versionado e gates de segurança válidos.
8. Aplicar CAP-03/09 para revisar afirmações e contradições, preservando referências.
9. Confirmar `context_version` na entrega; descartar resposta atrasada de versão antiga.
10. Solicitar validação humana ou da Pessoa quando necessária; só então publicar resultado substituto admissível.
11. Registrar evento, efeitos, erros, decisão e limitações em trilha auditável com minimização.

## 7. Política de obsolescência e consistência
- **Antes de mostrar:** conferir versão do contexto e escopo de autorização no serviço competente.
- **Resultados concorrentes:** um retorno tardio de contexto antigo não poderá substituir versão atual.
- **Eventos fora de ordem:** comparar versões canônicas e aplicar regras de idempotência.
- **Eventos repetidos:** não duplicar reavaliações ou efeitos.
- **Cadeia de dependências:** propagar invalidade para derivadas realmente impactadas, preservando análises independentes.
- **Falha ao propagar:** operar de forma conservadora, sinalizando que o resultado não está validado para uso atual.
- **Sem conectividade:** registrar incapacidade de confirmar atualidade; não alegar sincronia inexistente.
- **Retenção:** separar invalidação analítica de eliminação de dados e seguir políticas, base legal e autorizações vigentes.

Não presumir garantias transacionais distribuídas já existentes. Ordem de eventos, idempotência, observabilidade e compensação são requisitos futuros de implementação.

## 8. Contrato lógico de evento (exemplo sintético)
```json
{
  "event_id": "synthetic-event-001",
  "event_type": "person_context_corrected",
  "subject_ref": "synthetic-person",
  "source_ref": "synthetic-source",
  "old_source_version": "v3",
  "new_source_version": "v4",
  "occurred_at": "2026-10-31T13:00:00-03:00",
  "recorded_at": "2026-10-31T13:00:03-03:00",
  "purpose_scope_ref": "authorized-scope",
  "origin_service_ref": "canonical-context-service"
}
```
O evento deve ser emitido/validado pelo serviço canônico; campos enviados por clientes não constituem autoridade.

## 9. Contrato lógico de resposta (exemplo sintético)
```json
{
  "capability": "GAI-CAP-10",
  "method_version": "proposed-1",
  "event_ref": "synthetic-event-001",
  "impact_status": "revalidation_required",
  "affected_analyses": [
    {
      "analysis_ref": "synthetic-cap02-analysis",
      "old_context_version": "v3",
      "new_validity_status": "stale",
      "impact_reason": "Disponibilidade foi corrigida",
      "recommended_action": "recompute_if_authorized"
    }
  ],
  "consumer_actions": ["suppress_stale_current_summary"],
  "unaffected_analyses": [],
  "limitations": ["Reprocessamento ainda não executado"]
}
```
Contratos ilustrativos, **não executados**; não confundir ação recomendada com ação concluída. Retorno para cliente externo deve respeitar o escopo de visibilidade e não revelar identificadores de análises alheias.

## 10. Exemplo sintético
**Antes:** Pessoa relata disponibilidade às terças; síntese CAP-02 e percurso CAP-07 usam essa informação.

**Correção:** Pessoa informa que agora trabalha às terças e pode participar parcialmente às quintas.

**CAP-10 deverá:** reconhecer a versão corrigida, localizar análises dependentes, marcar as versões antigas como obsoletas, impedir que o Intelligence as exiba como atuais e solicitar nova análise autorizada. O percurso poderá mudar, mas a CAP-10 não deverá afirmar que a Pessoa desistiu do objetivo.

**Se um curso expirar ao mesmo tempo:** CAP-08 deve refletir o encerramento; CAP-07 deve retirar a indicação daquela oferta, sem descartar toda a possibilidade futura.

## 11. Revogação e privacidade
A revogação não é simples atualização de conteúdo. Exige:
- validação pelo serviço autorizado, com data, finalidade e alcance;
- bloqueio de novas leituras e usos incompatíveis com a autorização;
- comunicação a consumidores/caches sujeitos à política aplicável;
- distinção entre **revogar uso**, **invalidar resultado**, **cessar processamento**, **reter quando legitimamente obrigatório** e **excluir quando devido**;
- revisão de acessos profissionais e B2B separados;
- não transmitir conteúdo ou existência de dados restritos a destinatários não autorizados.

A CAP-10 registra e propaga **efeitos analíticos**, mas não assume autoridade para alterar políticas legais ou executar eliminação de armazenamento por conta própria.

## 12. Critérios de segurança, falhas e autorização
- Fonte/cadeia de dependência indisponível: marcar verificação como incompleta; não fingir análise atualizada.
- Evento de origem não confiável: recusar execução.
- Revogação/isolamento: prioridade de bloqueio sobre recálculo.
- Alteração de modelo: exigir avaliação e gates próprios; não reprocessar todos os dados automaticamente.
- Resultado tardio: rejeitar promoção para estado vigente.
- Revisão humana necessária: manter `under_review` até decisão autorizada.
- Informações sensíveis: minimizar registros e manter segregação.
- Contradição não resolvida: não converter nova resposta em certeza.

## 13. Casos sintéticos de avaliação — não executados
| ID | Situação | Resultado esperado |
| --- | --- | --- |
| CAP10-E01 | Pessoa corrige horário | Sínteses dependentes ficam obsoletas |
| CAP10-E02 | Resultado antigo chega após nova versão | Não sobrescrever resposta atual |
| CAP10-E03 | Evento repetido | Processamento idempotente |
| CAP10-E04 | Eventos fora de ordem | Respeitar versão canônica |
| CAP10-E05 | Oferta expira | Remover status de disponibilidade vigente |
| CAP10-E06 | Requisito muda | Reavaliar lacuna pertinente |
| CAP10-E07 | Objetivo é adiado | Não manter roteiro como escolha atual |
| CAP10-E08 | Revogação durante processamento | Interromper uso indevido |
| CAP10-E09 | Revogação de vínculo profissional | Restringir leitura do profissional, sem pressupor apagamento universal |
| CAP10-E10 | Mudança em fonte independente | Não invalidar análise não dependente |
| CAP10-E11 | Dependência transitiva CAP02→CAP06→CAP07 | Propagação às derivadas relevantes |
| CAP10-E12 | Falha no Neo4j | Estado de verificação incompleta |
| CAP10-E13 | Reprocessamento falha | Não alegar nova análise concluída |
| CAP10-E14 | Fonte clínica sensível fora de escopo | Nenhuma exposição |
| CAP10-E15 | Modelo concorda com conclusão obsoleta | Versão vigente prevalece |
| CAP10-E16 | Contradição substantiva recém-surgida | Suspender conclusão afetada |
| CAP10-E17 | Relatório histórico arquivado | Preservar contexto histórico autorizado sem apresentar como atual |
| CAP10-E18 | API externa mantém cache antigo | Sinalizar invalidação conforme contrato |
| CAP10-E19 | Fonte corrigida sem mudança material em claim | Documentar impacto e manter somente resultados justificadamente válidos |
| CAP10-E20 | Cliente envia evento forjado | Rejeitar por falta de autoridade |

**Métricas candidatas:** cobertura de dependências, taxa de resultados obsoletos exibidos, tempo de propagação, eventos duplicados, falsas invalidações, falhas de autorização, regressões e revisão humana. Limiares e aprovação ainda pendem de governança específica.

## 14. Integração e maturidade
**Guivos Intelligence** deverá impedir que o painel da Jornada substitua uma versão nova por uma resposta antiga. **Guivos AI** deverá devolver referências a fontes, análises e versões para futura invalidação. **Serviços canônicos** fornecerão eventos verificáveis. **Neo4j** poderá representar o grafo de dependências, sem ser a única autoridade.

A auditoria v0.7 da Jornada no Replit identificou componentes isolados, sem integração cognitiva pública ponta a ponta homologada. **Esta especificação não altera gates, código, chaves, memória ou automações do Replit.**

Antes de prototipar: aprovar contratos de evento e resultado, autoridade de versões, escopos de autorização, semântica de expiração, modelo de dependências, idempotência, testes sintéticos, rollback e autoridade dos gates.

## 15. Decisões pendentes
1. Autoridade sobre versão global versus versões por domínio;
2. Estratégia de propagação e reprocessamento mínimo;
3. Política de invalidação para caches B2B, relatórios e memória;
4. Regras de retenção e exclusão por finalidade;
5. Critérios de validade por capacidade e oferta;
6. Protocolo de revisão humana e de escolha pela Pessoa;
7. Contratos de evento assinado/autenticado e observabilidade;
8. Critérios de homologação e operação controlada.

**Referências:** [Documento Mestre](index.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-03](cap-03-interpretacao-fundamentada-evidencias.md) · [CAP-09](cap-09-gestao-incertezas-contradicoes.md) · [Modelo de Evidências](modelo-evidencias-rastreabilidade.md) · [Autoridade de Dados](autoridade-dados-memoria-contexto.md) · [Avaliação](avaliacao-validacao-qualidade.md).

**GKR, Replit e Neo4j permanecem inalterados.**
