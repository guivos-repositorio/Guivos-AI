# GAI-INT-19 — Consolidação de Arquitetura e Critérios de Prontidão para Implementação
**Versão documental 4.3 · 31/10/2026**
**Estado:** consolidação arquitetural proposta para orientar futuras decisões. Não constitui aprovação de arquitetura operacional, implementação, testes ou liberação.

## 1. Propósito, posição e limites
Estabelecer uma visão integrada, verificável e responsável da arquitetura-alvo da Guivos AI, com o que já foi **documentado**, o que permanece **proposto**, quais **decisões faltam** e quais **evidências devem ser obtidas** antes de qualquer execução ou implementação.

Este documento é o ponto de consolidação dos GAI-INT-01 a GAI-INT-18 e das GAI-CAP-01 a GAI-CAP-12. Não promove hipóteses técnicas a decisões aprovadas. A evolução documental 4.3 não significa progresso equivalente nos gates operacionais.

## 2. Fronteiras arquiteturais estáveis
| Componente | Responsabilidade | Limite |
| --- | --- | --- |
| **Guivos Intelligence** | Orquestrar Jornada da Pessoa, contexto, perguntas, validação humana, escolha e consumo de análises | Não é autoridade canônica para todo fato ou consentimento |
| **Guivos AI** | Fornecer capacidades especializadas de análise e resultados sustentados por evidências, hipóteses e limitações | Não é novo foundation model, não cria oferta, consentimento ou fatos canônicos |
| **Serviços canônicos da Guivos** | Identidades, autorização, contexto, evidências, ofertas, versões, entrega e retenção conforme domínio | Não devem delegar autoridade factual a saídas de LLM |
| **Adaptadores GPT/Claude/Gemini** | Processamento técnico com rastreabilidade de método e proveniência | Não são sistema de verdade nem concedem permissão |
| **Neo4j projetado** | Candidato a persistir relações de dependência, memória autorizada e projeções analíticas | Não é autoridade universal, pode estar defasado e exige reconciliação |
| **API CAP-12 / gateway** | Contratos de consumo interno/terceiros, escopo, autenticação, limites e erros | Não disponibiliza dados de Pessoas por mera existência de endpoint |
| **GKR** | Conhecimento institucional com governança própria | Permanece independente; referências controladas, sem sincronização automática |

## 3. Visão de fluxo — arquitetura-alvo, não deploy
```text
Pessoa ──> Guivos Intelligence (coleta, compreensão, validação)
                    │
                    ├──> Serviços canônicos autorizados
                    │       ├─ Identidade e autorização por finalidade
                    │       ├─ Contexto e fontes versionadas
                    │       └─ Oportunidades e disponibilidade
                    │
                    └──> Guivos AI (API CAP-12 governada)
                              ├─ CAP-01..CAP-11 especializadas
                              ├─ Adaptadores GPT / Claude / Gemini
                              ├─ Método + evidências + limites
                              └─ Dependências/revalidação CAP-10
                                           │
                                  Projeção Neo4j candidata
                                           │
                    <── Resultado tipado e autorizado ──┘
                    │
                    └──> Pessoa: síntese, escolhas e validação
                              (relatório/entrega com autorização própria)

Outros consumidores do ecossistema ou parceiros:
gateway autorizado ──> Guivos AI sob contratos, escopos e auditoria
```
Setas representam contratos de estudo; **não comprovam integrações vivas**. Validação da Pessoa, processamento e compartilhamento são operações diferentes, sujeitas a políticas próprias.

## 4. Inventário de entregas e estado
| Área | Artefatos | Estado verificável no repositório |
| --- | --- | --- |
| Capacidades especializadas | 12 GAI-CAP | Estudos conceituais e critérios propostos |
| Integração de arquitetura | GAI-INT-01 a 18 | Estudos documentais publicados |
| Contratos estruturais | 19 schemas `candidate-v1` | Candidatos, sem homologação |
| Testes estruturais | 25 + 24 = 49 fixtures | Preparadas, sem execução comprovada |
| Ferramentas de teste | 2 scripts Python offline | Criados, não executados nesta sequência |
| Evidência/revisão/auditoria | Manifestos e templates INT-15 a 18 | Não preenchidos por resultados reais |
| Decisões pendentes | PND-01 a PND-16 | Nenhuma encerrada neste trabalho |
| Gates de autorização | G0–G6 | G0 parcialmente documental; G1–G6 pendentes |

