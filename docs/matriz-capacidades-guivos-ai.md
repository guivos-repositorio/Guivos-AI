# Matriz de Capacidades da Guivos AI
**Versão documental 6.7 · 31/10/2026**
**Estado:** planejamento conceitual e priorização proposta, sem homologação técnica, comercial ou autorização de implantação.

## 1. Função deste documento
Transformar os fundamentos e estudos da Guivos AI em um catálogo rastreável de capacidades: **qual problema resolve, quais fontes autorizadas necessita, como analisa, que resultado entrega, como é avaliada, de que depende e onde poderá ser utilizada**.

**Premissa arquitetural aprovada:** Guivos Intelligence consome capacidades especializadas da Guivos AI. O serviço de contexto do ecossistema é autoridade pelos registros canônicos, versões e permissões; a Guivos AI é responsável pelo método analítico; Intelligence pela orquestração e pela experiência. Essa separação não equivale a integração técnica concluída.

### Vocabulário de estados
- **Conceituada:** existe especificação documental; não foi implementada.
- **Em protótipo:** código ou mecanismo isolado demonstrado; não significa operação no fluxo público.
- **Em avaliação:** há protocolo de teste ativo e resultados registrados para versão identificada.
- **Homologada:** cumpre critérios e aprovações explicitamente estabelecidos.
- **Operacional:** integrada e liberada para escopo delimitado, com monitoramento.
**Nenhuma capacidade abaixo é declarada homologada ou operacional.** Os componentes isolados já identificados no Replit pertencem à POC existente, não demonstram entrega da Guivos AI especializada.

## 2. Matriz de capacidades especializadas (proposta)
| ID | Capacidade | Entradas autorizadas principais | Método/resultado esperado | Avaliação específica | Aplicações candidatas | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| GAI-CAP-01 | Leitura de trajetória | Declarações, experiências, registros temporais | Linha contextual de acontecimentos e mudanças com fontes | Fidelidade factual, temporalidade e versões | Jornada; Relatório | Conceituada |
| GAI-CAP-02 | Síntese do momento atual | Contexto, condições, preferências e revisões | Quadro de condições conhecidas, desconhecidas e contestadas | Atualidade, separação fato/hipótese, omissões | Journey/Intelligence; Relatório | Conceituada |
| GAI-CAP-03 | Interpretação fundamentada | Evidências, eventos e fontes autorizadas | Afirmações com suporte, limites e perguntas | Suporte por afirmação, atribuição, não invenção | Todas as análises | Conceituada |
| GAI-CAP-04 | Identificação de lacunas | Requisitos verificados, condições e objetivos | Lacuna confirmada, possível ou informação desconhecida | Falsas lacunas; exatidão de requisitos | Jornada; Relatório; API | Conceituada |
| GAI-CAP-05 | Descoberta de possibilidades | Objetivos, experiências, competências, contexto | Futuros declarados, adjacentes, emergentes e exploratórios | Relevância, evidências, autonomia, diversidade | Jornada; mentoria; API | Conceituada |
| GAI-CAP-06 | Compatibilidade contextual futura | Possibilidade, requisitos e condições atuais | Estados por requisito, alternativas e incertezas | Requisitos corretos, temporalidade, não discriminação | Relatório; API; Journey | Conceituada |
| GAI-CAP-07 | Caminhos intermediários | Lacunas, condições, supply e restrições | Sequências alternativas com necessidades habilitadoras | Viabilidade, transparência, ausência de promessa | Jornada; Relatório | Conceituada |
| GAI-CAP-08 | Qualificação de oportunidades | Ofertas, emissores, requisitos, datas e eventos | Disponibilidade verificada e adequação condicional | Ofertas falsas/expiradas, semântica dos eventos | Journey; Mall/Travel quando aplicável | Conceituada |
| GAI-CAP-09 | Gestão de incerteza e contradição | Fontes, versões, escopos e tempos | Divergências tipadas e perguntas para esclarecer | Conflitos falsos, fontes duplicadas, calibração | Todas as análises | Conceituada |
| GAI-CAP-10 | Reavaliação e invalidação | Revisões, revogações, mudanças e dependências | Indicação de análises obsoletas e reprocessamento legítimo | Propagação de invalidação; bloqueio de dados revogados | Intelligence; API; Relatório | Conceituada |
| GAI-CAP-11 | Relatório de Trajetória e Possibilidades | Resultados GAI-CAP-01 a 10, escopo profissional | Relatório explicável, temporal, validável | Utilidade, clareza, integridade e acesso | Produto comercial inicial | Conceituada |
| GAI-CAP-12 | API especializada | Autenticação, escopo, contexto e capacidade solicitada | Resposta versionada de análises, sem histórico indiscriminado | Segurança, isolamento, contratos, custo e falhas | Plataformas parceiras; Intelligence | Conceituada |

