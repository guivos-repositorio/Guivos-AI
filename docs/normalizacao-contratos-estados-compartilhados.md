# GAI-INT-02 — Normalização dos Contratos e Estados Compartilhados
**Versão documental 2.6 · 31/10/2026**
**Estado:** especificação transversal proposta; sem schemas executáveis homologados, integração, testes ou autorização operacional.

## 1. Objetivo e autoridade
Definir uma **linguagem contratual comum** às GAI-CAP-01–12 sem remover particularidades de cada capacidade. A normalização orienta o futuro catálogo de schemas e a comunicação entre Guivos Intelligence, Guivos AI, serviços canônicos e consumidores B2B.

Este documento **não altera retroativamente** os exemplos sintéticos das CAPs, nem aprova automaticamente contratos técnicos. Em caso de conflito, registrar a divergência para decisão; não substituir silenciosamente a especificação de origem.

**Autoridade:** serviços canônicos verificam identidade, fatos e autorização; Guivos AI responde por método e análises; Guivos Intelligence coordena experiência e validação; API externa usa políticas próprias. Neo4j poderá projetar relações; GPT/Claude/Gemini não são autoridades canônicas.

## 2. Camadas de contrato
| Camada | Finalidade | Responsabilidade |
| --- | --- | --- |
| Transporte/identidade | Autenticação do consumidor, correlação, integridade e limites | Gateway e serviços |
| Autorização | Finalidade, sujeito, destinatário, tenant, validade, vínculo | Serviço canônico de autorização |
| Contexto | Fontes, revisões, períodos, escopo de acesso | Serviços de contexto/memória |
| Capacidade | Entradas e saídas especializadas CAP-01–11 | Guivos AI |
| Evidências | Claims, suportes, hipóteses, contradições | CAP-03/09 |
| Ciclo de vida | Processamento, atualidade, revisão, invalidação | CAP-10 e orquestradores |
| Entrega | Apresentação, relatório, destinatário e consentimento de compartilhamento | Intelligence/CAP-11/CAP-12 |

O contrato compartilhado é um **envelope**; cada capacidade acrescentará seu payload tipado.

## 3. Convenções de nomes e presença
- IDs e referências opacos: `request_id`, `analysis_id`, `subject_ref`, `source_ref`, sem codificar dados pessoais nos identificadores.
- Campos temporais em ISO 8601 com fuso explícito; distinguir `occurred_at`, `recorded_at`, `as_of`, `generated_at`, `valid_until`.
- `*_version` representa revisão identificável e não deve ser confundida com timestamp.
- `unknown` é estado epistêmico, não substituto universal de `null`.
- Campo omitido indica **não fornecido no contrato**; `null` indica valor explicitamente sem informação quando permitido pelo schema; string vazia não equivale a “desconhecido”.
- `[]` indica coleção fornecida sem itens, mas não prova inexistência no mundo real.
- Erro, resultado parcial e resultado válido precisam de objetos distinguíveis.
- O sujeito pode ser pseudonimizado e referências devem ser resolvidas apenas por serviços autorizados.

## 4. Envelope lógico de solicitação — proposto
```json
{
  "request_id": "synthetic-req-001",
  "correlation_id": "synthetic-correlation",
  "api_contract_version": "candidate-1",
  "capability_id": "GAI-CAP-06",
  "requested_capability_version": "candidate-1",
  "consumer_ref": "authorized-intelligence-service",
  "subject_ref": "synthetic-subject",
  "purpose": "explore_future_compatibility",
  "authorization_scope_ref": "opaque-server-validated-reference",
  "context_version": "context-revision-12",
  "as_of": "2026-10-31T13:00:00-03:00",
  "input_refs": ["synthetic-possibility", "synthetic-requirement"],
  "requested_output_scope": ["assessment", "unknowns", "questions"],
  "idempotency_key": "synthetic-idempotency-key"
}
```
**Verificação obrigatória do lado do serviço:** o cliente não concede permissão a si mesmo ao fornecer `authorization_scope_ref`, `consumer_ref` ou `subject_ref`.

