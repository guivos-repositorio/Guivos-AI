# GAI-INT-17 — Modelo de Rastreabilidade, Auditoria e Proveniência de Evidências de Gate
**Versão documental 4.1 · 31/10/2026**
**Estado:** especificação conceitual e modelos sintéticos. Sem execução de testes, evidências operacionais, revisão independente, adjudicação ou gate aprovado.

## 1. Finalidade
Estabelecer um modelo de rastreabilidade que permita responder, futuramente, **qual afirmação sobre conformidade é sustentada por qual artefato, execução, observação, revisor e autoridade de decisão**, com versões e limites verificáveis. Complementa GAI-INT-15 e GAI-INT-16; não os substitui.

A Guivos AI segue independente do GKR. O Guivos Intelligence consumirá as capacidades especializadas da Guivos AI; serviços canônicos permanecem autoridades de fatos, autorizações, identidade e versões. Neo4j pode hospedar projeções de relações, mas não ganha autoridade para criar evidência inexistente.

**Inventário documental de referência:** 12 capacidades, 16 estudos integrados anteriores, 19 schemas `candidate-v1`, 49 casos estruturais sintéticos, dois executores offline e 16 decisões pendentes. Não há run observado nem gate liberado.

## 2. Modelo de objetos auditáveis
| Entidade lógica | Identificador proposto | Obrigação de proveniência |
| --- | --- | --- |
| ContractArtifact | `artifact_ref` | Repositório, caminho, commit, hash e classificação |
| SchemaVersion | `schema_ref` | `$id`, versão, digest e relação com CAP |
| FixtureCatalog | `fixture_catalog_ref` | Hash, origem sintética, versão e owner futuro |
| TestCase | `case_ref` | Catálogo, esperado, schema e escopo |
| AuthorizationDecision | `authorization_ref` | Alçada, finalidade, escopo, validade e status |
| EnvironmentSnapshot | `environment_ref` | Dependências, isolamento e fingerprint |
| TestRun | `run_ref` | Autorização, artefatos congelados, horários e saída real |
| CaseObservation | `observation_ref` | Esperado vs observado, status e limitações |
| Defect | `defect_ref` | Severidade, evidência, correção, reteste e histórico |
| EvidencePackage | `evidence_package_ref` | Lista de observações e integridade |
| IndependentReview | `review_ref` | Responsável designado, independência, parecer e objeções |
| Adjudication | `adjudication_ref` | Divergência, resolução e fundamentos |
| GateDecision | `gate_decision_ref` | Autoridade formal, escopo, status e restrições |
| SupersessionEvent | `supersession_ref` | Registro substituído, motivo e novo registro |

**Obrigação:** cada referência deve resolver para um objeto verificável ou ficar marcada como indisponível; nunca completar lacunas com evidências presumidas.

## 3. Relações dirigidas propostas
```text
SchemaVersion ──DEFINED_IN──> ContractArtifact
TestCase ──TARGETS──> SchemaVersion
TestCase ──BELONGS_TO──> FixtureCatalog
TestRun ──AUTHORIZED_BY──> AuthorizationDecision
TestRun ──USES──> EnvironmentSnapshot / SchemaVersion / FixtureCatalog
CaseObservation ──OBSERVED_IN──> TestRun
CaseObservation ──EVALUATES──> TestCase
Defect ──SUPPORTED_BY──> CaseObservation
EvidencePackage ──INCLUDES──> CaseObservation / Defect
IndependentReview ──REVIEWS──> EvidencePackage
Adjudication ──CONSIDERS──> IndependentReview
GateDecision ──DECIDES_ON──> EvidencePackage
GateDecision ──GROUNDED_IN──> Adjudication / AuthorizationDecision
SupersessionEvent ──SUPERSEDES──> versão anterior
```
Arestas nunca substituem verificação de permissão para consultar os objetos. Um nó `TestRun` registrado **sem execução observada** não deve ser tratado como run concluído.

