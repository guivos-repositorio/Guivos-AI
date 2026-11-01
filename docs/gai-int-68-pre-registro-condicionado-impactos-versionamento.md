# GAI-INT-68 — Pré-registro Condicionado de Decisões e Impactos de Versionamento

**Data:** 01/11/2026 · **Estado:** preparação documental, sem deliberações emitidas.  
**Base:** [GAI-INT-67](gai-int-67-instrumento-deliberacao-politicas-pendentes.md), [GAI-INT-66](gai-int-66-reconciliacao-cobertura-decisoes-pendentes.md), [GAI-INT-61](gai-int-61-dicionario-canonico-campos-cardinalidade.md).

## 1. Regra de interpretação da concordância
A concordância da direção com a **continuidade documental** não seleciona nenhuma das alternativas A/B/C apresentadas em GAI-INT-67. Nenhuma decisão é atribuída à direção sem indicação **expressa** do identificador, alternativa escolhida e limites. Este pré-registro **não é** uma GAI-DEC e não constitui aprovação de política.

| Identificador | Alternativas oferecidas | Opção selecionada | Referência do ato | Estado |
| --- | --- | --- | --- | --- |
| DEL66-D04 | D04-A / D04-B / D04-C | `null` | `null` | **PENDENTE** |
| DEL66-I07 | I07-A / I07-B / I07-C | `null` | `null` | **PENDENTE** |
| DEL66-E07 | E07-A / E07-B / E07-C | `null` | `null` | **PENDENTE** |

## 2. Modelo de registro para eventual deliberação explícita
Campos **não preenchidos**: `decision_id`, `deliberation_id`, `selected_option`, `rationale`, `scope_of_design_approval`, `versioning_effect`, `affected_document_refs`, `compatibility_constraints`, `effective_date`, `decision_authority_verification_ref`, `independent_review_requirements`, `limitations`, `not_authorized_actions`, `supersession_refs`.  
O registro deverá distinguir: proposta, manifestação expressa de escolha, decisão documentada, verificação externa exigível, revisão competente e eventuais atos posteriores de implementação. Não preencher valores, datas de vigência ou assinaturas por inferência.

## 3. Mapa de impacto condicional — sem aplicação
| Eixo | Caso a direção escolha... | Impactos documentais a avaliar *depois* da escolha | Ação atual |
| --- | --- | --- | --- |
| D04 | A: coleção local; B: relações normalizadas; C: outra estrutura especificada | Cardinalidade, aliases, preservação de cronologia, decisões contraditórias/revogadas, GAI-INT-61, INV62-D04, F1 GAI-INT-57/59 | Somente inventário |
| I07 | A: pares proibidos; B: análise de risco; C: híbrido | Matriz de pares ROLE-REG/CUS/REV/OPS/AUD, DIR-C44-01..04, regras de exceção, suspensão, revisão independente, F2 | Somente inventário |
| E07 | A: política única; B: por classe; C: alternativa especificada | Retenção, algoritmos e verificador, classes, controle de acesso, custódia, proteção de dados, F3 e INV62-E07 | Somente inventário |

**Compatibilidade preservada:** não alterar schemas `candidate-v1` ou `candidate-v2-proposed`, runners, serviços, chaves, gateways, registros históricos ou permissões por força deste pré-registro. Qualquer migração futura exige escopo e aprovação próprios.

## 4. Checklist antes de qualquer decisão registrável
- [ ] A direção identifica **qual** DEL66 está sendo deliberada.
- [ ] A alternativa é indicada expressamente; opção C contém especificação suficiente ou mantém-se pendente de detalhamento.
- [ ] O alcance é limitado à política de desenho/versionamento quando assim deliberado.
- [ ] A justificativa e efeitos de compatibilidade são identificados sem presumir verificação técnica.
- [ ] Limitações e operações não autorizadas são explícitas.
- [ ] O registro distingue autoridade declarada de comprovação institucional exigida.
- [ ] Nenhum bloqueador ou gate é encerrado por inferência.

**Checklist ainda não executado como procedimento institucional**; são condições para deliberação futura. Manter os três registros `pending` até manifestação individual e rastreável.

## 5. Próximo encaminhamento
As próximas ações documentais possíveis são: (a) registrar **somente** as alternativas selecionadas expressamente pela direção, quando houver; ou (b) produzir uma comparação adicional de impactos/compatibilidade das alternativas ainda pendentes, sem assumir escolhas. Não há autorização para redigir uma GAI-DEC de aprovação sem opção declarada.

## 6. Limites permanentes
**15 bloqueadores** (7 P0, 7 P1, 1 P2) sem fechamento comprovado. **82 casos sintéticos sem execução verificada; 24 C63 e 3 A65 apenas conceituais. Pedido A concluído; Pedidos B/C não autorizados; COMP-04-P condicionado e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Não houve testes, pesquisa COMP-04-P, inspeção operacional, credencial, nomeação, implantação, alteração de schema ou aprovação de gate.
