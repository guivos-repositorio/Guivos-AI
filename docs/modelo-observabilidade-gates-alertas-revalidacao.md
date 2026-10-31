# GAI-INT-18 — Modelo de Observabilidade de Gates, Alertas e Revalidação Contínua
**Versão documental 4.2 · 31/10/2026**
**Estado:** especificação e modelos candidatos. Não há monitoramento instalado, gatilhos ativados, alerta real, teste executado, revalidação observada ou gate aprovado.

## 1. Objetivo e limites
Especificar como identificar futuramente perda de validade de evidências, alterações contratuais, expiração e revogação de decisões, defeitos críticos, divergência entre projeções e fontes, além de pendências de revalidação. Uma proposta de observabilidade não autoriza sondagem do Replit, Neo4j, provedores GPT/Claude/Gemini, parceiros ou dados reais.

**Referencial documental:** 12 capacidades, GAI-INT-01–17, 19 schemas `candidate-v1`, 49 fixtures sintéticas, dois executores preparados e 16 decisões PND-01–16 abertas. G0 parcial; G1–G6 pendentes.

## 2. Separações semânticas obrigatórias
- **Integridade da evidência:** o artefato existe, é íntegro e se vincula a um run observado.
- **Validade técnica:** o resultado continua representativo da versão testada e do contexto registrado.
- **Validade de autorização:** a finalidade, o sujeito, o tenant e o destinatário permanecem autorizados.
- **Validade do gate:** existe decisão formal em vigor, com alçada e escopo aplicáveis.
- **Disponibilidade do sistema:** a consulta/serviço está operante, o que não implica veracidade nem permissão.
- **Estado de alerta:** um sinal precisa de verificação; não implica automaticamente incidente ocorrido.

Nenhuma categoria substitui outra. O gate aprovado para uma versão não homologa automaticamente versões posteriores.

## 3. Fontes candidatas de sinais
| Fonte | Sinal candidato | Autoridade |
| --- | --- | --- |
| Registro de GateDecision | `gate_effective`, `gate_expired`, `gate_revoked`, `scope_changed` | Serviço de governança designado |
| Registro de autorização | `authorization_revoked`, `scope_expired` | Serviço canônico de permissões |
| Registro de contratos | `schema_version_changed`, `consumer_incompatible` | Owner dos contratos |
| Catálogo de evidências | `artifact_digest_changed`, `evidence_missing` | Armazenamento/auditoria autorizados |
| Execuções sintéticas | `run_failed`, `case_coverage_changed`, `runner_mismatch` | Executor controlado e curador |
| Registro de defeitos | `critical_finding_opened`, `finding_reopened` | Processo de QA |
| Projeção de dependências | `projection_lag_unknown`, `reconciliation_failed` | Serviço de projeção, não autoridade canônica |
| Consumers Intelligence/API | `stale_result_detected`, `delivery_blocked` | Serviço consumidor responsável |

Esses nomes são **eventos candidatos**, não eventos emitidos por software existente. Não fazer polling de serviços sem aprovação.

## 4. Tipologia de alertas
| Código | Condição candidata | Severidade proposta | Conduta recomendada |
| --- | --- | --- | --- |
| OBS-01 | Gate expirado/revogado usado como válido | Crítica | Bloquear uso; verificar autoridade e escopo |
| OBS-02 | Autorização revogada com processamento/entrega pendentes | Crítica | Interromper novas operações incompatíveis; escalar |
| OBS-03 | Integridade de artefato diverge do digest aceito | Alta | Marcar pacote inconclusivo e investigar |
| OBS-04 | Schema novo rompe contrato de consumidor | Alta | Não promover versão sem migração aprovada |
| OBS-05 | Defeito crítico aberto ou reaberto | Crítica ou alta conforme impacto | Suspender recomendação de gate relevante |
| OBS-06 | Cobertura de testes abaixo da matriz aprovada | Alta | Registrar lacuna e impedir declaração de cobertura integral |
| OBS-07 | Registro de execução sem autorização comprovável | Crítica para homologação | Desconsiderar como evidência válida |
| OBS-08 | Projeção de dependências atrasada ou incompleta | Alta | Falha segura e reconciliação autorizada |
| OBS-09 | Resultado obsoleto apresentado como vigente | Alta/crítica conforme uso | Bloquear exibição/entrega e reavaliar |
| OBS-10 | Revisor e executor sem independência exigida | Alta | Reabrir revisão |
| OBS-11 | Divergência de evidências não adjudicada | Alta | Gate pendente |
| OBS-12 | Sinal sem origem autenticada | Alta | Quarentena; não aplicar decisão automática |

