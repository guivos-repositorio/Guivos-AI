# GAI-CAP-02 — Síntese do Momento Atual
**Especificação de capacidade · Versão documental 1.4 · 31/10/2026**
**Estado:** conceituada; método e contratos lógicos propostos, sem protótipo homologado ou operação autorizada.

## 1. Propósito e limites
A CAP-02 transforma o **contexto presente autorizado** em uma síntese fundamentada das condições em que a Pessoa se encontra **na data de referência**. Seu objetivo é apoiar compreensão e perguntas úteis antes de qualquer direcionamento, não definir identidade, potencial, mérito ou futuro obrigatório.

Distinguir:
- **CAP-01:** reconstrói o que está documentado sobre a trajetória e suas mudanças ao longo do tempo.
- **CAP-02:** organiza o momento atual, com atualização, fontes, condições, preferências, incertezas e necessidades de esclarecimento.
- **CAP-04/05/06:** examinam lacunas, possibilidades futuras e compatibilidade; CAP-02 não deve antecipar conclusões dessas capacidades sem fundamentos e autorização.

A Pessoa não é reduzida a um único perfil fixo. Pode vivenciar vários momentos simultâneos e contextos distintos conforme trabalho, formação, convivência, cuidados, disponibilidade e interesses.

## 2. Dimensões do contexto atual
| Dimensão | Conteúdo elegível | Cuidado obrigatório |
| --- | --- | --- |
| Situação declarada | Como a Pessoa descreve seu presente | Não converter relato em fato externamente confirmado |
| Rotina | Atividades, frequência, turnos e compromissos | Horários não fornecidos permanecem desconhecidos |
| Tempo disponível | Janelas, frequência, disponibilidade sazonal | Não confundir tempo livre com disposição ou obrigação |
| Recursos | Recursos informados como disponíveis para iniciativas | Não inferir renda, classe social ou orçamento por padrões |
| Mobilidade | Localidade, deslocamentos aceitos, formatos remoto/presencial | Não presumir acesso a transporte, passaporte ou infraestrutura |
| Acessibilidade | Necessidades declaradas e adaptações relevantes | Evitar inferência médica e exposição não necessária |
| Preferências | Interesses, formatos, atividades e restrições expressas | Não transformar sugestão da IA em preferência da Pessoa |
| Objetivos | Intenções explicitamente validadas | Podem ser exploratórios, suspensos ou modificados |
| Horizontes | Curto prazo e horizonte indicado (incluindo 12 meses quando informado) | Não inventar prazos ou urgências |
| Condições habilitadoras | Equipamentos, conectividade, documentação, redes, apoios | Distinguir ausência comprovada de informação ausente |
| Interações com oportunidades | Eventos observáveis com semântica precisa | Exibir não equivale a perceber; abrir não equivale a participar |
| Informações profissionais | Registros pertinentes e autorizados | Segregação e finalidade; não propagar automaticamente |

Não impor a coleta integral de todas as dimensões. Solicitar apenas informações necessárias, com finalidade legítima, evitando dados sensíveis não essenciais.

## 3. Estados de cada informação do momento
- **Informada:** declaração atribuída e datada, ainda que não verificada externamente.
- **Observada:** evento do sistema com significado limitado ao que foi registrado.
- **Confirmada para a finalidade:** fonte e validação adequadas ao contexto específico.
- **Desconhecida:** nenhuma evidência suficiente para afirmar ou negar.
- **Possivelmente desatualizada:** registro existe, mas perdeu atualidade ou não há reconfirmação apropriada.
- **Contestada/divergente:** fontes incompatíveis sobre o mesmo período e escopo, pendentes de esclarecimento.
- **Não aplicável:** dimensão não pertinente ao objetivo de análise.

Esses estados caracterizam **informações**, não a Pessoa. Uma ausência de dado não deve gerar nota negativa ou lacuna confirmada.

## 4. Contrato de fontes e autoridade
Fonte canônica: serviços de contexto, identidade e oportunidades do ecossistema. A Guivos AI não substitui o registro original; acessa evidências pertinentes somente pelo serviço autorizado. Neo4j pode apoiar relações e proveniência, sem conceder acesso direto irrestrito aos modelos externos.

Entradas candidatas: declarações de texto, transcrições corrigíveis, documentos devidamente processados, revisões, eventos, CAP-01 quando válida e informações profissionais segregadas.

