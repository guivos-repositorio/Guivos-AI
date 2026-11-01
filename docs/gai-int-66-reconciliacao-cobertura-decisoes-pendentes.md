# GAI-INT-66 — Reconciliação da Cobertura Conceitual e Registro de Decisões Pendentes

**Data:** 01/11/2026  
**Natureza:** consolidação e encaminhamento documental; não é deliberação, aceite institucional, autorização operacional ou homologação.  
**Fontes:** [GAI-INT-62](gai-int-62-matriz-invariantes-regras-condicionais.md) · [GAI-INT-63](gai-int-63-matriz-casos-conceituais-condicoes-aceite-inv62.md) · [GAI-INT-64](gai-int-64-mapa-cobertura-inv62-c63.md) · [GAI-INT-65](gai-int-65-adendo-cenarios-cobertura-residual.md).

## 1. Resultado da reconciliação
A GAI-INT-62 cataloga **30 invariantes candidatos**. A GAI-INT-63 descreve **24 casos conceituais**, sem execução. A GAI-INT-64 identificou **27 regras com cenário direto, 2 com cenário indireto e 1 sem cenário**. O adendo GAI-INT-65 propôs **3 cenários adicionais**, elevando a **associação conceitual proposta a 30/30**: 24 cenários C63 preservados e 3 cenários A65 adicionados em documento separado.

**Cobertura documental não é validade de política.** O vínculo entre regra e caso não prova completude dos estados, verificação externa, funcionamento de software, segurança, conformidade contratual ou resolução de bloqueadores.

## 2. Registro de deliberações pendentes
| ID de encaminhamento | Invariante | Questão a decidir formalmente | Alternativas de desenho para apreciação (não selecionadas) | Dependência | Estado |
| --- | --- | --- | --- | --- | --- |
| DEL66-D04 | INV62-D04 | Como representar múltiplas decisões posteriores sobre um documento histórico sem perder alcance, precedência e cronologia | A: coleção `precedence_links` por documento; B: relação normalizada entre documento e decisões; C: outra estrutura justificada | Cardinalidade, proveniência, preservação do histórico, versionamento | Pendente de decisão |
| DEL66-I07 | INV62-I07 | Qual matriz de incompatibilidades e segregação vale para ROLE-REG, ROLE-CUS, ROLE-REV, ROLE-OPS e ROLE-AUD | A: proibição de combinações listadas; B: análise por risco e autorização de exceções com revisão independente; C: combinação explicitamente delimitada | GAI-DEC-013, identidades verificáveis, competência institucional, mecanismos de suspensão | Pendente de decisão |
| DEL66-E07 | INV62-E07 | Quais parâmetros e autoridades governam algoritmo de digest, retenção, acesso, custódia, revogação e atestação | A: política única institucional versionada; B: política por classe de evidência com controles mínimos comuns; C: outra política expressamente delimitada | Privacidade, segurança, autoridade, fonte normativa, confiabilidade independente | Pendente de decisão |

**As alternativas são para estruturação da análise, não recomendações aprovadas.** Não atribuir escolha A/B/C à direção a partir da publicação.

## 3. Condições para cada eventual decisão
### DEL66-D04 — precedência e cardinalidade
A futura decisão deve especificar: identificadores estáveis; cardinalidade documento–decisão; alcance parcial/integral; ordem temporal; tratamento de decisões contraditórias e revogadas; preservação da redação histórica; versionamento e aliases existentes. A escolha deve ser avaliada quanto à compatibilidade com [GAI-INT-61](gai-int-61-dicionario-canonico-campos-cardinalidade.md). Não alterar os arquivos históricos por inferência.

### DEL66-I07 — incompatibilidades institucionais
A futura decisão deve especificar: pares de papéis; conflitos absolutos e relativos; incompatibilidades por atividade concreta; exigência de revisão independente; política de exceções, se houver; regra de substituição e revogação. Nomeação, verificação de identidade, aceite e habilitação permanecem atos independentes. **Nenhum titular é indicado, nomeado ou habilitado neste registro.**

### DEL66-E07 — retenção, algoritmo e confiança
A futura decisão deve especificar: classes de evidência; formato de manifesto; algoritmo(s) aceitos com versionamento; digest esperado versus observado; verificador; retenção e descarte; segregação e controle de acesso; custódia adequada; proteção de dados; incidentes e reavaliação. Não fixar prazos, algoritmos, provedores ou meios de custódia sem a análise e aprovação competentes. A proposta **não autoriza pesquisa pública COMP-04-P**, que permanece inativa.

## 4. Outros requisitos não encerrados
Embora o vínculo conceitual chegue a 30/30, persistem: campos obrigatórios por estado, serialização, validade de referências, prova externa de autoridade, regras de confiança, revisão independente, tratamento de contradições, implementação de custódia e verificação real de integridade. Os três encaminhamentos acima não esgotam a matriz dos **15 bloqueadores** do GAI-INT-53/55.

## 5. Separação entre decisões e evidências
Uma decisão de desenho sobre DEL66-D04/I07/E07 não implica que: (i) a política tenha sido implementada; (ii) a evidência tenha sido coletada e validada; (iii) exista agente com autoridade criptograficamente verificável; (iv) o Pedido B/C esteja autorizado; (v) COMP-04-P esteja ativado; (vi) um bloqueador ou gate esteja encerrado.

**Registro de decisões:** `DEL66-D04: pending`; `DEL66-I07: pending`; `DEL66-E07: pending`. Não criar `decision_ref`, `acceptance_ref`, `closure_decision_ref` ou `gate_decision_ref` artificiais.

## 6. Próximo encaminhamento candidato
**GAI-INT-67 — Instrumento de Deliberação das Três Políticas Pendentes**, com perguntas institucionais e critérios de impacto para cada alternativa, sem impor escolha, nomear responsáveis, executar validadores ou ativar operações. Somente um ato posterior expresso da direção poderá aprovar política de desenho, com seus próprios limites.

## 7. Estado institucional inalterado
**15 bloqueadores** (7 P0, 7 P1, 1 P2), sem encerramento comprovado. **82 casos sintéticos anteriores**, nenhuma execução verificada; **24 cenários C63 + 3 A65**, apenas documentação. Pedido A concluído conforme registros. **Pedidos B e C não autorizados; COMP-04-P condicionado e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Nenhuma implantação, credencial, schema homologado, nomeação, verificação operacional ou gate aprovado decorre deste instrumento.
