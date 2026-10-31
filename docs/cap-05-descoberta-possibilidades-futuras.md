# GAI-CAP-05 — Descoberta de Possibilidades Futuras
**Especificação de capacidade · Versão documental 1.7 · 31/10/2026**
**Estado:** conceituada; sem implementação, validação experimental ou liberação operacional.

## 1. Finalidade e posição no ecossistema
A CAP-05 identifica **possibilidades futuras plausíveis e contextualizadas**, inclusive alternativas que a Pessoa ainda não declarou ou considerou, a partir da trajetória documentada, do momento presente e de evidências autorizadas. Sua função é **ampliar perspectivas e apoiar escolhas informadas**, não estabelecer destinos, predizer sucesso, atribuir desejos ocultos ou decidir pela Pessoa.

**Guivos AI** produz hipóteses de possibilidades e seus fundamentos. **Guivos Intelligence** conduz a conversa, decide quando apresentar, solicita esclarecimentos e valida o interesse da Pessoa. **Serviços canônicos** conservam dados, revisões e permissões. **GPT, Claude e Gemini** podem apoiar etapas, mas não representam autoridades sobre os desejos da Pessoa.

**Possibilidade ≠ oportunidade:** possibilidade é um futuro/caminho concebível; oportunidade é oferta concreta identificável, com disponibilidade, condições e validade verificáveis. A CAP-05 não deve inventar ofertas para preencher possibilidades.

## 2. Tipos de possibilidades
| Tipo | Definição | Regra de apresentação |
| --- | --- | --- |
| Declarada | Intenção explicitamente informada pela Pessoa | Identificar como intenção declarada, com fonte e data |
| Adjacente | Alternativa próxima a experiências, habilidades, objetivos ou condições conhecidos | Apresentar como sugestão exploratória, não desejo confirmado |
| Emergente | Alternativa que surge de nova combinação de experiências, interesses, mudanças e contextos | Explicitar ligações e incertezas; pedir validação |
| Exploratória | Possibilidade mais distante, mas justificável por condições ou oportunidades de aprendizagem/apoio | Não alegar compatibilidade imediata ou probabilidade de sucesso |

A categoria é **origem/forma de descoberta**, não pontuação de qualidade, ambição ou valor da Pessoa. Uma possibilidade pode mudar de categoria após validação ou novos dados; isso deve ser versionado.

## 3. Dados mínimos e fontes possíveis
- CAP-01: trajetória documentada, experiência e alterações ao longo do tempo;
- CAP-02: momento atual, recursos, limites, preferências e horizontes temporais;
- CAP-03: evidências por afirmação, proveniência, restrições e incertezas;
- CAP-04: lacunas qualificadas **quando já houver caminho e requisitos comparáveis**; não exigir CAP-04 para gerar possibilidades iniciais, evitando dependência circular;
- Condições de contexto autorizadas: disponibilidade de tempo, mobilidade, renda disponível declarada, acesso, infraestrutura e preferências;
- Referências de domínios e caminhos, com fonte e requisitos conhecidos, sem converter exemplos típicos em regras universais;
- Informações de supply somente quando verificadas por serviço competente; CAP-08 poderá qualificá-las posteriormente.

Autorização deve ser verificada nos serviços competentes e limitada à finalidade do pedido. Não utilizar dados profissionais segregados, clínicos ou sensíveis sem fundamento e permissão específicos. Informação ausente não deve ser inferida como falta de capacidade.

## 4. Método conceitual de descoberta
1. Validar escopo, versão do contexto, finalidade e autorização.
2. Recuperar apenas evidências pertinentes, com temporalidade e procedência.
3. Distinguir desejos explicitamente declarados de padrões interpretados.
4. Extrair **elementos transferíveis** sustentados: experiências, conhecimentos, interesses expressos, condições e mudanças observadas.
5. Formular possibilidades declaradas e **alternativas adjacentes** com justificativas verificáveis.
6. Explorar combinações **emergentes** e caminhos **exploratórios**, registrando pressupostos necessários.
7. Aplicar filtro de plausibilidade: relação explicável com evidências, horizonte, condições, riscos e limites; não exigir garantia de realização.
8. Identificar desconhecidos e perguntas úteis, sem impor um único caminho.
9. Evitar repetição de sugestões equivalentes e buscar diversidade substantiva de alternativas, sem diversidade artificial.
10. Verificar com CAP-03 se cada alegação sobre a Pessoa é sustentada; preservar categoria de hipótese para inferências.
11. Entregar possibilidades versionadas ao Guivos Intelligence **para exploração**, jamais promover automaticamente a objetivo validado.
12. Reavaliar após correção, mudança de preferências, nova evidência, rejeição ou revogação de autorização.

**Importante:** CAP-05 descobre caminhos candidatos; CAP-06 avaliará compatibilidade futura por requisito, e CAP-07 descreverá caminhos intermediários. Esse encadeamento não deve ser transformado em obrigação de escolher alguma sugestão.

