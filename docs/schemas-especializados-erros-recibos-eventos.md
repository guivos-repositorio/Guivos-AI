# GAI-INT-09 — Schemas Especializados, Contratos de Erro e Recibos de Eventos
**Versão documental 3.3 · 31/10/2026**
**Estado:** oito schemas candidatos JSON Schema Draft 2020-12, sem homologação, sem teste de conformidade executado e sem integração a serviço operacional.

## 1. Objetivo
Avançar a formalização iniciada no [GAI-INT-08](catalogo-formal-schemas-compatibilidade-servicos.md), distinguindo falhas, confirmação de entrega/aplicação, vínculos de dependência e payloads especializados. Cada artefato em `schemas/candidate-v1/` é **candidato técnico** e não altera contrato implementado.

**Princípios:** fatos e autorizações permanecem nos serviços canônicos; Guivos AI produz interpretações; Guivos Intelligence orquestra a experiência; Neo4j pode armazenar projeções, mas não é automaticamente autoridade por todos os fatos. Nenhum contrato autoriza processamento de dados reais.

## 2. Artefatos adicionados
| Schema | Papel | Arquivo |
| --- | --- | --- |
| ErrorResponse | Código de falha, categoria, possibilidade de retentativa e mensagem segura | [error-response](../schemas/candidate-v1/error-response.schema.json) |
| EventReceipt | Registra etapas de recebimento, validação e aplicação de eventos | [event-receipt](../schemas/candidate-v1/event-receipt.schema.json) |
| DependencyEdge | Registra relação entre uma versão derivada e fonte/dependência | [dependency-edge](../schemas/candidate-v1/dependency-edge.schema.json) |
| CAP-04 GapResult | Estado de lacuna por requisito, evidências e limites | [cap04-gap-result](../schemas/candidate-v1/cap04-gap-result.schema.json) |
| CAP-05 PossibilityResult | Origem da possibilidade e estado de interesse da Pessoa | [cap05-possibility-result](../schemas/candidate-v1/cap05-possibility-result.schema.json) |
| CAP-07 PathResult | Caminho com etapas sem converter categoria em oferta existente | [cap07-path-result](../schemas/candidate-v1/cap07-path-result.schema.json) |
| CAP-08 OfferResult | Publicação, verificação e disponibilidade independentes | [cap08-offer-result](../schemas/candidate-v1/cap08-offer-result.schema.json) |
| CAP-11 ReportResult | Relatório, seções, estados e autorização de processamento | [cap11-report-result](../schemas/candidate-v1/cap11-report-result.schema.json) |

**Contagem:** três schemas do INT-08 + oito do INT-09 = **onze schemas candidatos**. Os arquivos do INT-08 foram preservados sem alteração.

## 3. Contrato de erro
`ErrorResponse` exige `request_id`, `api_contract_version` e objeto `error` com `code`, `category`, `retryable`, `message_safe`. Códigos candidatos: `unauthenticated`, `forbidden`, `invalid_contract`, `capability_not_enabled`, `context_version_conflict`, `upstream_unavailable`, `rate_limited`, `access_revoked`, `needs_review`, `internal_failure`.

**Regra:** uma falha não deve ser mascarada como sucesso nem expor dados de outras Pessoas, segredos, prompts internos ou estrutura confidencial. Um erro transitório pode admitir tentativa futura **somente quando idempotência, escopo e autorização forem verificados**.

## 4. Contrato de recibo de evento
`EventReceipt` identifica `event_id`, `receipt_id`, `consumer_ref`, `operation`, `result` e `recorded_at`.

Operações distintas: `event_received`, `event_validated`, `impact_assessed`, `validity_applied`, `consumer_acknowledged`, `reassessment_completed`, `delivery_revalidated`. Resultados: `applied`, `not_applied`, `blocked`, `failed`, `inconclusive`.

**Recebido não significa aplicado. Aplicado por um consumidor não comprova atualização de todos os demais.** Recibos necessitam proveniência e correlação autorizadas em uma implementação futura.

## 5. Contrato de dependência
`DependencyEdge` exige origem de derivação, referência de fonte, tipo de ligação, versão do contexto, sujeito e escopo de autorização. Tipos: `uses_source_version`, `uses_claim`, `derived_from_analysis`, `references_opportunity`, `uses_context_version`, `requires_scope`, `presented_by`.

A relação `presented_by` documenta projeção ou exibição; **não prova atenção, leitura, interesse, inscrição, participação ou conclusão**. Relações de grafo são projeções candidatas, não esquema físico Neo4j.

## 6. Payloads especializados — recorte inicial
- **CAP-04:** `confirmed_gap`, `possible_gap`, `no_gap`, `unknown` e `not_assessable`. Não converter desconhecido em déficit pessoal.
- **CAP-05:** `declared`, `adjacent`, `emerging`, `exploratory`; interesse validável, não presumido.
- **CAP-07:** `direct_supply` e `enabling_supply` são categorias; só incluir `offer_ref` quando houver fonte confirmável. O schema não prova a oferta.
- **CAP-08:** `publication_status`, `verification_status` e `availability_status` são campos independentes; publicação não garante vaga.
- **CAP-11:** geração, revisão e entrega são fases distintas; `sharing_scope_ref` opcional **não autoriza entrega sem verificação do serviço competente**.

