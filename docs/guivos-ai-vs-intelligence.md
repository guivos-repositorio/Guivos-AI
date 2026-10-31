# Fronteira Arquitetural — Guivos AI e Guivos Intelligence
**Versão documental 0.6 · 31/10/2026**

## 1. Decisão e escopo
**Direção aprovada:** Guivos Intelligence consumirá Guivos AI. Ambos serão utilizados no ecossistema Guivos e desempenharão papéis distintos. Guivos AI e GKR preservam repositórios e governança documental independentes.

**Detalhamento abaixo:** proposta de distribuição técnica das responsabilidades; sujeita à validação de contratos, fluxos de autorização, integração e testes. Esta documentação não afirma implementação existente.

## 2. Definições
**Guivos AI — serviço de inteligência especializada.** Desenvolve e disponibiliza métodos de análise do universo Guivos: compreensão de trajetórias, evidências, lacunas, oportunidades, compatibilidade contextual, possibilidades atuais e futuros possíveis. Seus resultados incluem análises estruturadas, fontes, incertezas, hipóteses, perguntas e relatórios. Poderá servir tanto a Guivos Intelligence quanto a parceiros autorizados por API.

**Guivos Intelligence — camada de orquestração e inteligência aplicada ao ecossistema.** Conduz a interação nas superfícies Guivos, coordena o ciclo cognitivo e o fluxo da Jornada, escolhe quando solicitar análises especializadas, integra respostas a outros mecanismos e apresenta resultados adequados ao contexto e às validações da Pessoa.

**GKR — conhecimento institucional.** Mantém os fundamentos e decisões do ecossistema Guivos; não executa modelos de inteligência nem substitui o documento mestre Guivos AI.

## 3. Matriz de responsabilidades
| Capacidade | Guivos AI | Guivos Intelligence |
| --- | --- | --- |
| Métodos especializados de análise de trajetórias e possibilidades | Autoridade principal | Consome resultados |
| Modelagem de lacunas e compatibilidade futura | Autoridade principal | Integra à experiência |
| Fundamentação e rastreabilidade de interpretações | Produz evidências e limites do resultado | Preserva referências ao exibir ou aplicar |
| Ciclo conversacional na Jornada da Pessoa | Fornece análises e perguntas candidatas | Coordena interações e validações |
| Superfícies, navegação e estado da experiência | Não é responsável | Responsabilidade principal |
| Orquestração de fluxos e integrações internas | Oferece capacidades contratadas | Responsabilidade principal |
| Integração comercial com plataformas terceiras | Oferece serviço/API especializada | Não é dependência obrigatória |
| Identidade, autorização e finalidade de tratamento | Verifica o escopo recebido e aplica proteção no serviço | Obtém e encaminha contexto permitido conforme arquitetura |
| Persistência e fontes de dados | A definir contratualmente, minimizando duplicação | A definir contratualmente, minimizando duplicação |
| Seleção de provedores de modelos GPT, Claude e Gemini | Pode utilizar adaptadores próprios | Pode utilizar adaptadores para suas tarefas |
| Decisões que afetam a Pessoa | Não decide autonomamente | Não substitui decisão da Pessoa ou do profissional |

## 4. Fluxo de integração proposto
1. Pessoa interage com uma superfície Guivos.
2. Guivos Intelligence conduz o fluxo e determina a necessidade de análise.
3. O sistema verifica identidade, finalidade, vínculo profissional quando aplicável e permissões pertinentes.
4. Intelligence envia solicitação tipada à Guivos AI, com escopo, fontes permitidas e contexto mínimo necessário.
5. Guivos AI executa a análise especializada e retorna conteúdo estruturado: achados, evidências, incertezas, lacunas e perguntas.
6. Intelligence integra o resultado ao fluxo, solicita validações e apresenta oportunidades verificadas, sem fabricar certeza.
7. Feedback autorizado e correções são registrados conforme responsabilidades e políticas de dados definidas.

## 5. Contrato técnico conceitual
**Entrada:** finalidade, tipo de análise, escopo autorizado, referência contextual, horizonte temporal, fatos/evidências acessíveis, formato de saída.

**Saída:** tipo e versão da análise, conclusões com evidência, hipóteses, informações desconhecidas, alternativas, perguntas para validação, limitações, data e rastreabilidade.

**Regras:** versionar contratos; operar com escopo mínimo; não transferir todo o histórico indiscriminadamente; manter isolamento entre clientes; prever auditoria, recusa e revogação; permitir degradação segura quando Guivos AI estiver indisponível.

**A definir:** interface síncrona ou assíncrona, quem mantém memória canônica de cada informação, estratégia de cache, responsabilidades por consentimento e atualização de fontes.

## 6. Fronteira essencial
**Intelligence coordena o uso da inteligência; AI é autoridade pelos métodos especializados que publica.** Ambos podem empregar modelos de linguagem; isso não os torna serviços idênticos. O uso de múltiplos fornecedores (GPT, Claude, Gemini) não deve gerar conclusões concorrentes sem política de avaliação e resolução.

Guivos AI não deverá controlar decisões, interfaces e experiência geral das Homes. Guivos Intelligence não deverá duplicar indiscriminadamente os métodos especializados da Guivos AI.

## 7. Relação com o GKR
GKR documenta o ecossistema, sua arquitetura institucional e o papel das unidades. Guivos AI documenta seus próprios métodos, produtos, pesquisas, decisões e evolução. Mudanças em qualquer um dos dois repositórios exigem aprovação específica para repercussões no outro.

## 8. Pontos para amadurecimento
- Fronteira entre memória contextual da Jornada e memória especializada da Guivos AI.
- Definição de fonte canônica para cada fato e evento.
- Responsabilidade por monitoramento de qualidade e avaliações.
- Separação entre APIs internas e comerciais.
- Estratégia de custos, isolamento, segurança, autorização e auditoria.
- Resiliência a falhas do serviço especializado.
- Níveis de serviço para operações do ecossistema e clientes externos.
