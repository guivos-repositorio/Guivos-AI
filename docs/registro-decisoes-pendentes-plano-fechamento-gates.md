# GAI-INT-14 — Registro de Decisões Pendentes e Plano de Fechamento de Gates
**Versão documental 3.8 · 31/10/2026**
**Estado:** consolidação de pendências e plano de decisão. Não há decisão técnica recém-aprovada, execução de teste, homologação nem liberação operacional.

## 1. Objeto e autoridade
Consolidar os pontos de decisão de GAI-INT-01 a 13, as evidências esperadas para os gates G0–G6 e a sequência de trabalho para reduzir incertezas **sem transformar uma hipótese registrada em decisão aprovada**.

A Guivos AI é uma camada de análises especializadas consumida pelo Guivos Intelligence. Os serviços canônicos preservam autoridade sobre fatos, fontes, identidades, versões e autorizações; Neo4j é infraestrutura candidata de projeção; GPT/Claude/Gemini são processadores auxiliares, não fontes canônicas. GKR permanece independente.

Este registro de pendências **complementa**, sem alterar a natureza das aprovações anteriores, o [Registro de Decisões do Repositório](registro-decisoes.md).

## 2. Estado de prontidão consolidado
- **12** capacidades CAP-01–12 documentadas.
- **13** estudos integrados anteriores (GAI-INT-01 a 13).
- **19** schemas JSON Schema `candidate-v1`, não normativos e não homologados.
- **49** fixtures estruturais sintéticas e **2** scripts offline preparados, sem runs documentados.
- Gates **G0 parcialmente documental; G1–G6 pendentes**.
- Replit/Jornada, Neo4j, provedores, API real e fontes canônicas **não foram modificados** em função destes estudos.

Os números representam inventário documental, **não índice de maturidade, capacidade operacional ou sucesso de testes**.

## 3. Registro estruturado de decisões em aberto
| ID | Decisão ainda requerida | Dependência principal | Função responsável candidata | Prioridade | Gate |
| --- | --- | --- | --- | --- | --- |
| PND-01 | Determinar autoridade por tipo de dado, versão e evidência | Serviços canônicos, INT-05 | Governança de dados | Crítica | G0/G2 |
| PND-02 | Definir bases legais e finalidades por fluxo, incluindo B2B | Privacidade, INT-05 | Jurídico/privacidade | Crítica | G2 |
| PND-03 | Formalizar identidade, vínculo, tenant e escopos de processamento/entrega | INT-05, CAP-12 | Segurança/identidade | Crítica | G2 |
| PND-04 | Selecionar arquitetura de memória/projeção e papel físico Neo4j | Ontologia, INT-06/07 | Arquitetura de dados | Alta | G1/G4 |
| PND-05 | Normalizar envelopes, estados, claims e contratos de erro | INT-02, 08–11 | Engenharia de contratos | Alta | G1 |
| PND-06 | Aprovar política de versões, evolução, migração e descontinuação | INT-12/13 | Arquitetura e consumidores | Alta | G1 |
| PND-07 | Escolher autenticação, fila, recibos e reconciliação dos eventos | INT-06/07/09 | Integração e segurança | Crítica | G2/G4 |
| PND-08 | Definir política de revogação, retenção, caches e derivados | INT-05/06 | Privacidade e armazenamento | Crítica | G2 |
| PND-09 | Aprovar catálogo de fixtures sintéticas e rubricas de avaliação | INT-03/04/10/11 | QA e qualidade de IA | Alta | G3 |
| PND-10 | Autorizar ou não execução isolada, atribuir orçamento e limites | INT-03/12 | Governança e responsável técnico | Alta | G3 |
| PND-11 | Designar revisores independentes e autoridade por gate | INT-03/04/12 | Governança | Crítica | G0/G5 |
| PND-12 | Definir métricas, severidade, thresholds e política de bloqueio | INT-03/12 | QA, segurança, produto | Alta | G3/G5 |
| PND-13 | Definir escopo e autorização de inspeção do Replit existente | Diagnóstico de integração | Produto/arquitetura | Alta | G4 |
| PND-14 | Definir integração com provedores e critérios de custo/qualidade | Adaptadores, políticas | Arquitetura de IA | Alta | G4/G6 |
| PND-15 | Definir telemetria mínima, resposta a incidentes e rollback | INT-12/13 | Operações/segurança | Alta | G6 |
| PND-16 | Avaliar produto/API B2B após provas de segurança, escopo e valor | CAP-12, INT-05, 12 | Produto/comercial/jurídico | Posterior | G6 |

**Status de todas as linhas: `pending_decision`.** Funções são propostas, não pessoas ou autoridades designadas. Prioridades são critérios de sequenciamento, não aprovações de execução.

## 4. Ordem de resolução e dependências
**Fase A — Autoridade e papéis:** PND-01, 02, 03, 08, 11. Resolver a arquitetura de governança e os limites legais/finalidades antes de manipular dados além de fixtures sintéticas.

**Fase B — Contratos e persistência:** PND-04, 05, 06, 07. Definir schemas revisáveis, referências de dados, projeções, eventos e compatibilidade; não exigir Neo4j como única escolha sem decisão.

**Fase C — Avaliação sintética:** PND-09, 10, 12. Revisar fixtures, selecionar execução isolada, capturar resultados por run e impedir que casos `not_executed` apareçam como `pass`.

**Fase D — Integração condicionada:** PND-13, 14, 15. Inspecionar arquitetura real do Replit somente com autorização específica; provar revalidação temporal e de acesso antes de exposição a usuários.