**Nota:** estudos INT-12 a INT-18 adicionaram matrizes de cenários *propostos*, não novos casos executáveis nas 49 fixtures. Não somar seus cenários aos testes implementados.

## 5. Mapa dos domínios de implementação futura
| Domínio | Especificação-chave | Decisão crítica | Verificação exigida |
| --- | --- | --- | --- |
| Contexto, trajetória e evidência | CAP-01–03, INT-02/05 | PND-01, 03 | Proveniência, autorização, temporalidade |
| Lacunas, possibilidades e caminhos | CAP-04–07 | PND-05, 09, 12 | Rubricas, hipóteses e limites |
| Oferta qualificada | CAP-08, INT-06/07 | PND-01, 07 | Autoridade de supply, status e validade |
| Contradições e reavaliação | CAP-09/10, INT-06/07 | PND-07, 08 | Invalidação, recibos e reconciliação |
| Relatórios e compartilhamento | CAP-11, INT-05/16 | PND-02, 03, 08 | Finalidade, destinatário, retenção e entrega |
| API e integração | CAP-12, INT-08–13 | PND-05, 06, 13 | Contratos e compatibilidade entre consumidores |
| Observabilidade/auditoria | INT-14–18 | PND-11, 12, 15 | Evidência, revisão e GateDecision |

## 6. Decisões arquiteturais ainda abertas
Não são presumidas as escolhas de:
- arquitetura de persistência e Neo4j físico; transações canônicas, grafo projetado e retenção;
- autenticação/identidade, autorização por finalidade, escopos de partners e isolamento;
- orquestração, infraestrutura de eventos, garantias de entrega, outbox/inbox e reprocessamento;
- adoção de `AnalysisResponseTyped`, união tipada sucesso/erro e versionamento normativo;
- execução de adaptadores, fallbacks, decisão de transcrição, limites de custo e segurança;
- estratégias de armazenamento e manutenção dos resultados, cache e relatórios;
- política quantitativa de qualidade e adjudicação;
- configuração de ambientes, testes, incidentes, métricas, orçamento e rollback;
- nomeação de owners, revisores, autoridades de gate e aprovação de eventual release.

Relacionar cada proposta às PND-01–16 registradas no GAI-INT-14. **Um documento novo não fecha uma PND por si só.**

## 7. Prontidão por camada
| Camada | Documentação | Contrato candidato | Teste executado | Decisão de uso |
| --- | --- | --- | --- | --- |
| Fronteira Intelligence/AI | Sim | Parcial | Não verificado | Pendente em detalhes |
| Claims, evidências e versões | Sim | Parcial | Não | Pendente |
| CAP-01 a CAP-12 | Sim | Payloads mínimos para 12 CAPs | Não | Pendente |
| Eventos e dependências | Sim | Event/Edge/Receipt candidatos | Não | Pendente |
| Autorização, revogação e tenant | Sim | Referências lógicas parciais | Não | Pendente |
| Migração e compatibilidade | Sim | Plano candidato | Não | Pendente |
| Gates, auditoria e alertas | Sim | Templates candidatos | Não | Pendente |
| Integração real com Replit/Neo4j | Diagnóstico proposto | Não validado ponta a ponta | Não verificado | Não autorizado por este estudo |

Não classificar nenhuma camada como `ready_for_production` ou `G1_passed`.

## 8. Plano de realização futura com pontos de controle
**Fase 0 — Ratificação de governança:** nomear papéis, autoridade de dados, finalidades e alçadas; fechar pendências críticas PND-01/02/03/08/11; registrar G0 e G2 separadamente.

**Fase 1 — Contratos normativos:** revisar schemas, envelope tipado e erros, versionamento e owners; criar matrizes de compatibilidade; somente então solicitar evidências G1.

**Fase 2 — Validação sintética isolada:** congelar commit e dependências, autorizar ambiente, revisar fixtures, executar apenas com autorização específica, preservar runs; submeter evidência G3 e G1 conforme escopo.

**Fase 3 — Métodos e avaliação:** definir rubricas para claims, lacunas, caminhos, ofertas e relatórios; avaliar erros, contradições e bias; atribuir revisão independente G5.

**Fase 4 — Integração isolada:** somente após autorização adicional, examinar o Replit existente, serviços canônicos, Neo4j e provedores; testar concorrência, revogação, invalidação e fallback; solicitar G4.

**Fase 5 — Preparação operacional:** definir SLOs, custos, retenção, incidentes, alertas, rollback e limites de rollout; avaliação G6 por autoridade formal.

