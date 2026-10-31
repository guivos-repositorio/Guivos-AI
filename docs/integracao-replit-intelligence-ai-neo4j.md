# Arquitetura de Integração — Jornada da Pessoa, Guivos Intelligence, Guivos AI, Neo4j e Modelos
**Documento técnico v0.7 · 31/10/2026 · diagnóstico por inspeção de leitura no Replit e proposta arquitetural**

## 1. Separar estado observado de arquitetura desejada
**Observado:** inspeção sem alterações realizada pelo Replit Agent do projeto "Jornada da Pessoa" em 31/10/2026. Nenhum provedor, teste ou credencial foi executado/validado nesta inspeção; as evidências sobre campanhas externas são registros anteriores reportados pelo agente. As conclusões não devem ser promovidas a homologação operacional.

**Direção aprovada:** Guivos Intelligence consumirá Guivos AI, sendo ambos utilizados no ecossistema. Detalhes de contratos e implantação estão em estudo.

## 2. Papéis propostos
- **Jornada da Pessoa:** experiência de entrada multimodal e exibição dos resultados, sem acesso direto do navegador a modelos de IA nem a Neo4j.
- **Guivos Intelligence:** orquestra o fluxo conversacional e cognitivo, controla revisões, pedidos, validações, estados, seleção de capacidades e apresentação de respostas.
- **Guivos AI:** serviço de inteligência especializada em trajetórias, evidências, lacunas, oportunidades e possibilidades futuras; devolve análises estruturadas, hipóteses, fontes e limites; poderá atender plataformas externas por API.
- **Serviço de contexto e memória:** camada autorizada de leitura e escrita dos fatos e evidências, com Neo4j como componente de grafo; não pertence automaticamente ao provedor de linguagem nem deve ser duplicada em cada serviço.
- **GPT, Claude e Gemini:** motores de linguagem que podem ser chamados por adaptadores da orquestração Intelligence e/ou internamente pelo serviço Guivos AI, segundo finalidade e responsabilidades definidas.
- **Neo4j:** persistência de relações contextuais e proveniência, não um modelo de linguagem, não um agente autônomo.

## 3. Fluxo lógico recomendado
1. Pessoa fornece contribuição autorizada na Jornada.
2. Backend autentica, valida sessão, permissões, finalidade, tipo de material e estado da revisão.
3. Serviço de contexto persiste os fatos autorizados, produzindo versão e proveniência.
4. Guivos Intelligence solicita compreensão inicial via seus adaptadores conforme política e disponibilidade.
5. Quando necessário, Intelligence consulta Guivos AI por contrato especializado e fornece contexto mínimo autorizado, diretamente ou por identificadores acessíveis com escopo.
6. Guivos AI solicita/recebe evidências pela camada autorizada de contexto, utiliza motores apropriados e devolve resultado estruturado com incertezas, fontes, versão e perguntas.
7. Intelligence valida a vigência da resposta e apresenta ao usuário, sem converter hipóteses em certezas.
8. Correções e validações são preservadas no serviço de dados sob trilha auditável, com reavaliação controlada.

**Importante:** chamadas GPT/Claude/Gemini não precisam ser todas mediadas por Guivos AI. Guivos AI não deve se disfarçar de quarto provedor fundacional. Intelligence pode empregar modelos diretamente em tarefas de experiência e usar Guivos AI para especialização.

## 4. Diagnóstico atual do Replit (somente leitura)
Fonte: resposta do Replit Agent à pergunta de auditoria sobre a app "Jornada da Pessoa", consultada em 31/10/2026.

| Subsistema | Estado relatado |
| --- | --- |
| Interface da Jornada | Contribuições mantidas em estado React de sessão, sem persistência durável/rede no fluxo público; painel direito sem reavaliação semântica real |
| OpenAI/GPT | Transporte implementado em provedores e POC, não utilizado no fluxo público atual |
| Anthropic/Claude | Transporte implementado, sem operação cognitiva externa atual comprovada pela inspeção |
| Google/Gemini | Transporte cognitivo implementado; Gemini ASR também possui caminho técnico, mas bloqueado por gate |
| Neo4j | Testes sintéticos externos anteriores concluídos; campanha anterior relatada com 159/159 consultas e 32/32 transações, após limpeza; não vinculado às contribuições públicas |
| Orquestrador | prepareUnderstanding suporta provedores e autorizações, processamento paralelo, timeout, cancelamento e validação |
| Composição privada de testes | Fronteira de identidade → serviço de composição → memória → compreensão com fixtures, mantendo dados de teste em RAM |
| Persistência da Jornada | Não há ligação operacional e durável confirmada entre entradas reais, memória e análise |
| Graph Analytics | Sem integração operacional confirmada no fluxo |
| Áudio e anexos | Transcrição cognitiva e interpretação documental não operacionais na Jornada pública |

**Gates reportados:** cognition:false, asr:false, MEMORY_OPERATIONAL_RELEASE=false, MEMORY_SANDBOX_EXTERNAL_RELEASE=false. Gates privados de campanha não equivalem a liberação para usuários.

**Limitação:** não foram reexecutados testes nem verificados valores/validade de chaves. O agente relatou última suíte anterior com 1.040 testes/51 arquivos; isso não certifica o fluxo público.

## 5. Componentes técnicos existentes relevantes
O agente identificou transportes em módulos de provedores de Intelligence e adaptadores da POC; orquestrador prepareUnderstanding; adaptador ContextMemoryAdapter; backend de composição com fronteira de autenticação e service; armazenamento de sessões e revisões em memória de testes. Estes nomes são referências de inspeção e não contratos finais.

O catálogo atual suporta três famílias de provedores. A Guivos AI deve ter interface de capacidade própria, e não ser adicionada como falso provedor GPT/Claude/Gemini.

## 6. Fronteiras de dados a decidir
- Fonte canônica de contribuição, revisão, consentimento e evidência;
- Papel de Neo4j como grafo frente a eventual banco transacional;
- Como persistir contexto durável, recuperar versões e aplicar revogação;
- Controle de acesso e autorização entre serviços, incluindo parceiros externos;
- Quais conteúdos são enviados a provedores externos, com minimização;
- Retenção, exclusão, isolamento e auditoria;
- Contratos internos versus API comercial, custos, disponibilidade e monitoramento.

## 7. Sequência de evolução sugerida (não autorizada para implantação por este documento)
1. Inventariar os gates e sua autoridade de liberação.
2. Implantar verificador real de sessão e autorização, sob governança aprovada.
3. Conectar persistência durável da contribuição autorizada com trilha de versões.
4. Testar com fixtures a recuperação de contexto e reavaliação do painel.
5. Homologar chamadas reais a modelos em ambiente controlado e orçamento autorizado.
6. Integrar Guivos AI por contrato de capacidade especializado, mantendo componentes independentes.
7. Validar fluxos ponta a ponta e somente depois liberar gradualmente a experiência.

## 8. Critérios de aceitação
Entrada autorizada chega a armazenamento durável; contexto só é recuperado para sujeito/finalidade autorizados; correção e revogação são respeitadas; provedores não recebem dados indevidos; análises exibem evidências e limitações; respostas obsoletas não substituem estado novo; falhas não geram análises fictícias; interfaces não exibem certeza indevida.

## 9. Limites normativos
Este documento **não autoriza alteração dos gates, publicação de dados pessoais ou ativação de provedores**. A implantação no Replit dependerá de decisões de governança separadas. O GKR permanece inalterado até autorização própria.
