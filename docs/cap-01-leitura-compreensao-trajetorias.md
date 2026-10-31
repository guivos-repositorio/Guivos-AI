# GAI-CAP-01 — Leitura e Compreensão de Trajetórias
**Especificação de Capacidade · Documento v1.3 · 31/10/2026**
**Estado:** conceituada; contrato lógico proposto, não implementado/homologado.

## 1. Identidade, propósito e fronteira
**ID:** GAI-CAP-01. **Nome:** Leitura e Compreensão de Trajetórias.
**Responsável pelo método especializado:** Guivos AI.
**Consumidores previstos:** Guivos Intelligence (Jornada da Pessoa), Relatório de Trajetória e Possibilidades e API especializada autorizada.

**Objetivo:** compreender a sequência documentada de experiências, mudanças de contexto, declarações e decisões ao longo do tempo, produzindo uma **síntese temporal fundamentada** para apoiar a compreensão do presente. Não diagnosticar personalidade, causas psicológicas, intenção oculta ou previsão individual de futuro.

**Não é:** uma análise de adequação a oportunidades, pontuação de potencial, classificador de mérito, julgamento de carreira ou substituto da validação humana. Possibilidades e lacunas são atribuídas a capacidades posteriores (CAP-04, 05, 06) e não devem ser inventadas pela CAP-01.

## 2. Distinção entre trajetória real e trajetória documentada
A Guivos AI conhece apenas a **trajetória representada por informações disponíveis e autorizadas**. Ausência de registro não prova ausência de acontecimento, evolução, esforço ou decisão. A saída deve declarar cobertura temporal e lacunas informacionais. Um relato da Pessoa é um fato de declaração, não uma verificação externa automática do acontecimento relatado.

## 3. Entradas permitidas e responsabilidades
| Fonte | Informação candidata | Condição |
| --- | --- | --- |
| Jornada da Pessoa | Texto, transcrição, objetivos declarados, rotina, eventos e revisões | Identidade, finalidade e autorização válidas |
| Documentos compartilhados | Histórico profissional, formações, certificados e anexos | Extração identificada, correção possível; não presumir autenticidade |
| Serviços de oportunidades | Registro de exibição, abertura, interesse, inscrição, participação | Semântica exata dos eventos e origem verificável |
| Profissional autorizado | Observações com autor, data, escopo e versão | Segregação; não difundir automaticamente pela Jornada |
| Serviço de memória | Relações, evidências e histórico de versões autorizados | Recuperação filtrada e auditável; Neo4j não acessível diretamente ao modelo |
| Referências externas | Datas, requisitos e contexto de atividades, quando pertinentes | Fonte, validade temporal e limites explícitos |

Não coletar dados sensíveis desnecessários. Anexos e áudio exigem transcrição/extração validáveis; arquivos não processados permanecem explicitamente não interpretados. A fonte canônica dos dados não pertence à Guivos AI.

## 4. Processo analítico proposto
1. **Validar envelope:** sujeito, finalidade, escopo, autorização, versão e data de referência.
2. **Recuperar contexto mínimo:** somente fatos e documentos pertinentes ao pedido.
3. **Normalizar temporalidade:** separar `occurred_at`, `recorded_at`, intervalos válidos e datas desconhecidas.
4. **Separar tipos epistêmicos:** evento observado, relato atribuído, documento, interpretação e desconhecido.
5. **Reconstruir sequência:** ordenar acontecimentos sem transformar sequência em causalidade.
6. **Associar mudanças:** comparar versões do contexto; caracterizar mudanças observadas e possíveis, sem explicações psicológicas inventadas.
7. **Identificar contradições genuínas:** antes, verificar período, contexto, fonte e significado das afirmações.
8. **Determinar cobertura e limites:** intervalos sem dados, anexos não interpretados, evidências expiradas ou contestadas.
9. **Gerar síntese com claims:** associar cada afirmação relevante às referências que a sustentam.
10. **Produzir perguntas de validação:** somente para incertezas úteis ao propósito da análise.
11. **Versionar resultado e dependências:** permitir invalidação quando os fatos forem corrigidos ou a permissão revogada.

