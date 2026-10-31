# GAI-INT-16 — Modelo de Pacote de Evidências, Revisão Independente e Adjudicação de Gates
**Versão documental 4.0 · 31/10/2026**
**Estado:** proposta de governança e formulários candidatos. Nenhum teste executado, revisor designado, adjudicação realizada ou gate aprovado.

## 1. Finalidade e limites
Estabelecer uma cadeia verificável entre **escopo autorizado → execução real → evidências íntegras → revisão independente → adjudicação → decisão de gate**. Completa os estudos GAI-INT-03, 04, 12, 14 e 15, sem alterar suas autoridades nem presumir implementação.

O catálogo permanece com 19 schemas candidatos, 49 fixtures estruturais sintéticas, dois executores offline e 16 decisões PND-01–16 ainda pendentes. Estes números representam preparação documental. A mera publicação de templates, resultados sintéticos ou relatórios preenchidos com valores previstos **não autoriza liberação**.

## 2. Separação de objetos e responsabilidades
| Registro | Quem o produz (função candidata) | O que comprova | O que não comprova |
| --- | --- | --- | --- |
| Autorização de campanha | Autoridade competente designada | Permissão de executar o escopo específico | Aprovação de resultados futuros |
| Manifesto de execução | Executor/responsável técnico | Artefatos, ambiente, testes realmente disparados | Qualidade semântica, segurança ou adjudicação |
| Evidência individual | Sistema de teste e curador | Observação de um caso sob condições documentadas | Verdade fora do escopo da observação |
| Parecer independente | Revisor sem conflito material | Avaliação com rubrica e objeções | Poder de liberar produção, salvo alçada formal |
| Registro de adjudicação | Responsável por adjudicação | Resolução ou manutenção de divergências | Automaticamente aprovar G6 |
| GateDecision | Autoridade designada para o gate | Aprovação/rejeição/adiamento de um escopo e versão | Autorização universal de toda a plataforma |

A mesma Pessoa não deve atuar simultaneamente como única executora, revisora independente e autoridade de liberação em escopos de alto risco. Exceções requerem justificativa e revisão adicional documentadas.

## 3. Integridade do pacote
Um pacote de evidências candidato deve conter:
- Identidade da campanha `campaign_ref`, autorização `authorization_ref`, escopo `scope_ref`, gate solicitado `gate_id`.
- Commit imutável, hashes dos schemas, fixtures, executores, lockfile e configuração autorizada.
- Ambiente, isolamento, janela temporal, versão de validadores e registros de desvios autorizados.
- Lista exaustiva de casos previstos, iniciados, concluídos, falhos, inconclusivos e não executados.
- Observações por caso, erros minimizados, limitações, incidentes, retestes e relações com defeitos.
- Revisões independentes, objeções e eventual parecer de privacidade/segurança.
- Adjudicação e referência da decisão do gate, **se realmente ocorrerem**.

Publicação em repositório público não é destino automático adequado para logs sensíveis, provas de acesso, tokens ou dados pessoais. O pacote deve usar referências controladas, com política de retenção e sigilo definidos.

## 4. Estados distintos, sem atalho
**Campanha:** `draft` → `awaiting_authorization` → `authorized` → `executing` → `execution_completed|execution_failed|aborted`.

**Caso de teste:** `not_run`, `pass`, `fail`, `inconclusive`, `blocked`.

**Evidência:** `not_collected`, `collected`, `integrity_verified`, `integrity_failed`, `restricted`.

**Revisão:** `not_requested`, `awaiting_reviewer`, `under_review`, `completed_with_findings`, `returned_for_rework`.

**Adjudicação:** `not_started`, `under_adjudication`, `resolved`, `deferred`, `escalated`.

**Gate:** `not_requested`, `pending`, `approved_with_scope`, `rejected`, `deferred`, `revoked`, `expired`.

Nenhuma transição é automática entre estados de categorias diferentes. `execution_completed` não significa `pass` e `pass` não significa `approved_with_scope`.

## 5. Artefatos candidatos publicados
- [Modelo de pacote de evidências](../tests/contracts/candidate-v1/evidence-package-template.json): estrutura de autorização, artefatos, execução, achados, revisão e gate; `not_executed`.
- [Modelo de revisão e adjudicação](../tests/contracts/candidate-v1/gate-review-template.json): atribuição de revisão, conflitos, posicionamentos e decisões; `not_reviewed`/`not_adjudicated`.

Os arquivos são **templates documentais**, não exemplos de resultados reais. Campos `null` sinalizam informação inexistente, não aprovação tácita.

## 6. Rubricas de revisão independente
| Critério | Pergunta verificável | Evidência necessária |
| --- | --- | --- |
| Procedimento | A execução respeitou autorização e ambiente? | Manifesto, versão e logs minimizados |
| Integridade | Arquivos e resultados correspondem aos digests? | Hashes e armazenamento confiável |
| Cobertura | Quais dimensões e casos ficaram de fora? | Inventário e matriz de risco |
| Estrutura | Schemas aceitaram/rejeitaram o previsto? | Resultados observados por caso |
| Semântica | Claims, incerteza e limites foram preservados? | Rubricas e fontes autorizadas |
| Segurança | Identidade, finalidade, tenant e revogação foram verificadas? | Evidência de testes próprios; JSON Schema não basta |
| Temporalidade | Resultados obsoletos e eventos tardios foram tratados? | Testes de versionamento e invalidação |
| Consumo | Intelligence, relatório e API obedeceram escopo? | Integração isolada documentada |
| Operação | Falhas, retentativas, rollback e incidentes foram tratados? | Observabilidade e registros |
| Atribuição | Há conflitos de interesse ou lacunas de alçada? | Designação formal e declaração de independência |

