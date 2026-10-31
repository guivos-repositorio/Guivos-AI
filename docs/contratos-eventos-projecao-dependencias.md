# GAI-INT-07 — Contratos de Eventos e Projeção de Dependências
**Versão documental 3.1 · 31/10/2026**
**Estado:** especificação técnica conceitual. Não constitui schema homologado, alteração de banco Neo4j, código executado, ativação de fluxo ou gate aprovado.

## 1. Objetivo e escopo
Detalhar os contratos lógicos para eventos **emitidos por serviços canônicos** e os vínculos de derivação usados para localizar, invalidar e eventualmente reavaliar resultados das CAP-01 a CAP-12. Completa GAI-INT-06 sem substituir CAP-10, INT-05 ou INT-02.

Princípios: origem autenticada; dados mínimos; versão explícita; idempotência; semântica de tempo; isolamento da Pessoa e de tenants; escopo de autorização; propagação verificável e **falha segura**. Evento recebido não equivale a efeito aplicado. Neo4j é uma opção de projeção relacional, não autoridade jurídica ou única fonte transacional.

## 2. Autoridade e fluxo de informação
| Componente | Propriedade funcional | Restrições |
| --- | --- | --- |
| Contexto canônico | Declarações, correções, objetivos, versões | Emite eventos autenticados; não delega a LLM |
| Oportunidades | Publicação, requisitos, validade e status | CAP-08 não inventa vagas ou eventos |
| Identidade/autorização | Finalidades, escopos, revogações e vínculos | Prioridade de bloqueio antes de reprocessamento |
| Serviço de eventos | Entrega, repetição, retenção e evidência de transporte | Não é autoridade pelo conteúdo do evento |
| Projeção de dependências | Índice de fontes, claims, análises, versões e consumidores | Reconstruível de registros autorizados |
| Guivos AI CAP-10 | Impacto analítico e reavaliação condicionada | Não modifica fatos nem apaga dados por conta própria |
| Intelligence e API CAP-12 | Revalidar na leitura, suprimir resultados obsoletos | Não afirmar confirmação de atualização sem recibo |
| Armazenamento/Neo4j | Relações, proveniência e projeções sob política | Sem leitura direta irrestrita pelos provedores de IA |

## 3. Envelope comum de evento (candidato)
```json
{
  "event_id": "synthetic-event-001",
  "event_type": "person_statement_corrected",
  "schema_version": "candidate-1",
  "producer_service_ref": "canonical-context",
  "aggregate_ref": "synthetic-statement",
  "aggregate_version": "v4",
  "prior_version": "v3",
  "subject_scope_ref": "synthetic-subject",
  "tenant_scope_ref": "synthetic-tenant",
  "occurred_at": "2026-10-31T13:10:00-03:00",
  "recorded_at": "2026-10-31T13:10:03-03:00",
  "correlation_id": "synthetic-correlation",
  "authorization_policy_ref": "policy-ref",
  "payload_ref": "restricted-change-record"
}
```
Campos são candidatos, não um contrato implementado. `payload_ref` aponta para registro restrito; não carregar contribuições pessoais, anexos ou segredos no barramento sem necessidade. Identificadores e versões não são prova de origem: exigir autenticação do emissor e autorização para consumo.

## 4. Famílias de eventos
| Família | Exemplos | Reação necessária |
| --- | --- | --- |
| Contexto | `person_statement_corrected`, `goal_revised`, `context_revision_published` | Checar claims vinculados e versão |
| Evidências | `source_corrected`, `source_withdrawn` | Revisar suporte e hipóteses dependentes |
| Oportunidades | `opportunity_requirement_changed`, `opportunity_expired`, `opportunity_cancelled` | Atualizar CAP-08 e usos relacionados |
| Autorização | `authorization_scope_revoked`, `authorization_scope_expired` | Bloquear uso incompatível antes da análise |
| Método | `method_version_withdrawn` | Revisar saídas daquele método após decisão |
| Relatórios | `report_access_restricted` | Impedir consultas e entregas futuras não permitidas |

Um evento de revogação **não ordena automaticamente exclusão física de todos os registros**. A política e a autoridade do armazenamento definem medidas cabíveis.

