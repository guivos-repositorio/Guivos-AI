# GAI-INT-13 — Plano de Compatibilidade, Migração e Evolução de Contratos
**Versão documental 3.7 · 31/10/2026**
**Estado:** proposta técnica e de governança; nenhuma migração aplicada, nenhuma execução homologada, nenhum consumidor ou serviço operacional alterado.

## 1. Propósito
Definir como os contratos candidatos da Guivos AI poderão evoluir entre versões sem interromper usos autorizados, confundir os estados de resultados, perder proveniência ou permitir acesso indevido. O plano cobre produtores, consumidores, gateways, Guivos Intelligence, serviços canônicos, eventual API B2B, relatórios e projeções de dependências.

**Ponto de partida real:** 12 capacidades documentadas, 19 schemas `candidate-v1`, 49 casos sintéticos preparados e dois executores offline. Não existe versão contratual homologada ou baseline operacional validado. Portanto, as fases descritas abaixo são propostas para futuras decisões, **não ações em curso**.

## 2. Fronteiras e responsabilidades
| Parte | Contrato sob sua responsabilidade | Regra |
| --- | --- | --- |
| Serviço de contexto | Identidade de fonte, contexto, revisão, dado e provenance | Mantém autoridade canônica do fato |
| Serviço de autorizações | Finalidades, acessos, vínculos, revogação e destinatários | A versão do schema não concede autorização |
| Serviços de oportunidades | Oferta, requisitos, publicação, prazo e disponibilidade | Disponibilidade não é deduzida da publicação |
| Guivos AI | Entrada e saída das capacidades, método e claim | Não substitui fontes canônicas |
| Guivos Intelligence | Requisição, interpretação de resposta, escolha da Pessoa | Não promove hipótese a fato sem evidência e validação |
| CAP-12 / gateway B2B | Autenticação do cliente, segregação e contratos externos | Não herda privilégios do consumo interno |
| Event bus / CAP-10 | Eventos, versões, recibos e invalidações | Evento recebido não significa aplicado |
| Neo4j ou outra projeção | Dependências e proveniência reconstruíveis | Não presume ser fonte primária |

A governança do GKR permanece independente da Guivos AI. Nenhuma mudança neste repositório implica implantação no Replit.

## 3. Identidades de versão independentes
- `document_version`: evolução da documentação (v3.7); não é versão de API.
- `api_contract_version`: formato do envelope e semântica de consumo.
- `schema_version`: versão de eventos e artefatos tipados.
- `capability_version`: contrato e semântica de uma CAP.
- `method_version`: revisão do método analítico, sem alterar automaticamente o schema.
- `context_version` e `source_version`: estado das fontes canônicas.
- `analysis_version` e `report_version`: revisões derivadas sem transferir legitimidade de acesso.

Política candidata: mudanças incompatíveis exigem nova versão explícita, mapeamento de consumidores, fixtures e evidências de compatibilidade; mudanças editoriais não devem mascarar alteração de semântica.

## 4. Classes de mudança
| Classe | Exemplos | Efeito candidato |
| --- | --- | --- |
| Editorial | Descrição sem alterar campo/semântica | Corrigir documentação, revalidar referência |
| Aditiva condicionada | Campo opcional novo | Testar consumidores estritos (`additionalProperties:false`) antes de declarar compatibilidade |
| Restritiva | Campo passa a obrigatório, enum é reduzido | Quebra possível; versão nova |
| Expansão semântica | Enum novo, interpretação de estado ampliada | Quebra potencial para consumidores com switch exaustivo |
| Renomeação/remoção | `field_old` substituído | Migração com adaptador e prazo |
| Quebra de autoridade | Alteração de finalidade ou acesso | Não fazer migração automática de permissões |
| Quebra temporal | Alteração de semântica de validade/expiração | Reavaliar derivados e exibição |
| Mudança de modelo | GPT/Claude/Gemini ou método substituído | Testar regressões epistêmicas, sem tratar o provedor como fonte canônica |

**Regra:** nenhum caso será considerado retrocompatível apenas porque seu JSON permanece sintaticamente válido.