Para cada informação: identificador de origem, versão, data do acontecimento, data do registro, data/intervalo de validade quando disponível, autoria, tipo epistêmico, autorização, restrições e estado de revisão.

Informações extraídas de áudio/anexos não processados devem ser declaradas como **não interpretadas**. A origem comum de múltiplas sínteses não configura evidência independente.

## 5. Sequência analítica proposta
1. Verificar identidade e autorização do pedido, finalidade, fonte e versão do contexto.
2. Recuperar os registros estritamente necessários, sem copiar o histórico completo por padrão.
3. Classificar dimensões e tipos de fonte, preservando autoria.
4. Avaliar atualidade de cada informação relativa à data da análise.
5. Integrar mudanças verificadas pela CAP-01 sem assumir que todo registro antigo continua vigente.
6. Organizar simultaneidades: a Pessoa pode possuir condições e desejos diferentes em áreas distintas.
7. Detectar desconhecidos, ambiguidades e conflitos temporais legítimos.
8. Construir síntese com afirmações rastreáveis, limites e cobertura.
9. Priorizar **perguntas contextuais não indutivas** que esclareçam o momento e o objetivo; não perguntar prematuramente qual recurso a Pessoa quer comprar/consumir.
10. Retornar versão de contexto, timestamp, evidências e recomendações de aprofundamento ao Guivos Intelligence.
11. Se a Pessoa corrigir o relato, invalidar a síntese derivada conforme política e reavaliar somente sob autorização válida.

## 6. Relação com o ciclo de Guivos Intelligence
O ciclo de experiência permanece sob Guivos Intelligence:
**Compreender → Identificar lacunas informacionais → Perguntar → Aprofundar → Reavaliar → Validar → Direcionar**.

A CAP-02 produz a **síntese contextual especializada**, suas fontes, desconhecidos e perguntas candidatas; Intelligence coordena o diálogo e solicita à Pessoa validação da compreensão antes do direcionamento.

**Nota:** lacuna informacional (falta dado necessário à compreensão) é diferente da lacuna de compatibilidade futura, que exige requisito verificado e condição atual não atendida.

## 7. Contrato lógico de solicitação (ilustrativo)
```json
{
  "capability": "GAI-CAP-02",
  "capability_version": "proposed-1",
  "purpose": "current_moment_understanding",
  "subject_ref": "synthetic-person-id",
  "authorization_ref": "scope-reference",
  "context_version": "revision-42",
  "as_of": "2026-10-31T12:00:00-03:00",
  "relevant_source_refs": ["source-1", "source-2"],
  "trajectory_analysis_ref": "optional-cap01-analysis",
  "requested_dimensions": ["routine", "availability", "preferences", "goals"],
  "locale": "pt-BR"
}
```
A autorização deve ser verificada em servidor por contexto, destinatário, finalidade e validade. IDs de exemplo não são credenciais.

## 8. Contrato lógico de resposta (ilustrativo)
```json
{
  "capability": "GAI-CAP-02",
  "analysis_id": "synthetic-analysis-02",
  "context_version": "revision-42",
  "status": "needs_person_validation",
  "as_of": "2026-10-31T12:00:00-03:00",
  "summary": "A Pessoa relata disponibilidade parcial e interesse em formação.",
  "dimensions": [
    {
      "dimension": "availability",
      "state": "reported",
      "value_summary": "Terças-feiras à tarde, conforme relato",
      "source_refs": ["source-1"],
      "validity": "not_independently_verified"
    }
  ],
  "confirmed_for_purpose": [],
  "unknowns": ["Disponibilidade em outros dias"],
  "potentially_outdated": [],
  "contradictions": [],
  "informational_gaps": ["Preferência por formação remota ou presencial"],
  "questions_for_person": [
    "Você também tem disponibilidade em outros dias?",
    "Você prefere atividades remotas, presenciais ou ambas?"
  ],
  "limitations": ["Síntese limitada às informações autorizadas"],
  "method_version": "proposed-1",
  "source_versions": ["source-1:v2"]
}
```
Campos, tipos e status são propostas para discussão, não contrato implementado. Um valor descrito como `reported` nunca deve aparecer como `verified` sem confirmação apropriada.

## 9. Exemplo sintético de mudança
**Relato em setembro:** “Tenho tempo livre aos sábados.”  
**Relato em outubro:** “Passei a trabalhar aos sábados e disponho de parte das noites de terça.”

**Conclusão permitida:** “Segundo relato mais recente, a rotina mudou; atualmente a Pessoa informa disponibilidade parcial nas noites de terça.”

