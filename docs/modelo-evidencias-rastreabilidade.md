# Modelo de Evidências, Rastreabilidade e Revisão Analítica — Guivos AI
**Documento Mestre complementar · Versão documental 1.0 · 31/10/2026**
**Estado:** proposta de método e contrato conceitual; não implementado nem homologado.

## 1. Propósito
Tornar cada interpretação relevante da Guivos AI **inspecionável, contestável, atualizável e proporcional às evidências disponíveis**, sem confundir plausibilidade com comprovação.

A autoridade da Guivos AI deve decorrer de métodos auditáveis e resultados avaliados, não da declaração de que é uma IA especialista.

**Invariante:** nenhuma afirmação analítica relevante sem origem identificável, interpretação explicitada e limitação conhecida. Quando a fonte não permite sustentar uma conclusão, o sistema deve declarar o que não sabe.

## 2. Unidade mínima de análise: afirmação + suporte
A rastreabilidade deve ocorrer por **afirmação individual**, e não apenas por relatório inteiro. Cada afirmação contém:
- `claim_id`, `analysis_id`, `claim_text`, `claim_type`;
- `subject_ref`, `purpose`, `authorized_scope`;
- `evidence_refs`, `source_versions` e referências de requisitos externos;
- `reasoning_summary`: justificativa curta compreensível, sem expor raciocínio interno privado de modelos;
- `uncertainties`, `known_limitations`, `missing_information`;
- `observed_at`, `analyzed_at`, `valid_until` (quando aplicável);
- `status`: proposta, validada, contestada, obsoleta, substituída ou rejeitada;
- `method_version`, `model_execution_refs` para auditoria técnica quando permitida.

Nenhum identificador pessoal real deve ser publicado neste repositório. Contratos concretos de API e banco ainda dependem de análise de segurança.

## 3. Tipos de informação
| Classe | Pode sustentar | Não comprova |
| --- | --- | --- |
| Declaração da Pessoa | Que a Pessoa relatou algo naquele momento | Que o fato relatado foi externamente verificado |
| Registro de profissional | Que o profissional registrou observação sob sua responsabilidade | Diagnóstico ou causa automaticamente confirmados pela Guivos AI |
| Evento técnico | Exibição, abertura, clique ou inscrição registrados | Atenção consciente, entendimento, motivação ou participação não registrada |
| Registro de participação | Participação segundo fonte específica | Aprendizagem, benefício ou mudança pessoal sem evidências adicionais |
| Documento externo | Requisito, prazo ou condição segundo emissor e data | Validade permanente ou universal |
| Inferência de modelo | Uma hipótese fundamentada | Um fato independente ou causalidade demonstrada |

**Regra de fontes múltiplas:** repetição da mesma origem não equivale a corroboração independente. Duas sínteses geradas por modelos a partir do mesmo registro não são duas evidências independentes.

## 4. Matriz de estados epistêmicos
- **Fato de registro confirmado:** aconteceu no sistema e há evidência rastreável do evento.
- **Relato atribuído:** declaração identificada e versionada; conteúdo pode não ser externamente verificado.
- **Inferência sustentada:** interpretação apoiada por evidências, com limites expressos.
- **Hipótese exploratória:** alternativa plausível ainda não testada.
- **Informação desconhecida:** não há dados suficientes para afirmar ou negar.
- **Evidência contraditória:** fontes divergem ou registram contextos/tempos diferentes.
- **Evidência obsoleta:** fonte expirou, foi corrigida ou perdeu relevância temporal.
- **Conclusão refutada:** informações posteriores não sustentam a hipótese anterior.

Os estados não são pontuações de confiabilidade da Pessoa. Qualquer escore técnico futuro deverá ser calibrado em testes específicos e explicado.

## 5. Proveniência e cadeia de evidências
Fluxo conceitual:
**Fonte autorizada → Registro e versão → Extração/normalização identificada → Evidência vinculada → Análise/hipótese → Afirmação com referências → Relatório ou API → Revisão/correção.**

Registrar autoria, tipo de fonte, timestamp do acontecimento e do registro, versão, escopo de acesso, validade e transformação feita. Extrair de texto, voz ou documento não significa verificar a veracidade; transcrições e extrações podem conter erros e devem ser corrigíveis.

## 6. Tratamento de contradições
1. **Detectar** divergências apenas quando afirmações se referem à mesma condição, período e escopo.
2. **Distinguir** mudança legítima ao longo do tempo de conflito real.
3. **Atribuir** versões e fontes a ambos os registros.
4. **Suspender** conclusões dependentes da informação contestada quando necessário.
5. **Perguntar** à Pessoa/profissional autorizado sem induzir uma resposta.
6. **Reavaliar** após esclarecimento, preservando a trilha de revisão permitida.

**Exemplo:** relato anterior de disponibilidade às terças e relato posterior de disponibilidade às quartas não são necessariamente contraditórios; podem expressar mudança de rotina.

## 7. Lacunas e oportunidades: exigência de evidência
Para afirmar **lacuna confirmada**, exigir simultaneamente:
- possibilidade/caminho identificados e pertinentes;
- requisito verificável e atual;
- condição contextual relevante comprovadamente não atendida;
- evidência vigente e escopo de utilização legítimo.

Se faltar qualquer desses pontos, utilizar *possível lacuna* ou *informação desconhecida*. Não interpretar oportunidade exibida como oportunidade conscientemente ignorada, nem ausência de ação observável como autossabotagem.

