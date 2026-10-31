# Autoridade de Dados, Memória Canônica e Consumo de Inteligência
**Guivos AI · Documento de arquitetura v0.8 · 31/10/2026**

> Status: direção conceitual aprovada para separação de responsabilidades; detalhamento técnico é proposta em estudo. Não autoriza alteração operacional de POC/Replit, ativação de gates ou processamento de dados reais.

**Aprofundamento especializado:** [GAI-INT-05 — Autoridade de Dados, Consentimentos e Fluxos de Revogação v2.9](autoridade-dados-consentimentos-revogacao.md). O presente texto conserva o estudo de arquitetura v0.8; o GAI-INT-05 detalha autorizações e fluxos propostos, sem aprovação operacional.

## 1. Princípio arquitetural
A **autoridade pelos fatos e permissões** pertence aos serviços de contexto e identidade do ecossistema Guivos, não ao modelo de linguagem. A **autoridade metodológica sobre análises especializadas** pertence à Guivos AI. A **autoridade de orquestração e experiência** pertence à Guivos Intelligence. A Pessoa e, quando aplicável, o profissional permanecem responsáveis por validar escolhas e decisões que lhes competem.

Autoridade técnica **não** significa propriedade sobre dados pessoais, nem substitui direitos da Pessoa ou responsabilidades legais das organizações.

## 2. Fronteiras e responsabilidades
| Domínio | Autoridade funcional proposta | Consumidores e limites |
| --- | --- | --- |
| Identidade e vínculo | Serviço de identidade Guivos | Intelligence/AI verificam, não presumem autorização |
| Permissões, finalidades e revogações | Serviço de autorização | Consultas restritas por finalidade, papel, escopo e período |
| Contribuições da Jornada e revisões | Serviço canônico de contexto | Intelligence e AI apenas por interfaces autorizadas |
| Oportunidades e eventos observados | Serviços de oportunidades/ecossistema | Análises devem preservar a semântica dos eventos |
| Histórico relacional e proveniência | Serviço de memória; Neo4j como infraestrutura candidata | Não conceder consulta direta irrestrita a modelos |
| Métodos de análise de trajetórias, lacunas e futuros | Guivos AI | Intelligence e parceiros recebem resultados rastreáveis |
| Fluxo conversacional, estado de interação e apresentação | Guivos Intelligence | Solicita análises, valida atualidade, integra retorno |
| Decisões sobre a vida e participação | Pessoa e profissionais habilitados, conforme contexto | Nenhuma pontuação ou diagnóstico automático vinculante |
| API comercial | Guivos AI, sob autenticação e política da plataforma | Escopos explícitos; nunca venda de dados pessoais |

## 3. Memória: o que é canônico e o que é derivado
**Canônico:** identidade/referências; declarações da Pessoa; contribuições originais autorizadas; versões e correções; eventos de oportunidade; autorização; decisões e validações explícitas, cada qual no sistema de origem competente.

**Derivado:** resumo contextual, hipóteses, análises de compatibilidade, relações inferidas, sugestões de oportunidades, relatórios e respostas de modelos. Resultados derivados devem apontar para a versão de evidências empregada. Não sobrescrever fatos originais com inferências.

**Memória operacional transitória:** contexto de sessão e estado de execução usados pela Guivos Intelligence não são autoridade canônica. Podem ser descartados/reconstituídos segundo a política de retenção.

**Neo4j:** pode armazenar relações, tempo e proveniência mediante adaptadores. Banco de grafo não precisa ser único armazenamento transacional: definir arquitetura de fonte de verdade por tipo de dado antes da implantação.

## 4. Relações temporais e proveniência
Entidades conceituais: Pessoa, Momento, Declaração, Objetivo, Evidência, Fonte, Oportunidade, EventoDeInteração, Requisito, Possibilidade, Lacuna, Análise, Hipótese, VínculoProfissional, Autorização, Revisão.

Cada relação deve carregar quando pertinente:
- Identificador e versão da fonte;
- Origem (Pessoa, profissional, plataforma, parceiro, inferência);
- Ocorrência e registro temporal;
- Finalidade e escopo de acesso;
- Confirmação, contestação, validade temporal e incerteza;
- Política de retenção/correção/exclusão.

Não tratar recomendações exibidas como oportunidades conscientemente percebidas ou ignoradas.

## 5. Contrato de consumo Intelligence → Guivos AI (proposta)
**Solicitação:** finalidade da análise; identidade autenticada/escopo de autorização; tipo de capacidade especializada; referência de contexto com versão; dados mínimos estritamente necessários; horizonte temporal; restrições; identificador de correlação.