## 5. Semântica temporal e versionamento
- `occurred_at`: quando ocorreu a mudança; `recorded_at`: quando foi registrada; `received_at`: quando cada consumidor recebeu; `applied_at`: quando uma consequência foi aplicada.
- `aggregate_version` governa ordenação por entidade de origem. Não presumir ordem global entre serviços distintos.
- `schema_version` refere-se ao formato do evento; `method_version`, `context_version` e `analysis_version` são dimensões separadas.
- Eventos antigos, repetidos e fora de ordem exigem deduplicação, comparação de versão e reconciliação com fonte canônica.
- Mudança entre versões não prova impacto material até examinar dependências e claims.

## 6. Modelo lógico da projeção de dependências
Entidades candidatas: `SourceVersion`, `Claim`, `AnalysisVersion`, `OpportunityVersion`, `ContextVersion`, `ReportVersion`, `ConsumerProjection`, `AuthorizationScopeRef`, `EventReceipt`.

Arestas lógicas: `SUPPORTS_CLAIM`, `USES_SOURCE_VERSION`, `USES_CLAIM`, `DERIVED_FROM_ANALYSIS`, `REFERENCES_OPPORTUNITY`, `USES_CONTEXT_VERSION`, `REQUIRES_SCOPE`, `PRESENTED_BY`, `SUPERSEDES`.

Cada vínculo deve ter origem, tipo, versão, tempo e finalidade pertinentes. Uma aresta `PRESENTED_BY` não comprova que a Pessoa percebeu, aceitou ou participou de uma oportunidade.

### Exemplo semântico
```text
Fonte de rotina v3 → Claim A → CAP-02 análise v1
                                      ↓
                           CAP-06 compatibilidade v1
                                      ↓
                            CAP-07 caminho v1
                                      ↓
                         CAP-11 relatório versão 1

Fonte de rotina v4 → novo contexto → revisar a cadeia dependente.
Possibilidade não dependente da rotina → preservar, se fundamentada.
```

## 7. Requisitos de projeção e consulta
- Chaves lógicas estáveis para a combinação entidade + versão + escopo, sem codificar identificação pessoal no ID.
- Projeção somente de relações permitidas, com acesso mediado por serviço; não expor a existência de registros restritos a outro tenant.
- Índices candidatos por `source_ref/source_version`, `claim_id`, `analysis_id`, `subject_ref` autorizado, `context_version`, `authorization_scope_ref` e `validity_status`.
- Consulta de impacto percorre dependências **diretas e transitivas**, com limites de profundidade/volume e política de autorização.
- Manter evidência de cobertura do índice; índice incompleto não permite alegar “nenhum derivado afetado”.
- A projeção pode ser reconstruída por eventos/versões canônicos autorizados; divergências exigem reconciliação.
- Escolha entre Neo4j, armazenamento relacional, event log e outbox transacional é decisão de implementação pendente.

**Não criar esquema físico Neo4j neste documento.**

## 8. Contrato lógico de registro de dependência
```json
{
  "dependency_id": "synthetic-dependency-001",
  "derived_ref": "synthetic-cap06-analysis-v2",
  "derived_type": "analysis_version",
  "source_ref": "synthetic-statement",
  "source_version": "v3",
  "dependency_kind": "uses_source_version",
  "context_version": "context-20",
  "subject_scope_ref": "synthetic-subject",
  "authorization_scope_ref": "scope-ref",
  "recorded_at": "2026-10-31T13:00:00-03:00",
  "provenance_ref": "synthetic-claim-A"
}
```

## 9. Contratos de recibo: transporte, aplicação e reavaliação
| Recibo | Confirma | Não confirma |
| --- | --- | --- |
| `event_received` | Consumidor recebeu envelope | Impacto processado |
| `event_validated` | Origem/versão aceitas | Todas as dependências encontradas |
| `impact_assessed` | Análises afetadas avaliadas | Invalidação propagada |
| `validity_applied` | Estado persistido no domínio responsável | Cache externo atualizado |
| `consumer_acknowledged` | Consumidor confirmou operação específica | Reprocessamento semântico concluído |
| `reassessment_completed` | Nova análise versionada concluída | Interesse/aceite da Pessoa |
| `delivery_revalidated` | Destinatário autorizado no instante de entrega | Leitura efetiva da informação |

Um único campo `processed=true` não pode encobrir falha parcial. Proposta de recibo inclui `event_id`, `consumer_ref`, `operation`, `result`, `applied_version`, `recorded_at` e `limitations`.