## 5. Envelope lógico de resposta — proposto
```json
{
  "request_id": "synthetic-req-001",
  "analysis_id": "synthetic-analysis",
  "api_contract_version": "candidate-1",
  "capability_id": "GAI-CAP-06",
  "method_version": "candidate-1",
  "context_version": "context-revision-12",
  "lifecycle_status": "completed",
  "validity_status": "valid_for_recorded_context",
  "support_status": "partially_supported",
  "person_validation_status": "not_requested",
  "result": {
    "requirement_assessments": [],
    "unknowns": ["Disponibilidade em um dia específico"],
    "questions": ["Qual é sua disponibilidade nesse dia?"]
  },
  "claims": [],
  "source_refs": [],
  "limitations": ["Análise limitada às fontes autorizadas."],
  "dependencies": ["synthetic-context-revision-12"],
  "generated_at": "2026-10-31T13:00:05-03:00",
  "valid_until": null
}
```
`valid_until: null` não garante validade infinita. O consumidor verifica versão/escopo antes de exibir. Os exemplos são dados sintéticos e não são respostas de serviço real.

## 6. Taxonomia de estados: namespaces independentes
| Namespace | Estados candidatos | Autoridade/semântica |
| --- | --- | --- |
| `lifecycle_status` | accepted, queued, processing, awaiting_review, completed, failed, cancelled | Situação da execução, não verdade da conclusão |
| `validity_status` | valid_for_recorded_context, revalidation_required, stale, superseded, invalidated, blocked_by_authorization | Atualidade da análise, CAP-10 |
| `support_status` | supported, partially_supported, unsupported, contradictory, not_assessable | Fundamentação por claim; agregado não substitui detalhes |
| `person_validation_status` | not_requested, pending, accepted_for_exploration, confirmed_report, contested, declined, postponed | Escolha/declaração da Pessoa, escopo explícito |
| `publication_status` | draft, published, suspended, closed, cancelled, unknown | Registro da oferta pela fonte competente |
| `verification_status` | verified_current, verified_historical, pending_verification, stale, conflicting_sources, unverifiable | Verificação de oferta ou fonte |
| `availability_status` | confirmed_available, published_not_confirmed, not_available, unknown | Disponibilidade, distinta de publicação |
| `report_status` | draft, awaiting_evidence_review, awaiting_person_validation, ready_for_authorized_release, released_to_authorized_recipient, under_revision, stale, superseded, access_blocked, failed | Ciclo CAP-11 |
| `authorization_status` | authorized, denied, revoked, expired, requires_reverification | Resultado do serviço de autorização, não declaração da IA |

**Não usar `status` genérico para substituir esses campos.** Estados específicos das CAPs permanecem em `result` e podem exigir vocabulário adicional.

## 7. Invariantes entre estados
1. `lifecycle_status=completed` **não implica** `support_status=supported`, autorização para entrega ou validade atual.
2. `validity_status=valid_for_recorded_context` descreve versão histórica específica, não garantia de atualidade perpétua.
3. `person_validation_status=accepted_for_exploration` não representa escolha definitiva nem consentimento B2B.
4. `publication_status=published` não comprova `availability_status=confirmed_available`.
5. `authorization_status=revoked` bloqueia novas consultas incompatíveis, mesmo se a análise constar como `completed`.
6. `report_status=released_to_authorized_recipient` não significa que o destinatário leu ou concordou.
7. `support_status=unsupported` não pode ser apresentado como conclusão fundamentada.
8. `unknown` sobre condição da Pessoa não pode ser convertido em `not_met` ou incompatibilidade.
9. Um modelo que repete uma fonte não é nova fonte independente.
10. Resposta para contexto antigo não deve substituir a mais recente.

## 8. Evidências e claims: contrato mínimo
Cada afirmação material deve possuir: `claim_id`, `statement`, `epistemic_type` (observed_event, attributed_report, grounded_interpretation, exploratory_hypothesis, unknown), `support_status`, `evidence_refs[]`, `counterevidence_refs[]`, `source_versions[]`, `as_of`, `justification_summary`, `limitations[]`.

`evidence_refs` devem ser referências autorizadas. A justificativa explica o fundamento verificável, sem expor cadeia privada de raciocínio do modelo. A falta de fonte não deve ser mascarada com citação decorativa.

## 9. Contratos de falha e resultado parcial
Campos candidatos de erro: `error.code`, `error.category`, `error.retryable`, `error.message_safe`, `correlation_id`, `context_version`. Classes: `unauthenticated`, `forbidden`, `invalid_contract`, `capability_not_enabled`, `context_version_conflict`, `upstream_unavailable`, `rate_limited`, `access_revoked`.

Não retornar segredos, informações sobre outro sujeito, prompts internos ou dados de diagnóstico sensíveis. Recuperação parcial deve ser explicitada por `coverage`/`limitations`; não inventar um resultado completo.