**Resposta:** identificador e versão da análise; afirmações com referências de evidências; separação entre fatos, hipóteses e desconhecidos; lacunas qualificadas; alternativas; perguntas de aprofundamento; limites; prazo de validade/revisão; informação de modelo/método para auditoria.

**Regras:** a Guivos AI não decide automaticamente quais permissões valem; verifica o contrato/escopo por serviço seguro. A Intelligence rejeita resultados defasados, não inventa consenso entre modelos e não interpreta falha como conclusão de que a Pessoa não possui possibilidades.

## 6. Consumo por parceiros externos
A integração B2B poderá operar por API especializada, sem obrigar o parceiro a executar Guivos Intelligence. A Pessoa deverá existir na Guivos para a modalidade de relatórios ligada à Jornada e aprovar os acessos aplicáveis. O parceiro não recebe histórico bruto por padrão; recebe resultados autorizados, fundamentados e minimizados.

Notas profissionais potencialmente sensíveis permanecem segregadas e não são automaticamente incorporadas à Jornada Guivos. Aplicações clínicas exigem critérios próprios, avaliação profissional e governança reforçada.

## 7. Ciclo de correção, revogação e exclusão
1. A Pessoa contesta ou corrige uma informação.
2. O serviço de origem registra revisão/versionamento e invalida referências conforme regras.
3. Serviço de memória atualiza relações derivadas e emite sinal de invalidação.
4. Análises afetadas da Guivos AI são marcadas obsoletas e reavaliadas apenas se houver finalidade e autorização.
5. Intelligence deixa de apresentar resultados antigos como atuais.
6. Cópias e caches de parceiros seguem contratos de expiração, revogação e exclusão aplicáveis.

Revogação de acesso futuro e eliminação de dados sujeitos a regras de retenção são operações distintas; não prometer exclusão instantânea irrestrita.

## 8. Jornada da Pessoa: integração incremental sugerida
**Estado diagnosticado em v0.7:** UI pública guarda contribuições apenas em estado de sessão; não percorre persistência durável e IA real; POC possui adaptadores, executor de compreensão e Neo4j exercitado com dados sintéticos. Gates operacionais permanecem fechados.

**Sequência candidata, condicionada a autorização:**
1. Formalizar entidade de identidade e autorização real;
2. Selecionar fontes canônicas por evento e dado;
3. Conectar persistência durável com versões e trilha de auditoria;
4. Garantir recuperação de contexto autorizado e testes com fixtures;
5. Validar execução cognitiva em ambiente privado e controlado;
6. Adicionar chamada tipada à Guivos AI sem caracterizá-la como quarto provedor fundacional;
7. Apresentar análises versionadas e descartar respostas obsoletas;
8. Executar avaliações de segurança, qualidade e governança antes de qualquer release.

Não abrir gates nem alterar Replit em consequência exclusiva deste documento.

## 9. Falhas e resiliência
- **Neo4j indisponível:** não inventar histórico; sinalizar análise incompleta.
- **Guivos AI indisponível:** Intelligence pode continuar funcionalidades não especializadas, sem fingir relatório.
- **Modelo externo indisponível:** tratar timeout/erro e eventual fallback segundo política aprovada, preservando proveniência.
- **Permissão revogada:** bloquear novas leituras, revalidar resultados/cache e seguir ciclo de invalidação.
- **Contexto concorrente:** resultado associado a versão anterior deve ser descartado ou explicitamente marcado histórico.

## 10. Decisões ainda pendentes
- Quais bases serão fonte transacional de verdade para cada entidade?
- Neo4j será projeção relacional ou fonte canônica para subconjuntos específicos?
- Onde residirão os registros brutos e o arquivo de evidências?
- Quem será o responsável técnico por autorizações de uso interno e B2B?
- Qual contrato de evento/revisão sincroniza serviços?
- Qual política de persistência dos relatórios derivados e invalidação?
- Como isolar dados entre profissionais, instituições e parceiros?
- Quais avaliações/gates autorizam passar de fixture a dados reais?

## 11. Critérios de validação
Testes devem verificar identidade e segregação, autorização por finalidade, correção de versões, rastreabilidade, consistência da memória, invalidação, tratamento de falhas, não duplicação de fatos e rejeição de análises obsoletas. Casos sintéticos primeiro; dados reais apenas após governança e consentimentos apropriados.

## 12. Conexões documentais
- [Documento Mestre](index.md)
- [Papéis de AI e Intelligence](guivos-ai-vs-intelligence.md)
- [Auditoria da Jornada no Replit](integracao-replit-intelligence-ai-neo4j.md)
- [Governança do repositório](governanca-repositorio.md)

Este documento pertence exclusivamente à Guivos AI. O GKR não é alterado automaticamente.
