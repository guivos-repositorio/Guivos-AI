# GAI-INT-04 — Catálogo de Fixtures, Rubricas de Avaliação e Registro de Adjudicação
**Versão documental 2.8 · 31/10/2026**
**Estado:** estrutura de avaliação proposta. Nenhum teste executado, nenhuma adjudicação realizada, nenhuma capacidade homologada e nenhum gate liberado.

## 1. Objetivo e limites
Estabelecer um **catálogo rastreável de casos e dados sintéticos**, rubricas verificáveis para avaliação semântica/técnica e um registro de revisão e adjudicação humana. Complementa [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) e os contratos de [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md). Não transforma cenários planejados em resultados, não define limiares como já aprovados e não autoriza execução na Jornada real.

**Vocabulário:** *fixture* é entrada/estado sintético e seu oráculo esperado; *run* é uma execução identificada; *avaliação* compara observado com esperado; *revisão* é parecer de profissional designado; *adjudicação* é decisão autorizada sobre evidência/teste; *gate* é decisão separada sobre maturidade. Convergência GPT/Claude/Gemini não equivale a adjudicação.

## 2. Catálogo e hierarquia
- **Suite:** grupo versionado de testes de capacidade, contrato, integração, segurança ou regressão.
- **Case:** identificador estável, requisito/riscos, dados de entrada, oráculo e criticidade.
- **Fixture:** configuração sintética versionada, sem dados reais disfarçados.
- **Run:** captura técnica imutável de execução, ambiente, versões, saída e falha.
- **Review:** rubrica aplicada a uma execução por revisor autorizado.
- **Adjudication:** decisão formal, escopo, autoridade, evidências e ressalvas.
- **GateDecision:** avaliação independente de conjunto de evidências de maturidade.

O catálogo deve referenciar **CAP01-E01 etc.** das doze especificações, **CTR-01 a CTR-18** de INT-02 e **INT03-E2E-01 a E2E-12** de INT-03 sem renumerá-los silenciosamente. A lista inicial de CAPs contém casos documentados, mas não fixtures em arquivos executáveis.

## 3. Campos obrigatórios candidatos de um caso
`case_id`, `suite_id`, `fixture_id`, `fixture_version`, `capability_ids[]`, `requirement_refs[]`, `risk_class`, `purpose`, `synthetic_data_provenance`, `preconditions[]`, `input_refs[]`, `expected_assertions[]`, `forbidden_assertions[]`, `expected_state_transitions[]`, `review_rubrics[]`, `required_roles[]`, `status`.

**Regra:** uma asserção precisa permitir observação/inspeção de uma saída específica, não apenas dizer “resposta boa”. Estados da fixture: `draft`, `under_review`, `approved_for_synthetic_test`, `deprecated`; aprovação de fixture não é aprovação da CAP.

## 4. Pacotes de fixtures propostos
| Pacote | Cobertura | Contraste obrigatório |
| --- | --- | --- |
| FX-TRAJECTORY | CAP-01/02/03 | Relato, evento observado, ausência de dado e atualização temporal |
| FX-GAPS | CAP-04/06 | Requisito atendido, não atendido, desconhecido e inválido |
| FX-FUTURES | CAP-05/07 | Possibilidades não consideradas, exploração opcional, rotas alternativas |
| FX-SUPPLY | CAP-07/08 | Oferta direta/habilitadora, publicada sem vaga confirmada, expirada |
| FX-EPISTEMIC | CAP-03/09 | Conflito real/aparente, mesmas fontes entre três modelos |
| FX-REVISION | CAP-09/10 | Correções, revogações, eventos duplicados e retornos fora de ordem |
| FX-REPORT | CAP-11 | Separação entre gerar, validar e entregar; destinatário não autorizado |
| FX-API | CAP-12 | Isolamento, finalidade, tenant, limites e falha segura |
| FX-INTEGRATION | CAP-01–12 conforme fluxo | Cenários INT03-E2E-01 a INT03-E2E-12 |

Nenhum pacote indica teste existente ou aprovado. Priorizar fixtures simples, adversariais e de fronteira temporal; evitar replicar casos com diferenças apenas cosméticas.