Classificações não são eventos reais e deverão ser calibradas por risco e responsáveis.

## 5. Envelope lógico de sinal
O [template de sinal e alerta](../tests/contracts/candidate-v1/gate-observability-signal-template.json) contém `signal_id`, `signal_type`, `source_ref`, `observed_at`, `subject_gate_ref`, `scope_ref`, `referenced_version`, `evidence_refs[]`, `integrity_status`, `authorization_status`, `proposed_severity` e `handling_status`.

Proibir a inserção de PII, credenciais ou payloads de análises em alertas por padrão. Referências devem ser resolvidas somente por consumidores autorizados. Sinal sem fonte verificada não altera sozinho a decisão de gate.

## 6. Estados de tratamento
```text
candidate_signal
  → received
  → source_verification_pending
  → verified | rejected | inconclusive
  → impact_assessment_pending
  → no_material_impact | revalidation_required | escalation_required
  → reviewed
  → closed | reopened
```
Revogação canônica de autorização exige bloqueio imediato no ponto de acesso conforme política própria; não aguarda revisão manual do alerta para restringir novas operações. Em contrapartida, **a criação de um alerta não revoga uma decisão formal por si só**; eventual revogação do gate exige autoridade competente e procedimento de emergência definido.

## 7. Revalidação contínua proposta
A revalidação poderá ser acionada futuramente por:
1. **Tempo:** `expires_at` da decisão, prazo de validade da autorização ou janela de revisão definida.
2. **Mudança:** novo commit/schema/enum, método ou versão de serviço com impacto material.
3. **Evidência:** nova falha, reteste, digest divergente ou fonte retirada.
4. **Autoridade:** mudança de finalidade, destinatário, escopo, revogação.
5. **Dependência:** alteração de contexto, oferta, fonte canônica ou projeção incompleta.

Cada revalidação produziria `revalidation_ref`, `trigger_ref`, `affected_gate_refs[]`, `scope`, `as_of`, `impact_class`, `required_evidence_refs[]`, `decision_status` e `limitations[]`. **Nenhuma periodicidade, SLA ou threshold foi aprovado.**

## 8. Regras de propagação e consistência
- Eventos são idempotentes por `event_id`; versões canônicas não podem retroceder por chegada fora de ordem.
- Um recibo `event_received` não comprova impacto aplicado nem cache revalidado.
- Falta de cobertura do índice impede concluir que nenhuma decisão é afetada.
- Gates aplicam-se a `subject_scope`, `consumer`, `contract_version` e janela autorizada quando pertinentes; não há aprovação universal.
- Cache, relatório e API precisam revalidar autorização no momento do uso segundo política de domínio, além de consultar validade técnica.
- Reprocessamento de dados requer autorização própria; revogação de processamento e retirada de entrega não são a mesma operação.
- Nem observabilidade nem grafo Neo4j substituem os registros transacionais canônicos de autoridade.

## 9. Indicadores e métricas candidatos
| Indicador | Definição futura | Advertência |
| --- | --- | --- |
| Cobertura de decisões vigentes | Gates válidos com evidências requeridas revisadas | Denominador exige inventário autorizado |
| Latência de detecção | Intervalo entre evento canônico e verificação do sinal | Não estimar SLA sem medições |
| Latência de propagação | Intervalo entre mudança e aplicação confirmada nos consumidores | Recebimento ≠ aplicação |
| Taxa de alertas inconclusivos | Sinais sem evidência suficiente sobre sinais triados | Nunca contar como conformes |
| Dívida de revalidação | Decisões com revisão requerida pendente | Registrar risco sem extrapolação |
| Integridade de artefatos | Digests confirmados sobre os esperados | Hash não prova legitimidade da origem |
| Incidentes de autorização | Violações confirmadas por autoridade | Não interpretar alertas como incidentes confirmados |