## 5. Matriz producer × consumer proposta
| Produtor | Consumidor | Mudança | Verificação |
| --- | --- | --- | --- |
| Intelligence antigo | Guivos AI novo | Solicitação `AnalysisRequest` | Aceita versão anterior explicitamente suportada ou rejeita com erro tipado |
| Intelligence novo | Guivos AI antigo | Campo opcional novo | Confirmar comportamento com `additionalProperties:false` |
| Guivos AI antigo | Intelligence novo | `AnalysisResponse` flexível | Não presumir que `result` obedece ao envelope tipado |
| Guivos AI novo | Intelligence antigo | `AnalysisResponseTyped` | Compatibilidade e mapeamento obrigatório por CAP |
| Serviços canônicos antigo/novo | Consumidor de eventos | `CanonicalEvent` | Ordem por agregado, autenticidade, revogação e versão |
| CAP-10 | Caches e relatórios | Novo recibo `EventReceipt` | Diferenciar recebimento, avaliação, aplicação e revalidação |
| API interna | Gateway de parceiro | Resultado específico | Filtragem de campos por destinatário, finalidade e tenant |
| CAP-11 | Destinatário autorizado | Versão de relatório | Não confundir relatório anterior, atual e acesso revogado |

## 6. Estratégias de migração candidatas
**M1 — Versionamento paralelo:** produtor pode manter contratos de versões distintas por janela definida formalmente. Exigir segregação por consumidor e observabilidade.

**M2 — Adaptador explícito:** traduz `candidate-1` a formato posterior sem inventar dados, omitir desconhecidos relevantes ou aumentar permissões. Perdas semânticas exigem `limitations` e, quando necessário, rejeição.

**M3 — Migração expandir-validar-contrair:** adicionar contrato novo, testar, habilitar consumidores gradualmente, manter compatibilidade durante janela de revisão e só então descontinuar o antigo.

**M4 — Falha fechada:** versões desconhecidas, escopos revogados ou impossibilidade de converter campos essenciais retornam erro tipado; não cair silenciosamente em contrato mais permissivo.

**M5 — Invalidação controlada:** mudança de contexto/autorizações exige revalidação de resultados derivados, sem reprocessamento automático de dados pessoais fora de escopo.

Nenhuma estratégia foi escolhida como padrão de produção.

## 7. Ciclo de mudança com decisões separadas
```text
Proposta de mudança + justificativa
  → análise de impacto por contrato/CAP/consumidor/tenant
  → revisão de segurança, fontes e semântica
  → schema candidato + fixtures de compatibilidade
  → aprovação de execução em ambiente isolado
  → execução com evidências versionadas
  → adjudicação de compatibilidade e gates aplicáveis
  → autorização explícita de migração com escopo
  → rollout controlado e monitorado
  → avaliação de depreciação e encerramento de versão
```
A conclusão de um passo documental não autoriza o próximo passo operacional.

## 8. Política proposta de depreciação
Campos mínimos de um aviso de descontinuação: `contract_ref`, `old_version`, `replacement_version`, `affected_consumers[]`, `change_class`, `migration_guide_ref`, `notice_at`, `planned_end_at`, `compatibility_evidence_refs[]`, `support_contact_role`, `approval_ref`.

Antes de fixar um prazo ou desligar versão, exigir inventário de consumidores e dependências, risco de dados históricos, autorização de stakeholders, plano de rollback e testes sobre versões ainda em uso. **Não estabelecer datas de sunset sem deliberação real**.

## 9. Rollout e rollback por escopo
**Rollout futuro:** teste isolado → avaliação de compatibilidade → implantação restrita por consumer/tenant/capacidade, se autorizada → métricas e alertas → ampliação apenas mediante evidência.

**Gatilhos candidatos para interrupção:** acesso indevido, falha de revogação, perda de proveniência, resultado obsoleto tratado como atual, erro sistêmico de contrato, divergência de enum material, entrega B2B inadequada.

**Rollback futuro:** reverter rota/versão para consumidores elegíveis, preservar trilha imutável, impedir retorno de autorização revogada, não restaurar dados excluídos legitimamente, revalidar relatórios e caches. Um rollback técnico não pode desfazer automaticamente entregas já realizadas.

## 10. Registro de migração proposto
```json
{
  "migration_id": "synthetic-migration-plan-001",
  "status": "proposed_not_executed",
  "from_contract_version": "candidate-1",
  "to_contract_version": "future-candidate",
  "affected_consumer_refs": ["synthetic-intelligence"],
  "affected_capability_ids": ["GAI-CAP-08"],
  "change_class": "semantic_enum_evolution",
  "required_fixture_refs": ["synthetic-compat-case"],
  "authorization_review_status": "pending",
  "execution_run_refs": [],
  "gate_decision_ref": null,
  "rollback_plan_ref": "synthetic-plan-ref"
}
```
A versão `future-candidate` é fictícia, não publicada. O registro não comprova uma migração.