## 5. Fixture sintética ilustrativa
```json
{
  "case_id": "INT03-E2E-03",
  "fixture_id": "fx-gap-wednesday-001",
  "fixture_version": "candidate-1",
  "status": "draft",
  "subject_ref": "synthetic-person",
  "sources": [
    {"source_ref": "reported-availability", "statement": "Disponível na terça-feira", "epistemic_type": "attributed_report"},
    {"source_ref": "offer-requirement", "statement": "Encontro na quarta-feira", "epistemic_type": "source_record"}
  ],
  "expected_assertions": [
    {"field": "person_condition_wednesday", "equals": "unknown"},
    {"field": "gap_status", "not_equals": "confirmed_gap"}
  ],
  "forbidden_assertions": ["Pessoa indisponível na quarta", "Oferta incompatível"],
  "required_rubrics": ["R-EPI", "R-REQ", "R-AUT"],
  "execution": null,
  "adjudication": null
}
```
Esta fixture é **uma representação documental ilustrativa**, não um arquivo de testes implementado. O valor `null` em execução/adjudicação é ausência de registro, nunca resultado “pass”.

## 6. Rubricas de avaliação propostas
| Código | Dimensão | Pergunta de avaliação | Falha bloqueadora candidata |
| --- | --- | --- | --- |
| R-EPI | Evidência e epistemologia | Cada afirmação relevante preserva suporte, incerteza e proveniência? | Fato inventado ou hipótese apresentada como certeza |
| R-TIME | Temporalidade | Versões, vigência e correções estão coerentes? | Resultado vencido apresentado como vigente |
| R-REQ | Requisitos e lacunas | Requisitos válidos são diferenciados de desconhecidos? | Falsa incompatibilidade relevante |
| R-AUT | Autonomia da Pessoa | Interesse/recusa são expressos sem atribuição indevida? | Atribuição de desejo/deficiência não sustentada |
| R-SUP | Oportunidades | Publicação, verificação, vaga e categoria estão separadas? | Vaga ou oferta inventada |
| R-PRIV | Privacidade | Escopos, vínculos, autorização e isolamento são respeitados? | Exposição de dados ou uso após revogação |
| R-INT | Integração | Contratos, estados, versões e dependências preservados? | Resposta antiga promovida a atual |
| R-REPORT | Relatório | Fatos/hipóteses e autorização de entrega separados? | Compartilhamento indevido ou diagnóstico impróprio |
| R-OPS | Confiabilidade | Falha técnica, timeout e resultados parciais são honestamente reportados? | Execução inventada ou erro com vazamento |

Escala candidata por rubrica: `meets`, `partially_meets`, `does_not_meet`, `not_assessable`, `not_applicable`. **Não calcular média numérica entre dimensões para compensar falha crítica.** Definir âncoras detalhadas e limiares somente após deliberação formal.

## 7. Registro de execução proposto
Campos: `run_id`, `case_id`, `fixture_version`, `executed_at`, `environment_ref`, `commit_ref`, `api_contract_version`, `capability_versions[]`, `method_versions[]`, `model_versions[]`, `input_digest`, `output_digest`, `observed_assertions[]`, `technical_result`, `failure_refs[]`, `restricted_evidence_location`, `runner_ref`.

Resultados técnicos: `pass`, `fail`, `inconclusive`, `failed_to_execute`. O registro deve distinguir quando não houve execução. Identificadores de evidência devem resolver em armazenamento autorizado, não exigir anexar dados sensíveis ao GitHub.

## 8. Registro de revisão humana e adjudicação
**Review:** `review_id`, `run_id`, `reviewer_role`, `reviewer_ref`, `reviewed_at`, `rubric_results[]`, `rationale_summary`, `evidence_refs[]`, `limitations[]`, `conflict_of_interest_status`, `recommendation`.

**Adjudication:** `adjudication_id`, `review_refs[]`, `decision_authority_ref`, `scope`, `decision` (`accepted`, `rejected`, `needs_retest`, `blocked`), `decided_at`, `evidence_refs[]`, `dissent_refs[]`, `conditions[]`, `expiry_or_review_at`.

**GateDecision:** `gate_id`, `gate_decision_ref`, `adjudication_refs[]`, `responsible_authority_ref`, `decision` (`approved`, `not_approved`, `deferred`), `release_scope`, `recorded_at`, `conditions[]`.

**Nenhum registro real de execução, review, adjudication ou GateDecision foi criado.** Campos são modelos documentais. Não atribuir uma pessoa real como revisora ou autoridade sem designação.