**Fase 6 — Evolução de produto:** avaliar consumidores adicionais e B2B somente conforme segurança, evidência de valor e autorização por finalidade.

**Sequência sugerida, não calendário aprovado.** A ordem pode exigir tarefas paralelas, desde que dependências de autorização sejam preservadas.

## 9. Critérios mínimos para uma futura decisão de implementação
Uma proposta de implementação deve conter:
1. Componente e versão exatos, owner e serviço canônico afetado.
2. Fronteira de confiança, dados processados, finalidade e política de autorização.
3. Contrato aprovado, estados independentes e semântica temporal.
4. Dependências e risco de indisponibilidade/ordenação.
5. Casos de teste, ambiente e evidências observadas.
6. Medidas de privacidade, logs, retenção e isolamento.
7. Métricas de qualidade, custo e desempenho, sem valores inventados.
8. Plano de falha segura, reconciliação e rollback.
9. Responsável de revisão e autoridade competente para autorizar a etapa.
10. Relação com gate e PND ainda abertos.

**Prontidão para pedir uma decisão de implementação não é permissão para implementar.**

## 10. Riscos transversais e salvaguardas
| Risco | Salvaguarda futura obrigatória |
| --- | --- |
| Supor LLM como fonte | Proveniência canônica, tipo epistêmico e limitações |
| Falsa correspondência entre Pessoa e oferta | Separar possibilidade, elegibilidade, publicação e disponibilidade |
| Resultado antigo apresentado como válido | CAP-10, temporalidade, recibos e revalidação |
| Consentimento confundido com entrega | Verificações específicas por finalidade, sujeito e destinatário |
| Violação entre tenants | Autorização no serviço, segmentação e testes negativos |
| Neo4j com projeção incompleta | Fonte canônica, reconciliação e sinalização de cobertura |
| Schema aceito tratado como qualidade | Testes semânticos e revisão humana |
| Gate criado sem autoridade | GateDecision formal, validade e trilha de evidência |
| Fallback multi-modelo sem avaliação | Métodos versionados, qualidade e segurança |
| Integração prematura do Replit | Escopo e autorização de inspeção/execução próprios |

## 11. Critérios de gate preservados
- **G0:** parcialmente documentado; faltam owners e ratificações.
- **G1:** contratos e schemas candidatos exigem testes/revisão e decisão formal.
- **G2:** segurança, autoridade, autorização e revogação exigem comprovação real.
- **G3:** fixtures ainda sem resultados observados/adjudicados.
- **G4:** nenhuma integração isolada foi autorizada ou comprovada por estes estudos.
- **G5:** revisão independente e adjudicação não executadas.
- **G6:** nenhuma liberação ou autorização de produção estabelecida.

## 12. Pacote de navegação
Arquitetura: [INT-01](arquitetura-integrada-plano-validacao.md) · [INT-02](normalizacao-contratos-estados-compartilhados.md).
Segurança: [INT-05](autoridade-dados-consentimentos-revogacao.md).
Eventos: [INT-06](modelo-dependencias-eventos-propagacao-invalidacao.md) · [INT-07](contratos-eventos-projecao-dependencias.md).
Contratos: [INT-08](catalogo-formal-schemas-compatibilidade-servicos.md) · [INT-09](schemas-especializados-erros-recibos-eventos.md) · [INT-10](conformidade-schemas-casos-contrato-compatibilidade.md) · [INT-11](cobertura-contratos-especializados-integracao-schemas.md).
Homologação e evolução: [INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [INT-13](plano-compatibilidade-migracao-evolucao-contratos.md).
Decisões e avaliação: [INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [INT-15](preparacao-execucao-sintetica-controlada-evidencias-gate.md) · [INT-16](pacote-evidencias-revisao-independente-adjudicacao-gates.md) · [INT-17](modelo-rastreabilidade-auditoria-proveniencia-gates.md) · [INT-18](modelo-observabilidade-gates-alertas-revalidacao.md).

## 13. Próximo avanço recomendado
[**GAI-INT-20 — Matriz de Dependências, Sequenciamento de Decisões e Critérios de Entrada na Implementação**](matriz-dependencias-sequenciamento-entrada-implementacao.md) para transformar esta visão integrada em backlog arquitetural priorizado, com ownership candidato e pré-requisitos concretos. Permanecer na governança documental até que ocorra autorização expressa de execução.

**Nenhuma alteração ao Replit, Neo4j, provedores, API, GKR ou gates operacionais foi realizada por este estudo.**
