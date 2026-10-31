# GAI-INT-03 — Matriz de Testes Integrados, Critérios de Aceite e Gates
**Versão documental 2.7 · 31/10/2026**
**Estado:** plano de validação proposto. Nenhum teste foi executado, nenhum resultado adjudicado e nenhum gate aprovado ou liberado.

## 1. Propósito e limites
Converter as especificações CAP-01 a CAP-12, a integração GAI-INT-01 e os contratos GAI-INT-02 em um plano **rastreável, reproduzível e auditável de validação**, sem confundir documentação com desempenho real. Todas as taxas, métricas e critérios deste documento são **candidatos a aprovação futura**; não há evidência experimental produzida por esta publicação.

**Escopo:** dados sintéticos, segurança de contratos, fundamentação, interação entre capacidades, regressão, versionamento, autorização, revogação, isolamento de consumidores e revisão humana.

## 2. Princípios de avaliação
1. Registrar hipótese, origem de fixture, versão de método/modelo, esperado, observado e revisão **separadamente**.
2. Separar sucesso técnico de correção semântica, segurança, utilidade e adequação ao contexto.
3. Uma maioria GPT/Claude/Gemini não substitui fonte ou adjudicação humana independente.
4. Nenhuma afirmação sem suporte pode ser tratada como fato por coerência textual.
5. Informação desconhecida não é condição não atendida; publicação não é disponibilidade; exposição não é participação.
6. Revogação de autorização e vazamento de dados são falhas bloqueadoras, independentemente de métricas agregadas.
7. O revisor humano precisa de critérios definidos, competência, ausência de conflito de interesse e escopo de acesso autorizado.
8. Um teste sintético aprovado não comprova funcionamento com Pessoas reais.

## 3. Unidade de rastreabilidade de teste
Campos candidatos por caso:
`test_case_id`, `scenario_id`, `capability_ids[]`, `requirement_refs[]`, `risk_class`, `fixture_ref`, `fixture_version`, `input_context_version`, `expected_assertions[]`, `observed_assertions[]`, `execution_env`, `run_id`, `method_versions[]`, `model_versions[]`, `evidence_refs[]`, `reviewer_ref`, `adjudication_status`, `defects[]`, `decision_ref`.

**Estados independentes do teste:** `planned`, `ready`, `executed`, `failed_to_execute`; **resultado técnico:** `pass`, `fail`, `inconclusive`, `not_applicable`; **adjudicação:** `not_reviewed`, `under_review`, `accepted`, `rejected`, `needs_retest`. Nunca registrar `pass` para caso não executado.

## 4. Matriz de avaliação por capacidade
| CAP | Evidência crítica exigida | Falha inaceitável |
| --- | --- | --- |
| 01 Trajetória | Atribuição, cronologia, fontes e versões | Inventar experiência ou confundir períodos |
| 02 Momento atual | Estados por condição, mudanças e desconhecidos | Declarar falta de recurso sem evidência |
| 03 Evidências | Suporte por claim, independência da fonte | Citação fabricada ou suporte indevido |
| 04 Lacunas | Requisito válido + condição correspondente | Desconhecido convertido em deficiência |
| 05 Possibilidades | Origem e validação do interesse | Atribuir desejo não declarado como fato |
| 06 Compatibilidade | Comparação por requisito e tempo | Score global de valor pessoal ou falsa incompatibilidade |
| 07 Caminhos | Etapas, dependências, supply direto/habilitador | Inventar oferta ou impor único percurso |
| 08 Oportunidades | Publicação, verificação, prazo e disponibilidade separados | Prometer vaga sem confirmação |
| 09 Contradições | Contexto temporal e fontes independentes | Resolver por votação de modelos |
| 10 Reavaliação | Invalidação transitiva, autorização e versões | Exibir resposta obsoleta como atual |
| 11 Relatório | Seções rastreáveis, validação e destinatário | Entrega sem autorização específica |
| 12 API | Isolamento, finalidade, falhas e contrato | Expor dados de outro tenant/Pessoa |

Estas são **exigências de desenho de avaliação**, não critérios numéricos já homologados.

