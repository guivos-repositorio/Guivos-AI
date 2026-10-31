# GAI-CAP-03 — Interpretação Fundamentada em Evidências
**Especificação de capacidade · Versão documental 1.5 · 31/10/2026**
**Estado:** capacidade conceituada, sem implementação, execução de testes, homologação ou liberação operacional.

## 1. Propósito, papel e limites
A CAP-03 atua transversalmente às capacidades Guivos AI para produzir e verificar **afirmações analíticas individualmente rastreáveis**. Cada afirmação deve distinguir dados observados, relatos atribuídos, inferências, hipóteses e informações desconhecidas; associar evidências autorizadas; explicitar a justificativa inteligível e reconhecer limites.

A CAP-03 **não** decide pela Pessoa, diagnostica condições psicológicas ou clínicas, transforma eventos de navegação em intenções nem presume que a concordância GPT/Claude/Gemini representa verdade.

**Autoridades:** fontes e permissões pertencem aos serviços canônicos do ecossistema. Guivos AI é responsável pelo método especializado de interpretação e por sua rastreabilidade. Guivos Intelligence orquestra consumo, apresentação e validação com a Pessoa. Revisão profissional não substitui consentimento nem autoriza inferências clínicas automatizadas.

## 2. Unidade fundamental — afirmação sustentada
Uma análise ou relatório pode conter múltiplas afirmações. **Cada afirmação relevante exige suporte verificável**, e a evidência deve ser pertinente ao significado exato da afirmação, não apenas ao tema geral.

Campos lógicos candidatos:
- `claim_id`, `analysis_id`, `claim_type`, `statement`;
- `subject_ref`, `purpose`, `authorized_scope_ref`;
- `evidence_refs` e `source_versions`;
- `support_assessment`: sustentada, parcialmente sustentada, não sustentada, contraditória ou não avaliável;
- `justification_summary`: explicação acessível de como o suporte se relaciona à afirmação, sem expor pensamento interno privado de modelos;
- `uncertainties`, `unknowns`, `counterevidence_refs`;
- `as_of`, `source_validity`, `claim_status`, `method_version`.

**Regra de integridade:** quando não houver suporte suficiente, rebaixar a afirmação a hipótese ou desconhecido, pedir evidências adicionais ou omiti-la; nunca adicionar citação decorativa para conferir aparência de comprovação.

## 3. Classes de informação e escopo de inferência
| Origem | Afirmação permitida | Conclusão não permitida sem evidência adicional |
| --- | --- | --- |
| Declaração da Pessoa | A Pessoa relatou determinada situação em data específica | O relato foi externamente verificado |
| Documento anexado | O documento contém determinada informação, caso extração confiável | A informação é autêntica ou atual apenas por estar no arquivo |
| Registro profissional autorizado | O profissional registrou observação identificada | Diagnóstico confirmado pela IA ou compartilhamento irrestrito |
| Evento da plataforma | Ocorreu evento tecnicamente observável | A Pessoa percebeu, compreendeu ou recusou conscientemente |
| Registro de inscrição | Houve inscrição registrada | Participação efetiva, aprendizagem ou evolução |
| Requisito publicado | A fonte indicou condição ou prazo em data verificada | Regra universal ou permanente |
| Síntese anterior de IA | Um método produziu interpretação com fontes | Evidência independente da fonte original |

**Independência de fontes:** dois modelos ou dois resumos oriundos da mesma informação não equivalem a duas confirmações independentes.

## 4. Estados epistêmicos e do processo
**Tipo epistêmico:** observação registrada, relato atribuído, interpretação fundamentada, hipótese exploratória, desconhecido.

**Suporte:** sustentado, parcialmente sustentado, contraditório, sem suporte, não avaliável.

**Ciclo do claim:** proposto → examinado → elegível para apresentação → validado/contestado → vigente, obsoleto ou substituído. A validação pela Pessoa confirma a sua percepção ou relato pertinente, mas não comprova automaticamente todos os fatos externos.

