# GAI-INT-65 — Adendo de Cenários de Cobertura Residual INV62

**Data:** 01/11/2026 · **Natureza:** especificação estática de três cenários conceituais adicionais, **não executados**.  
**Bases:** [GAI-INT-62](gai-int-62-matriz-invariantes-regras-condicionais.md), [GAI-INT-63](gai-int-63-matriz-casos-conceituais-condicoes-aceite-inv62.md) e [GAI-INT-64](gai-int-64-mapa-cobertura-inv62-c63.md).

## 1. Objetivo e fronteira
Complementar as duas regras anteriormente cobertas apenas indiretamente (INV62-T07 e INV62-D03) e a única regra sem cenário (INV62-T10). Preservar integralmente os **24 casos C63** originais; estas **3 novas entradas A65** não são fixtures, não são testes e **não integram os 82 casos sintéticos** registrados para a campanha anterior.

## 2. Cenários adicionais

| ID | Regra | Classe | Condição conceitual | Expectativa de desenho |
| --- | --- | --- | --- | --- |
| A65-T-N01 | INV62-T10 | Negativo | Um adaptador renomeia `acceptance_ref` para `acceptance_ref_private`, sem existir aceite individual verificável, e passa a declarar o papel institucional como aceito. | Proibido inferir ocorrência/aceite apenas por alias; manter situação não comprovada |
| A65-T-C01 | INV62-T07 | Condicionado | Há um ato alegado de autorização com escopo e prazo, mas a fonte de revogação e a identidade da autoridade não estão verificadas independentemente. | Não declarar permissão eficaz; exigir validação de autoridade, escopo, prazo e revogação |
| A65-D-N01 | INV62-D03 | Negativo | Uma decisão posterior aprova apenas uma parte do desenho, mas um registro atribui a ela revogação integral da versão histórica sem cláusula expressa. | Proibir supersessão integral inferida; preservar texto original e limitar precedência ao escopo expresso |

**Observação:** os cenários descrevem expectativas normativas de desenho, não resultados de uma implementação. Nenhuma chave, pessoa real ou dado privado foi utilizado.

## 3. Critérios de revisão documental
1. O cenário **A65-T-N01** precisa demonstrar a diferença entre equivalência de nomes e efetiva existência de aceite; nomes adaptados não criam eventos.
2. O cenário **A65-T-C01** deve manter estado *não comprovado* até existir evidência institucional confiável, com prazo, escopo e revogação verificáveis; uma declaração do próprio requerente não basta.
3. O cenário **A65-D-N01** deve distinguir adendo editorial, alteração factual e decisão normativa; a decisão posterior só prevalece em seu alcance expresso.
4. Os três IDs A65 devem ser estáveis, separados da série C63, e citados por referência sem renumerar os documentos originais.
5. Uma avaliação futura pode marcar o **desenho do cenário** como coerente, mas jamais como execução, validação técnica, encerramento de bloqueador ou aprovação de gate.

## 4. Cobertura documental revisada — apenas prospectiva
| Métrica | GAI-INT-64 original | Com adendo GAI-INT-65 | Qualificação |
| --- | ---: | ---: | --- |
| INV62 com cenário direto | 27 | 30 | Associação conceitual, sujeita a revisão documental |
| INV62 com somente cenário indireto | 2 | 0 | Cenários específicos propostos para T07 e D03 |
| INV62 sem cenário | 1 | 0 | Cenário proposto para T10 |
| Regras INV62 totais | 30 | 30 | Inventário original inalterado |
| Cenários C63 originais | 24 | 24 | Arquivo original não alterado |
| Cenários novos A65 | 0 | 3 | Não executados |

**Atenção:** a cobertura de associação **30/30** não demonstra abrangência exaustiva de estados, testes de fronteira, validação de schema, verificação de evidência, aceitação institucional nem eficácia. INV62-D04, I07 e E07 permanecem dependentes de deliberações de política, embora seus cenários existam.

## 5. Dependências ainda não resolvidas
- **INV62-D04:** cardinalidade e semântica canônica de várias decisões para o mesmo documento.
- **INV62-I07:** matriz ratificada de incompatibilidades e regras de segregação por pares de funções.
- **INV62-E07:** política de algoritmos, retenção, local de custódia e critérios de confiança.
- **Institucional:** verificação independente de autoridades, revisores e custódia; nenhuma nomeação decorre desta especificação.
- **Técnica:** nenhuma execução autorizada de casos, validadores ou ambientes.

## 6. Próximo encaminhamento candidato
**GAI-INT-66 — Reconciliação da Cobertura Conceitual e Registro de Decisões Pendentes**, com leitura estática dos documentos 62 a 65 e foco em D04/I07/E07, sem decidir políticas por inferência e sem iniciar testes.

## 7. Estado e autorização
**82 casos sintéticos anteriores, zero execuções verificadas; 24 cenários C63 e 3 cenários A65 são somente conceituais.** Os **15 bloqueadores** (7 P0, 7 P1, 1 P2) permanecem sem fechamento. Pedido A concluído conforme registros; **Pedidos B e C não autorizados**; **COMP-04-P aprovado em princípio e inativo**; **G0 parcial, G1–G6 pendentes, PND-01 a PND-16 abertas**. Nenhum contrato, credencial, runner, schema, gate ou infraestrutura foi alterado.