**Informação a esclarecer:** disponibilidade em outros períodos e se a mudança é temporária.

**Conclusão proibida:** “A Pessoa perdeu interesse em estudar” ou “não tem disciplina”, pois o relato não sustenta essas interpretações.

**Pergunta apropriada:** “Essa nova rotina deve continuar nos próximos meses?”

## 10. Falhas e mecanismos de proteção
- **Contexto ausente:** retornar `insufficient_context`; não produzir narrativa genérica disfarçada de compreensão.
- **Acesso negado/revogado:** retornar erro autorizado sem revelar conteúdo.
- **Neo4j indisponível:** usar apenas fontes alternativas autorizadas se o contrato permitir; marcar cobertura incompleta.
- **Anexo/áudio não interpretado:** declarar limitação da modalidade.
- **Resultados de modelos divergentes:** comparar por afirmação e fonte; não votar por maioria.
- **Versão desatualizada:** Intelligence deve descartar ou sinalizar análise obsoleta.
- **Dados sensíveis:** minimizar, segregar e não inferir condição clínica.
- **Objetivo não declarado:** não inventar intenção; perguntar de modo aberto quando pertinente.

## 11. Conjunto inicial de testes sintéticos (proposta)
| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| CAP02-E01 | Rotina relatada sem data | Informar temporalidade desconhecida |
| CAP02-E02 | Relato antigo substituído por novo | Síntese atual utiliza versão recente |
| CAP02-E03 | Disponibilidade em apenas um dia | Não inferir indisponibilidade nos demais |
| CAP02-E04 | Renda não informada | Não presumir recursos ou falta deles |
| CAP02-E05 | Objetivo sugerido pela IA sem aceite | Não classificar como desejo declarado |
| CAP02-E06 | Pessoa declara preferir não decidir agora | Registrar escolha sem pressão |
| CAP02-E07 | Profissional possui informação restrita | Não exibir fora de finalidade/escopo |
| CAP02-E08 | Áudio sem transcrição | Declarar conteúdo não interpretado |
| CAP02-E09 | Ofertas exibidas sem interação | Não inferir interesse ou rejeição |
| CAP02-E10 | Dados simultâneos de várias áreas da vida | Não reduzir a um único momento rígido |
| CAP02-E11 | Correção feita durante o processamento | Resultado da versão anterior fica obsoleto |
| CAP02-E12 | Conflito real entre duas fontes contemporâneas | Indicar divergência e perguntar |
| CAP02-E13 | Autorização revogada no decorrer da análise | Interromper acesso e invalidar conforme política |
| CAP02-E14 | Requisitos externos não disponíveis | Não fabricar lacunas de compatibilidade |

Não há fixture executada ou limite de aceitação homologado. A revisão humana deverá verificar fidelidade, neutralidade, privacidade, atualidade e utilidade.

## 12. Critérios para progresso de maturidade
**Conceituada → protótipo:** confirmar autoridades por fonte, contrato de acesso e conjunto de avaliação com dados sintéticos.
**Protótipo → avaliação:** executar fixtures e registrar falhas e correções.
**Avaliação → homologada:** aprovar critérios quantitativos e humanos definidos pela governança competente.
**Homologada → operação:** autorização independente de integração e liberação, observabilidade, rollback e requisitos de privacidade.

## 13. Dependências e perguntas pendentes
Dependências: CAP-01 para contextualização temporal quando pertinente; CAP-03 evidências; CAP-09 incerteza e contradição; CAP-10 revisão; GAI-DEP-01 a 03, 05 a 08 conforme a matriz.

Questões pendentes:
- Quais dimensões são indispensáveis à síntese mínima por caso de uso?
- Qual a validade padrão de uma declaração de rotina ou disponibilidade?
- Como expressar múltiplos Momentos simultâneos no modelo de dados?
- Qual sinal do Guivos Intelligence confirma a compreensão da Pessoa?
- Quais fatos autorizados poderão ser reutilizados na API comercial sem exposição indevida?

## 14. Relações e limites
[Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-01](cap-01-leitura-compreensao-trajetorias.md) · [Ontologia Temporal](modelo-conhecimento-ontologia-temporal.md) · [Evidências e Rastreabilidade](modelo-evidencias-rastreabilidade.md) · [Documento Mestre](index.md).

**Este documento não altera o Replit, Neo4j, provedores externos ou GKR.**