## 5. Contrato lógico de solicitação — proposta, não API final
```json
{
  "capability": "GAI-CAP-01",
  "capability_version": "proposed-1",
  "purpose": "understand_person_trajectory",
  "subject_ref": "pseudonymous-subject-id",
  "context_version": "context-revision-id",
  "as_of": "2026-10-31T12:00:00-03:00",
  "authorized_scope_ref": "authorization-reference",
  "source_refs": ["authorized-source-reference"],
  "time_window": {"from": null, "to": "2026-10-31"}
}
```

O envelope deve ser autenticado e autorizado por sistemas próprios. Uma referência de autorização não vale como permissão autoafirmada pelo cliente. O exemplo é sintético e não contém credenciais.

## 6. Contrato lógico de resposta — proposta
```json
{
  "capability": "GAI-CAP-01",
  "analysis_id": "synthetic-analysis-id",
  "analysis_version": "1",
  "context_version": "context-revision-id",
  "status": "needs_validation",
  "coverage": {"from": null, "to": "2026-10-31", "limits": ["incomplete_history"]},
  "timeline": [
    {"event_ref": "synthetic-event-ref", "period": "2026-09", "kind": "person_report", "source_refs": ["synthetic-source-ref"]}
  ],
  "claims": [
    {"claim_id": "synthetic-claim", "kind": "attributed_report", "statement": "A Pessoa relatou mudança de rotina.", "evidence_refs": ["synthetic-source-ref"], "uncertainties": []}
  ],
  "observed_changes": [],
  "possible_changes_to_verify": [],
  "contradictions": [],
  "unknowns": [],
  "questions_for_person": [],
  "limitations": ["No inference of causality from sequence alone"],
  "method_version": "proposed-1",
  "generated_at": "2026-10-31T12:00:00-03:00"
}
```

Não são campos definitivos de produção. O contrato deve evoluir junto à ontologia e aos mecanismos de identidade/autorização. Falha de acesso, ausência de fonte ou análise cancelada precisam resultar em estados explícitos, jamais em narrativa fabricada.

## 7. Semântica de acontecimentos e mudanças
- **Acontecimento observado:** registro comprovável no sistema (por exemplo, abertura de uma página).
- **Acontecimento relatado:** declaração atribuída à Pessoa/profissional, sem validação externa presumida.
- **Mudança observada:** diferenças entre estados/relatos datados com evidências suficientes.
- **Mudança possível:** hipótese de alteração ainda a verificar.
- **Ausência de evidência:** cobertura insuficiente, não ausência de mudança.
- **Contradição:** incompatibilidade pertinente entre afirmações sobre mesmo período, escopo e sentido; divergências em tempos distintos podem ser evolução real.

Uma experiência relatada como concluída não deve ser confundida com uma inscrição registrada ou uma oportunidade meramente exibida.

## 8. Exemplo sintético
**Setembro:** Pessoa relata ter experiência em atendimento, sem declarar interesse por novas funções.
**Outubro:** Pessoa relata que passou a estudar análise de dados.
**Registro da plataforma:** curso foi exibido e depois aberto; participação não foi confirmada.

**Síntese admitida:** “A Pessoa relatou experiência em atendimento e, posteriormente, iniciou estudos em análise de dados segundo seu próprio relato. Há registro de abertura de uma oferta relacionada.”

**Desconhecido:** se concluiu estudos, se participou do curso exibido, quando começou efetivamente e como avalia seu próprio interesse.

**Não afirmar:** “A Pessoa abandonou atendimento porque descobriu sua verdadeira vocação” ou “recusou oportunidades”. Isso exigiria evidências não presentes.

**Pergunta proposta:** “Você gostaria de esclarecer quando começou a estudar análise de dados e se houve alguma experiência prática desde então?”

