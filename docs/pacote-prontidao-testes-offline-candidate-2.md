# GAI-INT-37 — Pacote de Prontidão para Campanha Sintética Offline
**Versão documental 6.5 · 31/10/2026**
**Estado: preparação, não autorização de execução.**

## 1. Objetivo e limites
Organizar a futura verificação estrutural dos contratos Guivos AI somente com dados sintéticos, dentro do Pedido B **ainda não autorizado**. O pacote é documental: nenhum script foi executado, dependência instalada, segredo consultado ou ambiente operacional acessado.

Referência de planejamento: commit GitHub `f787ba13c754d9d45dc12866f1a1d59ebf247e8f`. **Não é um congelamento de execução**: o SHA definitivo deve ser escolhido e fixado depois da conclusão dos artefatos e antes de qualquer campanha autorizada.

## 2. Inventário de casos
| Catálogo | Casos documentados | Executor atual | Situação |
| --- | ---: | --- | --- |
| `tests/contracts/candidate-v1/cases.json` | 25 | `run_schema_cases.py` | Runner existente, não executado |
| `tests/contracts/candidate-v1/typed-cases.json` | 24 | `run_typed_cases.py` | Runner existente, não executado |
| `docs/matriz-casos-compatibilidade-v2-candidata.json` | 15 | Nenhum homologado | Matriz de desenho, formato específico |
| `docs/matriz-casos-protocolo-candidate-2.json` | 18 | Nenhum homologado | Matriz de desenho, formato específico |
| **Total** | **82** | **Dois runners v1** | **Zero execuções verificadas** |

**Bloqueio técnico:** os runners atuais usam caminhos fixos `candidate-v1`, não consomem automaticamente matrizes v2, e o runner tipado monta registry apenas da pasta v1. Não é correto afirmar que os 82 casos estão prontos para execução só porque estão catalogados. Será necessário preparar e revisar executor v2 independente e registry offline para resolver as referências cruzadas entre candidate-v1 e candidate-v2-proposed. Sua construção e posterior execução exigem decisões delimitadas.

## 3. Dependências e congelamento de versões
Os scripts existentes declaram `jsonschema>=4,<5`, e o runner tipado acrescenta `referencing>=0.35,<1`; não declaram versão exata de Python nem hashes/lockfiles. **Versões instaladas e integridade não foram verificadas.**

Antes de executar, registrar: SHA imutável de todo o repositório; hash/digest de cada schema e catálogo; versão exata de Python, jsonschema, referencing e dependências transitivas; artefatos de instalação em cache sem acesso externo; ambiente isolado sem rede nem credenciais; lista e hash do registry local; catálogo de casos escolhido e expectativa imutável.

## 4. Evidências mínimas
- Identificador único de campanha, autorização B específica, executor e revisor independente;
- commit congelado, hashes dos arquivos e dependências;
- manifesto do ambiente offline e comprovação de ausência de credenciais/dados reais;
- resultado por caso: ID, schema, versão, esperado, observado, erros formatados e classificador de divergência;
- totais, divergências, limitações, incidente, decisão de revisão e assinatura/aceite de governança;
- evidência de que nenhum endpoint externo foi consultado;
- adjudicação independente antes de qualquer proposta de gate.

Usar como inspiração os templates já existentes `evidence-package-template.json` e `gate-review-template.json` — ambos seguem **não preenchidos**.

## 5. Condições de interrupção
Interromper e registrar incidente quando ocorrer: tentativa de rede externa, acesso a segredo, dados não sintéticos, divergência de versão/SHA, schema `$ref` não resolvido, instalação fora do ambiente isolado, efeito colateral inesperado, evidência inconsistente ou ausência de responsável/revisor nomeado. Sem autorização expressa, a própria tentativa de execução é condição de não início.

## 6. Critérios de entrada e de saída
**Entrada (não satisfeita):** decisão específica do Pedido B; operador identificado; revisor independente; escopo de catálogos; commit congelado; lockfile/digests; ambiente offline; runner v2/registry compatível; fixtures revisadas; critérios de parada aprovados.

**Saída (futura):** evidências completas e resultados revisados; falhas classificadas; riscos e limitações registrados; proposta separada de adjudicação. **Passar em testes estruturais não aprova privacidade, semântica, integração, produção ou G0–G6.**

## 7. Situação de autoridade
GAI-DEC-012 aprovou A1/B1/C1 somente como política de desenho. GAI-DEC-011 mantém controle central das autorizações. **Pedido B não autorizado; Pedido C não autorizado.** Nenhum gate aprovado, G0 parcial, G1–G6 pendentes, 16 PNDs abertas.

[Manifesto JSON deste pacote](manifesto-prontidao-testes-offline-candidate-2.json) · [GAI-INT-36](matriz-casos-protocolo-candidate-2.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md).
