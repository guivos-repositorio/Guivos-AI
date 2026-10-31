# GAI-CAP-07 — Identificação de Caminhos Intermediários
**Especificação de capacidade · Versão documental 1.9 · 31/10/2026**
**Estado:** conceituada. Especificação metodológica e contratos lógicos propostos; não implementada, testada ou homologada.

## 1. Propósito
Identificar **caminhos de aproximação** entre o momento da Pessoa e uma possibilidade futura explorada, representando etapas opcionais, condições habilitadoras, alternativas, dependências e incertezas. A capacidade responde: **quais percursos plausíveis poderiam tornar uma possibilidade mais acessível e sob quais condições?**

O caminho é um **mapa exploratório**, não plano obrigatório, previsão de sucesso ou prescrição de comportamento. A Pessoa pode escolher outro caminho, adiar ou interromper a exploração sem receber classificação negativa.

**Guivos AI:** formula e analisa caminhos fundamentados. **Guivos Intelligence:** orquestra apresentação, perguntas, comparação e validação de escolhas. **Serviços do ecossistema:** fornecem contexto canônico, requisitos e oportunidades verificadas. **GPT/Claude/Gemini:** executores técnicos, não autoridades sobre fatos. **Neo4j:** infraestrutura candidata a representar relações e proveniência sob acesso autorizado.

## 2. Definições
- **Possibilidade de destino:** futuro concebível proveniente da CAP-05 ou declarado pela Pessoa; exploração não equivale a desejo confirmado.
- **Caminho intermediário:** sequência ou rede de etapas candidatas entre condições atuais e possibilidade, com dependências e alternativas.
- **Etapa:** condição, atividade ou experiência de aproximação, descrita sem pressupor disponibilidade comercial.
- **Condição habilitadora:** recurso ou suporte que possibilita executar etapa (ex.: transporte, internet, acessibilidade, cuidado infantil).
- **Oportunidade concreta:** oferta com emissor, requisitos, período e disponibilidade verificáveis pela CAP-08/serviço de ofertas.
- **Categoria de oportunidade:** modalidade abstrata que poderia ajudar, mas **não** representa oferta disponível.
- **Dependência:** etapa que precisa preceder outra apenas quando essa sequência é demonstrável; não inventar necessidade.
- **Cenário alternativo:** percurso distinto com pressupostos próprios e sem ranking universal.
- **Ponto de decisão:** momento em que a Pessoa pode confirmar, modificar, adiar, descartar ou solicitar outra rota.

## 3. Relação com as capacidades anteriores e posteriores
| Capacidade | Contribuição |
| --- | --- |
| CAP-01 | Evidências de experiências e mudanças históricas |
| CAP-02 | Condições presentes: rotina, tempo, recursos, preferências, mobilidade |
| CAP-03 | Verificação de afirmações, proveniência e limitações |
| CAP-04 | Estados de requisitos e lacunas específicas, sem confundir desconhecido com ausência |
| CAP-05 | Possibilidades declaradas, adjacentes, emergentes ou exploratórias |
| CAP-06 | Compatibilidade condicional por requisito e horizonte |
| CAP-08 | Verificação posterior de oportunidades específicas, prazo e requisitos |
| CAP-09 / CAP-10 | Contradições, mudanças, correções e invalidação |
| CAP-11 / CAP-12 | Exposição em relatório e API, somente em escopo autorizado |

A CAP-07 pode propor uma **categoria** antes de CAP-08 encontrar oferta real. Não deverá depender de CAP-08 para formular caminhos conceituais nem substituir a verificação de ofertas por especulação.

