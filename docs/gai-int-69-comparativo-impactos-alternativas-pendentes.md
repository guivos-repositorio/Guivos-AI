# GAI-INT-69 — Comparativo de Impactos e Dependências das Alternativas Pendentes

**Data:** 01/11/2026 · **Natureza:** análise comparativa documental; **nenhuma seleção, decisão, aprovação, nomeação ou autorização operacional**.  
**Referências:** [GAI-INT-67](gai-int-67-instrumento-deliberacao-politicas-pendentes.md), [GAI-INT-68](gai-int-68-pre-registro-condicionado-impactos-versionamento.md), [GAI-INT-66](gai-int-66-reconciliacao-cobertura-decisoes-pendentes.md) e [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md).

## 1. Regra de comparação
Analisar opções A/B/C individualmente nos eixos: rastreabilidade histórica; simplicidade de governança; independência de revisão; privacidade; compatibilidade documental; risco de ambiguidades; condições para versão candidata. **Não atribuir pontuação numérica, ranking ou vitória presumida onde faltam parâmetros ratificados.** Nenhuma alternativa abaixo é uma escolha da direção.

## 2. DEL66-D04 — Estrutura de precedência de decisões
| Alternativa | Capacidade | Vantagem documental | Risco / custo | Dependência antes de ratificação |
| --- | --- | --- | --- | --- |
| D04-A — vínculos aninhados | Registrar várias decisões e suas notas no histórico de cada documento | Contexto reunido para leitura por documento | Repetição de decisões em muitos históricos e risco de divergência | Regra de atualização de referências, identificadores e precedência |
| D04-B — relações normalizadas | Modelo muitos-para-muitos de documentos, decisões e relações | Maior controle de identidade de decisões reutilizadas | Maior custo de modelagem, navegação e versionamento | Definição de relação canônica, validade de refs e migração futura |
| D04-C — alternativa especificada | Permitir outro desenho mediante justificativa formal | Adaptação a requisito ainda não identificado | Impossível avaliar compatibilidade sem estrutura concreta | Entrega prévia de especificação, critérios e análise comparável |

**Não negociáveis:** preservar o conteúdo histórico, distinguir decisões normativas de adendos e alterações factuais, suportar cronologia, escopo parcial e situações contraditórias/revogadas. Efeitos possíveis em GAI-INT-61/F1 e INV62-D04; sem implementação.

## 3. DEL66-I07 — Segregação de funções
| Alternativa | Capacidade | Vantagem documental | Risco / custo | Dependência antes de ratificação |
| --- | --- | --- | --- | --- |
| I07-A — pares proibidos | Declarar incompatibilidades objetivas | Fácil explicação e auditoria das proibições | Pode ser inflexível ou insuficiente diante de conflitos por atividade | Lista fundamentada de pares e escopos incompatíveis |
| I07-B — análise por risco | Examinar combinações e exceções caso a caso | Adaptação ao contexto e ao risco | Exceções inconsistentes ou dependência excessiva de julgamento | Critérios de risco, autoridade de exceção e revisão independente |
| I07-C — híbrido | Conjugar proibições absolutas e avaliação condicionada | Equilíbrio entre barreiras e contexto | Regras sobrepostas e necessidade de precedência entre controles | Matriz de conflito e critérios para casos condicionados |

**Não negociáveis:** GAI-DEC-013/DIR-C44-01..04; separação entre indicação, verificação externa de identidade, aceite, habilitação, atuação e adjudicação; suspensão/revogação. Os papéis ROLE-REG/CUS/REV/OPS/AUD permanecem sem nomeação em decorrência deste documento.

## 4. DEL66-E07 — Política de evidências
| Alternativa | Capacidade | Vantagem documental | Risco / custo | Dependência antes de ratificação |
| --- | --- | --- | --- | --- |
| E07-A — política única | Controles e governança comuns | Menor divergência entre classes | Desproporcionalidade entre riscos e tipos de evidência | Escopo, exceções e tratamento de classes específicas |
| E07-B — política por classe | Controles mínimos comuns mais regras especializadas | Proporcionalidade e distinção de sensibilidade | Fragmentação e conflitos de precedência | Taxonomia de classes, políticas de herança e revisão |
| E07-C — alternativa especificada | Outro arranjo a fundamentar | Flexibilidade sob justificativa | Impossibilidade de análise definitiva sem desenho | Especificação e demonstração de controles comuns |

**Não negociáveis:** integridade observada separada da declarada; verificador confiável; retenção com fundamento; segregação de custódia/revisão; proteção de dados; acesso mínimo; incidentes; revogação e rastreabilidade. Não escolher algoritmo, prazo, fonte pública ou provedor por inferência. COMP-04-P permanece condicionado/inativo.

## 5. Matriz transversal de implicações
| Eixo de análise | D04 | I07 | E07 |
| --- | --- | --- | --- |
| Atualização provável de documento de desenho | GAI-INT-61 F1; INV62-D04 | GAI-INT-57/59 F2; INV62-I07 | GAI-INT-57/59 F3; INV62-E07 |
| Migração operacional implícita | Não | Não | Não |
| Compatibilidade com versões anteriores | Necessita análise futura | Necessita análise de responsabilidades | Necessita análise de evidências |
| Ato institucional independente | Sim para adoção | Sim para política e atos individuais | Sim para política e custódia |
| Fechamento automático de BLK-D01/I01/E05 | Não | Não | Não |
| Aprovação automática de gate | Não | Não | Não |

## 6. Perguntas abertas que impedem seleção por inferência
1. D04: qual regra de identidade e precedência garante consistência em documentos que compartilham uma decisão posterior?
2. I07: quais conflitos são absolutos, quais são condicionais e quem pode avaliar exceções sem perder independência?
3. E07: quais classes, controles mínimos, prazos de retenção e referências normativas são realmente exigíveis?
4. Para todas: quais evidências suportam a política e quais etapas futuras demandarão autorização específica?

## 7. Estado do registro e próximo encaminhamento
**DEL66-D04=pending; DEL66-I07=pending; DEL66-E07=pending.** Opções não escolhidas; `decision_ref=null`. Para avançar a uma **decisão de desenho**, a direção deverá indicar expressamente cada alternativa e seus limites. Se não houver escolha, o trabalho poderá continuar em análise documental de requisitos, sem criar GAI-DEC fictícia.

**Próxima etapa candidata: GAI-INT-70 — Checklist de Suficiência para Deliberação das Três Políticas**, exclusivamente para organizar dependências de decisão, sem autorizar implementação.

## 8. Fronteiras preservadas
**15 bloqueadores** (7 P0, 7 P1, 1 P2) não encerrados; **82 casos sintéticos** sem execução verificada, 24 cenários C63 e 3 A65 conceituais. Pedido A concluído conforme registro; **Pedidos B/C não autorizados**, **COMP-04-P inativo**, **G0 parcial, G1–G6 pendentes, PND-01..16 abertas**. Nenhum teste, credencial, operação, pesquisa COMP-04-P, migração, homologação, nomeação ou gate foi realizado.