## 4. Semântica de estados e tempo
- **Preparação:** `documented`, `fixture_prepared`, `runner_prepared`.
- **Execução:** `not_authorized`, `authorized`, `not_executed`, `running`, `completed`, `failed`, `aborted`.
- **Observação:** `not_run`, `pass`, `fail`, `inconclusive`, `blocked`.
- **Verificação de integridade:** `pending`, `verified`, `failed`.
- **Revisão:** `not_reviewed`, `under_review`, `completed_with_findings`.
- **Adjudicação:** `not_adjudicated`, `under_adjudication`, `resolved`, `deferred`.
- **Gate:** `not_requested`, `pending`, `approved_with_scope`, `rejected`, `deferred`, `expired`, `revoked`.

Registrar separadamente `created_at`, `observed_at`, `reviewed_at`, `decided_at`, `effective_at`, `expires_at` quando aplicáveis. **Tempo de publicação no GitHub não equivale a tempo de execução**. Os estados devem ser derivados de registros com autoridade, não da simples existência de links.

## 5. Manifesto de rastreabilidade candidato
O [traceability-record-template.json](../tests/contracts/candidate-v1/traceability-record-template.json) preserva campos de vínculos entre artefatos, casos, observações, revisão, adjudicação e decisão, todos sem resultados efetivos. Um registro inicial com `execution_status=not_executed` **não é** um teste concluído.

Exemplo de relação documental — sem execução:
```json
{
  "record_kind": "candidate_evidence_trace",
  "document_version": "4.1",
  "status": "draft_unexecuted",
  "schema_family": "candidate-v1",
  "planned_fixture_refs": [
    "tests/contracts/candidate-v1/cases.json",
    "tests/contracts/candidate-v1/typed-cases.json"
  ],
  "run_refs": [],
  "observation_refs": [],
  "review_refs": [],
  "adjudication_ref": null,
  "gate_decision_ref": null
}
```

## 6. Princípios de integridade e auditoria
1. **Não reescrever histórico:** correções e retestes geram novo registro, ligado por `supersedes` ou `retest_of`.
2. **Conteúdo e ambiente identificáveis:** registrar hash criptográfico de conteúdo, commit e dependências; hash não comprova, isoladamente, legitimidade da origem.
3. **Associação mínima:** cada observação deve apontar ao caso e à execução real; cada execução, à autorização válida no momento.
4. **Completude demonstrável:** comparar casos planejados, executados, faltantes, bloqueados e inconclusivos; nenhum item ausente é `pass`.
5. **Trilha de decisão:** gate aprovado requer revisão, adjudicação e autoridade com alçada comprovada, além de escopo e prazo.
6. **Acesso controlado:** indexação de evidências não concede permissão para ler seus dados; logs sensíveis fora de repositório público.
7. **Reconstrução:** uma auditoria futura deve ser capaz de verificar o pacote a partir de versões e referências autorizadas.
8. **Assinaturas/atestações:** são propostas futuras; **nenhum documento atual é prova de assinatura digital**.

## 7. Consultas e verificações candidatas
| Consulta | Resposta que deve ser possível no futuro | Bloqueio |
| --- | --- | --- |
| Qual schema foi testado? | ID, commit e digest exatos | Versão desconhecida → inconclusivo |
| Quem autorizou o run? | Alçada, escopo, vigência e registro | Ausente → run não serve para gate |
| O que foi observado? | Casos, saídas, erro e ambiente | Apenas esperado → não observado |
| Quais defeitos permanecem? | Severidade, estado, evidência e reteste | S0 aberto → não liberar escopo |
| Quem revisou? | Independência, parecer e dissensos | Revisão exigida ausente → pendente |
| Qual decisão liberou? | GateDecision formal com restrições | Registro candidato → sem liberação |
| O gate ainda vale? | Validade, revogação e substituições | Expirado/revogado → não usar |
| Qual informação não pode ser exibida? | Escopo de acesso e retenção | Não revelar conteúdo restrito |

## 8. Neo4j, eventos e fontes canônicas
Um eventual grafo pode materializar relações do catálogo, mas o registro transacional de autorização, execução e decisão permanece sob o serviço responsável. Projeções atrasadas devem sinalizar cobertura incompleta, exigir reconciliação e evitar declaração de `zero falhas` ou `todos os gates válidos`.

