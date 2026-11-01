# GAI-INT-39 — Implementação Isolada do Executor Offline v2

**Versão documental 6.7 · 31/10/2026**  
**Estado:** código criado por autorização de implementação, não executado ou homologado.

## Entrega confirmada
Foi criado [`tests/contracts/run_candidate_v2_cases.py`](../tests/contracts/run_candidate_v2_cases.py), independente dos runners v1, para processar os **33 casos sintéticos candidatos v2**. A autorização dada pela direção por "de acordo, segue" refere-se somente à criação de código, sem autorizar o Pedido B (execução).

## Fluxo implementado em código, ainda não testado
1. Exige parâmetros explícitos `--authorization`, `--repo-sha` e `--evidence-out`; sem parâmetros ou autorização compatível recusa iniciar.
2. Exige autorização estruturada e específica com `approved=true`, `scope=offline_synthetic_B`, confirmação de isolamento offline, hash do lockfile de dependências, SHA do repositório, operador e revisor distintos.
3. Carrega os 15 casos de GAI-INT-33 com mapeamento explícito dos três nomes lógicos, e os 18 casos de GAI-INT-36 com caminhos allowlist. Verifica contagem e unicidade dos IDs.
4. Constrói `referencing.Registry` apenas com JSON Schemas sob `candidate-v1` e `candidate-v2-proposed`; exige `$id` compatível com caminho e rejeita referências externas não representadas localmente.
5. Em execução futura, usaria `Draft202012Validator` e `FormatChecker` e geraria evidências por caso, com expectativa e observação separadas.
6. Recusa sobrescrever evidências e grava o resultado fora do repositório. Não chama Replit, Neo4j, GPT, Anthropic ou Gemini.

## Limitações relevantes
**O código não foi executado nem passou por revisão independente.** Uma verificação estática das strings publicadas não comprova execução, conformidade, segurança ou reprodutibilidade. O arquivo de autorização fornecido à execução será um documento de controle que ainda não existe e requer aprovação explícita da direção.

A presença do sinal `offline_isolation_confirmed=true` **não bloqueia acesso à rede por si só**; a campanha deverá ocorrer em ambiente externo isolado e validado. A integridade da dependência e o SHA informado ainda não são verificados contra o estado real pelo código, e a prova de ambiente exige controles externos. A captura de uma falha não substitui um sistema de auditoria; erros de resolução e inconsistências de infraestrutura devem impedir qualquer interpretação de aprovação.

## Pendências antes de autorizar execução
- Revisão estática independente do novo runner, incluindo falhas de entrada, registry e segurança.
- Decisão específica do Pedido B com escopo, ambiente, executor, revisor e duração.
- Ambiente isolado sem rede/Secrets/dados reais, bloqueado externamente.
- Versões de Python, `jsonschema`, `referencing` e transitivas imutáveis, com hashes de pacotes.
- Commit e artefatos congelados, evidências assinadas e critérios de parada.
- Nenhuma decisão de gate pode ser inferida de `matched=33`.

## Situação preservada
Runners v1 e seus 49 casos preservados; matrizes v2 de 15 e 18 casos preservadas; 82 casos totais catalogados. **Zero execuções verificadas, Pedido B/C não autorizados, G0 parcial, G1–G6 pendentes, 16 PNDs abertas.**

Referências: [GAI-INT-38](especificacao-executor-offline-33-casos-v2.md) · [GAI-INT-37](pacote-prontidao-testes-offline-candidate-2.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md).

## Revisão estática posterior
O [GAI-REV-002](revisao-estatica-executor-offline-v2-rev002.md) identificou 11 achados; código implementado permanece não executado e não homologado.
