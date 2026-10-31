# GAI-INT-22 — Encaminhamento das Decisões D21-01 e D21-02: Autoridade Canônica e Alçadas
**Versão documental 4.6 · 31/10/2026**
**Estado:** direcionamento conceitual registrado; ratificação formal de responsáveis e alçadas **pendente**. G0 parcial, G2 pendente. Sem autorização de execução, testes, nomeações ou gates concedidos.

## 1. Resultado desta deliberação documental
A continuidade aprovada permite **consolidar o desenho de autoridade por domínio e a separação de responsabilidades**. Não significa que um responsável jurídico, técnico ou de segurança tenha aceitado formalmente sua alçada. A arquitetura mantém:
- autoridade canônica dos fatos e permissões nos **serviços proprietários de cada domínio**;
- Guivos Intelligence como orquestrador da experiência e da validação contextual pela Pessoa;
- Guivos AI como produtor de análises especializadas, evidências derivadas e limitações, não como fonte de verdade;
- GPT/Claude/Gemini como adaptadores de inferência, nunca autoridades sobre identidade, disponibilidade ou consentimento;
- Neo4j como banco e projeção de memória/relacionamentos **dentro do escopo autorizado**, não substituto automático de fonte canônica;
- GKR independente de Guivos AI, com referências conceituais controladas.

**D21-01:** direção conceitual escolhida para especificação = autoridade distribuída por domínio; **ratificação formal do inventário e do responsável de cada serviço ainda necessária**.

**D21-02:** direção conceitual escolhida para especificação = responsabilidades segregadas e revisão independente para riscos altos/críticos; **nomeações e competências de aprovação não realizadas**.

O [registro estruturado candidato](matriz-autoridade-alcadas-g0-g2-candidata.json) conserva explicitamente essas distinções.

## 2. Matriz de autoridade proposta
| Domínio | Origem/autoridade canônica candidata | Guivos Intelligence | Guivos AI | Neo4j |
| --- | --- | --- | --- | --- |
| Identidade de Pessoa, Organização, Coletivo | Serviço de identidade | Consumir e orquestrar | Consumir claims autorizados | Projeção não autoritativa |
| Contexto, declarações e versões da Pessoa | Serviço de contexto/evidências | Capturar, solicitar validação e mostrar revisão | Derivar análises sustentadas | Memória autorizada, revalidável |
| Base legal, finalidade, autorização e revogação | Serviço de autorização e políticas | Solicitar/explicar permissões | Aplicar limites em cada uso | Nunca conceder permissão |
| Oportunidade, publicação, elegibilidade e disponibilidade | Serviço canônico de oferta/supply | Apresentar possibilidades e limites | Analisar compatibilidade sem fabricar match | Índice reconciliável |
| Evidências, origem e correções | Proprietário de cada fonte | Mostrar suporte e incerteza | Manter proveniência de claims | Dependências versionadas |
| Relatórios, compartilhamento e entrega | Serviço responsável pela entrega/recibos | Confirmar fluxo e destinatário | Produzir artefato de análise candidato | Não provar entrega |
| Decisão de gate | Instância de governança designada | Sem poder automático de gate | Fornecer evidência, nunca autoaprovar | Projeção de estado, não autoridade |

**A matriz identifica funções candidatas, não serviços de fato verificados ou nomeados na infraestrutura atual.** Uma implementação real precisará provar quem mantém cada dado e quais contratos regulam sua emissão.

## 3. Papéis e segregação de atribuições
| Função a designar | Responsabilidade | Não pode presumir |
| --- | --- | --- |
| Responsável de arquitetura | Revisar fronteiras, dependências e ADRs | Ser titular de autorização de dados |
| Responsável por dados canônicos | Fonte, proveniência e correção no domínio | Aprovar todas as finalidades legais |
| Privacidade/jurídico | Parecer sobre base, finalidade, retenção e entrega | Substituir teste técnico de segurança |
| Segurança/identidade | Isolamento, credenciais, revogação e controle de acesso | Declarar análise semântica correta |
| Engenharia de contratos | Versão, schemas, compatibilidade e erros | Homologar G6 unilateralmente |
| Executor de QA | Rodar somente campanhas autorizadas e preservar logs | Aprovar o próprio resultado como gate |
| Revisor independente | Avaliar execução, resultados, limites e conflitos | Dar release sem alçada |
| Autoridade de gate | Decidir escopo, evidência, validade e restrições | Autorizar uso de dados fora da política canônica |

