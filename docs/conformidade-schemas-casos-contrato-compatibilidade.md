# GAI-INT-10 — Conformidade de Schemas, Casos de Contrato e Compatibilidade
**Versão documental 3.4 · 31/10/2026**
**Estado:** catálogo sintético e executor offline publicados. Não há resultados de execução, homologação de schema, integração operacional ou gate aprovado.

## 1. Objetivo
Preparar um protocolo reprodutível de conformidade estrutural para os **11 JSON Schemas candidatos** publicados em GAI-INT-08 e GAI-INT-09. Separar explicitamente: (a) presença/forma dos campos, (b) consistência semântica entre campos, (c) autorização/privacidade, (d) integração e propagação de eventos, (e) adjudicação humana. Uma comparação estrutural bem-sucedida **não** cobre (b) a (e).

## 2. Entregas versionadas
| Artefato | Papel |
| --- | --- |
| [cases.json](../tests/contracts/candidate-v1/cases.json) | Catálogo de 25 instâncias sintéticas, resultado estrutural esperado e schema de referência |
| [run_schema_cases.py](../tests/contracts/run_schema_cases.py) | Executor offline com jsonschema Draft 2020-12 e FormatChecker |
| [Schemas candidate-v1](../schemas/candidate-v1/analysis-request.schema.json) | Contratos propostos para análise, evento, erro, recibo, dependência e resultados selecionados |

O catálogo contém **11 casos estruturalmente válidos, 11 negativos por remoção de campo obrigatório e três negativos adicionais** (ID de capacidade inválido, disponibilidade fora do enum e campo inesperado). A cobertura é inicial, não exaustiva.

## 3. Matriz de conformidade inicial
| Schema | Caso válido | Negativo obrigatório | Dimensão de risco adicional |
| --- | --- | --- | --- |
| AnalysisRequest | Requisição sintética | Ausência de request_id | Capability ID fora do catálogo |
| AnalysisResponse | Resposta concluída com limitações | Ausência de support_status | Campo inesperado |
| CanonicalEvent | Alteração canônica sintética | Ausência de produtor | Autenticidade e ordenação fora do schema |
| ErrorResponse | Negativa de autorização | Ausência do objeto error | Mensagem segura exige revisão |
| EventReceipt | Recibo de recebimento | Ausência de event_id | Recebido ≠ aplicado |
| DependencyEdge | Dependência com escopo | Ausência de escopo | Permissões e ciclos fora do schema |
| CAP-04 GapResult | Requisito desconhecido | Ausência de gap_status | Unknown ≠ gap confirmado |
| CAP-05 PossibilityResult | Possibilidade exploratória | Ausência de interest_status | Interesse não presumido |
| CAP-07 PathResult | Etapa esclarecedora | Ausência de path_ref | Categoria ≠ oferta real |
| CAP-08 OfferResult | Publicada sem vaga confirmada | Ausência de availability_status | Estado fora do enum |
| CAP-11 ReportResult | Relatório rascunho | Ausência de processing_scope_ref | Entrega exige autorização própria |

## 4. Procedimento de execução futura
A execução, quando expressamente autorizada, deverá ocorrer **em ambiente isolado e somente com fixtures sintéticas**:
1. Identificar commit da suite e todos os schemas.
2. Registrar ambiente Python e versão da dependência `jsonschema`.
3. Instalar validador compatível em ambiente aprovado.
4. Executar `python tests/contracts/run_schema_cases.py` na raiz do repositório.
5. Registrar cada `case_id`, validade esperada, validade observada, divergência e causa.
6. Preservar saída e checksum dos artefatos em local autorizado.
7. Abrir defeitos quando houver falha; executar novo run após correção, sem sobrescrever o histórico.
8. Solicitar revisão independente e posterior decisão de gate, sem presumir aprovação por contagem de casos.

**Comando e executor são instruções para futura execução.** Esta publicação não afirma que o comando foi executado.