Eventos futuros candidatos: `artifact_version_published`, `campaign_authorized`, `run_completed`, `observation_recorded`, `finding_opened`, `review_completed`, `adjudication_recorded`, `gate_decision_recorded`, `gate_revoked`. Não supor publicação real desses eventos. Não transportar dados sensíveis no barramento quando referências autorizadas forem suficientes.

## 9. Catálogo de 18 cenários sintéticos de auditoria
| ID | Cenário | Resultado exigido |
| --- | --- | --- |
| INT17-A01 | Caso planejado sem execução | `not_run`, nunca `pass` |
| INT17-A02 | Run sem autorização | Não usar como prova de gate |
| INT17-A03 | SHA divergente | Marcar integridade falha |
| INT17-A04 | Alteração posterior de fixture | Versão anterior preservada |
| INT17-A05 | Caso negativo corretamente rejeitado | `pass` daquela comparação observada |
| INT17-A06 | Defeito corrigido em reteste | Preservar defeito e ligação `retest_of` |
| INT17-A07 | Parecer sem responsável | Revisão não comprovada |
| INT17-A08 | Revisor com conflito não tratado | Escalar independência |
| INT17-A09 | Adjudicação com dissenso aberto | Decisão condicionada ou adiada |
| INT17-A10 | GateDecision sem alçada | Não aprovar |
| INT17-A11 | Gate expirado | Não usar como autorização vigente |
| INT17-A12 | Gate revogado | Bloquear novos usos autorizados por ele |
| INT17-A13 | Grafo incompleto | Não afirmar cobertura integral |
| INT17-A14 | Artefato de outro tenant | Negar referência indevida |
| INT17-A15 | Evidência contém PII | Restringir, tratar conforme política |
| INT17-A16 | Resultado sem vínculo com caso | Evidência órfã, inconclusiva |
| INT17-A17 | Evento `run_completed` duplicado | Não duplicar efeitos de estado |
| INT17-A18 | Registro de execução sem `observed_at` | Exigir revisão de procedência |

**Todos são cenários planejados, sem execução ou revisão.**

## 10. Critérios para futura solicitação de auditoria
Um pacote só será candidato a análise de gate quando: (a) autorização houver sido concedida e esteja válida; (b) cada artefato usado tenha digest/versão; (c) execução observada e reproduzível exista; (d) resultados incluam negativas, inconclusivos e bloqueios; (e) revisão independente e conflitos estejam registrados; (f) alçada de decisão esteja designada; (g) dados, retenção e acessos sejam compatíveis com a política vigente.

A ausência de qualquer condição relevante mantém `pending`, `inconclusive` ou `blocked`; não presumir aprovação parcial.

## 11. Gates e pendências
- **G0:** arquitetura e responsáveis parcialmente documentados; faltam ratificações.
- **G1:** schemas e compatibilidade exigem execução/revisão.
- **G2:** identidade, autorização, revogação e isolamento exigem testes específicos.
- **G3:** 49 fixtures estruturais permanecem não executadas.
- **G4:** integração controlada ainda não autorizada.
- **G5:** revisão/adjudicação humana ainda não realizada.
- **G6:** liberação exige decisão formal, observabilidade e rollback.

As 16 PND-01–16 permanecem abertas; nenhuma delas foi encerrada neste estudo.

## 12. Próximo estudo recomendado
**GAI-INT-18 — Modelo de Observabilidade de Gates, Alertas e Revalidação Contínua**, especificando como detectar expiração, revogação, mudanças de versão, perda de cobertura e divergências de evidência **sem acionar monitoramento operacional** antes de aprovação.

**Referências:** [GAI-INT-16](pacote-evidencias-revisao-independente-adjudicacao-gates.md) · [GAI-INT-15](preparacao-execucao-sintetica-controlada-evidencias-gate.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [GAI-INT-07](contratos-eventos-projecao-dependencias.md) · [GAI-INT-04](catalogo-fixtures-rubricas-adjudicacao.md).

**Sem alterações em Replit, Neo4j, provedores, API e GKR. Nenhum gate foi aprovado.**