### Especificações documentadas das capacidades
- [GAI-CAP-01 — Leitura e Compreensão de Trajetórias](cap-01-leitura-compreensao-trajetorias.md): especificação v1.3, contrato lógico, temporalidade, evidências e testes sintéticos propostos. **Estado: conceituada**.
- [GAI-CAP-02 — Síntese do Momento Atual](cap-02-sintese-momento-atual.md): especificação v1.4, dimensões contextuais, estados de informação, perguntas e contratos lógicos. **Estado: conceituada**.
- [GAI-CAP-03 — Interpretação Fundamentada em Evidências](cap-03-interpretacao-fundamentada-evidencias.md): especificação v1.5, afirmações verificáveis, suporte por fonte, incerteza, contradições e validação transversal. **Estado: conceituada**.
- [GAI-CAP-04 — Identificação e Qualificação de Lacunas](cap-04-identificacao-qualificacao-lacunas.md): especificação v1.6, comparação por requisito, estados, evidências e oportunidades habilitadoras. **Estado: conceituada**.
- [GAI-CAP-05 — Descoberta de Possibilidades Futuras](cap-05-descoberta-possibilidades-futuras.md): especificação v1.7, possibilidades declaradas, adjacentes, emergentes e exploratórias; evidências e validação de interesse. **Estado: conceituada**.
- [GAI-CAP-06 — Inteligência de Compatibilidade Futura](cap-06-inteligencia-compatibilidade-futura.md): especificação v1.8, avaliação condicionada por requisito, estados e cenários temporais, sem score de valor pessoal. **Estado: conceituada**.
- [GAI-CAP-07 — Identificação de Caminhos Intermediários](cap-07-caminhos-intermediarios.md): especificação v1.9, rotas alternativas, etapas e dependências, oportunidades diretas/habilitadoras e autonomia da Pessoa. **Estado: conceituada**.
- [GAI-CAP-08 — Qualificação de Oportunidades](cap-08-qualificacao-oportunidades.md): especificação v2.0, existência e atualidade da oferta, verificação de disponibilidade, requisitos e pertinência contextual. **Estado: conceituada**.
- [GAI-CAP-09 — Gestão de Incertezas e Contradições](cap-09-gestao-incertezas-contradicoes.md): especificação v2.1, conflitos temporais e semânticos, divergências GPT/Claude/Gemini, incertezas e revisão humana. **Estado: conceituada**.
- [GAI-CAP-10 — Reavaliação e Invalidação de Análises](cap-10-reavaliacao-invalidacao-analises.md): especificação v2.2, eventos, dependências, validade das análises, propagação e atualização sob autorização. **Estado: conceituada**.
- [GAI-CAP-11 — Relatório de Trajetória e Possibilidades](cap-11-relatorio-trajetoria-possibilidades.md): especificação v2.3, seções modulares, proveniência, validação pela Pessoa e entrega sob autorização específica. **Estado: conceituada**.
- [GAI-CAP-12 — API Especializada da Guivos AI](cap-12-api-especializada-guivos-ai.md): especificação v2.4, contratos internos e B2B, autorização por finalidade, versionamento e segurança. **Estado: conceituada**.

**Primeira rodada documental concluída:** CAP-01 a CAP-12 têm especificações; nenhuma capacidade foi declarada homologada ou operacional.

**Revisão integrada:** [GAI-INT-01 — Arquitetura Integrada e Plano de Validação v2.5](arquitetura-integrada-plano-validacao.md). Identifica dependências não circulares, limites de autoridade, estados compartilhados e critérios de avaliação ponta a ponta. Não altera os estados de maturidade.

**Contratos e estados transversais:** [GAI-INT-02 — Normalização dos Contratos e Estados Compartilhados v2.6](normalizacao-contratos-estados-compartilhados.md). Distingue status de execução, validade, suporte, escolha da Pessoa, publicação e disponibilidade da oferta; os contratos seguem propostos e não homologados.

**Testes integrados e gates:** [GAI-INT-03 — Matriz de Testes Integrados, Critérios de Aceite e Gates v2.7](matriz-testes-integrados-criterios-aceite-gates.md). Plano de cenários, severidade, evidência e adjudicação humana, sem testes executados ou alteração da maturidade das capacidades.

