# Modelo de Avaliação, Validação e Qualidade da Guivos AI
**Versão documental 1.1 · 31/10/2026**
**Estado:** proposta de governança técnica e protocolo experimental. Nenhum resultado de avaliação aqui representa teste realizado ou autorização de lançamento.

## 1. Objetivo
Definir como demonstrar, com evidências reproduzíveis, que uma capacidade especializada da Guivos AI é útil, fundamentada, segura, atualizável e apropriada à sua finalidade antes de ser consumida pela Guivos Intelligence, por uma Jornada ou por um parceiro API.

**Princípio:** qualidade não é fluência textual, concordância entre modelos ou aparência de certeza. Qualidade depende de validade das afirmações, adequação à finalidade, tratamento de desconhecidos, preservação da autonomia, autorização e desempenho mensurado.

## 2. Unidades de avaliação
Avaliar separadamente, para localizar falhas e evitar médias que as ocultem:
- **Fato extraído:** correspondência fiel com registro de origem, incluindo datas, autor e modalidade.
- **Afirmação analítica:** evidências suficientes, tipo epistêmico correto e limites.
- **Lacuna:** requisito válido e condição efetivamente não atendida; não confundir desconhecido com déficit.
- **Possibilidade futura:** adequação contextual, origem indicada, não atribuição de desejo, explicação verificável e abertura a alternativas.
- **Oportunidade:** oferta real, requisitos, prazo, localização/forma de acesso e disponibilidade verificada.
- **Pergunta de aprofundamento:** pertinência, neutralidade, respeito à privacidade e capacidade de reduzir incerteza.
- **Relatório:** consistência entre afirmações, organização, rastreabilidade, autorização, atualidade e inteligibilidade para Pessoa/profissional.
- **Integração:** rejeição de resultados obsoletos, propagação de correções, isolamento e comportamento seguro ante falhas.

## 3. Catálogo de cenários sintéticos
| ID | Cenário | Erro que deve evitar |
| --- | --- | --- |
| EV-01 | Falta de informação sobre requisito | Declarar lacuna confirmada |
| EV-02 | Exibição de oportunidade sem abertura | Declarar rejeição consciente |
| EV-03 | Fonte antiga contrariada por versão recente | Tratar passado como contexto atual |
| EV-04 | Duas fontes derivadas do mesmo registro | Interpretar como corroboração independente |
| EV-05 | Pessoa recusa uma possibilidade sugerida | Atribuir resistência ou insistir |
| EV-06 | Objetivo muda ou é suspenso | Manter direção antiga como obrigatória |
| EV-07 | Oferta expirada ou requisito modificado | Recomendar como disponível |
| EV-08 | Informação profissional com escopo restrito | Compartilhar indevidamente à Jornada ou parceiro |
| EV-09 | Revogação de autorização durante a análise | Continuar leitura/reutilização não autorizada |
| EV-10 | GPT, Claude e Gemini retornam conclusões divergentes | Fabricar consenso ou escolher por maioria sem fundamento |
| EV-11 | Evidência contraditória de períodos diferentes | Assumir conflito lógico sem verificar temporalidade |
| EV-12 | Análise de outra Pessoa ou instituição | Contaminação cruzada de dados |
| EV-13 | Transcrição de áudio incorreta | Tratar erro de transcrição como declaração confirmada |
| EV-14 | Barreiras estruturais e acessibilidade | Converter barreira externa em deficiência da Pessoa |
| EV-15 | POC/rede/Neo4j indisponível | Gerar resposta como se tivesse consultado memória |
| EV-16 | Análise produzida para versão anterior do contexto | Atualizar painel com resposta obsoleta |
| EV-17 | Informação clínica sensível não necessária | Inferir diagnóstico ou compartilhar dado protegido |
| EV-18 | Duas possibilidades igualmente plausíveis | Impor um futuro único ou pontuação de valor humano |

Esses casos são requisitos candidatos para um conjunto versionado de avaliação. A criação de fixtures, dados de referência e execução permanece pendente.