## 10. Versionamento e compatibilidade
| Versão | Governança |
| --- | --- |
| `api_contract_version` | Envelope, mensagens, compatibilidade entre consumidores |
| `capability_version` | Semântica e campos específicos de cada CAP |
| `method_version` | Método analítico e suas revisões |
| `context_version` | Conjunto contextual canônico autorizado |
| `source_versions` | Revisões dos registros e fontes |
| `analysis_version` | Revisão do resultado derivado |
| `report_version` | Revisão do relatório, sem equivaler ao contexto |

Alterações incompatíveis exigem migração, testes de contrato, deprecation e consumidores identificados. Alterar método não aprova reprocessamento de dados pessoais sem autorização.

## 11. Semântica de revisão e autorização
Correções, eventos de expiração, revogação e mudança de requisitos devem ser emitidos por serviços com autoridade. CAP-10 propaga invalidação analítica; não executa por conta própria apagamento nem redefine autorização canônica.

Separar: (a) direito de processar, (b) direito de consultar resultado, (c) direito de compartilhar/entregar, (d) direito de reprocessar. Um vínculo profissional ou contrato pago não substitui a autorização da Pessoa quando exigida.

## 12. Matriz de normalização por capacidade
| CAP | Payload específico mantido | Estados críticos |
| --- | --- | --- |
| 01 | Eventos, trajetória, períodos | suporte, temporalidade |
| 02 | Dimensões contextuais, desconhecidos | atualidade, conhecimento |
| 03 | Claims e fontes por afirmação | support_status |
| 04 | Requisitos, conditions, gap_status | met/not_met/unknown |
| 05 | Possibilidades e origem | interesse/validação da Pessoa |
| 06 | Compatibilidade por requisito | desconhecido não vira incompatibilidade |
| 07 | Caminhos, etapas, dependências | caminho proposto não é obrigação |
| 08 | Publicador, oferta, inscrições | publicação/verificação/disponibilidade |
| 09 | Divergências, fontes, impacto | conflito aberto ou resolvido |
| 10 | Eventos, dependências, invalidação | validity_status |
| 11 | Seções, destinatário, entrega | report_status e autorização de entrega |
| 12 | Consumer, tenant, gateway, quotas | authorization_status, lifecycle_status |

O envelope é transversal e o payload de cada CAP continua tipado.

## 13. Testes de contrato candidatos (não executados)
| ID | Verificação |
| --- | --- |
| CTR-01 | Mensagem com versão e finalidade presentes |
| CTR-02 | Referência de autorização forjada não concede acesso |
| CTR-03 | `completed` com claim `unsupported` não vira fato |
| CTR-04 | `published` com disponibilidade desconhecida não vira vaga confirmada |
| CTR-05 | Contexto corrigido impede resposta anterior de substituir nova |
| CTR-06 | Revogação bloqueia recuperação de resultado |
| CTR-07 | Campos de outro tenant não vazam no erro |
| CTR-08 | Dados ausentes mantêm estado desconhecido |
| CTR-09 | Versão incompatível falha de forma tipada |
| CTR-10 | CAP-11 não entrega relatório sem compartilhamento autorizado |
| CTR-11 | Fonte duplicada por modelos não gera corroboração independente |
| CTR-12 | Retorno parcial mantém limitações e cobertura explícitas |
| CTR-13 | Evento repetido de revisão é idempotente conforme política |
| CTR-14 | Campos temporais preservam referência de fuso |
| CTR-15 | Alteração de método não reprocessa dados sem autorização |
| CTR-16 | Oportunidade expirada invalida uso atual sem apagar história |
| CTR-17 | Rota CAP-07 proposta não promove interesse da Pessoa |
| CTR-18 | Mensagem de falha não expõe conteúdo pessoal ou credenciais |

**Maturidade:** nenhum teste executado; G1 (contratos), G2 (dados/segurança) e G3 (testes) permanecem pendentes.

## 14. Decisões pendentes e próximo estudo
A resolver: schema formal JSON Schema/OpenAPI; enumerações definitivas; validação semântica por capacidade; política de idempotência, TTL e concorrência; identidade e autorizações por consumidor; política de eventos; tratamento de exceções; compatibilidade com protótipos Replit; métricas de testes de contratos.

Próximo passo recomendado: **GAI-INT-03 — Matriz de Testes Integrados, Critérios de Aceite e Gates**, com casos rastreáveis aos estados e contratos acima, responsáveis por adjudicação e critérios explícitos sem inventar resultados.

**Referências:** [GAI-INT-01](arquitetura-integrada-plano-validacao.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [Evidências](modelo-evidencias-rastreabilidade.md) · [Avaliação](avaliacao-validacao-qualidade.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Guivos AI e GKR preservam governanças independentes; Replit, Neo4j, provedores e gates permanecem inalterados.**