**Catálogo de avaliação:** [GAI-INT-04 — Fixtures, Rubricas e Adjudicação v2.8](catalogo-fixtures-rubricas-adjudicacao.md). Organiza casos, dados sintéticos, rubricas, runs e decisões humanas sem atribuir resultados ou gates aprovados.

**Autoridade e revogação:** [GAI-INT-05 — Autoridade de Dados, Consentimentos e Fluxos de Revogação v2.9](autoridade-dados-consentimentos-revogacao.md). Separa autoridade canônica, autorização por finalidade, consentimento quando aplicável, processamento, entrega e efeitos de revogação. Não altera a maturidade das capacidades.

**Eventos e invalidação:** [GAI-INT-06 — Modelo de Dependências, Eventos e Propagação de Invalidação v3.0](modelo-dependencias-eventos-propagacao-invalidacao.md). Complementa CAP-10 e INT-05 com semântica de eventos canônicos, dependências diretas/transitivas e propagação seletiva, sem homologar capacidade.

**Contratos de eventos e projeções:** [GAI-INT-07 — Contratos de Eventos e Projeção de Dependências v3.1](contratos-eventos-projecao-dependencias.md). Define semântica de envelopes, índices, recibos e consistência, sem instalar schema Neo4j ou executar testes.

**Catálogo de schemas:** [GAI-INT-08 — Catálogo Formal de Schemas e Compatibilidade entre Serviços v3.2](catalogo-formal-schemas-compatibilidade-servicos.md). Três contratos JSON Schema candidatos, ainda não homologados, para envelope de análise e evento canônico.

**Schemas especializados e recibos:** [GAI-INT-09 — Schemas Especializados, Contratos de Erro e Recibos de Eventos v3.3](schemas-especializados-erros-recibos-eventos.md). Oito novos schemas candidatos, sem homologação, integração aos envelopes ou execução de testes.

**Conformidade de contratos:** [GAI-INT-10 — Conformidade de Schemas, Casos de Contrato e Compatibilidade v3.4](conformidade-schemas-casos-contrato-compatibilidade.md). Catálogo sintético de 25 casos e executor offline candidato, ainda sem resultados de execução ou homologação.

**Cobertura de contratos:** [GAI-INT-11 — Cobertura dos Contratos Especializados e Integração dos Schemas v3.5](cobertura-contratos-especializados-integracao-schemas.md). Sete novos payloads, envelope tipado por CAP e 24 casos sintéticos não executados; sem alteração de maturidade.

**Prontidão e homologação:** [GAI-INT-12 — Relatório de Conformidade e Estratégia de Homologação Contratual v3.6](relatorio-conformidade-estrategia-homologacao-contratual.md). Consolida critérios, evidências, riscos e gates pendentes; não constitui teste nem homologação.

**Compatibilidade e migração:** [GAI-INT-13 — Plano de Compatibilidade, Migração e Evolução de Contratos v3.7](plano-compatibilidade-migracao-evolucao-contratos.md). Mapeia versões, consumidores, adaptação, regressão e rollback; não altera a maturidade das capacidades.

**Decisões e gates:** [GAI-INT-14 — Registro de Decisões Pendentes e Plano de Fechamento de Gates v3.8](registro-decisoes-pendentes-plano-fechamento-gates.md). Consolida 16 decisões ainda em aberto e evidências exigidas para gates, sem alteração da maturidade das capacidades.

**Preparação de avaliação:** [GAI-INT-15 — Execução Sintética Controlada e Evidências de Gate v3.9](preparacao-execucao-sintetica-controlada-evidencias-gate.md). Exige autorização formal, ambiente isolado, evidências de run e revisão independente; nenhuma execução está autorizada.

**Evidências e adjudicação:** [GAI-INT-16 — Pacote de Evidências, Revisão Independente e Adjudicação de Gates v4.0](pacote-evidencias-revisao-independente-adjudicacao-gates.md). Define evidências, pareceres, dissensos e decisão formal de gate, com modelos não preenchidos e nenhuma aprovação.

**Rastreabilidade de evidências:** [GAI-INT-17 — Modelo de Rastreabilidade, Auditoria e Proveniência de Evidências de Gate v4.1](modelo-rastreabilidade-auditoria-proveniencia-gates.md). Objetos e relações de auditoria, 18 cenários sintéticos e template não preenchido; gates inalterados.