Para afirmar **oportunidade real e disponível**, verificar emissor, prazo, requisitos, acesso e data da verificação. Distinguir oferta do ecossistema de categoria de oferta ainda a buscar.

## 8. Interpretações retrospectivas, contextuais e prospectivas
**Retrospectiva:** afirmações sobre registros passados precisam de evidências temporalmente consistentes.

**Contextual:** afirmações de estado atual exigem atualidade e contexto suficiente; declarações antigas devem ser tratadas como históricas até confirmação.

**Prospectiva:** possibilidades e caminhos são hipóteses condicionais; não são previsões pessoais de sucesso/fracasso. Explicitar requisitos, incertezas, alternativas e escolha humana.

## 9. Correções, revogação e invalidação
Eventos que podem tornar uma análise obsoleta: correção de declaração, nova evidência, prazo vencido, revogação de acesso, alteração de objetivo, mudança em requisito externo ou constatação de erro de extração.

Processo proposto:
1. Sistema canônico recebe evento de alteração ou revogação;
2. Serviço de memória atualiza projeções autorizadas;
3. Serviço Guivos AI identifica afirmações dependentes;
4. Resultado é marcado obsoleto/contestado, com propagação à Guivos Intelligence e parceiros quando aplicável;
5. Reanálise ocorre somente sob autorização e finalidade legítimas;
6. Relatórios não continuam se apresentando como atuais quando dependem de evidência invalida.

Revogação de acesso e eliminação completa obedecem requisitos jurídicos e políticas de retenção distintas.

## 10. Modelo de apresentação em relatório
Para cada achado importante:
- **Afirmação:** texto simples, sem causa inferida indevidamente.
- **Tipo:** observado, relatado, interpretação ou hipótese.
- **Evidências:** registros que a sustentam e contexto das fontes.
- **O que ainda não sabemos:** lacunas informacionais, possíveis fontes de erro.
- **Alternativas plausíveis:** diferentes explicações quando cabíveis.
- **Perguntas de validação:** para Pessoa ou profissional habilitado.
- **Atualidade:** quando foi produzido e se permanece válido.
- **Revisão:** confirmação, contestação ou correção, conforme competência e autorização.

## 11. Exemplo sintético
**Registros:** a Pessoa afirma querer aprimorar competências digitais. Uma formação foi exibida em 5/10 e houve abertura de detalhes em 6/10. Não há inscrição registrada. O profissional relata dificuldades de agenda, com autorização.

**Afirmação admitida:** “Há registro de abertura dos detalhes da formação, mas não de inscrição na Guivos até a data analisada.”

**Hipótese a investigar:** “A dificuldade de agenda relatada pode ter influenciado a decisão; ainda não existe evidência causal.”

**Não afirmar:** “A Pessoa ignorou a formação por autossabotagem”.

**Pergunta:** “O horário, o conteúdo ou outra circunstância influenciou sua decisão de não se inscrever?”

## 12. Avaliação e testes
Conjunto de casos sintéticos cobrindo: documentos contraditórios, datas divergentes, ofertas expiradas, fonte duplicada, eventos de clique sem participação, mudança de preferência, transcrição incorreta, evidência inacessível, revogação e tentativa de cruzamento entre Pessoas distintas.

Métricas sugeridas:
- Percentual de afirmações relevantes com referência de suporte válida;
- Taxa de citação de fonte que não sustenta a afirmação;
- Taxa de falsas lacunas por informação ausente;
- Detecção correta de obsolescência e contradição temporal;
- Calibração de incerteza, medida com conjunto de validação adequado;
- Latência de invalidação e taxa de vazamento entre escopos;
- Utilidade da explicação, revisada por Pessoas e especialistas.

Nenhum limite numérico de aprovação foi definido; requisitos de qualidade dependem de experimentos e governança.

## 13. Divisão de responsabilidades
- **Fontes canônicas do ecossistema:** registros originais, versões, permissões e evidências de sistema.
- **Serviço de memória/Neo4j:** relações e proveniência acessíveis sob escopo autorizado.
- **Guivos AI:** classificação das afirmações, análise, justificativas, incertezas, dependências e status dos resultados.
- **Guivos Intelligence:** orquestra chamada, apresenta resultado corretamente e não exibe análise obsoleta como vigente.
- **Profissional/Pessoa:** validações dentro de suas competências e direitos.
- **GPT, Claude, Gemini:** executores de tarefas específicas, não autoridades finais sobre fatos.

## 14. Decisões e limites
O princípio de **evidências, hipóteses e limitações** já integra a direção aprovada da Guivos AI. As estruturas e contratos deste documento são hipóteses técnicas para validação. Não representam autorização para alterar Replit, liberar gates, modificar Neo4j operacional ou tratar dados clínicos.

## 15. Próximos estudos
- Contrato formal de claims/evidence e estratégia de armazenamento;
- Mapeamento da ontologia v0.9 para esquema de grafo;
- Políticas de invalidação propagadas e eventos;
- Avaliação independente das explicações;
- Governança de dados e permissões no produto B2B.

**Referências internas:** [Documento Mestre](index.md) · [Modelo de Conhecimento](modelo-conhecimento-ontologia-temporal.md) · [Autoridade de Dados](autoridade-dados-memoria-contexto.md) · [Governança](governanca.md).

**Separação:** documento pertencente exclusivamente ao repositório Guivos-AI; GKR e Replit permanecem inalterados nesta etapa.