**Não colapsar estados:** uma hipótese plausível não se torna fato por ter sido apresentada em relatório. Um claim sustentado em 2026 pode ser obsoleto para descrever o contexto atual futuro.

## 5. Pipeline lógico proposto
1. Receber finalidade, versão de contexto, escopo e conjunto de afirmações candidatas.
2. Validar identidade, finalidade e permissão no serviço apropriado.
3. Recuperar somente as evidências pertinentes e suas versões, com controle de acesso.
4. Classificar origem e independência das fontes; reconhecer transformações de voz/anexos.
5. Verificar correspondência semântica: o que a evidência afirma e o que **não** permite afirmar.
6. Verificar tempo de ocorrência, registro, validade e eventuais revisões.
7. Procurar contraindícios, contradições e explicações alternativas, quando cabíveis.
8. Classificar suporte e incerteza por claim, sem inventar números de confiança.
9. Produzir justificativa concisa, fontes, limites e perguntas necessárias.
10. Entregar resultado tipado para Guivos AI/Intelligence e registrar dependências de invalidação.
11. Reavaliar após correção, revogação, nova evidência ou expiração.

## 6. Contrato lógico de entrada (exemplo sintético, não API implementada)
```json
{
  "capability": "GAI-CAP-03",
  "method_version": "proposed-1",
  "purpose": "validate_analytical_claims",
  "subject_ref": "synthetic-subject",
  "authorization_ref": "authorization-scope-reference",
  "context_version": "revision-7",
  "as_of": "2026-10-31T12:00:00-03:00",
  "candidate_claims": [
    {"claim_id": "c-1", "claim_type": "inference", "statement": "A Pessoa participou do curso.", "evidence_refs": ["event-opening"]}
  ]
}
```

## 7. Contrato lógico de saída (exemplo sintético)
```json
{
  "capability": "GAI-CAP-03",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-7",
  "status": "completed_with_insufficient_support",
  "claims": [
    {
      "claim_id": "c-1",
      "support_assessment": "unsupported",
      "eligible_for_presentation": false,
      "evidence_refs": ["event-opening"],
      "justification_summary": "A abertura de uma oferta não comprova participação.",
      "unknowns": ["Não há evidência de participação."],
      "recommended_action": "request_confirmation_or_remove_claim"
    }
  ],
  "method_version": "proposed-1",
  "limitations": ["Avaliação restrita a fontes autorizadas."],
  "generated_at": "2026-10-31T12:00:00-03:00"
}
```
**Nota:** o exemplo rejeita uma conclusão incompatível com a evidência. Não representa execução real dos modelos. Identificadores são sintéticos, sem dados pessoais.

## 8. Integração com as demais capacidades
- **CAP-01 (Trajetória):** verifica se cada acontecimento e mudança está atribuído a fontes e períodos adequados.
- **CAP-02 (Momento Atual):** examina atualidade, origem, escopo e desconhecidos de cada condição presente.
- **CAP-04 (Lacunas):** exige suporte independente para requisitos e condições não atendidas; desconhecido não vira deficiência.
- **CAP-05 (Possibilidades):** classifica propostas exploratórias como hipóteses, não desejos próprios da Pessoa.
- **CAP-06 (Compatibilidade):** avalia afirmações por requisito, sem score global de valor pessoal.
- **CAP-07/08 (Caminhos/Oportunidades):** confirma fontes, prazos e limites de disponibilidade.
- **CAP-09 (Contradições):** encaminha divergências qualificadas, em vez de conciliá-las artificialmente.
- **CAP-10 (Reavaliação):** rastreia dependências dos claims para invalidação e nova análise.
- **CAP-11/12 (Relatório/API):** entregam conclusões com suporte, limites, versionamento e controle de escopo.

## 9. Divergências entre GPT, Claude e Gemini
Comparar cada **afirmação e sua evidência**, não apenas a resposta completa do modelo. Separar:
- mesma conclusão derivada da mesma fonte;
- conclusões semanticamente equivalentes com limites distintos;
- interpretações diferentes mas defensáveis;
- contradição factual refutável por evidência;
- discordância inconclusiva que demanda pergunta ou revisão.