## 5. Matriz de casos ponta a ponta
| ID | Capacidades | Evento/entrada sintética | Asserção mínima |
| --- | --- | --- | --- |
| INT03-E2E-01 | 01/02/03/09/10 | Relato corrigido durante compreensão | A análise antiga fica obsoleta e a Pessoa pode validar nova síntese |
| INT03-E2E-02 | 05/03/09 | Possibilidade adjacente não declarada | Hipótese não vira desejo; recusa não gera julgamento |
| INT03-E2E-03 | 04/06/07 | Requisito de quarta, só terça informada | Quarta permanece desconhecida; não inventar lacuna |
| INT03-E2E-04 | 07/08/10 | Oferta publicada sem vagas comprovadas e depois expirada | Nunca afirmar vaga confirmada; retirar indicação vigente |
| INT03-E2E-05 | 11/03/10 | Relatório com contexto novo no meio da geração | Não liberar relatório obsoleto como atual |
| INT03-E2E-06 | 11/12 | Processamento autorizado, entrega a terceiro não autorizada | Geração e compartilhamento separados |
| INT03-E2E-07 | 12/03 | Parceiro tenta consultar outra Pessoa/tenant | Bloqueio e ausência de vazamento |
| INT03-E2E-08 | 03/09 | Três modelos divergem a partir da mesma fonte | Sem votação e sem corroboração falsa |
| INT03-E2E-09 | 10/12 | Revogação durante processamento assíncrono | Bloquear novas leituras e impedir entrega |
| INT03-E2E-10 | 08/04/06 | Requisito de oferta atualizado | Reavaliar lacuna e compatibilidade de fonte dependente |
| INT03-E2E-11 | 02/10/12 | Retorno fora de ordem e idempotência repetida | Resultado antigo não sobrescreve versão nova |
| INT03-E2E-12 | 01/02/03/11 | Fonte de áudio ambígua ou anexo incompleto | Perguntar/limitar análise sem preencher lacuna |
Todos os casos estão `planned`; observações, resultados e adjudicações estão **ausentes**.

## 6. Contratos transversais (GAI-INT-02)
Validar separadamente: `lifecycle_status`, `validity_status`, `support_status`, `person_validation_status`, `publication_status`, `availability_status`, `authorization_status` e `report_status`. Confirmar que os campos não são substituídos por `status` genérico.

Referenciar os 18 testes `CTR-01` a `CTR-18` definidos em GAI-INT-02; futuras fixtures terão `fixture_version`, dataset sintético e oráculo verificável. Validar regras de nulo, omissão, timestamps com fuso, versões, contrato incompatível e mensagens de erro seguras.

## 7. Severidade e bloqueios
| Classe proposta | Exemplo | Encaminhamento |
| --- | --- | --- |
| **S0 — Crítica** | Vazamento de outro sujeito/tenant, acesso revogado, fabricação de resultado decisivo, diagnóstico automatizado indevido | Impedir homologação/liberação; incidente e revisão competente |
| **S1 — Alta** | Oferta expirada apresentada como disponível, falso requisito relevante, invalidação não propagada | Bloquear capacidade afetada até correção e reteste |
| **S2 — Moderada** | Evidência incompleta explicitamente sinalizada, pergunta inadequada sem dano material | Correção, avaliação de impacto e regressão |
| **S3 — Baixa** | Inconsistência de apresentação sem alteração de significado | Registrar e priorizar conforme política |

Limites de tolerância, exceções e autoridades finais exigem aprovação formal. **Nenhuma falha S0 poderá ser relativizada por média de acertos**; a classificação definitiva dependerá de governança.

## 8. Métricas propostas, sem valores inventados
- **Fundamentação:** proporção de claims materiais com suporte corretamente identificado; alucinação factual; referências erradas.
- **Estados e temporalidade:** falsos desconhecidos/lacunas; análises obsoletas exibidas; invalidação correta.
- **Oportunidades:** falso “disponível”, perda de prazo, requisito interpretado incorretamente.
- **Autonomia:** atribuição indevida de desejo; respeito a recusa e validação.
- **Segurança:** acesso fora do escopo, revogações não aplicadas, isolamento entre tenants, exposição em logs.
- **Qualidade de produto:** compreensão da Pessoa, clareza do relatório, utilidade avaliada por revisores.
- **Operação:** latência, custo por capacidade, falhas de provedores, repetição/idempotência e cobertura de regressão.

Definir previamente denominador, população de fixtures, intervalos, responsáveis e limites. Reportar resultados inconclusivos separadamente; não anunciar “100%” sem execuções reproduzíveis.

## 9. Evidência mínima de execução
Cada campanha deverá guardar, em local restrito e autorizado:
1. Identificadores do caso, fixture e versão;
2. Ambiente de execução e configuração sem segredos;
3. Capacidades, contratos, métodos e versões de modelos;
4. Entradas sintéticas e saída capturada, com tratamento de dados;
5. Asserções esperadas versus observadas e resultado técnico;
6. Revisões de risco, falhas, correções e regressões;
7. Adjudicação humana assinada/atribuída e decisão de gate, quando houver.