**Fase E — Produto e liberação:** PND-16 após decisões e gates relevantes; não presumir consumo comercial autorizado por existir schema CAP-12.

**A ordem é recomendação documental.** Dependências podem ser replanejadas formalmente, com justificativa e histórico.

## 5. Pacote mínimo por decisão
Campos candidatos:
`decision_candidate_id`, `subject`, `question`, `alternatives[]`, `recommended_option`, `rationale`, `tradeoffs[]`, `risk_class`, `affected_components[]`, `required_evidence_refs[]`, `authority_role`, `assigned_reviewer_refs[]`, `decision_status`, `decision_ref`, `review_by`, `supersedes_ref`.

Estados: `pending_decision`, `under_review`, `approved_with_scope`, `rejected`, `deferred`, `superseded`. Só `approved_with_scope` com evidência, alçada e registro formal poderá sustentar uma decisão de implementação, respeitando gates independentes.

Exemplo **sintético, sem aprovação**:
```json
{
  "decision_candidate_id": "PND-06",
  "question": "Qual política contratual de compatibilidade adotar?",
  "alternatives": ["versoes_paralelas", "adaptadores_explicitos", "mudanca_unica"],
  "decision_status": "pending_decision",
  "decision_ref": null,
  "authority_role": "contract_governance_to_designate",
  "required_evidence_refs": ["GAI-INT-13"],
  "execution_authorized": false
}
```

## 6. Plano de fechamento dos gates
| Gate | Condição mínima para submissão à autoridade | Evidência faltante | Estado |
| --- | --- | --- | --- |
| G0 — Escopo e governança | Responsáveis e fronteiras ratificados; pendências/riscos registradas | Aprovação formal de donos e alçadas | Parcial |
| G1 — Contratos | Schemas revistos, testes estruturais executados, semântica aprovada, compatibilidade documentada | Runs, testes cruzados, decisão de owners | Pendente |
| G2 — Autoridade e segurança | Política de finalidade, autenticação, tenant, revogação e entrega aprovada e testada | Serviços/controles verificados e evidências | Pendente |
| G3 — Avaliação sintética | Casos positivos/negativos e adversariais executados e revisados | Run manifests, defeitos, adjudicação | Pendente |
| G4 — Integração controlada | Fluxos ponta a ponta isolados; tratamento de concorrência, falhas e rollback | Aprovação de ambiente e testes integrados | Pendente |
| G5 — Revisão humana | Revisores independentes designados e decisões sobre falhas/limites | Atas, pareceres, adjudicação e dissensos | Pendente |
| G6 — Liberação restrita | Autoridade de release, observabilidade, incidentes, custo, restrições | GateDecision, escopo e plano de reversão | Pendente |

Um gate não é concedido por percentual de artefatos publicados. **Falha S0 de privacidade/autorização bloqueia o avanço do escopo relevante, independentemente de médias.**

## 7. Critérios para definir que uma pendência foi fechada
1. A questão e alternativas foram explicitadas sem ambiguidade.
2. A alçada responsável foi identificada e autorizada.
3. Há evidência suficiente, com versões e limites verificáveis.
4. A decisão foi registrada separadamente da hipótese.
5. Os riscos residuais e condições de revisão constam do registro.
6. Documentos e consumidores afetados receberam encaminhamento.
7. A eventual alteração operacional requer autorização específica; **fechamento documental não significa deploy**.

Não marcar decisão como `approved` apenas pela criação deste GAI-INT-14.

## 8. Registro de risco sem mascaramento
| Risco | Consequência potencial | Regra de bloqueio |
| --- | --- | --- |
| Autoridade de dados ambígua | Conflito entre fontes e acesso indevido | G2 não aprovar sem autoridade e escopo |
| Permissão de processamento confundida com entrega | Compartilhamento indevido | Separar e validar autorizações |
| Resposta obsoleta exibida como vigente | Direcionamento incorreto | CAP-10 e consumers devem revalidar |
| Neo4j tratado como fonte canônica universal | Divergência entre projeção e origem | Definir owners e reconciliação |
| JSON Schema confundido com segurança | Vazamento não detectado por forma | Exigir testes de domínio e pen-test apropriado |
| Discordância de modelos tratada como prova | Claims sem fundamento | Revisão de evidência independente |
| Gate liberado sem run | Falsa homologação | Evidência real obrigatória |
| Migração reativa permissão revogada | Violação de escopo | Bloquear rollback permissivo |

## 9. Cadência sugerida de governança
Manter um registro versionado das propostas e decisões, com revisão por domínio conforme disponibilidade dos responsáveis. Separar reuniões de arquitetura, privacidade e testes; não inventar cronograma, responsáveis ou prazos. Nenhuma automação ou auditoria recorrente adicional é instituída por este documento.

## 10. Próximo passo condicionado
**GAI-INT-15 — Plano de Preparação para Execução Sintética Controlada e Evidências de Gate**, apenas como detalhamento documental futuro. Antes de executar qualquer suíte, exigir designação dos responsáveis, autorização de ambiente, critérios de segurança e versão congelada dos contratos.

**Referências:** [Registro de decisões existente](registro-decisoes.md) · [GAI-INT-13](plano-compatibilidade-migracao-evolucao-contratos.md) · [GAI-INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [GAI-INT-11](cobertura-contratos-especializados-integracao-schemas.md).

**Nenhum gate passou e nenhum teste ou serviço foi executado/alterado. Guivos AI e GKR seguem independentes.**