## 4. Estrutura do caminho
Cada caminho deverá identificar:
- Possibilidade explorada e estado de validação do interesse;
- Horizonte temporal declarado (ou indefinido);
- Pressupostos, condições de entrada e requisitos pertinentes;
- Etapas candidatas e suas relações de precedência **somente quando justificadas**;
- Percursos alternativos e pontos de decisão;
- Esforço, tempo, custos, mobilidade e acessibilidade **apenas quando sustentados**;
- Condições habilitadoras, inclusive externas à formação e emprego;
- Evidências, fontes, lacunas, desconhecidos e limitações;
- Oportunidades concretas verificadas, quando existentes, separadas de categorias abstratas;
- Versão, data de referência e dependências para revisão.

Não transformar rede de possibilidades em um funil linear rígido. Alguns passos podem ocorrer simultaneamente, ser opcionais ou tornar-se irrelevantes.

## 5. Tipos de etapas candidatas
**Exploração:** conversa, observação de campo, evento informativo, orientação, aproximação comunitária.

**Preparação:** formação, prática supervisionada, desenvolvimento de competências ou documentação necessária.

**Experimentação:** projeto pequeno, vivência, voluntariado, participação temporária, experiência prática.

**Acesso:** inscrição, candidatura, participação em processo seletivo ou etapa formal de elegibilidade.

**Habilitação externa:** acesso digital, transporte, equipamento, apoio de cuidado, recursos de acessibilidade, infraestrutura e mobilidade.

**Revisão e escolha:** avaliação de interesse, pertinência e consequências antes de seguir.

Nenhum tipo precisa estar presente em todos os caminhos; o sistema deve justificar por que determinada etapa é pertinente.

## 6. Método de construção de caminhos
1. **Validar** identidade, finalidade, escopo, autorização, versão de contexto e possibilidade a explorar.
2. **Recuperar** evidências pertinentes das CAP-01/02/03 e estado da possibilidade CAP-05.
3. **Examinar** requisitos e condições qualificados pelas CAP-04/06, distinguindo desconhecidos de lacunas confirmadas.
4. **Gerar** múltiplas rotas candidatas quando houver alternativas substantivas; permitir uma única rota fundamentada quando não houver dados para outras.
5. **Representar** pré-requisitos, paralelismos e etapas opcionais como relações justificadas.
6. **Verificar** barreiras e condições habilitadoras por rota, incluindo supply direto e habilitador.
7. **Avaliar** viabilidade condicional sem prometer conclusão, contratação ou evolução.
8. **Distinguir** etapas conceituais de oportunidades reais verificadas; chamar CAP-08 somente quando houver oferta concreta a qualificar.
9. **Aplicar** CAP-03 a alegações relevantes, registrar hipóteses e ignorância explícita.
10. **Formular** perguntas neutras e pontos de escolha, preservando autonomia da Pessoa.
11. **Entregar** caminhos versionados ao Guivos Intelligence, com suporte e limites.
12. **Reavaliar** após novos fatos, correção, revogação, expiração de oferta ou mudança de interesse.

## 7. Organização de Direct e Enabling Supply
| Classe | Exemplos | Uso correto |
| --- | --- | --- |
| **Direct Supply** | Curso, mentoria, vaga, atividade cultural, evento, voluntariado, atividade física, comunidade de prática | Pode ser etapa de aproximação quando pertinente; oferta real só com verificação |
| **Enabling Supply** | Transporte, internet, equipamento, acessibilidade, cuidado infantil, documentação, mobilidade, infraestrutura | Pode tornar possível executar uma etapa direta; não é falha inerente da Pessoa |

Não presumir que a oferta indicada pela Guivos existe ou está disponível. Disponibilidade, prazo, requisitos e legitimidade devem ser sustentados por fonte competente.

## 8. Exemplo sintético com dois percursos
**Situação:** Pessoa relata experiência em atendimento, interesse em explorar análise de dados e dispõe de tempo restrito. Não há informação confirmada sobre equipamento próprio.

**Possibilidade explorada:** conhecer atividades de análise de indicadores operacionais.

**Caminho A — Experimentação inicial:** esclarecer disponibilidade → buscar atividade introdutória compatível → experimentar análise de pequeno conjunto de dados → avaliar se deseja aprofundar.