**Observabilidade de gates:** [GAI-INT-18 — Observabilidade de Gates, Alertas e Revalidação Contínua v4.2](modelo-observabilidade-gates-alertas-revalidacao.md). Contempla sinais e revalidação de evidências, versões e autorizações; sem monitoramento operacional.

**Arquitetura consolidada:** [GAI-INT-19 — Consolidação de Arquitetura e Critérios de Prontidão para Implementação v4.3](consolidacao-arquitetura-prontidao-implementacao.md). Mapa integrado das 12 CAPs, serviços, contratos, decisões e gates pendentes; não autoriza implementação.

**Backlog e dependências:** [GAI-INT-20 — Matriz de Dependências, Sequenciamento e Entrada na Implementação v4.4](matriz-dependencias-sequenciamento-entrada-implementacao.md). Define 16 itens e dependências por gate; responsáveis e execução não autorizados.

**Deliberação e autorização:** [GAI-INT-21 — Decisões G0/G2 e Autorização de Validação Estrutural v4.5](pacote-decisoes-g0-g2-autorizacao-validacao-estrutural.md). Oito propostas pendentes para fundamentar gates e eventual campanha offline; nenhuma execução autorizada.

**Autoridade e alçadas:** [GAI-INT-22 — Encaminhamento de D21-01/D21-02 v4.6](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md). Define fronteiras conceituais de fonte e revisão; atribuições formais e gates permanecem pendentes.

**Responsabilidades e ratificação:** [GAI-INT-23 — Dossiê de Ratificação v4.7](dossie-ratificacao-responsaveis-autoridade-alcadas.md). Define evidências de nomeação, aceite e alçada para 16 funções candidatas; nenhuma atribuição formal registrada.

**Administração e autoridade:** [GAI-INT-24 — Verificação de Controle do GitHub v4.8](verificacao-administracao-repositorio-limites-autoridade.md). A conexão atual tem administração técnica do repositório, sem evidência de mandato institucional de gate ou dados.

**Governança inicial:** [GAI-DEC-009 — Instância de Governança Estratégica](decisao-instancia-governanca-direcao-guivos.md). A direção da Guivos conduz nomeações e decisões iniciais, mas não há titulares ou gates homologados.

**Designações e segregação:** [GAI-INT-25 — Modelo Inicial de Designações v5.0](modelo-inicial-designacoes-segregacao-responsabilidades.md). Papéis candidatos P0–P3, responsabilidades técnicas e revisão independente; sem nomeações formais.

**Inventário técnico verificado:** [GAI-INT-26 — Inventário e Designações P0 v5.1](inventario-tecnico-inicial-designacoes-p0.md). Inspeção dos diretórios GitHub e separação de artefatos candidatos dos serviços operacionais ainda não verificados.

**Designações P0:** [GAI-INT-27 — Termos P0-A/P0-B v5.2](termos-designacao-coordenacao-arquitetura-inventario-canonico.md). Mandatos candidatos para coordenação de arquitetura e inventário canônico; sem responsáveis ratificados.

**Indicação P0 pendente:** [GAI-INT-28 — Minuta Executiva v5.3](minuta-executiva-indicacao-p0-a-p0-b.md). Alternativas de alocação para P0-A/P0-B sem nomeados nem mandatos.

**Coordenação temporária:** [GAI-DEC-010](decisao-coordenacao-temporaria-direcao-p0-a-p0-b.md). Alternativa C confirmada para P0-A/P0-B, sem nomeação individual ou gate aprovado.

**Representação P0:** [GAI-INT-29](encaminhamento-representante-temporario-p0.md) prepara indicação e aceite de representantes temporários pela direção, sem delegação operacional.

**Controle de autorização:** [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md). Aprovação administrativa prévia e específica centralizada no representante declarante da direção; nenhuma execução ou gate automaticamente autorizado.

**Revisão estática autorizada:** [GAI-REV-001](relatorio-revisao-estatica-autorizada-pedido-a.md) registra achados STA-01 a STA-10 sobre contratos candidate-v1; nenhuma execução, validação semântica ou gate aprovado.

**Correções prioritárias propostas:** [GAI-INT-31](propostas-correcao-contratos-prioritarios-sta01-sta02-sta03.md) define condições para compartilhamento, recibos e eventos canônicos, ainda sem aprovação de schemas ou testes.

**Schemas candidatos v2:** [GAI-INT-32](schemas-candidatos-v2-propostas-sta01-sta02-sta03.md), três arquivos isolados de candidate-v1, sem execução nem homologação.

