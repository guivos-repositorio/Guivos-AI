# GAI-INT-34 — Envelope Tipado v2 Independente e Política Proposta de Ciclo de Vida
**Versão documental 6.1 · 31/10/2026**
**Estado:** schema candidato criado e publicado; sem validação executada, integração, homologação ou gate.

## 1. Artefato criado
Foi publicado [`analysis-response-typed.schema.json` v2 proposto](../schemas/candidate-v2-proposed/analysis-response-typed.schema.json) em diretório independente de `candidate-v1`. A definição de 14 cláusulas em `allOf` inclui:
- uma referência explícita ao envelope `analysis-response.schema.json` de `candidate-v1`;
- uma regra condicional de `lifecycle_status`;
- doze regras condicionais para resultados tipados das capacidades GAI-CAP-01 a GAI-CAP-12.

O resultado de **GAI-CAP-11** utiliza o schema [cap11 v2 proposto](../schemas/candidate-v2-proposed/cap11-report-result.schema.json). As outras 11 capacidades ainda referenciam contratos `candidate-v1`, mediante URIs absolutas.

## 2. Semântica de ciclo de vida — proposta que exige aprovação
| `lifecycle_status` | `result` no envelope v2 proposto | Justificativa |
| --- | --- | --- |
| `completed` | Obrigatório e validado pelo schema da capacidade | Resultado é parte do payload concluído |
| `accepted` / `queued` / `processing` | Proibido | Estado não demonstra conclusão do resultado |
| `awaiting_review` | Proibido | Revisão ainda pendente; alternativa pode ser negociada com produto |
| `failed` / `cancelled` | Proibido | Representação de erro ou cancelamento deve ser definida separadamente |

**Esta regra ainda não está homologada**; a proibição de resultados parciais deve ser revisada com os consumidores. A tentativa de enviar progresso parcial com `result` seria incompatível com a proposta.

## 3. Compatibilidade e limitações críticas
1. **Versão de protocolo ainda é `candidate-1`:** o envelope-base candidato v1 possui `api_contract_version: {const:"candidate-1"}`. Assim, o novo schema v2 é uma **revisão de formato em proposta**, não uma migração protocolar v2 pronta; decidir versão e negociação antes de uso.
2. **URI e referências:** usa `$id` de `candidate-v2-proposed` e `$ref` absolutos para os schemas candidatos v1 e cap11 v2. Um registry local versionado deverá resolver todos sem depender de consultas externas.
3. **Compatibilidade retroativa:** versões v1 que retornem `result` antes de `completed` ou concluídas com CAP-11 sem escopo de compartilhamento podem ser rejeitadas; não alterar os consumidores sem inventário real.
4. **Envelopes e estados:** `error-response.schema.json` é separado. Definir correlação, códigos, condições e semântica de falha com responsáveis técnicos.
5. **Ausência de observações de execução:** não houve validator, runner, instalação de dependências, testes de integração, contato com provedores ou ambiente operacional.

## 4. Matriz de casos conceituais a preparar
| ID | Cenário | Esperado na proposta |
| --- | --- | --- |
| ENV2-P01 | `completed` com CAP-11 `draft` e campos obrigatórios | Válido |
| ENV2-P02 | `queued` sem `result` e envelope íntegro | Válido |
| ENV2-P03 | `failed` sem `result` e envelope íntegro | Válido |
| ENV2-N01 | `completed` sem `result` | Inválido |
| ENV2-N02 | `queued` com `result` | Inválido |
| ENV2-N03 | `completed` CAP-11 `released_to_authorized_recipient` sem `sharing_scope_ref` | Inválido |
| ENV2-N04 | `completed` CAP-11 com `result.capability_id` diferente do envelope | Inválido |
| ENV2-N05 | `failed` com `result` | Inválido |

São **expectativas de desenho**, não observações de teste. Os 49 casos v1 e 15 casos v2 de GAI-INT-33 permanecem inalterados.

## 5. Governança
A preparação deste artefato decorre do encaminhamento da direção para envelope v2 separado. Não concede decisão de adoção, autorização do Pedido B ou do Pedido C, acesso a dados ou aprovação de G0–G6. PND-01 a PND-16 continuam em aberto.

**Próxima decisão material:** escolher política de respostas parciais, versão de protocolo e compatibilidade; somente depois preparar validação offline sob autorização específica.

Referências: [GAI-INT-33](compatibilidade-contrato-tipado-matriz-casos-v2.md) · [GAI-INT-32](schemas-candidatos-v2-propostas-sta01-sta02-sta03.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md).

## Atualização após GAI-DEC-012
A direção aprovou A1/B1/C1 somente como política de desenho. Foi criado [base candidate-2](../schemas/candidate-v2-proposed/analysis-response.schema.json), e o [envelope tipado v2](../schemas/candidate-v2-proposed/analysis-response-typed.schema.json) passou a referenciá-lo. O envelope anterior candidate-v1 permanece preservado; sem teste ou homologação.