**Caminho B — Orientação e apoio:** conversar com profissional autorizado → compreender atividades reais da área → verificar acesso a equipamento/conectividade → explorar projeto assistido.

**Condição habilitadora potencial:** acesso a computador, **caso necessário e ainda não disponível**. Sem evidência de ausência de equipamento, não há lacuna confirmada.

**Não afirmar:** “A Pessoa precisa comprar um computador”, “um curso garante emprego” ou “Caminho A é necessariamente superior”.

**Nenhuma oferta concreta foi verificada neste exemplo.** Os percursos são ilustrativos, não recomendações personalizadas reais.

## 9. Contrato lógico de solicitação (sintético; não implementado)
```json
{
  "capability": "GAI-CAP-07",
  "method_version": "proposed-1",
  "purpose": "explore_intermediate_paths",
  "subject_ref": "synthetic-person",
  "authorization_ref": "verified-server-scope",
  "context_version": "revision-41",
  "possibility_ref": "synthetic-possibility",
  "possibility_status": "under_exploration",
  "compatibility_analysis_ref": "optional-cap06-analysis",
  "horizon": {"months": 12, "origin": "person_reported"},
  "as_of": "2026-10-31T12:00:00-03:00"
}
```
Referências de autorização jamais substituem autenticação e verificação server-side. Horizonte de doze meses é exemplo, não padrão atribuído automaticamente.

## 10. Contrato lógico de resposta (sintético; não implementado)
```json
{
  "capability": "GAI-CAP-07",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-41",
  "status": "paths_require_person_validation",
  "possibility_ref": "synthetic-possibility",
  "paths": [
    {
      "path_id": "path-A",
      "state": "proposed",
      "title": "Exploração prática inicial",
      "assumptions": ["Interesse em experimentar análise de indicadores"],
      "steps": [
        {"step_id": "A1", "type": "clarification", "title": "Confirmar tempo disponível", "depends_on": [], "evidence_refs": []},
        {"step_id": "A2", "type": "exploration", "title": "Explorar atividade introdutória", "depends_on": ["A1"], "evidence_refs": []}
      ],
      "enabling_conditions_to_verify": ["Disponibilidade de dispositivo"],
      "verified_opportunity_refs": [],
      "unknowns": ["Acesso a equipamento"],
      "limitations": ["Não há oferta concreta validada nesta análise."]
    }
  ],
  "questions_for_person": ["Qual percurso você gostaria de explorar, se algum?"],
  "method_version": "proposed-1"
}
```
Dependências de etapas são hipóteses e deverão ser revisadas. Etapas não devem usar `verified_opportunity_refs` para itens meramente conceituais.

## 11. Autonomia e linguagem de apresentação
- “Um caminho possível seria...” em vez de “Você deve...”.
- “Caso haja acesso a...” em vez de pressupor o recurso.
- “Poderá ser necessário verificar...” em vez de afirmar uma falta não comprovada.
- “Quer explorar essa alternativa?” em vez de declarar intenção.
- Rejeição, adiamento ou mudança de rota devem ser respeitados.
- Não produzir ranking de valor pessoal, métricas de destino, promessa de mobilidade social ou causalidade inventada.

## 12. Revisões, custos e resiliência
- **Mudança do Momento:** reavaliar etapas dependentes; não manter restrições antigas automaticamente.
- **Requisito externo expirado:** suspender etapa dependente até nova validação.
- **Revogação de autorização:** bloquear novas consultas e acionar invalidação/retenção aplicável.
- **Oferta indisponível:** remover condição de oferta ativa; preservar categoria de passo quando útil.
- **Falha Neo4j/modelo:** devolver estado incompleto ou indisponível; nunca inventar trajetória ou disponibilidade.
- **Custos e duração desconhecidos:** marcá-los como desconhecidos; nunca fabricar estimativas.
- **Divergência GPT/Claude/Gemini:** comparar fundamentos de rotas sem votação automática.
- **Relatórios a terceiros:** não compartilhar históricos, dados sensíveis ou opiniões profissionais além da autorização aplicável.