Sem evidência resolutiva, preservar alternativas e incertezas. Nenhum consenso automático por maioria ou pontuação subjetiva não validada.

## 10. Contradições, correções e temporalidade
Comparar fontes relativas ao **mesmo período, finalidade e conceito**. Mudança de rotina entre setembro e outubro pode ser evolução e não contradição. Correções de registros invalidam claims afetados; relatórios anteriores devem ser marcados históricos ou obsoletos conforme política.

Revogação de acesso bloqueia novas consultas e desencadeia tratamento apropriado de análises/cache, respeitando regras de retenção. A CAP-03 não substitui o serviço de autorização.

## 11. Segurança e falhas
- Fonte ausente: não apresentar claim como sustentado.
- Fonte fora do escopo: não acessar, citar ou revelar.
- Fonte expirada: sinalizar obsolescência e solicitar reconfirmação.
- Documento/transcrição não interpretado: declarar limite.
- Neo4j ou provedor indisponível: retorno de erro/resultado incompleto, jamais síntese fabricada.
- Mudança de versão durante processamento: resultado anterior não pode sobrescrever análise atual.
- Dados clínicos sensíveis: não produzir diagnóstico automatizado e exigir controles adicionais.
- Fonte comum a modelos: não apresentar como corroboração independente.

## 12. Casos sintéticos para avaliação (não executados)
| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| CAP03-E01 | Clique citado como participação | Suporte rejeitado |
| CAP03-E02 | Documento antigo como condição presente | Aviso de desatualização |
| CAP03-E03 | Dois resumos do mesmo registro | Dependência comum identificada |
| CAP03-E04 | Afirmação sem evidência | Desconhecida/não sustentada |
| CAP03-E05 | Relato da Pessoa apresentado como fato externo | Atribuição corrigida |
| CAP03-E06 | Duas evidências contraditórias no mesmo período | Contradição sinalizada |
| CAP03-E07 | Registros em períodos diferentes | Sem falso conflito |
| CAP03-E08 | Data original corrigida | Claim anterior invalidado |
| CAP03-E09 | Revogação de autorização | Bloqueio e tratamento conforme política |
| CAP03-E10 | Modelos concordam com premissa falsa | Não aceitar votação como verdade |
| CAP03-E11 | Requisito de oferta expirado | Não tratar como vigente |
| CAP03-E12 | Informação profissional segregada | Não expor fora do escopo |
| CAP03-E13 | Evidência apoia apenas parte do claim | Suporte parcial, limites explícitos |
| CAP03-E14 | Transcrição ambígua | Pedir confirmação, não inventar conteúdo |
| CAP03-E15 | Nova versão de contexto chega durante execução | Resultado anterior obsoleto |
| CAP03-E16 | Ausência de registro de inscrição | Não concluir recusa consciente |

**Critérios para homologação:** a definir com protocolo de avaliação v1.1, métricas de suporte factual, erro de citação, integridade de fontes, isolamento de dados, temporalidade, segurança e revisão humana. Falhas críticas de privacidade ou afirmações materiais fabricadas impedem liberação.

## 13. Critério de maturidade e decisões pendentes
Esta especificação não estabelece um motor em execução. Para avançar: confirmar taxonomia de claims e suportes, schema contratual, fonte canônica, política de validade de evidências, rubricas de revisores, mecanismos de contestação e autoridade dos gates.

A CAP-03 poderá ser usada como função transversal por outras capacidades, mas seu contrato e sua operação precisarão de versionamento e avaliação independentes.

**Documentos relacionados:** [Modelo de Evidências](modelo-evidencias-rastreabilidade.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-01](cap-01-leitura-compreensao-trajetorias.md) · [CAP-02](cap-02-sintese-momento-atual.md) · [Modelo de Avaliação](avaliacao-validacao-qualidade.md) · [Documento Mestre](index.md).

**GKR e Replit não são alterados nesta etapa documental.**
