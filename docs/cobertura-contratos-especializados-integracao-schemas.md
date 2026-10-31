# GAI-INT-11 — Cobertura dos Contratos Especializados e Integração dos Schemas
**Versão documental 3.5 · 31/10/2026**
**Estado:** oito novos JSON Schemas candidatos, 24 fixtures sintéticas e executor offline preparado. Nenhum teste executado, contrato homologado ou gate liberado.

## 1. Objetivo
Ampliar a cobertura formal dos resultados especializados para **GAI-CAP-01 a GAI-CAP-12** e especificar como o campo `AnalysisResponse.result` deverá corresponder obrigatoriamente ao identificador `capability_id`.

**Atenção:** cobertura estrutural **não é** cobertura semântica integral das capacidades, nem comprovação de origem de dados, autorização, resultado clínico ou qualidade das análises. A CAP-12 é camada de API; seu payload candidato descreve metadados de serviço/escopo, não promete que a API produza análise de pessoa diretamente.

## 2. Cobertura anterior e novos artefatos
A rodada GAI-INT-09 disponibilizou payloads parciais de CAP-04, 05, 07, 08 e 11. A presente rodada adiciona os sete payloads ainda ausentes e um envelope composto.

| Arquivo criado | Capacidade / papel |
| --- | --- |
| [cap01-trajectory-result.schema.json](../schemas/candidate-v1/cap01-trajectory-result.schema.json) | Eventos de trajetória, origem e temporalidade |
| [cap02-moment-result.schema.json](../schemas/candidate-v1/cap02-moment-result.schema.json) | Dimensões do momento e estado de conhecimento |
| [cap03-evidence-result.schema.json](../schemas/candidate-v1/cap03-evidence-result.schema.json) | Claims, origem epistêmica e sustentação |
| [cap06-compatibility-result.schema.json](../schemas/candidate-v1/cap06-compatibility-result.schema.json) | Compatibilidade condicionada por requisito |
| [cap09-contradictions-result.schema.json](../schemas/candidate-v1/cap09-contradictions-result.schema.json) | Conflitos, fontes e revisão |
| [cap10-invalidation-result.schema.json](../schemas/candidate-v1/cap10-invalidation-result.schema.json) | Eventos de alteração e validade de derivados |
| [cap12-api-service-result.schema.json](../schemas/candidate-v1/cap12-api-service-result.schema.json) | Metadados de capacidade/API e escopo de consumidor |
| [analysis-response-typed.schema.json](../schemas/candidate-v1/analysis-response-typed.schema.json) | Associação condicional entre envelope e resultado da CAP |

**Catálogo:** 11 schemas anteriores + 8 novos = **19 schemas candidatos** na família `candidate-v1`.

## 3. Regra de integração do envelope
O schema `analysis-response-typed.schema.json` combina, por `allOf`, a estrutura de `analysis-response.schema.json` com regras `if/then`:

- Se `capability_id = GAI-CAP-01`, `result` deve satisfazer o schema CAP-01;
- Se `capability_id = GAI-CAP-08`, `result` deve satisfazer o schema CAP-08;
- A mesma lógica foi declarada para as **12 capacidades**.

Cada payload também especifica sua constante `capability_id` para evitar associação equivocada. O campo `result` torna-se obrigatório no envelope composto. O envelope original INT-08 permanece inalterado por compatibilidade documental.

**Limite importante:** os `$ref` dependem de resolução por um registry de schemas. Publicar o arquivo não configura validação automática em nenhum serviço; clientes que apenas validam o schema original **não** executam essas regras novas.

## 4. Convenções de interpretação
- CAP-01: relato e observação têm origens distintas; a ordem temporal depende de evidência.
- CAP-02: `unknown` não equivale a ausência da condição.
- CAP-03: claim `unsupported` não pode ser divulgado como fato.
- CAP-04: requisito e lacuna precisam de contexto específico.
- CAP-05: descoberta exploratória não prova interesse da Pessoa.
- CAP-06: avaliação por requisito não mede o valor de alguém.
- CAP-07: uma etapa `direct_supply` não prova oferta disponível.
- CAP-08: publicação, verificação e disponibilidade são independentes.
- CAP-09: concordância de GPT/Claude/Gemini não substitui evidência independente.
- CAP-10: validade derivada não substitui autorização canônica.
- CAP-11: geração e compartilhamento exigem controles próprios.
- CAP-12: metadados de escopo não concedem acesso ao histórico.