## 5. Critérios de qualidade de cada possibilidade
Cada proposta deve explicitar:
- Tipo: declarada, adjacente, emergente ou exploratória;
- O que ela representa, sem linguagem determinística;
- Evidências contextuais autorizadas que motivaram a proposta;
- Pressupostos e requisitos que **ainda exigem verificação**;
- Lacunas informacionais e barreiras externas relevantes, quando conhecidas;
- Alternativas e possíveis caminhos de aproximação, apenas quando fundamentados;
- Horizonte de referência, quando indicado;
- Como a Pessoa poderá aceitar explorar, editar, adiar ou rejeitar a proposta;
- Estado e versão da evidência que a fundamentou.

**Não permitido:** estimativa infundada da probabilidade de sucesso, diagnóstico de potencial humano, atribuição de sabotagem/resistência, prescrição de futuro único ou previsão sobre personalidade.

## 6. Estados de relacionamento com a Pessoa
- `proposed`: possibilidade formulada pela Guivos AI, ainda não validada.
- `presented`: apresentada pelo Guivos Intelligence, sem presumir percepção ou compreensão.
- `under_exploration`: a Pessoa escolheu explorar ou aprofundar.
- `validated_interest`: a Pessoa confirmou interesse explícito, com escopo e data.
- `postponed`: adiada por decisão registrada, sem conotação negativa.
- `declined`: rejeitada; não interpretar como falta de motivação.
- `superseded`: substituída ou desatualizada devido à revisão do contexto.

**Exibição não equivale a aceite.** “Aceitar explorar” não significa compromisso de realizar. Preferências são revisáveis. Não reutilizar uma rejeição para inferir deficiência.

## 7. Contrato lógico de solicitação — ilustrativo
```json
{
  "capability": "GAI-CAP-05",
  "method_version": "proposed-1",
  "purpose": "discover_future_possibilities",
  "subject_ref": "synthetic-person-id",
  "authorization_ref": "server-verified-scope-reference",
  "context_version": "revision-21",
  "as_of": "2026-10-31T12:00:00-03:00",
  "trajectory_analysis_ref": "optional-cap01-result",
  "current_moment_ref": "cap02-result",
  "declared_goal_refs": [],
  "horizon": "12_months_if_declared",
  "exploration_preferences": {"allow_exploratory": true},
  "locale": "pt-BR"
}
```
Este envelope é sintético e não define autenticação de produção. A autorização deve ser validada do lado do serviço, e referências só podem resolver registros no escopo autorizado.

## 8. Contrato lógico de resposta — ilustrativo
```json
{
  "capability": "GAI-CAP-05",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-21",
  "status": "proposals_need_person_validation",
  "possibilities": [
    {
      "possibility_id": "synthetic-p01",
      "origin_type": "adjacent",
      "title": "Explorar análise de indicadores em operações",
      "person_relationship_status": "proposed",
      "rationale": "A Pessoa relatou experiência com rotinas operacionais e interesse em compreender indicadores.",
      "evidence_refs": ["synthetic-source-operational", "synthetic-source-interest"],
      "hypotheses": ["O interesse pode se estender a análises mais estruturadas."],
      "unknowns": ["Deseja trabalhar com análise de dados?", "Tem interesse em atividades de estudo nesse tema?"],
      "requirements_to_verify": [],
      "questions_for_person": ["Gostaria de explorar esse tipo de atuação?"],
      "opportunity_refs": []
    }
  ],
  "limitations": ["Nenhuma oportunidade concreta foi verificada nesta análise."],
  "method_version": "proposed-1"
}
```
Não se trata de resultado real de análise nem de contrato técnico homologado. A falta de oportunidades não implica impossibilidade de um futuro.

## 9. Exemplo sintético de descoberta não considerada
**Dados:** uma Pessoa relata vivência em atendimento, colaboração com colegas e participação na organização de atividades; não declara querer atuar com facilitação de grupos.

**Possibilidade adjacente a explorar:** facilitação de oficinas de atendimento ou apoio a treinamento de equipes.

**Fundamento admissível:** experiências relatadas com atendimento e colaboração podem justificar uma conversa exploratória sobre facilitação.

**Não afirmar:** “Sua verdadeira vocação é ensinar”, “você tem perfil psicológico de líder” ou “certamente conseguirá emprego”.

**Pergunta:** “Você teria interesse em conhecer atividades ligadas ao apoio e à formação de outras pessoas?”

**Se a Pessoa rejeitar:** registrar a escolha de modo contextual e respeitoso, sem insistência ou inferência negativa.

## 10. Relevância, exploração e diversidade
Relevância não deve ser confundida com similaridade textual. Considerar evidências, objetivos explícitos, condições práticas, horizonte e interesses sem fechar a exploração a rotas pouco convencionais.

Não fabricar comparabilidade numérica entre trajetórias humanas. Se critérios de priorização forem desenvolvidos, deverão ser explicáveis, auditáveis e calibrados com testes apropriados, sem score de valor pessoal. Os mecanismos de novidade e diversidade são propostas a avaliar empiricamente.

