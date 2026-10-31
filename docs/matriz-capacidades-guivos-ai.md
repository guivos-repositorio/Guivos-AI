# Matriz de Capacidades da Guivos AI
**Versão documental 2.3 · 31/10/2026**
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

### Detalhamento da primeira capacidade
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