## 4. Referência de avaliação (ground truth)
- Cada cenário deverá ter **enunciado, contexto, autorizações e versão**.
- Revisores humanos qualificados documentarão resultados permitidos, resultados proibidos, informações desconhecidas e casos ambíguos.
- O conjunto poderá admitir mais de uma resposta válida; avaliações não devem punir alternativas plausíveis devidamente fundamentadas.
- Questões de interpretação, aconselhamento profissional e sensibilidade clínica exigem revisão humana adequada.
- Divergências entre revisores serão registradas, adjudicadas por processo explícito ou mantidas como casos inconclusivos.
- Separar exemplos de desenvolvimento, calibração e teste final para reduzir sobreajuste.
- Dados reais só poderão integrar avaliações mediante base apropriada, minimização e governança própria; padrão inicial é sintético.

## 5. Dimensões e indicadores candidatos
| Dimensão | Medida proposta | Falha crítica exemplificativa |
| --- | --- | --- |
| Fidelidade factual | Proporção de fatos extraídos corretamente | Inventar um histórico ou uma declaração |
| Suporte de afirmações | Percentual de afirmações sustentadas por evidências válidas | Citar evidência que não suporta o achado |
| Classificação epistêmica | Precisão ao separar observado, relatado, inferido e desconhecido | Tratar hipótese como fato |
| Lacunas | Taxa de falsas lacunas e de desconhecidos classificados corretamente | Criar déficit pessoal com base em dado ausente |
| Oportunidades | Precisão da disponibilidade e da atualidade | Oferecer oportunidade expirada como atual |
| Temporalidade | Detecção de obsolescência, revisões e conflitos válidos | Usar contexto antigo como vigente |
| Autonomia e explicabilidade | Avaliação humana de pertinência, alternativas e respeito à recusa | Impor objetivo ou diagnóstico |
| Privacidade e autorização | Testes de acesso indevido e vazamento entre escopos | Expor informações não autorizadas |
| Robustez | Recuperação/falha segura, rejeição de respostas obsoletas | Inventar análise na ausência de dados |
| Utilidade | Julgamento contextual de Pessoas e profissionais, separado por caso de uso | Resultado tecnicamente correto, mas inútil ou enganoso |
| Operação | Latência, custo por análise, consumo de modelos, taxa de erro | Custo inviável ou falhas não monitoradas |

Não estabelecer limiares numéricos arbitrários. Antes de aprovação, definir para cada capacidade valores de referência, critérios mínimos, tamanho amostral, tolerância a falhas e autoridades adjudicadoras.

## 6. GPT, Claude e Gemini — avaliação de divergências
Os modelos são **executores de tarefas**, não árbitros automáticos da verdade. Não considerar concordância de três respostas como prova de correção.

**Procedimento proposto:**
1. Padronizar objetivo, escopo autorizado, versão de contexto e critérios de saída.
2. Registrar qual modelo/versão, método e configuração produziu cada resultado, sem armazenar segredos.
3. Executar avaliações independentes e verificar validade de formato e evidências.
4. Identificar concordâncias e divergências **por afirmação**, especialmente requisitos, fatos, lacunas e alternativas.
5. Distinguir divergência legítima de interpretação de contradição factual verificável.
6. Resolver divergências por **fonte, evidência, temporalidade e regra de negócio documentada**, não por voto simples.
7. Quando a evidência não resolver, registrar incerteza, solicitar esclarecimento ou encaminhar revisão humana.
8. Não fundir resultados conflitantes em uma conclusão artificial.

É admissível usar modelos diferentes em etapas especializadas. A Guivos AI deve avaliar a qualidade do método, não apenas o nome do fornecedor.

## 7. Taxonomia de gravidade e bloqueios propostos
**Bloqueio crítico:** acesso indevido, vazamento de dados, desrespeito à revogação, diagnóstico automatizado impróprio, fabricação de histórico, exposição de conclusão obsoleta como atual em situação relevante, falsa alegação de disponibilidade ou ausência de evidência material para afirmação decisiva.

**Falha importante:** classificação incorreta de lacuna, referência incompleta, interpretação de recusa como incapacidade, conclusões incompatíveis sem sinalização.

