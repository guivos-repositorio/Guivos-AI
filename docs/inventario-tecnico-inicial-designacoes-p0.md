# GAI-INT-26 — Inventário Técnico Inicial e Encaminhamento de Designações P0
**Versão documental 5.1 · 31/10/2026**
**Estado:** verificação de artefatos do GitHub e proposta de designações prioritárias. Nenhuma pessoa designada, serviço operacional validado, teste executado ou gate aprovado.

## 1. Objetivo
Começar a passagem da documentação para a identificação verificável dos componentes da Guivos AI, sem presumir que um serviço descrito em arquitetura esteja implantado. O escopo desta verificação foi **somente o repositório GitHub** `guivos-repositorio/Guivos-AI`, branch `main`. Replit, Neo4j, provedores e GKR não foram inspecionados nem alterados.

A [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) confirma a administração da Guivos, inicialmente representada por sua direção, como instância de nomeações e decisões estratégicas. Não nomeia automaticamente responsáveis técnicos.

## 2. Resultado da inspeção do repositório
A leitura do índice de diretórios GitHub confirmou:
| Componente | Localização | Evidência e conclusão |
| --- | --- | --- |
| Schemas candidatos | `schemas/candidate-v1/` | **19 arquivos JSON Schema** listados no repositório |
| Catálogos de fixtures | `tests/contracts/candidate-v1/cases.json` e `typed-cases.json` | Dois catálogos presentes; **49 casos é a contagem documental anterior, não recontada nesta inspeção** |
| Scripts candidatos | `tests/contracts/run_schema_cases.py`, `run_typed_cases.py` | Dois arquivos de runner presentes; não executados |
| Documento Mestre | `docs/index.md` | Arquivo publicado |
| Índice público-fonte | `index.html` | Arquivo versionado; deploy efetivo não validado |
| Documentação principal | `README.md` | Arquivo publicado |

**Conclusão positiva limitada:** há ativos documentais e artefatos de teste no GitHub. A listagem **não demonstra que os schemas são válidos, que os runners funcionam ou que exista API/backend operacional**.

## 3. Mapa dos 19 schemas observados
**Envelope e infraestrutura (7):** `analysis-request`, `analysis-response`, `analysis-response-typed`, `canonical-event`, `dependency-edge`, `error-response`, `event-receipt` (sufixo `.schema.json`).

**Capacidades (12):** `cap01-trajectory-result`, `cap02-moment-result`, `cap03-evidence-result`, `cap04-gap-result`, `cap05-possibility-result`, `cap06-compatibility-result`, `cap07-path-result`, `cap08-offer-result`, `cap09-contradictions-result`, `cap10-invalidation-result`, `cap11-report-result` e `cap12-api-service-result` (sufixo `.schema.json`).

A presença dos schemas não equivale à existência das 12 capacidades em código executável.

## 4. Serviços ainda não verificados operacionalmente
| Domínio a inventariar | Candidato a autoridade | Evidência real ainda necessária |
| --- | --- | --- |
| Identidade e autenticação | Serviço de identidade da Guivos | Repositório, serviço, API e responsável efetivos |
| Autorização, finalidades e revogação | Serviço canônico de políticas | Contratos, escopos, tenant, responsável e testes negativos |
| Contexto e evidências da Pessoa | Serviço de contexto | Origem, versões, correção, mandato e limites de uso |
| Supply/oportunidades | Serviço de ofertas | Publicação, disponibilidade, elegibilidade e owner |
| Relatórios e entrega | Serviço de entrega autorizado | Controle de destinatários, finalidade e recibos |
| Jornada da Pessoa/Intelligence | Aplicação e orquestrador | Verificação posterior autorizada de versão e contratos |
| Neo4j | Banco/projeção sob owner técnico | Conexão, banco, autoridade, modelo e reconciliação |
| GPT/Claude/Gemini | Adaptadores da orquestração | Implementação, chamadas, segurança e custos |
| API B2B | Gateway/serviço futuro | Existência real, políticas de acesso e contratos |

**Não classificar as linhas desta tabela como serviços operantes, provisionados ou não existentes:** todas permanecem `not_verified_in_this_scope`.

## 5. Primeiras duas designações para decisão da direção
### P0-A — Coordenação de arquitetura
**Papel:** validar as fronteiras Guivos Intelligence/Guivos AI/serviços canônicos, revisar ADRs e organizar integração de contratos. A direção pode nomear responsável inicial ou equipe.

**Mandato mínimo futuro:** `person_or_team_ref`, `scope_ref`, `appointment_decision_ref`, `acceptance_ref`, `effective_at`, limites de aprovação e critérios de substituição. O indicado não se torna automaticamente autoridade jurídica, de segurança ou gate G6.

**Estado:** `pending_nomination`.

### P0-B — Responsável pelo inventário dos serviços canônicos
**Papel:** identificar em cada serviço real proprietário, origem de dados, finalidade, política, versão, dependências e meios de correção. Pode ser coordenador de inventário distinto dos proprietários de cada domínio.

**Mandato mínimo futuro:** autorização para consulta aos responsáveis e documentações pertinentes; escopo sem acesso implícito a dados pessoais, sistemas privados ou segredos; aceite e prazo.

**Estado:** `pending_nomination`.

## 6. Critério de aceite para o inventário
Para cada serviço: `service_ref`, `repository_or_system_ref`, `environment`, `lifecycle_state`, `canonical_domain`, `responsible_role_ref`, `authorization_policy_ref`, `contract_version_ref`, `dependency_refs`, `evidence_of_existence_ref`, `verified_at` e `limitations`.

`lifecycle_state` deve distinguir `proposed`, `code_present`, `deployed_unverified`, `running_verified`, `deprecated` e `unknown`. Nenhum estado `running_verified` decorre apenas de um arquivo no GitHub.

## 7. Condições para a próxima inspeção
O próximo passo material depende de **indicações/aceites de P0-A/P0-B** e de acesso autorizado aos projetos relevantes. Toda inspeção dos ambientes Replit, Neo4j ou serviços de dados deverá ter autorização e finalidade próprias, sem realizar escrita operacional involuntária.

As decisões PND-01/PND-11 permanecem abertas, apesar de GAI-DEC-009. As 16 funções do GAI-INT-23 seguem sem titulares formalizados. G0 parcial; G1–G6 pendentes.

## 8. Publicação estruturada
O [registro JSON de evidências e lacunas](inventario-tecnico-inicial-guivos-ai.json) contém somente fatos verificados nos diretórios GitHub e serviços ainda não verificados. Não contém credenciais, pessoas designadas, evidências de deploy ou resultados de testes.

**Referências:** [GAI-INT-25](modelo-inicial-designacoes-segregacao-responsabilidades.md) · [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md) · [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) · [Registro de Decisões](registro-decisoes.md).

**Sem autorização de teste, nomeações ou mudanças operacionais.**
