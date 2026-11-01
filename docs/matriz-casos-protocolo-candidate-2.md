# GAI-INT-36 — Matriz de Casos do Protocolo candidate-2

**Versão documental 6.4 · 31/10/2026**  
**Estado:** catálogo sintético candidato, não executado.

## Escopo
A [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md) aprovou A1 + B1 + C1 apenas como política de desenho. A matriz preparada em [JSON](matriz-casos-protocolo-candidate-2.json) contém **18 casos** para o envelope tipado candidate-2: **8 esperados válidos** e **10 esperados inválidos**. As expectativas não são resultados de validação.

## Cobertura
| Grupo | Casos e objetivo |
| --- | --- |
| Conclusão | `completed` com resultado tipado CAP-11, ausência de `result`, divergência de capacidade |
| Processamento | `accepted`, `queued`, `processing`, `awaiting_review` sem resultado; rejeição de resultados prematuros |
| Falhas e cancelamentos | `failed` e `cancelled` sem `result`; rejeição de `result` nesses estados |
| Versão | `candidate-2` aceito; `candidate-1` rejeitado pelo envelope candidato v2 |
| Compartilhamento | CAP-11 liberado com referência de escopo; rejeição quando ausente ou vazia |

## Dependências e limites de compatibilidade
A leitura dos arquivos candidatos identifica: (a) envelope tipado v2 referenciando base candidate-2; (b) base candidate-2 declarando `api_contract_version=candidate-2`; (c) CAP-11 apontando ao resultado v2; (d) as onze outras capacidades mantendo payloads v1. Essa coexistência de versões é **proposta técnica**, não compatibilidade operacional demonstrada.

Seis verificações complementares do registry foram catalogadas, incluindo resolução de todos os `$ref` sem rede e definição futura de contrato correlacionado para falhas B1. O mecanismo de erro seguro B1 ainda não foi projetado como artefato candidate-2 e não é validado por esta matriz.

## Evidência de execução
**Nenhuma:** não houve Python, JSON Schema validator, instalação de bibliotecas, chamadas externas, leitura de sistemas privados nem atualização dos runners. Os 49 casos v1 e 15 casos da matriz anterior permanecem separados e sem execução verificada.

## Próximo gate documental
Revisar a consistência das expectativas, congelar commit/registry e identificar executor e revisor independente. A **execução de testes é Pedido B e continua não autorizada**. A inspeção operacional é Pedido C, igualmente não autorizada. G0 parcial; G1–G6 pendentes; 16 PNDs abertas.

Referências: [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md) · [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md) · [GAI-INT-33](compatibilidade-contrato-tipado-matriz-casos-v2.md).