Não apresentar dashboards com dados simulados como evidência de operação; qualquer visualização futura precisa indicar seu estado metodológico aos revisores.

## 10. Casos sintéticos de validação planejados
| ID | Cenário | Comportamento esperado |
| --- | --- | --- |
| INT18-O01 | Gate sem `expires_at` e política indefinida | Vigência não presumida |
| INT18-O02 | Gate expirado referenciado em consumo | Rejeitar vigência |
| INT18-O03 | Gate formalmente revogado | Não permitir novo uso como autorização |
| INT18-O04 | Revogação de finalidade no meio de fluxo | Bloquear novas operações incompatíveis |
| INT18-O05 | Schema muda sem compatibilidade testada | Revalidação requerida |
| INT18-O06 | Digest de fixture divergente | Pacote não íntegro |
| INT18-O07 | Caso negativo não executado | Cobertura não comprovada |
| INT18-O08 | Defeito crítico reaberto | Escalar e reavaliar gate |
| INT18-O09 | Recibo apenas de recebimento | Não concluir propagação |
| INT18-O10 | Evento duplicado | Efeito lógico idempotente |
| INT18-O11 | Evento antigo recebido após novo | Não retroceder versão |
| INT18-O12 | Projeção Neo4j indisponível | Cobertura inconclusiva, falha segura |
| INT18-O13 | Autorização tenant A | Não vazar estado do tenant B |
| INT18-O14 | Alerta falsificado | Rejeitar/quarentenar |
| INT18-O15 | Sinal sem evidência suficiente | Não revogar gate automaticamente |
| INT18-O16 | Revisão com conflito de interesse | Reabrir revisão |
| INT18-O17 | Relatório anteriormente entregue | Não alegar recolhimento automático |
| INT18-O18 | Revalidação conclui impacto material | Exigir nova evidência e decisão por autoridade |
| INT18-O19 | Monitoramento indisponível | Não afirmar ausência de alertas |
| INT18-O20 | Mudança de método sem schema novo | Revalidar semântica e proveniência |

**Todos os 20 cenários são propostas; nenhum foi executado, adjudicado ou aplicado.**

## 11. Gatilhos, escalonamento e decisão
As funções de primeira análise, responsável técnico, segurança/privacidade, titular do serviço canônico, revisor independente e autoridade de gate permanecem por designar. Para cada alerta futuro, registrar autor, origem, versão, escopo, confirmação, responsável de tratamento, prazo atribuído formalmente e resultado.

Sinais de potencial risco crítico a dados exigirão caminho de contenção e notificação segundo políticas aprovadas; a criação desse caminho é **decisão pendente**, não controle operacional já em funcionamento.

## 12. Gates e pendências preservados
| Gate | Requisito para observar/revalidar | Estado |
| --- | --- | --- |
| G0 | Autoridades e escopos definidos | Parcial |
| G1 | Contratos e critérios de compatibilidade homologados | Pendente |
| G2 | Identidade, finalidades, isolamento e revogação verificados | Pendente |
| G3 | Runs sintéticos com evidências reais de execução | Pendente |
| G4 | Fluxos de propagação e recuperação demonstrados em ambiente autorizado | Pendente |
| G5 | Revisão e adjudicação independentes | Pendente |
| G6 | Liberação, monitoramento e resposta a incidentes aprovados | Pendente |

As PND-01–16 continuam abertas. Nenhum alerta ou template alterou o Registro de Decisões ou as condições de acesso.

## 13. Próxima etapa
[**GAI-INT-19 — Consolidação de Arquitetura e Critérios de Prontidão para Implementação**](consolidacao-arquitetura-prontidao-implementacao.md), reunindo contratos, governança, observabilidade e dependências em um roteiro verificável para futuras decisões, sem iniciar a implementação.

**Referências:** [GAI-INT-17](modelo-rastreabilidade-auditoria-proveniencia-gates.md) · [GAI-INT-16](pacote-evidencias-revisao-independente-adjudicacao-gates.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [GAI-INT-07](contratos-eventos-projecao-dependencias.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md).

**Replit, Neo4j, provedores e GKR permanecem inalterados. Sem monitoramento operacional, testes ou gates aprovados.**