São exemplos de **payload parcial**, não cobertura integral das capacidades. As CAP-01, 02, 03, 06, 09, 10, 12 e demais campos de cada CAP ainda requerem schemas específicos futuros.

## 7. Integração ao envelope INT-08
Os payloads específicos devem futuramente compor `AnalysisResponse.result` conforme `capability_id`, sob `oneOf`/`if-then` ou outra estratégia formal e validada. **Atualmente não há ligação executável que force essa relação**: o envelope do INT-08 mantém `result` extensível e os arquivos INT-09 são validados isoladamente.

Da mesma maneira, `ErrorResponse` ainda não forma união discriminada com `AnalysisResponse`; não há OpenAPI ou AsyncAPI homologado. Evitar declarar integração concluída.

## 8. Versionamento e compatibilidade
Todos os arquivos são candidatos em `candidate-v1`. Alterar enum, obrigatoriedade ou significado pode romper consumidores e exige revisão e testes de regressão. `api_contract_version`, `method_version`, `context_version`, `source_version` e `schema_version` não são intercambiáveis.

Schemas podem validar forma, mas não identidade/autorização, sequência de eventos, existência de vaga, veracidade de claims, cobertura de dependências ou aplicação de revogação.

## 9. Plano de testes de contrato — não executados
| ID | Cenário | Critério esperado |
| --- | --- | --- |
| INT09-T01 | ErrorResponse sem `error.code` | Rejeitar estrutura |
| INT09-T02 | Erro com dados confidenciais em `message_safe` | Detectar por revisão de segurança; schema isolado é insuficiente |
| INT09-T03 | EventReceipt sem `event_id` | Rejeitar estrutura |
| INT09-T04 | `event_received` registrado | Não inferir `validity_applied` |
| INT09-T05 | Recibo duplicado | Idempotência operacional, fora do schema |
| INT09-T06 | DependencyEdge sem escopo | Rejeitar estrutura |
| INT09-T07 | Dependência cíclica | Detectar por teste de grafo, fora do schema |
| INT09-T08 | CAP-04 `unknown` | Não promover para lacuna confirmada |
| INT09-T09 | CAP-05 exploratória | Não afirmar interesse validado |
| INT09-T10 | CAP-07 sem `offer_ref` | Não inventar oferta |
| INT09-T11 | CAP-08 publicada e disponibilidade desconhecida | Não afirmar vaga |
| INT09-T12 | CAP-11 rascunho sem permissão de entrega | Bloquear entrega |
| INT09-T13 | `AnalysisResponse.result` do tipo errado para CAP | Necessita união formal futura |
| INT09-T14 | Versão de contrato incompatível | Migração ou erro tipado |
| INT09-T15 | Consumidor de outro tenant | Negar por autorização, fora do schema |
| INT09-T16 | Revogação durante reprocessamento | Bloquear uso antes da entrega |
| INT09-T17 | Evento fora de ordem | Não retroceder estado |
| INT09-T18 | Falha de provedor e fallback não aprovado | Não fabricar sucesso |
| INT09-T19 | Fonte de oferta expirada | CAP-08/CAP-10 sinalizam obsolescência |
| INT09-T20 | Relatório já entregue | Não confundir entrega com leitura ou possibilidade de recolhimento |

Todos os cenários estão **planejados**, sem resultados de execução, revisão ou adjudicação.

## 10. Lacunas e critérios de gate
**G1 pendente:** faltam schemas dos demais payloads, união tipada de sucesso/erro, normalização de claims, perfis de timestamp com fuso e contratos normativos de revisão. **G2 pendente:** autorização, isolamento e revogação não se comprovam pelo JSON Schema. **G3 pendente:** nenhum validador/campanha de teste executado nesta etapa. **G4–G6 pendentes:** nenhuma integração, adjudicação ou liberação operacional.

O estudo seguinte está disponível em [GAI-INT-10 — Conformidade de Schemas, Casos de Contrato e Compatibilidade](conformidade-schemas-casos-contrato-compatibilidade.md), para definir validação automatizável com fixtures sintéticas e resultados reproduzíveis, preservando aprovação de gates separada.

**Referências:** [GAI-INT-08](catalogo-formal-schemas-compatibilidade-servicos.md) · [GAI-INT-07](contratos-eventos-projecao-dependencias.md) · [GAI-INT-04](catalogo-fixtures-rubricas-adjudicacao.md) · [CAP-04](cap-04-identificacao-qualificacao-lacunas.md) · [CAP-08](cap-08-qualificacao-oportunidades.md) · [CAP-11](cap-11-relatorio-trajetoria-possibilidades.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Nenhuma alteração operacional no Replit, Neo4j, provedores ou GKR.**