## 5. Modelo proposto de resultado e evidência
Cada execução futura deverá produzir `run_id`, `catalog_version`, `schema_commit_refs`, `environment_ref`, `validator_version`, `case_results[]`, `observed_at`, `failure_refs[]` e `review_status`. O executor entregue imprime resultados por caso, **mas ainda não gera relatório de execução imutável**, e não deve ser tratado como instrumento de homologação.

Estados distintos: `planned`, `executed`, `failed_to_execute`; comparações `pass`, `fail`, `inconclusive`; revisão `not_reviewed`, `under_review`, `adjudicated`.

**Estado real desta rodada:** 25 casos preparados, 0 runs registrados, 0 adjudicações registradas.

## 6. Compatibilidade e semântica que JSON Schema não testa
- A existência de `authorization_scope_ref` não comprova autorização efetiva.
- `lifecycle_status=completed` não demonstra evidência suficiente nem atualidade.
- `publication_status=published` não implica `availability_status=confirmed_available`.
- `event_received` não implica aplicação de invalidação em todos os consumidores.
- Uma declaração ausente não significa incapacidade da Pessoa.
- Schema do resultado especializado ainda não é automaticamente vinculado por `capability_id` ao `AnalysisResponse.result`.
- Mensagens seguras e diferenças entre tenants exigem testes semânticos e de segurança.
- Dados de teste são sintéticos; não copiar registros pessoais do Replit/Neo4j para formar fixtures.

## 7. Compatibilidade entre versões e evolução
A versão `candidate-1` permanece **não homologada**. Para mudanças incompatíveis em enums, obrigatoriedade, campos e semântica, exigir versão nova e matriz de consumidores. Testar pelo menos: candidato atual com casos atuais; candidato novo com casos legados; emissão antiga contra consumidor novo; emissão nova contra consumidor antigo; erro/recibo fora da versão esperada.

Os schemas possuem `additionalProperties:false` em diversos envelopes. Adicionar campo pode quebrar validação estrita e deve passar por revisão de contrato, não ser assumido aditivo automaticamente.

## 8. Critérios preliminares de aceite e gates
| Dimensão | Evidência futura necessária | Estado |
| --- | --- | --- |
| G1 Contratos | Schemas aprovados, cobertura por capacidade e teste executado | Pendente |
| G2 Segurança | Autorização, isolamento, revogação e validação de fontes | Pendente |
| G3 Testes | Runs rastreáveis e casos negativos com resultado observado | Pendente |
| G4 Integração | Replit/Intelligence/Guivos AI em ambiente controlado, após autorização | Pendente |
| G5 Revisão | Adjudicação independente por responsáveis designados | Pendente |
| G6 Liberação | Aprovação delimitada, observabilidade, custos e rollback | Pendente |

Nenhum desses gates é aprovado automaticamente pela publicação da suite. G0 continua com pendências documentais.

## 9. Lacunas prioritárias
1. Finalizar schemas das capacidades restantes e vincular `AnalysisResponse.result` ao schema específico.
2. Formalizar contrato de erros como união discriminada de sucesso/falha.
3. Adicionar fixtures de datas inválidas, `null`, versões incompatíveis e eventos em conflito.
4. Especificar fixtures semânticas de autorização e isolamento por tenant.
5. Capturar relatórios imutáveis de runs e evidência de revisão humana.
6. Aprovar versões, critérios de severidade, política de compatibilidade e responsáveis.
7. Separar formalmente teste de estrutura, teste de domínio e testes integrados sem dados reais.

**Estudo seguinte publicado:** [GAI-INT-11 — Cobertura dos Contratos Especializados e Integração dos Schemas](cobertura-contratos-especializados-integracao-schemas.md), antes de considerar homologação G1.

## 10. Referências
[GAI-INT-08](catalogo-formal-schemas-compatibilidade-servicos.md) · [GAI-INT-09](schemas-especializados-erros-recibos-eventos.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [GAI-INT-04](catalogo-fixtures-rubricas-adjudicacao.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Replit, Neo4j, provedores, GKR e gates operacionais não foram alterados.**
