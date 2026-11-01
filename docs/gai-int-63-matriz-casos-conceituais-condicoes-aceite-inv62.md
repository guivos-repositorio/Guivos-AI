# GAI-INT-63 — Matriz de Casos Conceituais e Condições de Aceite INV62

**Data:** 01/11/2026 · **Estado:** desenho documental de casos; **não executados**, sem schema criado, homologação ou alteração de contratos.

## 1. Origem e fronteira
Derivado de [GAI-INT-62](gai-int-62-matriz-invariantes-regras-condicionais.md) e [GAI-INT-61](gai-int-61-dicionario-canonico-campos-cardinalidade.md). Esta matriz apresenta **24 cenários conceituais novos**, separados dos **82 casos sintéticos anteriormente catalogados**. Não adicioná-los ao inventário de execução B nem tratar expectativas como observações.

**Classificação:** Positivo = coerente com a regra de desenho, mas sem aprovação institucional; Negativo = combinação que a regra proposta rejeita; Condicionado = depende de fonte, política, autoridade ou estrutura ainda não ratificada. Nenhuma classificação prova que um validador tenha operado.

## 2. Casos
| ID | INV62 relacionado | Classe | Situação abstrata | Expectativa conceitual |
| --- | --- | --- | --- | --- |
| C63-T-P01 | T01/T02/T03 | Positivo | Registro documental BLK-D01 com ID, fontes e limitações | Coerente em desenho |
| C63-T-N01 | T02 | Negativo | institutional_nomination associado a BLK-E05 | Incompatível |
| C63-T-N02 | T04 | Negativo | reviewed sem revisor ou prova de competência | Incompatível |
| C63-T-C01 | T04/T07 | Condicionado | Revisor identificado, porém prova externa indisponível | Pendente de verificação |
| C63-T-N03 | T05 | Negativo | Parecer usado para gerar gate_decision_ref automaticamente | Proibido |
| C63-T-N04 | T06/T08 | Negativo | approved=true autodeclarado e dados pessoais publicados | Proibido |
| C63-T-N05 | T09 | Negativo | expires_at anterior a effective_at | Incompatível |
| C63-D-P01 | D01/D02 | Positivo | Documento histórico com decisão superveniente e escopo explícito | Coerente em desenho |
| C63-D-N01 | D02 | Negativo | Precedência normativa sem decisão ou escopo | Incompatível |
| C63-D-N02 | D03/D06 | Negativo | Reescrever o registro original como se a decisão posterior já existisse | Proibido |
| C63-D-C01 | D04 | Condicionado | Mesmo documento com três decisões posteriores e somente campo escalar | Exige modelo multirreferência |
| C63-D-C02 | D05 | Condicionado | Aceite editorial mencionado sem fonte de revisão verificada | Pendente de evidência |
| C63-I-P01 | I01/I02 | Positivo | Indicação e aceite como atos separados, com verificações externas | Coerente em desenho; sem nomeação real |
| C63-I-N01 | I03 | Negativo | role_id preenchido é tratado como permissão B | Proibido |
| C63-I-N02 | I06 | Negativo | Assinatura sem vínculo institucional é tratada como prova de autoridade | Proibido |
| C63-I-C01 | I04/I07 | Condicionado | Dois papéis acumulados sem matriz ratificada de conflitos | Não adjudicável |
| C63-I-N03 | I05 | Negativo | Aceite considerado vigente após revogação aplicável | Incompatível |
| C63-E-P01 | E01/E02 | Positivo | Item com origem, digest esperado/observado e verificador independente | Coerente em desenho; integridade não observada |
| C63-E-N01 | E02 | Negativo | digest_observed sem algoritmo ou verificador | Incompatível |
| C63-E-N02 | E03 | Negativo | Digest observado autodeclarado é anunciado como verificado | Proibido |
| C63-E-C01 | E04/E07 | Condicionado | Custódia prevista sem política de retenção aprovada | Não comprova custódia |
| C63-E-N03 | E05 | Negativo | accepted_for_scope sem revisor independente | Incompatível |
| C63-E-N04 | E06 | Negativo | Parecer aceito encerra gate automaticamente | Proibido |
| C63-E-C02 | E07 | Condicionado | Algoritmo de hash sem política aprovada | Pendente de decisão |

**Contagem:** 24 casos: 4 positivos; 14 negativos; 6 condicionados. Todas as expectativas são propostas de avaliação, não resultados.

## 3. Condições de aceite para análise documental futura
1. **Rastreabilidade:** cada caso aponta ao identificador da regra INV62, seu significado e ao instrumento F1/F2/F3 aplicável.
2. **Consistência:** campos canônicos, tipos lógicos, obrigatoriedade condicional e cardinalidade devem concordar com GAI-INT-61, ou a divergência ser registrada.
3. **Segregação:** casos envolvendo identidade, nomeação, autorização, revisor ou adjudicação não podem afirmar competência sem prova institucional independente.
4. **Privacidade:** exemplos contêm somente descrições abstratas e nenhum dado real; modelos públicos não carregam evidência privada.
5. **Observabilidade:** distinguir expectativa, evidência recebida, verificação independente, parecer e decisão; não preencher campo de resultado observado.
6. **Casos condicionados:** mantê-los como `pending_policy_decision` ou `pending_external_evidence` até ratificação pertinente, sem reclassificar como positivos por conveniência.
7. **Gates:** `closure_decision_ref` e `gate_decision_ref` permanecem nulos sem atos separados.
8. **Revisão:** eventual aceite desta matriz exige revisão documental competente; não autoriza execução do Pedido B.

## 4. Limites da cobertura
Os casos não esgotam todas as combinações possíveis, especialmente cardinalidades múltiplas, transições de `record_status`, definição de conflitos entre papéis, resolução de vínculos de assinatura, retenção e revogação. A matriz futura pode ser ampliada apenas por versionamento e decisão documental rastreável, sem execução implícita.

## 5. Pendências para decisão de desenho
- Regras formais para `precedence_links` e cardinalidade de decisões supervenientes.
- Estados de registro, obrigatoriedade e transições válidas por tipo.
- Matriz institucional de pares incompatíveis, sem designar titulares.
- Critérios de integridade, algoritmos e retenção com fonte normativa própria.
- Separação de aprovação de formulário, aceite institucional, concessão de autorização, fechamento de bloqueador e gate.

## 6. Encaminhamento
**GAI-INT-64 (candidato):** mapa de cobertura INV62 × casos C63 e lacunas de decisão, para revisão estática e possível fechamento apenas de pendências **documentais** quando comprovadas; não é proposta de testes.

## 7. Estado preservado
**82 casos sintéticos anteriores sem execução verificada; 24 novos cenários meramente conceituais sem execução.** Os 15 bloqueadores (7 P0, 7 P1, 1 P2) não foram encerrados. Pedido A concluído conforme registros; Pedidos B/C não autorizados; COMP-04-P aprovado em princípio, inativo; G0 parcial, G1–G6 pendentes; PND-01..16 abertas. Nenhum gate aprovado, dado privado acessado, schema implementado ou ambiente alterado.
