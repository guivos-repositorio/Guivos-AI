# GAI-INT-38 — Especificação de Executor Offline para 33 Casos v2
**Versão documental 6.6 · 31/10/2026**
**Estado:** projeto técnico não implementado, não autorizado para execução.

## 1. Escopo
Especificar, sem implementar ou executar, um executor independente para **15 casos** de `docs/matriz-casos-compatibilidade-v2-candidata.json` e **18 casos** de `docs/matriz-casos-protocolo-candidate-2.json`. Os dois runners Python existentes permanecem destinados exclusivamente aos 49 casos `candidate-v1`.

## 2. Entradas e adaptações obrigatórias
| Catálogo | Estrutura observada | Adaptação projetada |
| --- | --- | --- |
| GAI-INT-33 (15) | `cases[].schema` é nome lógico sem caminho; usa `expected_valid_v2`, e `expected_valid_v1` é previsão de comparação não observada | Resolver o nome lógico por mapa explícito e usar apenas `expected_valid_v2` para o alvo v2 |
| GAI-INT-36 (18) | `cases[].schema` é caminho de arquivo; usa `expected_valid`; contém status de execução não realizada | Resolver caminho exclusivamente da allowlist e usar `expected_valid` |
| Verificações adicionais | `typed_integration_checks` (5) e `registry_checks` (6) | **Não são fixtures JSON Schema** e não devem ser contabilizadas como os 33 testes; manter checklist separado, com observações estáticas e pendências |

**Mapa lógico explícito v2:** `cap11-report-result` → `schemas/candidate-v2-proposed/cap11-report-result.schema.json`; `event-receipt` → `schemas/candidate-v2-proposed/event-receipt.schema.json`; `canonical-event` → `schemas/candidate-v2-proposed/canonical-event.schema.json`. Outros nomes desconhecidos devem provocar interrupção, nunca resolução implícita.

**Regra de entrada:** `instance` deve existir, expectativa deve ser booleana e `case_id` deve ser único entre ambos os catálogos. Valores inesperados, ausência de path permitido ou dados fora de sintéticos interrompem antes da execução.

## 3. Registro local de schemas
1. Preparar allowlist imutável de schemas sob `schemas/candidate-v1/` e `schemas/candidate-v2-proposed/`; coletar `$id` e SHA-256 do conteúdo no momento do congelamento.
2. Recusar duplicidade de `$id`, referências a hosts externos, URI sem destino local, traversal de caminho, symlink fora da raiz ou URI que não corresponda ao conteúdo fixado.
3. Resolver `$ref` absolutos e relativos apenas em `referencing.Registry` local, sem rede. CAP-11 tipado usa schema v2; as outras 11 capacidades referenciam payloads v1; base de resposta candidate-2 permanece isolada.
4. Checar integridade estrutural dos documentos com `Draft202012Validator.check_schema` e usar `FormatChecker`, **apenas em campanha futura explicitamente autorizada**.
5. Falha de referência deve gerar erro de infraestrutura/manifesto, **não** ser contada como caso inválido esperado.

## 4. Interface de executor futura
**Entrada candidata:** `--manifest <path>`, `--catalog <id>`, `--evidence-out <path>`, `--offline`. Antes de iniciar, o executor precisará verificar autorização B identificável, commit congelado, ambiente isolado, executor/revisor nomeados e hashes de dependências.

**Processamento futuro:** normalizar caso → conferir integridade dos schemas → selecionar validator correspondente → avaliar instância sintética → comparar `observed_valid` versus expectativa → preservar erros e caminhos sanitizados → produzir evidência imutável. Nunca alterar fixtures ou ajustar expectativas automaticamente para obter sucesso.

**Contrato candidato de resultado por caso:** `case_id`, `catalog_id`, `schema_uri`, `schema_digest`, `expected_valid`, `observed_valid`, `matched`, `error_paths`, `failure_kind`, `duration_ms`. Campos de observação permanecem **ausentes** no manifesto desta especificação porque não ocorreu execução.

**Saída de campanha futura:** `campaign_id`, `authorization_ref`, `repository_sha`, `environment_ref`, `dependency_lock_digest`, `registry_digest`, `operator_ref`, `reviewer_ref`, `case_results`, `summary`, `limitations`, `incident_refs`, `evidence_digest`, `gate_decision_ref=null`.

## 5. Dependências e segurança
Os scripts atuais declaram `jsonschema>=4,<5` e `referencing>=0.35,<1`; ainda não há pinning verificável de Python, transitivas ou artefatos offline. Antes de qualquer campanha, gerar lockfile/digests e isolar execução sem Secrets, redes, dados pessoais ou conexões a Neo4j/GPT/Claude/Gemini/Replit. Não adicionar bibliotecas ou runners por mera aprovação deste documento.

## 6. Condições de interrupção
Ausência de autorização B, operador/revisor independente, SHA congelado, ambiente offline, integridade de hashes, resolução local dos `$ref`, catálogo sintético consistente ou possibilidade de acesso a rede/Secrets → **não iniciar**. Divergência inesperada, erro de infraestrutura, possível dado real e efeitos externos → interromper, registrar incidente e não produzir aprovação de gate.

## 7. Critérios de aceite do projeto técnico
- Mapear 15 + 18 casos sem confundir verificações documentais com testes.
- Não modificar `candidate-v1` ou alterar contagem de 49 casos.
- Resolver somente `$id`/$ref locais e negar ambiguidades.
- Definir evidência reproduzível com versão, hashes, expectativa e observação separadas.
- Definir lógica de erro de infraestrutura separada de divergência de caso.
- Aprovar desenho com donos técnicos e revisor independente antes de implementar.
- Autorizar separadamente implementação e, depois, qualquer execução do Pedido B.

**Estado:** especificação publicada; executor v2 não criado, testes não executados, Pedido B/C não autorizados, G0 parcial, G1–G6 pendentes, PND-01–16 abertas.

Referências: [GAI-INT-37](pacote-prontidao-testes-offline-candidate-2.md) · [GAI-INT-36](matriz-casos-protocolo-candidate-2.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md).