**Compatibilidade do contrato tipado:** [GAI-INT-33](compatibilidade-contrato-tipado-matriz-casos-v2.md) delimita CAP-11 v1/v2, recibos e eventos e prepara 15 casos não executados.

**Envelope tipado v2 candidato:** [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md) define proposta de `result` apenas para `completed`, mantendo os contratos anteriores.

**Deliberação de compatibilidade pendente:** [GAI-INT-35](deliberacao-compatibilidade-versionamento-envelope-v2.md) organiza escolhas A/B/C e recomenda A1/B1/C1, ainda não ratificadas.

**Política de envelope confirmada:** [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md). A1/B1/C1 para desenho candidato, sem homologação ou execução. O contrato-base candidate-2 está isolado.

**Casos candidate-2:** [GAI-INT-36](matriz-casos-protocolo-candidate-2.md) documenta 18 casos não executados e seis verificações de compatibilidade.

**Prontidão de testes sintéticos:** [GAI-INT-37](pacote-prontidao-testes-offline-candidate-2.md). 82 casos preparados, com runners v2 e execução ainda pendentes de decisões específicas.

**Executor v2 proposto:** [GAI-INT-38](especificacao-executor-offline-33-casos-v2.md) estabelece interface, normalização de 33 casos e registry local, sem implementação ou execução.

**Executor v2 implementado:** [GAI-INT-39](implementacao-executor-offline-v2-nao-executado.md) registra código isolado para os 33 casos v2, ainda não testado e sem autorização B.

## 3. Capacidades estruturais habilitadoras (não equivalentes à Guivos AI)
| ID | Responsável proposto | Capacidade habilitadora | Dependência |
| --- | --- | --- | --- |
| GAI-DEP-01 | Serviços de identidade/autorização | Verificação de Pessoa, vínculo e finalidade | Pré-requisito de consulta com dados reais |
| GAI-DEP-02 | Serviço de contexto canônico | Persistência, versões, correções e retenção | Base de rastreabilidade |
| GAI-DEP-03 | Serviço de memória/Neo4j | Recuperação autorizada de relações e proveniência | Fonte de evidências relacionais |
| GAI-DEP-04 | Serviços de oportunidades | Ofertas, requisitos, data de verificação e eventos | Validade de supply |
| GAI-DEP-05 | Guivos Intelligence | Orquestração da Jornada, validação e exibição | Consumo interno e UX |
| GAI-DEP-06 | Adaptadores de modelos | Execução controlada GPT/Claude/Gemini; limites e auditoria | Tecnologia sob escolha por capacidade |
| GAI-DEP-07 | Governança/evaluations | Fixtures, revisores, bloqueios e decisão de release | Homologação antes de uso real |
| GAI-DEP-08 | Segurança/observabilidade | Segregação, custos, logs apropriados, rollback | Operação controlada |

**Neo4j não deve ser tratado como substituto automático do armazenamento transacional.** Dados e registros canônicos continuam subordinados à decisão arquitetural por domínio.

## 4. Dependências entre capacidades
- CAP-01, CAP-02 e CAP-03 formam base analítica de contexto e evidências.
- CAP-04 depende de CAP-02, CAP-03 e requisitos válidos de ofertas/caminhos.
- CAP-05 depende de CAP-01 a CAP-03, e não pode converter sugestões em objetivos declarados.
- CAP-06 depende de CAP-02, CAP-03, CAP-04 e CAP-05.
- CAP-07 depende de CAP-04, CAP-06 e oferta/recurso verificável quando houver.
- CAP-08 depende de fontes de oportunidades e de verificação temporal.
- CAP-09 é transversal, inclusive em comparações GPT/Claude/Gemini.
- CAP-10 depende da proveniência de CAP-03 e de mecanismos de correção dos serviços canônicos.
- CAP-11 integra resultados conforme finalidade e permissões; não pode contornar dependências.
- CAP-12 expõe apenas capacidades homologadas para o escopo do consumidor.

## 5. Priorização preliminar por ondas (não cronograma de implantação)
**Onda A — Fundamentos verificáveis:** evidências/afirmações (CAP-03), momento atual (CAP-02), trajetória (CAP-01), contradições (CAP-09), revisão (CAP-10). Pré-requisitos: identidade, contexto versionado, fixtures, autorização e contratos.

**Onda B — Inteligência prospectiva:** lacunas (CAP-04), possibilidades (CAP-05), compatibilidade (CAP-06), oportunidades (CAP-08), caminhos (CAP-07). Depende de uma base analítica confiável e fontes de supply verificadas.