Conclusões permitidas: `supported_by_evidence`, `partially_supported`, `unsupported`, `inconclusive`; sempre com justificativa e referência. Não atribuir notas inventadas.

## 7. Adjudicação e dissenso
1. Receber pacote íntegro, com autorização e objeto da decisão claramente delimitados.
2. Confirmar identidade funcional e independência dos revisores.
3. Verificar observações, amostragem, métricas e limitações, incluindo casos não executados.
4. Registrar cada objeção e conflito com severidade proposta S0–S3.
5. Resolver apenas o que a evidência permite; o restante permanece `deferred`/`inconclusive`.
6. Registrar decisão fundamentada, dissensos persistentes, condicionantes e escopo.
7. Encaminhar autorização de gate para **autoridade designada**, sem presumir que o adjudicador tenha poder de release.
8. Em reteste, criar novos identificadores e preservar os registros anteriores; nunca sobrescrever falhas.

**Bloqueios:** evidência forjada, ausência de autorização, exposição indevida, falha crítica de segregação/revogação, falta de revisão requerida e divergência material sem resolução impedem `approved_with_scope` do gate aplicável.

## 8. Contrato lógico de GateDecision
O registro formal futuro deve conter `gate_decision_id`, `gate_id`, `status`, `authority_ref`, `authority_scope`, `campaign_ref`, `evidence_package_ref`, `review_refs[]`, `adjudication_ref`, `decision_at`, `effective_at`, `expires_at`, `limitations[]`, `conditions[]`, `reversal_criteria[]`, `supersedes_ref`.

Uma decisão deve ser **versionada, revogável conforme governança e restrita ao escopo**. O status `approved_with_scope` não pode ser atribuído quando `authority_ref` ou as evidências obrigatórias estiverem ausentes. Template sem assinatura ou decisão verificável deve permanecer `not_requested`.

## 9. Gates e evidências por risco
| Gate | Pacote mínimo requerido | Estado nesta publicação |
| --- | --- | --- |
| G0 | Arquitetura, papéis e autoridades ratificados, pendências registradas | Parcial |
| G1 | Contratos normalizados, execução estrutural, compatibilidade e revisão de owners | Pendente |
| G2 | Testes específicos de identidade, escopo, revogação e segregação | Pendente |
| G3 | Execução sintética documentada, casos adversariais, rubricas e defeitos | Pendente |
| G4 | Integração isolada, eventos, caches, concorrência e recuperação comprovadas | Pendente |
| G5 | Revisão independente, dissenso e adjudicação formal | Pendente |
| G6 | Decisão autorizada de liberação, limites, observabilidade e rollback | Pendente |

Em todas as fases, autorização de processamento ≠ autorização de entrega. Revogação não equivale automaticamente a apagamento histórico. Dados fictícios não tornam segura uma integração não autorizada.

## 10. Casos de auditoria sintética, apenas propostos
| ID | Cenário | Regra de julgamento |
| --- | --- | --- |
| INT16-A01 | 49 fixtures preparadas, sem run | Nenhum `pass` observado |
| INT16-A02 | Run sem autorização | Não usar como prova para aprovação |
| INT16-A03 | Checksum do schema divergente | Invalidar pacote até reconciliação |
| INT16-A04 | Caso negativo é corretamente rejeitado | Registrar `pass` apenas daquele caso observado |
| INT16-A05 | Executor completou, mas casos falharam | Não inferir conformidade |
| INT16-A06 | Revisores discordam sobre risco material | Registrar dissenso e escalar |
| INT16-A07 | Revisor é também executor único | Exigir independência adequada |
| INT16-A08 | Revogação detectada em avaliação | Bloquear gate afetado |
| INT16-A09 | Relatório B2B sem autorização de entrega | Bloquear liberação |
| INT16-A10 | Reteste corrige defeito anterior | Preservar histórico de falha |
| INT16-A11 | Incidente S0 aberto | Bloquear gate do escopo relevante |
| INT16-A12 | Gate expirado ou revogado | Não permitir uso como autorização vigente |
| INT16-A13 | Documento aprovado, execução não realizada | Permanecer pendente |
| INT16-A14 | Resultado de modelo sem prova de fonte | Revisão epistêmica inconclusiva |
| INT16-A15 | Revalidação de cache não confirmada | Não declarar propagação concluída |
| INT16-A16 | Pacote expõe PII em logs | Restringir e tratar incidente conforme política |

Nenhum cenário foi executado ou adjudicado.

## 11. Pendências de decisão
As PND-01–16 do [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) seguem abertas. Antes de operacionalizar o pacote: designar autoridades; definir formato normativo e retenção de evidências; congelar versões e ambiente; aprovar rubricas e severidades; estabelecer independência da revisão; decidir autorização isolada; executar e registrar testes efetivos.

Não aprovar G1–G6 com base na criação de templates. Não alterar o [Registro de Decisões](registro-decisoes.md) para marcar novas aprovações inexistentes.

## 12. Próximo estudo recomendado
**GAI-INT-17 — Modelo de Rastreabilidade, Auditoria e Proveniência de Evidências de Gate**, para documentar relacionamentos entre commits, fixtures, runs, defeitos, revisões e decisões, mantendo o escopo documental até autorização.

**Referências:** [GAI-INT-15](preparacao-execucao-sintetica-controlada-evidencias-gate.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [GAI-INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [GAI-INT-04](catalogo-fixtures-rubricas-adjudicacao.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md).

**Nenhum dado real utilizado. Replit, Neo4j, provedores e GKR permanecem sem alterações operacionais.**
