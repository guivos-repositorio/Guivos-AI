# GAI-INT-67 — Instrumento de Deliberação das Três Políticas Pendentes

**Data:** 01/11/2026 · **Estado:** instrumento documental submetível à direção; **sem escolhas registradas ou aprovadas**.  
**Fonte:** [GAI-INT-66](gai-int-66-reconciliacao-cobertura-decisoes-pendentes.md), [GAI-INT-62](gai-int-62-matriz-invariantes-regras-condicionais.md), [GAI-INT-61](gai-int-61-dicionario-canonico-campos-cardinalidade.md) e [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md).

## 1. Objetivo e limites
Oferecer à direção três escolhas **independentes**, cada uma restrita a eventual **política de desenho e versionamento documental**. O envio, leitura ou publicação deste instrumento não seleciona alternativas, não cria ato de decisão nem autoriza execução, teste, inspeção, custódia operacional, nomeação ou gates.

## 2. DEL66-D04 — Precedência de múltiplas decisões
**Questão:** como representar decisões supervenientes múltiplas, parciais ou contraditórias para um mesmo documento histórico?

| Alternativa | Desenho | Vantagem | Risco / custo de governança |
| --- | --- | --- | --- |
| **D04-A** | `precedence_links[]` aninhados no registro documental, cada vínculo com ID de decisão, data, alcance, status e proveniência | Consulta e auditoria de um documento em um registro | Duplicação de decisão e necessidade de sincronizar referências |
| **D04-B** | Entidades normalizadas `historical_documents`, `decisions` e `precedence_relations` com vínculo de muitos-para-muitos | Integridade referencial e possibilidade de múltiplos usos | Complexidade de versionamento, migração e consulta |
| **D04-C** | Estrutura alternativa a justificar mediante proposta escrita e comparação | Flexibilidade para requisito ainda não capturado | Sem critérios verificáveis até apresentação formal |

**Condições mínimas de qualquer escolha:** não reescrever documentos históricos; preservar escopo parcial, precedência, conflito, revogação, data e versão; distinguir decisão normativa de nota editorial; identificar efeito sobre GAI-INT-61 e casos A65-D-N01.  
**Registro de escolha:** `pending`. **Sem recomendação aprovada.**

## 3. DEL66-I07 — Segregação e incompatibilidades institucionais
**Questão:** qual política de combinação dos papéis ROLE-REG, ROLE-CUS, ROLE-REV, ROLE-OPS e ROLE-AUD deverá ser adotada futuramente?

| Alternativa | Desenho | Vantagem | Risco / condição |
| --- | --- | --- | --- |
| **I07-A** | Matriz explícita de pares proibidos; demais acúmulos exigem verificação conforme atividades e escopo | Simplicidade de interpretação e regra restritiva | Pode impedir operação legítima se proibições não forem bem especificadas |
| **I07-B** | Avaliação baseada em risco para cada combinação, com revisão independente e exceções formalizadas | Flexibilidade sob evidência e escopo | Risco de exceções inconsistentes, exige controle institucional robusto |
| **I07-C** | Modelo híbrido com proibições absolutas e casos condicionados | Combina invariantes rígidos e revisão contextual | Exige classificar cada par, alçadas e regras de conflito |

**Condições mínimas de qualquer escolha:** compatibilidade com DIR-C44-01..04/GAI-DEC-013; definir conflitos por atividade concreta, revisão independente, exceções, suspensão, reavaliação e revogação; distinguir política de papéis de nomeações individuais. **A direção permanece autoridade central de autorização; este documento não designa titulares.**  
**Registro de escolha:** `pending`. Nenhum par é declarado permitido, proibido ou autorizado neste instrumento.

## 4. DEL66-E07 — Integridade, retenção e custódia
**Questão:** qual estrutura normativa governará digest, retenção, acesso, custódia, revogação e confiança?

| Alternativa | Desenho | Vantagem | Risco / condição |
| --- | --- | --- | --- |
| **E07-A** | Política institucional única versionada, com requisitos comuns a todas as classes | Uniformidade e auditoria central | Tratamento pouco proporcional a classes de risco distintas |
| **E07-B** | Política versionada por classe de evidência com controles mínimos transversais | Controles proporcionais às classes | Complexidade de precedência e governança de múltiplas políticas |
| **E07-C** | Modelo alternativo expressamente especificado e justificado | Flexibilidade condicionada a justificativa | Escopo indefinido até especificação e revisão |

**Condições mínimas de qualquer escolha:** separar digest esperado/observado e verificação independente; definir responsável competente, classes, proveniência, retention, eliminação, incidentes, retenção legal, sigilo, controle de acesso, política de algoritmos e substituição; não publicar dados privados; registrar revisão periódica e revogação. Valores concretos, prazos, algoritmos, fornecedores e locais de custódia **não são aprovados aqui**. **COMP-04-P permanece inativo.**  
**Registro de escolha:** `pending`.

## 5. Matriz comparativa de impacto
| Critério | D04 | I07 | E07 |
| --- | --- | --- | --- |
| Preservação de histórico e rastreabilidade | Central | Indireto | Indireto |
| Separação de poderes | Indireto | Central | Central |
| Integridade e prova independente | Relevante | Central | Central |
| Proteção de dados | Conforme evidência | Alta | Central |
| Dependência de decisão institucional | Sim | Sim | Sim |
| Autorização operacional decorrente | **Nenhuma** | **Nenhuma** | **Nenhuma** |

## 6. Instrumento de decisão futura — campos vazios
Para cada identificador `DEL66-*`, registrar somente após deliberação explícita: `selected_option`, `rationale`, `decision_ref`, `approved_scope`, `effective_date`, `superseded_documents` (quando cabível), `limitations`, `decision_authority_verification_ref`, `independent_review_requirements`, `next_action_not_authorized`.

**Estado atual:** `DEL66-D04=pending`, `DEL66-I07=pending`, `DEL66-E07=pending`; `decision_ref=null` para os três. A concordância com **a preparação deste instrumento** não é seleção de A/B/C.

## 7. Encaminhamento candidato
Após a direção emitir escolhas expressas e escopos específicos, poderá ser preparado **GAI-INT-68 — Registro das Decisões de Desenho e Impactos de Versionamento**. Se as escolhas permanecerem pendentes, a próxima ação possível é apenas complementação documental comparativa, sem criar decisão fictícia.

## 8. Estado institucional preservado
**15 bloqueadores** (7 P0, 7 P1, 1 P2) não encerrados por esta publicação. **82 casos sintéticos sem execução verificada, 24 cenários C63 e 3 cenários A65 não executados.** Pedido A concluído conforme registro; **Pedidos B/C não autorizados; COMP-04-P aprovado em princípio e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Nenhum schema, runner, credencial, inspeção, implantação, nomeação, adjudicação ou gate aprovado.