## 9. Tratamento de erros e reavaliação
- Correção de data/fonte: atualizar versão canônica, identificar claims dependentes e marcar análise anterior como obsoleta.
- Revogação de acesso: bloquear novas leituras e aplicar política de invalidação/retenção correspondente.
- Fonte inacessível: devolver cobertura incompleta, não reconstruir conteúdo sem evidência.
- Falha do Neo4j ou de modelo: declarar indisponibilidade/degradação, sem simular síntese.
- Nova contribuição durante execução: evitar substituir contexto recente por resultado de versão antiga.
- Divergência GPT/Claude/Gemini: comparar por claim e fonte, sem votação simples ou consenso fabricado.

## 10. Matriz de avaliação inicial (fixtures propostas)
| Caso | Situação | Esperado |
| --- | --- | --- |
| CAP01-E01 | Dados em ordem cronológica fora de sequência | Reordenação por acontecimento, preservando data do registro |
| CAP01-E02 | Relato sem data | Data desconhecida visível, sem inventar período |
| CAP01-E03 | Mesma informação em dois resumos derivados | Não contar como duas fontes independentes |
| CAP01-E04 | Declarações divergentes em meses diferentes | Tratar mudança temporal antes de apontar contradição |
| CAP01-E05 | Informação corrigida na Jornada | Resposta antiga obsoleta; nova análise usa versão corrigida |
| CAP01-E06 | Clique sem participação | Não declarar participação ou conclusão |
| CAP01-E07 | Profissional com escopo restrito | Bloquear compartilhamento fora da autorização |
| CAP01-E08 | Documento não extraído | Declarar anexo não interpretado |
| CAP01-E09 | Ausência de eventos em período longo | Não concluir inatividade pessoal |
| CAP01-E10 | Revogação durante execução | Interromper acesso e aplicar invalidação conforme política |
| CAP01-E11 | Contexto alterado durante processamento | Descartar ou sinalizar resposta anterior como obsoleta |
| CAP01-E12 | Duas interpretações de modelos conflitantes | Preservar controvérsia e evidências, solicitar revisão |

**Condições de aprovação a definir:** limites mensuráveis de fidelidade factual, erro temporal, citações inadequadas, privacidade, regressões, cobertura e revisão humana. Falhas críticas de acesso indevido, história fabricada e afirmação sem suporte relevante impedem homologação.

## 11. Integração com Guivos Intelligence e Replit
**Responsabilidade Guivos AI:** realizar a análise especializada e devolver síntese temporal estruturada e rastreável.
**Responsabilidade Guivos Intelligence:** conduzir perguntas, orquestrar execução, verificar contexto/autorização e apresentar resultado validável à Pessoa.
**Serviços de contexto:** manter dados originais, versões e direitos de acesso.

O diagnóstico de 31/10/2026 apontou que a Jornada pública no Replit ainda não encaminha automaticamente entradas reais a uma cadeia durável de contexto + modelos + painel, apesar de componentes privados e testes sintéticos. **Este documento não altera o Replit, não ativa provedores, não libera gates e não representa implementação da CAP-01.**

## 12. Critérios para avanço e decisões pendentes
Antes de prototipar:
1. Estabelecer fonte canônica por modalidade de contribuição.
2. Definir contrato de autorização, identidade e minimização.
3. Especificar como eventos, evidências e revisões serão acessados.
4. Fixar versão do contrato e rubricas de avaliação.
5. Aprovar escopo da prova sintética e autoridade dos gates.
6. Definir estados de erro e invalidação end-to-end.

**Dependências:** GAI-DEP-01/02/03/06/07/08; CAP-03 evidências, CAP-09 contradições e CAP-10 reavaliação são capacidades transversais.

**Documentos relacionados:** [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [Ontologia Temporal](modelo-conhecimento-ontologia-temporal.md) · [Evidências](modelo-evidencias-rastreabilidade.md) · [Avaliação](avaliacao-validacao-qualidade.md) · [Documento Mestre](index.md).

**GKR e Replit permanecem inalterados nesta etapa documental.**