## 5. Fixtures e executor candidato
| Artefato | Objetivo |
| --- | --- |
| [typed-cases.json](../tests/contracts/candidate-v1/typed-cases.json) | **24 casos sintéticos**: 12 positivos, 12 negativos de divergência CAP envelope/payload |
| [run_typed_cases.py](../tests/contracts/run_typed_cases.py) | Validador offline com JSON Schema Draft 2020-12 e registry local para resolver referências |
| [cases.json](../tests/contracts/candidate-v1/cases.json) | Preserva os 25 casos anteriores, sem os reclassificar como executados |
| [run_schema_cases.py](../tests/contracts/run_schema_cases.py) | Preserva o executor básico dos schemas individuais |

O novo executor usa `jsonschema` e `referencing` para resolver as referências dos arquivos `candidate-v1` a partir de um registry local, sem depender de disponibilidade HTTP do GitHub Pages. O comando proposto, **para execução futura em ambiente autorizado**, é `python tests/contracts/run_typed_cases.py`.

**Nenhuma execução foi realizada nesta etapa.** Nenhum resultado observado, ambiente de teste, revisor humano ou aprovação foi registrado.

## 6. Matriz de teste estrutural
Cada payload possui:
1. Caso positivo com `capability_id` do envelope e do resultado compatíveis e atributos mínimos;
2. Caso negativo com o `capability_id` do envelope apontando para outra CAP enquanto `result` permanece com sua CAP de origem.

A validação negativa busca impedir que o Guivos Intelligence ou um parceiro receba `result` de tipo diferente do esperado pelo envelope. Os 24 casos não avaliam autorização de acesso, consistência de fontes, segurança dos provedores, qualidade de interpretações ou entrega a terceiros.

## 7. Compatibilidade e limites
- Continuam candidatos o envelope `AnalysisResponse` original e o novo `AnalysisResponseTyped`; a adoção deste é uma decisão de migração ainda pendente.
- Campos internos das CAPs são **mínimos estruturais**, não esquemas exaustivos de resultados analíticos.
- `additionalProperties:false` exige revisão formal ao acrescentar campos, evitando alegar compatibilidade aditiva automática.
- `AnalysisResponseTyped` não inclui união de `ErrorResponse` com sucesso; contrato de erro segue independente.
- Uma resposta estruturalmente válida pode estar obsoleta, sem sustentação ou não autorizada.
- Um `EventReceipt` de recebimento não comprova aplicação de invalidação por todos os serviços.
- Nenhuma integração com a POC do Replit, Neo4j ou provedores foi efetuada.

## 8. Próximas validações e gates
**G1:** revisar schemas com responsáveis, perfis formais de enum/timestamp, contrato de erros e compatibilidade de consumidores; **G2:** validar autorização, isolamento e revogação em sistemas apropriados; **G3:** executar casos sintéticos e registrar resultado reprodutível; **G4:** integração isolada; **G5:** adjudicação; **G6:** liberação expressa. Todos pendentes. A documentação G0 permanece parcial.

**Próximo estudo recomendado:** **GAI-INT-12 — Relatório de Conformidade e Estratégia de Homologação Contratual**, para especificar evidências de runs, política de compatibilidade, critérios de aceite e plano de fechamento das lacunas antes de qualquer liberação.

**Referências:** [GAI-INT-10](conformidade-schemas-casos-contrato-compatibilidade.md) · [GAI-INT-09](schemas-especializados-erros-recibos-eventos.md) · [GAI-INT-08](catalogo-formal-schemas-compatibilidade-servicos.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Guivos AI e GKR mantêm governanças independentes. Replit, Neo4j, provedores e gates permanecem inalterados.**