## 11. Cenários de compatibilidade candidatos
| ID | Mudança/condição | Resultado esperado |
| --- | --- | --- |
| INT13-C01 | Campo novo com consumidor estrito | Detectar incompatibilidade, negociar versão |
| INT13-C02 | Campo obrigatório removido | Rejeitar contrato sem promover campos padrão inventados |
| INT13-C03 | Enum de disponibilidade expandido | Não interpretar valor desconhecido como disponibilidade confirmada |
| INT13-C04 | Envelope flexível vs tipado CAP-08 | Impedir troca de payload por CAP equivocada |
| INT13-C05 | Método analítico muda sem alterar schema | Exigir revisão semântica independente |
| INT13-C06 | `validity_status` muda significado | Tratar como mudança incompatível |
| INT13-C07 | Evento duplicado após migração | Idempotência e versão canônica |
| INT13-C08 | Evento fora de ordem entre duas versões | Não restaurar análise vencida |
| INT13-C09 | Parceiro permanece em contrato antigo | Não conceder novos dados/escopos |
| INT13-C10 | Autorização revogada antes de rollback | Não restabelecer acesso |
| INT13-C11 | CAP-11 relatório entregue em versão anterior | Manter histórico/limites de entrega sem afirmar recolhimento |
| INT13-C12 | Adaptador perde campo de incerteza | Falhar ou expor perda; não fabricar certeza |
| INT13-C13 | Fonte canônica retificada no meio da migração | Bloquear exibição obsoleta e revisar dependências |
| INT13-C14 | Gateway recebe versão desconhecida | Erro tipado e seguro |
| INT13-C15 | Provedor multi-modelo altera formato | Não ampliar autoridade factual da resposta |
| INT13-C16 | Consumidor de evento recebeu, mas não aplicou | Recibos separadamente verificáveis |
| INT13-C17 | Mudança em tenant A | Não afetar tenant B sem dependência legítima |
| INT13-C18 | Resultado parcial durante fallback | Preservar cobertura e limitações |
| INT13-C19 | Desativação de versão sem inventário | Bloquear decisão de sunset |
| INT13-C20 | Rollback com grafo de dependências atrasado | Exigir reconciliação e falha segura |

**Todos planejados.** São cenários de governança e integração, não resultados de execução.

## 12. Indicadores e critérios de aceite futuros
Medidas candidatas: contratos incompatíveis detectados; distribuição de versões por consumer; falhas de tradução semântica; perdas de campos de suporte; problemas de autorização; erros por versão; eventos não aplicados; relatórios obsoletos exibidos; latência e custo de adaptadores; tempo real de rollback.

**Critérios mínimos:** ausência de falhas críticas abertas no escopo; evidência de execução reproduzível; autorização e isolamento preservados; responsabilidade de cada sistema confirmada; plano de rollback testado; revisão humana independente; decisão explícita do gate. Não fixar percentuais antes de experimentos e governança.

## 13. Gates e responsabilidades
| Gate | Prova esperada | Estado |
| --- | --- | --- |
| G0 | Fronteiras e dependências coerentes | Parcial |
| G1 | Compatibilidade e schemas normativos revisados e testados | Pendente |
| G2 | Autorizações, escopos, revogação e isolamento demonstrados | Pendente |
| G3 | Execuções sintéticas e retestes rastreáveis | Pendente |
| G4 | Rollout/rollback controlado em ambiente isolado | Pendente |
| G5 | Adjudicação por responsáveis formalmente designados | Pendente |
| G6 | Liberação restrita e observabilidade aprovadas | Pendente |

As funções de owner do contrato, responsável por serviço, segurança, dados, experiência, revisão de IA e governança ainda precisam de designação explícita.

## 14. Pendências para decisão
1. Estabelecer formato definitivo de versionamento e política de compatibilidade entre serviços.
2. Escolher união discriminada de sucesso e erro e perfil de evolução de enums.
3. Especificar inventário real de consumidores, tenants e contratos quando houver autorização para inspeção.
4. Determinar ciclo de depreciação com períodos concretos e responsáveis.
5. Definir ferramentas, testes e armazenamento de evidências de migração.
6. Formalizar limites de rollout/rollback e critérios de incidentes.
7. Ratificar autoridade canônica e controles de dados em cada fluxo.
8. Distinguir migração técnica de mudança de base legal/finalidade.

## 15. Próximo estudo
[**GAI-INT-14 — Registro de Decisões Pendentes e Plano de Fechamento de Gates**](registro-decisoes-pendentes-plano-fechamento-gates.md), publicado como consolidação das decisões de contrato, segurança, fontes e avaliação, antes de qualquer pedido de autorização operacional.

**Referências:** [GAI-INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [GAI-INT-11](cobertura-contratos-especializados-integracao-schemas.md) · [GAI-INT-10](conformidade-schemas-casos-contrato-compatibilidade.md) · [GAI-INT-07](contratos-eventos-projecao-dependencias.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Somente documentação. Replit, Neo4j, provedores, GKR e gates operacionais permanecem inalterados.**