## 9. Exemplo de registro ainda não executado
```json
{
  "case_id": "INT03-E2E-03",
  "fixture_id": "fx-gap-wednesday-001",
  "fixture_version": "candidate-1",
  "execution_status": "planned",
  "technical_result": null,
  "review_status": "not_reviewed",
  "adjudication_status": "not_adjudicated",
  "gate_decision": null
}
```
Nunca preencher automaticamente `pass`, `accepted` ou `approved` com base na existência da fixture ou por votação dos modelos.

## 10. Severidade, divergências e reteste
Empregar a classificação **S0/S1/S2/S3 proposta em GAI-INT-03**. Falha S0 exige bloqueio até análise pela autoridade competente; não é neutralizada por aprovação de outros testes. S1 exige correção e reteste da capacidade afetada segundo política ainda a aprovar.

Divergências entre avaliadores devem registrar justificativas e, se necessário, revisão independente. Distinguir `reviewer_disagreement` de `model_disagreement`. Uma correção cria **novo run e novas evidências**, não sobrescreve a falha histórica.

## 11. Integridade, isolamento e armazenamento
- Catálogo documental GitHub: IDs, schemas propostos, fixtures **estritamente sintéticas** aprovadas para publicação e referências desidentificadas.
- Resultados técnicos e relatórios de execução: armazenamento restrito com controles de acesso, versões e retenção a definir.
- Nunca publicar prompts contendo dados privados, chaves, dumps de Neo4j, dados de Pessoas ou observações profissionais segregadas.
- Usar hash/digest para verificar integridade quando houver implementação, sem presumir que anonimização por hash seja suficiente.
- Diferenciar dados sintéticos gerados de dados reais anonimizados: estes últimos exigem avaliação de privacidade própria.
- Proteger resultados, logs e revisões contra alterações sem histórico; registrar quem aprovou/desaprovou cada decisão.

## 12. Relação com gates e responsáveis
| Gate | Artefatos de avaliação requeridos | Situação |
| --- | --- | --- |
| G0 | Catálogo de capacidades, dependências, pendências de autoridade | Parcial |
| G1 | Contratos/schemas versionados e fixtures de contrato revisadas | Pendente |
| G2 | Política de autorização e testes de isolamento/revogação | Pendente |
| G3 | Runs sintéticos reproduzíveis com resultados e revisões | Pendente |
| G4 | Runs integrados controlados e regressões | Pendente |
| G5 | Adjudicações humanas atribuídas e resolvidas | Pendente |
| G6 | GateDecision formal, observabilidade, rollback, custo e escopo | Pendente |

Papéis candidatos: engenharia de testes; avaliador de qualidade de IA; arquitetura de dados; segurança e privacidade; experiência/UX; autoridade de governança. Pessoas responsáveis e competências formais **não foram designadas**.

## 13. Plano incremental sem execução
1. Catalogar referências CAP-01–12, CTR-01–18 e E2E-01–12, verificando unicidade.
2. Definir oráculos e dados sintéticos revisáveis para um conjunto mínimo de alto risco.
3. Aprovar rubricas, critérios de severidade e revisor independente quando aplicável.
4. Escolher armazenamento e política de evidências, retenção e acesso.
5. Formalizar schemas em ferramentas apropriadas em etapa própria.
6. Somente com autorização explícita, executar testes sintéticos em ambiente isolado.
7. Registrar runs/revisões/adjudicações em vez de inferir aprovação pela execução.
8. Planejar revisão do código existente do Replit separadamente, preservando gates.

## 14. Pendências e sequência recomendada
Decidir: orçamento e infraestrutura de execução; autoridade pelos gates; origem e aprovação de fixtures; seleção de primeiros casos; critérios por risco; independência dos revisores; evidência mínima; forma de auditabilidade de resultados.

**Próximo estudo sugerido:** **GAI-INT-05 — Autoridade de Dados, Consentimentos e Fluxos de Revogação**, detalhando a fronteira entre Guivos AI, Intelligence, serviços canônicos e parceiros antes de qualquer integração real.

**Referências:** [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md) · [Avaliação](avaliacao-validacao-qualidade.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md).

**Guivos AI, GKR, Replit, Neo4j e provedores permanecem sem alterações operacionais.**