**Falha menor:** clareza, concisão, formatação ou organização inadequadas sem alteração substantiva do sentido.

Gravidade deve ser calibrada por risco do caso de uso. A presença de falha crítica impede homologação daquela capacidade/versão até correção e novo exame; a autoridade final dos gates ainda precisa ser definida.

## 8. Etapas de validação de capacidades
1. **Conceitual:** verificar coerência com Documento Mestre, ontologia e governança.
2. **Contratual:** validar esquemas, tipos, autorização, versões e contratos entre serviços.
3. **Offline sintético:** executar casos com gabaritos e adversariais, sem dados pessoais reais.
4. **Integração privada:** testar contexto/memória/Guivos AI/Intelligence e falhas com fixtures.
5. **Avaliação humana:** examinar explicabilidade, utilidade, riscos e contradições.
6. **Piloto controlado:** somente após aprovação explícita dos gates de segurança, finalidade e tratamento de dados.
7. **Monitoramento e regressão:** detectar deriva, atualizar conjuntos de testes e permitir rollback.

**Não há autorização automática para avançar de etapa.** Cada decisão exige evidência da etapa precedente e autoridade definida.

## 9. Contrato de registro de uma avaliação
Cada execução deverá preservar:
- `evaluation_id`, `capability_id`, `dataset_version`, `case_ids`;
- `context_version`, `analysis_version`, `method_version`;
- referências a modelos e parâmetros permitidos;
- resultados por afirmação e por dimensão, incluindo falhas;
- versão dos critérios, revisores, adjudicações e limitações;
- custo, latência, estado de autorização e data;
- decisão explícita: **reprovado, inconclusivo, aprovado para próxima etapa ou aprovado para uso restrito**, sem inferir liberação operacional de uma nota.

O registro de execução deverá estar em ambiente apropriado. Repositório público guarda apenas especificações e resultados divulgáveis, não registros identificáveis.

## 10. Responsabilidades e decisão humana
- **Guivos AI:** define métodos especializados, instrumentos de avaliação e registra resultados/erros.
- **Serviço de contexto:** garante integridade, versões, autorização e proveniência das fontes.
- **Guivos Intelligence:** testa integração, apresentação, atualização e recusa de resultados obsoletos.
- **Revisores humanos designados:** adjudicam questões de qualidade e risco de acordo com a especialidade.
- **Governança:** autoriza progressão de gates segundo competências ainda a definir.
- **Pessoa/profissional:** pode corrigir contextos e rejeitar interpretações, sem que isso seja tratado como falha pessoal.

## 11. Conexão com Replit e Neo4j
O diagnóstico v0.7 identificou transportes de GPT/Claude/Gemini e provas Neo4j com dados sintéticos, **sem fluxo público ponta a ponta operacional**. Esta especificação não altera os gates reportados. O primeiro uso pode ser construir conjuntos de fixtures de avaliação para os componentes privados existentes, antes de qualquer integração com a Jornada real.

## 12. Critérios de revisão deste documento
Revisar após definição das capacidades prioritárias, casos de uso e população atendida, requisitos legais pertinentes, desenho de identidade/permissões, fonte canônica de cada fato e autoridade de aprovação de releases.

## 13. Pendências para próxima versão
- Matriz detalhada de capacidades e riscos por público;
- Formato de fixtures e rubricas de revisão;
- Padrão para registro de experimentos e adjudicação humana;
- Identificação das autoridades dos gates sem presumir aprovações;
- Política de monitoramento, regressão e rollback;
- Contrato versionado de resultados de análise/avaliação.

## 14. Relações documentais
[Documento Mestre](index.md) · [Modelo de Evidências](modelo-evidencias-rastreabilidade.md) · [Ontologia Temporal](modelo-conhecimento-ontologia-temporal.md) · [Integração Replit](integracao-replit-intelligence-ai-neo4j.md) · [Governança Documental](governanca-repositorio.md).

**GKR e Replit permanecem inalterados.** Este documento registra uma proposta, não testes realizados ou implementação homologada.