## 13. Avaliação sintética inicial (não executada)
| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| CAP07-E01 | Possibilidade sem interesse confirmado | Caminho apenas exploratório |
| CAP07-E02 | Etapa com pré-requisito comprovado | Dependência justificada |
| CAP07-E03 | Etapas independentes | Não impor sequência artificial |
| CAP07-E04 | Rotas alternativas válidas | Preservar mais de uma opção |
| CAP07-E05 | Recurso não informado | Desconhecido, não ausência |
| CAP07-E06 | Barreira externa e apoio habilitador | Considerar Enabling Supply |
| CAP07-E07 | Curso inexistente sugerido por modelo | Não apresentar como oferta real |
| CAP07-E08 | Oferta real expirada | Não manter como disponível |
| CAP07-E09 | Pessoa recusa um caminho | Registrar escolha sem interpretação negativa |
| CAP07-E10 | Custo ou tempo desconhecido | Não inventar valores |
| CAP07-E11 | Correção de rotina | Invalidar etapas afetadas |
| CAP07-E12 | Acesso profissional fora de escopo | Bloquear compartilhamento |
| CAP07-E13 | Dois modelos sugerem percursos distintos | Comparar evidências sem votar |
| CAP07-E14 | Caminho traz diagnóstico psicológico | Rejeitar inferência imprópria |
| CAP07-E15 | Lacuna informacional tratada como confirmada | Corrigir para desconhecido |
| CAP07-E16 | Revogação durante geração | Impedir novas leituras e seguir regras de invalidação |
| CAP07-E17 | Oferta foi exibida, sem participação | Não inferir experiência |
| CAP07-E18 | Mudança do objetivo da Pessoa | Reavaliar pertinência do caminho |
| CAP07-E19 | Sugestões redundantes apenas com nomes diferentes | Consolidar sem mascarar alternativas reais |
| CAP07-E20 | Caminho válido mas sem oferta disponível | Preservar plano exploratório, sem fabricar match |

**Critérios de aprovação pendentes:** fundamentação, diversidade substantiva, consistência temporal, autonomia, integridade de dependências, precisão de custos/prazos, isolamento e revisão humana. Falhas críticas de privacidade ou oferta fabricada impedem homologação.

## 14. Fronteira com o Replit e critérios para avanço
O diagnóstico da Jornada v0.7 identifica componentes isolados de memória e provedores, mas não um fluxo público completo homologado. Esta especificação não altera gates, prompts, adaptadores, Neo4j nem código do Replit.

Antes de prototipar CAP-07: confirmar contratos CAP-04/05/06, política de autorização, modelo de caminhos como grafo temporal, origem de ofertas, fixture set e autoridade para transições de maturidade.

## 15. Pendências arquiteturais
- Modelo de grafo para rotas, etapas e dependências opcionais/conjuntas;
- Regras de precedência, simultaneidade e comparação de percursos;
- Representação de custos e duração com incertezas;
- Como uma Pessoa valida/edita somente parte do caminho;
- Critérios para acionamento da CAP-08;
- Política de invalidação entre CAP-07, relatório e API;
- Proteções para recomendações de maior impacto.

**Referências:** [Documento Mestre](index.md) · [Matriz](matriz-capacidades-guivos-ai.md) · [CAP-04](cap-04-identificacao-qualificacao-lacunas.md) · [CAP-05](cap-05-descoberta-possibilidades-futuras.md) · [CAP-06](cap-06-inteligencia-compatibilidade-futura.md) · [Avaliação](avaliacao-validacao-qualidade.md) · [Ontologia](modelo-conhecimento-ontologia-temporal.md).

**Guivos AI e GKR permanecem independentes. Nenhuma implementação foi autorizada por este documento.**