**Ainda não há titulares individuais designados, assinaturas, orçamentos ou prazos registrados.** As linhas do GAI-INT-14 PND-01 e PND-11 não podem ser marcadas como encerradas.

## 4. Regras para decisões G0/G2 futuras
1. Cada fonte deverá indicar `domain`, `canonical_owner_ref`, `service_ref`, `subject_scope`, `tenant_scope`, `source_version`, `effective_at`, `retention_policy_ref`, `authorization_policy_ref` e `correction_event_ref` quando aplicáveis.
2. Nenhum dado recebido de um modelo, relatório ou grafo vira canônico pelo consumo posterior.
3. Processar, compartilhar, reter e invalidar são operações distintas: cada uma requer política e prova específica.
4. Sem permissão vigente, o sistema consumidor deve falhar de modo seguro, incluindo revalidação de caches e derivados.
5. Eventos e recibos distinguem recebido, validado e aplicado; ausência de confirmação não vira evidência positiva.
6. Um gate exige `authority_ref` designado, escopo, decisão formal, evidências, validade e condições, e não uma ata de intenção.

## 5. Decisões pendentes transformadas em verificações objetivas
| Ref | O que precisa ser comprovado | Estado |
| --- | --- | --- |
| PND-01 / D21-01 | Inventário real de fontes, donos de serviço, contratos de atualização e políticas de correção | Ratificação pendente |
| PND-11 / D21-02 | Nomeação de funções, alçadas de G0/G2/G5/G6, revisão independente e impedimentos | Designação pendente |
| PND-02 | Bases legais e finalidades por fluxo, com revisão competente | Pendente |
| PND-03 | Identidade, isolamento tenant, escopos e consumidores reais | Pendente |
| PND-08 | Revogação, retenção e destino de derivados/entregas | Pendente |
| PND-09/12 | Fixtures, critérios e severidades revisados | Pendente |
| PND-10 | Autorização explícita de campanha offline delimitada | Não autorizada |

**As 16 decisões PND-01 a PND-16 continuam abertas.** Este estudo qualifica duas delas, não as conclui.

## 6. Condições para eventual primeira execução offline
O conjunto de 19 schemas candidatos e 49 fixtures estruturais sintéticas poderá ser proposto a uma campanha isolada, somente após definição de responsáveis, revisão de artefatos, dependências travadas, ambiente sem credenciais externas, critérios de parada, autorização formal da campanha e decisão de armazenamento de evidências.

Nenhum dos dois runners foi executado nesta etapa. Mesmo que a validação estrutural passe no futuro, não prova autorização, causalidade, qualidade das análises nem integração Replit/Neo4j.

## 7. Dossiê de ratificação
O [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md) prepara evidências de nomeação e aceite de titulares, sem alterar o estado pendente de D21-01 e D21-02.

## 8. Próximo trabalho de maior valor
A próxima ação recomendada não é produzir outro plano de alto nível: **designar autoridades reais para D21-01/D21-02** e revisar, em ambiente autorizado, o inventário de serviços que de fato existem. Só então preparar uma decisão separada para execução offline da campanha sintética.

**Referências:** [GAI-INT-21](pacote-decisoes-g0-g2-autorizacao-validacao-estrutural.md) · [GAI-INT-20](matriz-dependencias-sequenciamento-entrada-implementacao.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [Registro de Decisões](registro-decisoes.md).

**Sem alteração operacional em Replit, Neo4j, provedores, API ou GKR. Nenhum gate aprovado.**
