# GAI-INT-23 — Dossiê de Ratificação de Responsáveis e Alçadas
**Versão documental 4.7 · 31/10/2026**
**Estado:** proposta de ratificação. Nenhuma pessoa ou equipe formalmente designada, nenhum gate aprovado e nenhum teste executado.

## 1. Finalidade
Materializar a próxima etapa de D21-01/PND-01 e D21-02/PND-11, já especificadas em [GAI-INT-22](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md). A evolução documental não é ratificação institucional.

Foi identificado nos registros existentes que os responsáveis são definidos por **funções candidatas**, e não por titularidade real. Um nome em commit, acesso ao GitHub ou gestão de protótipo não prova mandato para decidir sobre dados, segurança ou gates.

## 2. Inventário de designações necessárias
O [registro estruturado](registro-ratificacao-titulares-alcadas-candidato.json) estabelece **16 posições funcionais a verificar**, todas sem atribuição. Isso não implica a necessidade de 16 pessoas distintas.

| Grupo | Posição a confirmar | Evidência exigida |
| --- | --- | --- |
| Arquitetura | Responsável técnico pela arquitetura | Mandato de arquitetura e escopo |
| Fonte canônica | Responsáveis por identidade, contexto, autorização, oportunidades, evidências e entrega | Serviço efetivo, proprietário e política de correção |
| Governança | Privacidade/jurídico e segurança | Competência, alçada e aceitação |
| Contratos e QA | Engenheiro de contratos e executor dos testes | Responsabilidade, escopo e processo de registro |
| Revisão | Revisor independente | Independência e aceite |
| Decisão | Autoridades de G0, G2, G5 e G6 | Delegação, limites e vigência |

Sem confirmação e aceite do titular, o status permanece `unassigned_pending_formal_ratification`.

## 3. Fluxo de ratificação proposto
1. Identificar o serviço ou domínio real, distinguindo serviço existente de serviço apenas projetado.
2. A instância legitimada apresenta nomeação e delimita escopo.
3. O indicado aceita formalmente sua função.
4. Revisores avaliam independência e eventuais conflitos.
5. Registra-se a decisão de ratificação, com validade e restrições.
6. Atualizam-se as PNDs e o Registro de Decisões apenas mediante decisão verificável.

Não inferir titulares por participação em discussões ou autoria de código.

## 4. Autoridade por domínio
| Domínio | Responsabilidade candidata | Limite arquitetural |
| --- | --- | --- |
| Identidade | Serviço canônico de identidade | Intelligence e AI são consumidores autorizados |
| Contexto da Pessoa | Fonte versionada de contexto e evidências | Validação de compreensão não altera propriedade da origem |
| Finalidades/autorização | Serviço de autorização | Neo4j e modelos não concedem permissão |
| Oportunidades | Serviço de oferta e disponibilidade | Possibilidade não é disponibilidade confirmada |
| Evidências | Serviço proprietário de cada fonte | Derivações devem preservar proveniência |
| Relatório/entrega | Serviço de distribuição autorizado | Gerar não equivale a compartilhar |
| Gate | Instância de governança designada | Executor e revisor não autoaprovam release |

Guivos Intelligence orquestra a experiência; Guivos AI produz análises; GPT, Claude e Gemini são adaptadores; Neo4j pode projetar dependências autorizadas. Guivos AI e GKR mantêm governança independente.

## 5. Critérios de fechamento das pendências
**D21-01/PND-01:** inventário verificável de fontes e serviços, responsável por domínio, contratos, política de retificação, proveniência e aceite formal.

**D21-02/PND-11:** autoridades de gates, revisores e responsáveis nomeados por instância legítima, alçadas explícitas, conflitos examinados e registros verificáveis de aceite.

Sem esses elementos, **as 16 PNDs permanecem abertas**; G0 parcial e G1–G6 pendentes.

## 6. Limite da execução sintética
Os 19 schemas e 49 fixtures continuam preparados, não executados. Nenhum runner foi disparado, e o [pedido candidato de campanha](pacote-decisoes-g0-g2-autorizacao-validacao-estrutural.md) permanece sem autorização. Não houve acesso operacional a Replit, Neo4j, provedores ou GKR.

## 7. Verificação da administração GitHub
O [GAI-INT-24](verificacao-administracao-repositorio-limites-autoridade.md) constatou permissão administrativa da conexão no GitHub, sem comprovar mandato institucional de nomeação ou homologação. As 16 funções permanecem sem titulares ratificados.

## 8. Confirmação da instância de nomeações
A [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) confirma a direção da Guivos como instância inicial de nomeações e decisões estratégicas. Essa confirmação não preenche os 16 papéis do cadastro nem concede alçadas de gate. Os mandatos e aceites individuais permanecem por registrar.

## 9. Próxima ação efetiva
A instância de governança legítima precisa identificar os titulares e confirmar os mandatos para que o cadastro deixe de ser apenas candidato. **Prosseguir com documentação não substitui essa confirmação organizacional.**

**Referências:** [GAI-INT-22](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [Registro de Decisões](registro-decisoes.md).