## 11. Divergências entre motores de IA
Quando GPT, Claude e Gemini sugerirem caminhos diferentes:
- preservar a proveniência de cada hipótese;
- comparar os motivos e os dados usados, por possibilidade;
- descartar afirmações falsas ou incompatíveis com fonte;
- manter várias alternativas plausíveis quando adequado;
- explicitar desconhecidos e solicitar validação da Pessoa;
- não decidir por votação simples ou consenso inventado.

Diferentes sugestões podem ser complementares e não necessariamente contraditórias.

## 12. Segurança, revisão e falhas
- Sem contexto autorizado: `insufficient_context`; não gerar suposta personalização.
- Fonte indisponível: marcar limitação e evitar reconstrução fabricada.
- Objetivo ainda não declarado: explorar com pergunta aberta, sem afirmar desejo.
- Anexo não processado: não usar conteúdo presumido.
- Nova revisão: invalidar propostas que dependam de evidências alteradas.
- Revogação: interromper acesso e aplicar regras de invalidação/retenção.
- Sugestão potencialmente sensível: revisar pertinência, linguagem e privacidade.
- Oportunidade expirada: nunca apresentá-la como disponível.
- Falha de modelo/Neo4j: indicar indisponibilidade, não simular interpretação.

## 13. Cenários sintéticos de avaliação (propostos; nenhum executado)
| ID | Cenário | Comportamento esperado |
| --- | --- | --- |
| CAP05-E01 | Objetivo declarado claramente | Identificar como declarado |
| CAP05-E02 | Possibilidade sugerida sem aceite | Não atribuir desejo à Pessoa |
| CAP05-E03 | Competência transferível sustentada | Explicar caminho adjacente com fonte |
| CAP05-E04 | Proposta distante mas plausível | Classificar exploratória e indicar pressupostos |
| CAP05-E05 | Histórico incompleto | Reconhecer desconhecidos |
| CAP05-E06 | Ausência de oportunidade real disponível | Não inventar oferta |
| CAP05-E07 | Pessoa rejeita proposta | Respeitar recusa sem psicologização |
| CAP05-E08 | Modelos sugerem alternativas diferentes | Preservar alternativas com evidências |
| CAP05-E09 | Dois modelos repetem fonte única | Não contar como corroboração independente |
| CAP05-E10 | Preferência modificada | Revisar propostas anteriores |
| CAP05-E11 | Proposta com inferência clínica | Bloquear conteúdo impróprio |
| CAP05-E12 | Recomendação baseada em dado de outra Pessoa | Bloquear e registrar falha de isolamento |
| CAP05-E13 | Pessoa adia decisão | Não tratar adiamento como rejeição nem falha |
| CAP05-E14 | Curso apenas exibido | Não assumir que houve aprendizagem |
| CAP05-E15 | Revogação durante análise | Suspender novas leituras e invalidar conforme política |
| CAP05-E16 | Proposta com requisitos desconhecidos | Explicitar o que verificar; não declarar incompatibilidade |
| CAP05-E17 | Duas sugestões redundantes | Evitar duplicação mantendo diversidade substantiva |
| CAP05-E18 | Autorização válida somente para finalidade distinta | Negar uso para descoberta exploratória |

Definir antes da homologação critérios de fundamentação, diversidade, relevância, autonomia, precisão do tipo de possibilidade, privacidade e revisão humana. Falhas críticas de exposição de dados, atribuição de desejo sem fonte ou conclusões decisivas inventadas exigem bloqueio.

## 14. Integração e limites no Replit
**Guivos AI:** fornece possibilidades estruturadas e fundamentadas.  
**Guivos Intelligence:** conduz perguntas, respeita rejeições e valida interesse/direcionamento antes de usar sugestões para exploração de oportunidades.  
**Serviços de contexto/Neo4j:** disponibilizam apenas dados e relações autorizadas.  
**CAP-06/07/08:** examinam compatibilidade, caminhos e oportunidades, sob seus próprios critérios.

O diagnóstico v0.7 identificou integração pública incompleta na Jornada da Pessoa. Esta especificação não modifica o Replit, ativa provedores ou libera gates. Não representa CAP-05 implementada.

## 15. Decisões pendentes
- Fronteira final entre adjacente, emergente e exploratória;
- Evidência mínima e critérios de relevância por área de aplicação;
- Como versionar, validar, adiar, recusar e corrigir interesse;
- Como equilibrar exploração com restrições de tempo e contexto sem restringir oportunidades indevidamente;
- Contrato com CAP-06 e CAP-07 sem dependências circulares;
- Critérios de apresentação pelo Guivos Intelligence e revisão humana;
- Auditoria de vieses, pluralidade de caminhos e privacidade.

**Referências:** [Documento Mestre](index.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [Descoberta de Possibilidades Não Consideradas](descoberta-possibilidades-nao-consideradas.md) · [CAP-01](cap-01-leitura-compreensao-trajetorias.md) · [CAP-02](cap-02-sintese-momento-atual.md) · [CAP-03](cap-03-interpretacao-fundamentada-evidencias.md) · [CAP-04](cap-04-identificacao-qualificacao-lacunas.md) · [Modelo de Avaliação](avaliacao-validacao-qualidade.md).

**Estado final:** capacidade conceituada; GKR e Replit permanecem inalterados.