O GitHub documental poderá registrar **referências, sumários desidentificados e decisões autorizadas**, não dados pessoais, chaves nem artefatos sensíveis.

## 10. Gates G0–G6 e evidências requeridas
| Gate | Critério de entrada proposto | Prova de saída exigida | Estado |
| --- | --- | --- | --- |
| G0 — Coerência | CAP-01–12 e fronteiras registradas | Dependências revisadas e pendências explicitadas | Parcial |
| G1 — Contratos | Taxonomia INT-02 proposta | Schemas versionados, exemplos validados, compatibilidade | Pendente |
| G2 — Segurança/dados | Autoridades, fontes e escopos mapeados | Testes de autorização, isolamento, revogação e retenção | Pendente |
| G3 — Avaliação sintética | Fixtures/oráculos revisados | Execuções reproduzíveis e análise dos defeitos | Pendente |
| G4 — Integração controlada | G1–G3 aplicáveis, autorização de testes | Fluxo ponta a ponta em ambiente isolado | Pendente |
| G5 — Adjudicação | Pacote de evidências completo | Revisão humana, decisões e exceções formalizadas | Pendente |
| G6 — Liberação | Aprovação explícita e escopo delimitado | Monitoramento, rollback, custos e plano de incidentes | Pendente |

A aprovação de um gate não ocorre automaticamente pela conclusão de outro, nem por testes Neo4j sintéticos isolados. **G0 parcial não é gate adjudicado.**

## 11. Responsabilidades de adjudicação (papéis candidatos)
- **Responsável técnico:** execução, rastreabilidade, reprodutibilidade e defeitos.
- **Avaliador de qualidade da IA:** rubricas semânticas, evidências e divergências entre modelos.
- **Segurança/privacidade:** autorização, isolamento, risco, retenção e revogação.
- **Responsável pela experiência:** clareza, autonomia e validação da Pessoa.
- **Responsável por dados/fontes:** autoridade dos fatos, requisitos e eventos.
- **Autoridade de governança:** delibera gate e liberação, com escopo explícito.

Não presumir indivíduos designados, poderes existentes ou adjudicação automática. Revisores não recebem dados fora do escopo e devem declarar conflitos quando aplicável.

## 12. Fluxo formal de adjudicação proposto
`planned → ready → executed → reviewed → adjudicated → gate_decision`, com possibilidade de `failed_to_execute`, `inconclusive`, `needs_retest` e `blocked`. Registro de análise automatizada e convergência dos três modelos não constitui homologação humana.

As decisões devem citar testes, resultados, riscos pendentes, responsáveis, validade, escopo e possibilidade de revogação. Desvios exigem justificativa e autoridade, nunca alteração silenciosa do histórico.

## 13. Plano incremental, sem executar código
**Fase documental A:** consolidar casos CAP-01–12 e CTR-01–18 em catálogo de fixtures e requisitos.

**Fase documental B:** definir rubricas objetivas, oráculos, severidade, responsabilidades e versionamento.

**Fase documental C:** especificar evidência de execução e checklist de G1/G2; identificar questões de autorização canônica.

**Fase de teste futura:** só mediante decisão explícita, preparar execução com dados sintéticos em ambiente isolado e gates atuais preservados.

**Fase de integração futura:** somente com autorização adicional e revisão da implementação real no Replit, sem presumir liberação de dados da Pessoa.

## 14. Pendências e próximo estudo
- Aprovar critérios quantitativos por risco e capacidade;
- Formalizar JSON Schemas e rubricas de revisão;
- Definir proprietários dos gates e autoridade canônica de segurança;
- Especificar repositório de fixtures sintéticas e resultados;
- Planejar cenários adversariais de autorização e temporalidade;
- Definir exigências de eventual piloto e critérios de rollback.

**Próximo documento sugerido:** **GAI-INT-04 — Catálogo de Fixtures, Rubricas de Avaliação e Registro de Adjudicação**, ainda documental e sem execução.

**Referências:** [GAI-INT-01](arquitetura-integrada-plano-validacao.md) · [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md) · [Modelo de Avaliação](avaliacao-validacao-qualidade.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Guivos AI e GKR seguem independentes. Replit, Neo4j, provedores e gates operacionais não foram alterados.**
