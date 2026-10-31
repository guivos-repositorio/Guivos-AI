# GAI-INT-33 — Compatibilidade do Contrato Tipado e Matriz de Casos v2
**Versão documental 6.0 · 31/10/2026**
**Estado:** revisão estática e desenho de casos. Nenhum teste ou validador executado, nenhuma adoção de schema ou gate aprovado.

## 1. Escopo e evidência
Foram inspecionados `analysis-response-typed.schema.json`, `analysis-response.schema.json`, os três contratos isolados em `schemas/candidate-v2-proposed/` e o catálogo `typed-cases.json`, todos no repositório público Guivos AI.

**Verificação estrutural:** o contrato tipado candidate-v1 possui 13 blocos em `allOf` (um envelope-base e 12 condicionais por capacidade). A condicional de `GAI-CAP-11` refere-se a `cap11-report-result.schema.json` **relativamente ao $id em candidate-v1**, portanto não aponta automaticamente para `candidate-v2-proposed`. Os novos contratos de `event-receipt` e `canonical-event` **não fazem parte das referências desse envelope tipado**; são contratos auxiliares separados. Não cabe reescrever seus `$ref` no envelope como se fossem payloads de capacidade.

## 2. Matriz de compatibilidade
| Interface | Situação atual | Risco e encaminhamento |
| --- | --- | --- |
| Response typed v1 → CAP-11 v1 | Vínculo mantido | A publicação da proposta v2 não impõe o campo de sharing às respostas tipadas correntes |
| Response typed v2 futura → CAP-11 v2 proposta | Ainda inexistente | Criar envelope candidato separado, trocar exclusivamente a referência de CAP-11 e examinar resolução de URIs por registry |
| Response envelope v1 isolado | `result` genérico, `lifecycle_status` com estados intermediários | Contrato isolado não substitui validação de payload tipado |
| Typed `allOf` candidato | Exige `result` condicionado à capacidade inclusive se envelope estiver em `queued` ou `failed` | Definir protocolo de status sem payload antes de homologar resposta tipada v2 |
| Canonical event v2 / Event receipt v2 | Contratos independentes do typed response | Exigem versão/consumidores próprios; não ativar por simples existência no diretório |
| Catalog `typed-cases.json` | 24 casos existentes (12 positivos e 12 negativos) | Não reescrever nem contabilizar como execução dos casos v2 |

## 3. Matriz de casos preparada (sem execução)
A [matriz JSON de casos candidatos](matriz-casos-compatibilidade-v2-candidata.json) contém **15 casos de desenho**: 6 esperados válidos e 9 esperados inválidos. Distribuição: STA-01 (5), STA-02 (5), STA-03 (5). Há ainda **5 verificações de integração**, das quais 2 são constatações estáticas e 3 são verificações futuras a executar somente após autorização específica.

| Achado | Casos positivos | Casos negativos | Invariante |
| --- | --- | --- | --- |
| STA-01 | Rascunho sem escopo; liberado com escopo | Liberação sem escopo; pronto para liberação sem escopo; escopo vazio | Exigência condicional de `sharing_scope_ref` |
| STA-02 | Recebimento sem aplicação; aplicação versionada | `event_received/applied`; `event_validated/applied`; aplicação sem versão | Relação entre fase de operação e efeito |
| STA-03 | Revogação com escopos; evento global sem sujeito | Revogação sem campos; sujeito nulo; política vazia | Identidade/política para eventos de revogação |

**Os casos são exemplos sintéticos de projeto** e as expectativas ainda não foram comparadas com um validador. O arquivo não é um catálogo de resultados observados.

## 4. Achados adicionais
**COMP-01:** a nova exigência em `cap11` só será efetiva no endpoint tipado quando o contrato v2 e o registry local forem explicitamente compostos. A alteração do arquivo isolado não altera o comportamento atual de nenhum consumidor.

**COMP-02:** os candidatos v2 para eventos e recibos precisam de um plano de versão separado do contrato de análise; não há evidência de integração existente.

**COMP-03:** o uso de `allOf` com condicionais não decide se `result` deve ser obrigatório para respostas em progresso. Essa decisão é uma dependência de produto/contrato e não deve ser presumida.

**COMP-04:** um escopo de compartilhamento não prova sua validade jurídica ou operacional. Resultados `applied` e eventos de revogação exigem verificação adicional de efeitos no serviço canônico.

## 5. Critérios para eventual campanha de testes
Antes de executar o Pedido B: decisão de autorização específica, executor, revisor independente, SHA congelado, registry v2 explícito, dependências e ambiente isolado, pacote de evidências e critérios de encerramento. O manifesto existente permanece `not_authorized`.

## 6. Envelope v2 preparado
O [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md) publicou um envelope tipado v2 independente, com CAP-11 v2 e regra candidata para estado de conclusão. Continua sem testes ou adoção.

## 7. Próxima decisão
A direção pode autorizar **somente a preparação documental de um envelope tipado v2 alternativo** (sem ativação nem testes), condicionada à decisão sobre respostas intermediárias `queued/failed`. **Esta publicação não autoriza a execução do Pedido B ou inspeção C.**

**Estado preservado:** 19 schemas candidate-v1 e três candidates v2 separados; 49 fixtures v1 ainda não executadas; G0 parcial e G1–G6 pendentes; PNDs abertas.

Referências: [GAI-INT-32](schemas-candidatos-v2-propostas-sta01-sta02-sta03.md) · [GAI-INT-31](propostas-correcao-contratos-prioritarios-sta01-sta02-sta03.md) · [GAI-REV-001](relatorio-revisao-estatica-autorizada-pedido-a.md).