## 10. Consistência e falhas
**Padrão candidato:** entrega ao menos uma vez, consumidores idempotentes, reconciliação periódica, verificação de autorização antes de leitura/entrega. Isto é **proposta**, não garantia de sistema existente.

Sem exactly-once ou transação distribuída presumida. Em duplicação, não duplicar efeitos; em atraso, não promover versão antiga; em falha de projeção, bloquear afirmação de atualidade sem evidência. Registros de falha e tentativas futuras devem respeitar minimização e quotas. Envio de eventos para parceiros requer escopo e política específica.

## 11. Regras de segurança
O barramento não poderá ser usado como canal de exfiltração de conteúdo pessoal; URLs e payloads provenientes de terceiros são dados não confiáveis. Autenticação do publicador, controle por consumidor, isolamento por Pessoa/tenant e política de expiração devem ser verificados nos serviços competentes. Revogação tem prioridade sobre reprocessamento, mas retenção e eliminação exigem decisão de autoridade própria.

## 12. Cenários sintéticos de avaliação (nenhum executado)
| ID | Cenário | Oráculo esperado |
| --- | --- | --- |
| INT07-E01 | Evento duplicado | Um efeito lógico idempotente |
| INT07-E02 | Duas versões fora de ordem | Não retroceder estado |
| INT07-E03 | Evento de origem forjada | Rejeição |
| INT07-E04 | Payload referencia dado não autorizado | Negar acesso |
| INT07-E05 | Fonte v4 substitui v3 | Localizar claims dependentes |
| INT07-E06 | Cadeia transitiva CAP-02→06→07→11 | Propagar marcação relevante |
| INT07-E07 | Possibilidade independente | Evitar falsa invalidação |
| INT07-E08 | Oferta expirada | CAP-08 não afirma vaga vigente |
| INT07-E09 | Autorização revogada durante execução | Negar nova leitura/entrega |
| INT07-E10 | API de parceiro em outro tenant | Bloquear sem vazamento |
| INT07-E11 | Recibo de entrega sem aplicação | Não declarar concluído |
| INT07-E12 | Cache falha ao aplicar evento | Registrar pendência e reautorizar |
| INT07-E13 | Projeção Neo4j indisponível | Cobertura não confirmada, falha segura |
| INT07-E14 | Índice de dependências incompleto | Não concluir impacto zero |
| INT07-E15 | Retorno tardio de modelo | Rejeitar versão obsoleta |
| INT07-E16 | Método antigo retirado | Revisar dependentes sob política |
| INT07-E17 | Conteúdo sensível no envelope | Rejeitar/minimizar |
| INT07-E18 | Evento válido, análise sem autorização atual | Bloquear reprocessamento |
| INT07-E19 | Reentrega com mesmo event_id, versão divergente | Detectar integridade inconsistente |
| INT07-E20 | Consulta de impacto recursiva cíclica | Evitar loop e registrar limite |
| INT07-E21 | Exigência de exclusão versus retenção aplicável | Encaminhar ao domínio competente |
| INT07-E22 | Destinatário já recebeu relatório | Não alegar recolhimento automático |

## 13. Gates e decisões pendentes
G0 permanece parcial; G1 necessita schemas e compatibilidade formal; G2 exige autoridade de eventos, isolamento e revogação; G3 exige execução de fixtures; G4 requer fluxo controlado com recibos; G5 revisão/adjudicação; G6 liberação explícita e observabilidade. Nenhum gate passou por avaliação operacional.

**A decidir:** modelo de dados da projeção; contratos JSON Schema/AsyncAPI; eventos por domínio; outbox/inbox e reconciliação; garantias de entrega; TTL de caches; índices e segregação Neo4j; cronologia entre agregados; auditoria de recibos; responsáveis pelos gates.

**Catálogo candidato publicado:** [GAI-INT-08 — Schemas e Compatibilidade entre Serviços](catalogo-formal-schemas-compatibilidade-servicos.md), como etapa preparatória para validação técnica.

**Referências:** [GAI-INT-06](modelo-dependencias-eventos-propagacao-invalidacao.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md) · [Autoridade e Memória](autoridade-dados-memoria-contexto.md).

**Replit, Neo4j, provedores e GKR permanecem inalterados.**