**Onda C — Produtos e integração:** relatório (CAP-11), API (CAP-12). Exige autorização, avaliação de utilidade, isolamento entre consumidores e validação técnica/comercial.

A ordem poderá mudar por risco, viabilidade e resultados experimentais. Não há datas, recursos nem esforço estimados e não existe autorização automática de desenvolvimento.

## 6. Matriz de riscos por consumidor
| Consumidor | Objetivo | Risco relevante | Controle necessário |
| --- | --- | --- | --- |
| Jornada da Pessoa | Compreensão e descoberta | Direcionamento indevido ou hipótese como certeza | Validação explícita da Pessoa e evidências |
| Guivos Intelligence | Orquestração | Uso de resposta obsoleta ou fora de escopo | Versão contextual, autorização, cancelamento |
| Mentores/orientadores | Relatórios de apoio | Conclusões interpretadas como julgamento da Pessoa | Transparência, limites, revisão profissional |
| Sistemas educacionais | Orientação de caminhos | Padronização excessiva de trajetórias | Caminhos alternativos e condições contextuais |
| Aplicações clínicas | Uso potencial de dados sensíveis | Diagnóstico indevido, exposição e dano | Governança e aprovação específicas; não inferir disponibilidade comercial |
| Parceiros por API | Integração B2B | Vazamento entre Pessoas, profissionais ou instituições | Isolamento, credenciais, contrato e auditoria |

## 7. Ficha padrão de capacidade
Cada capacidade terá documento próprio com:
1. Identificador, nome, propósito e responsável funcional;
2. Casos de uso, usuários e situações de **não uso**;
3. Entradas, fontes canônicas, dados mínimos, finalidades e autorizações;
4. Método, relações conceituais e limites;
5. Contrato de saída: evidências, hipóteses, incertezas e versão;
6. Dependências e estados de falha/fallback;
7. Métricas e casos de avaliação;
8. Riscos, gate aplicável, revisor e autoridade de aprovação;
9. Estado real, artefatos, resultados de teste e data da última revisão;
10. Histórico de decisões, mudanças e compatibilidade com consumers.

## 8. Critérios para transição de estado
**Conceituada → protótipo:** autorização de construção e contrato de teste.  
**Protótipo → em avaliação:** fixtures executáveis, ambientes isolados, resultados reproduzíveis.  
**Em avaliação → homologada:** evidências comparadas a limites aprovados e adjudicação formal.  
**Homologada → operacional:** integração, segurança, monitoramento, política de rollback e liberação explícita.

Nenhum teste dos adaptadores atuais do Replit transforma uma capacidade Guivos AI desta matriz em operacional. Não assumir que um teste de conexão externa valida qualidade analítica.

## 9. Como a matriz orienta GKR, Replit e produtos
- **GKR:** apenas referência cruzada institucional aprovada; sem edição automática.
- **Replit/Jornada:** utilizar a matriz para identificar pontos futuros de consumo sem alterar os gates existentes.
- **Neo4j:** mapear gradualmente as entidades temporais, fontes e projeções autorizadas conforme ontologia v0.9.
- **Relatório:** usar capacidades fundamentadas e autorizadas; não vender promessas de inferência causal ou diagnóstico.
- **API:** definir um contrato de capacidade especializado, sem tratar Guivos AI como quarto modelo GPT/Claude/Gemini.

## 10. Questões abertas
1. Qual conjunto mínimo de capacidades gera um Relatório de Trajetória e Possibilidades útil e verificável?
2. Qual a primeira métrica prioritária de utilidade e qualidade para os consumidores?
3. Quais capacidades requerem revisão humana obrigatória?
4. Quais dados de supply estarão confiáveis para CAP-08?
5. Como versionar contratos internos e externos e controlar consumo?
6. Quais são os custos por análise, público e modalidade de atualização?

## 11. Documentos de referência
[Documento Mestre](index.md) · [Modelo de Conhecimento](modelo-conhecimento-ontologia-temporal.md) · [Evidências e Rastreabilidade](modelo-evidencias-rastreabilidade.md) · [Avaliação e Validação](avaliacao-validacao-qualidade.md) · [Papéis Guivos AI / Intelligence](guivos-ai-vs-intelligence.md) · [Integração Replit](integracao-replit-intelligence-ai-neo4j.md).

**Estado final:** catálogo conceitual e proposta de sequenciamento; não foi desenvolvido software, criado esquema físico Neo4j, executado teste de IA ou autorizado release.
