# GAI-INT-61 — Dicionário Canônico de Campos e Regras de Cardinalidade

**Data:** 01/11/2026 · **Estado:** proposta documental de normalização, não contrato operacional homologado.  
**Base:** [GAI-INT-57](gai-int-57-instrumentos-aceite-parecer.md), [GAI-INT-58](gai-int-58-roteiro-revisao-completude-segregacao.md), [GAI-INT-59](gai-int-59-adendos-completude-instrumentos.md) e [GAI-INT-60](gai-int-60-matriz-aderencia-formularios-adendos.md).

## 1. Semântica dos campos
Tipos são **tipos lógicos candidatos**, não JSON Schema validado: `string` (identificador opaco não vazio); `datetime` (instante com offset explícito); `boolean`; `enum`; `array<T>`; `object`; `null` (valor ainda não existente).  
**O** = obrigatório em registro efetivamente constituído; **C** = obrigatório apenas se a condição indicada ocorrer; **P** = opcional; **N** = deve ser nulo até haver decisão real. Ausência do dado nunca equivale a aprovação. Campos pessoais e referências privadas não devem conter seus valores sensíveis no GitHub público.

## 2. Envelope comum candidato
| Campo canônico | Tipo | Regra | Cardinalidade | Descrição |
| --- | --- | --- | --- | --- |
| `record_id` | string | O quando o registro existe | 1 | Identificador único da ocorrência, distinto do nome do modelo |
| `record_kind` | enum | O | 1 | `documentary_review`, `institutional_nomination`, `evidence_adjudication` |
| `blocker_id` | enum | O | 1 | BLK-D01, BLK-I01 ou BLK-E05 conforme instrumento |
| `form_template_ref` | string | O | 1 | Versão do formulário GAI-INT-57 |
| `addendum_ref` | string | O quando houver complemento aplicável | 1 | Referência ao adendo GAI-INT-59, sem substituir original |
| `record_status` | enum | O | 1 | `draft`, `pending_review`, `reviewed`, `superseded`, `revoked` |
| `source_document_refs` | array<string> | O | 1..N | Documentos de apoio, não provas automáticas |
| `limitations` | array<string> | O | 0..N | Lacunas e limites, inclusive lista vazia expressa |
| `contradiction_refs` | array<string> | P, C se divergência encontrada | 0..N | Referências específicas a contradições |
| `reviewer_role_ref` | string/null | C ao haver revisão | 0..1 | Função verificada, sem presumir nomeação |
| `reviewer_identity_verification_ref` | string/null | C ao haver revisão formal | 0..1 | Prova privada e independente |
| `closure_decision_ref` | string/null | N até encerramento formal | 0..1 | Decisão específica de encerramento do bloqueador |
| `gate_decision_ref` | string/null | N até decisão própria de gate | 0..1 | Nunca derivar do fechamento do bloqueador |

## 3. F1 — BLK-D01: precedência documental
| Campo | Tipo | Regra | Cardinalidade |
| --- | --- | --- | --- |
| `historical_entries` | array<object> | O em revisão documental efetiva | 1..N |
| `historical_entries[].historical_document_ref` | string | O | 1 por entrada |
| `historical_entries[].historical_blob_sha` | string/null | C quando verificação de integridade exigível | 0..1 |
| `historical_entries[].historical_date` | datetime/null | C quando data comprovável | 0..1 |
| `historical_entries[].supervening_document_ref` | string/null | C quando houver documento posterior pertinente | 0..1 |
| `historical_entries[].supervening_decision_ref` | string/null | C quando a precedência for normativa | 0..1 |
| `historical_entries[].decision_scope` | string/null | C junto da decisão normativa | 0..1 |
| `historical_entries[].supersession_type` | enum/null | C se superveniência afirmada | 0..1 (`normative_decision`, `factual_update`, `editorial_addendum`) |
| `historical_entries[].interpretation_note` | string | O | 1 |
| `link_check_refs` / `diff_refs` | array<string> | C em revisão concluída | 0..N |
| `editorial_acceptance_ref` | string/null | N até aceite competente | 0..1 |

Uma entrada representa **um documento histórico**; se houver múltiplas decisões posteriores para ele, registrar relação em coleção adicional `precedence_links` (0..N) antes de formalizar contrato, para evitar truncamento de informações. A estrutura é proposta, não modelo validado.

## 4. F2 — BLK-I01: indicação, identidade e aceite
| Campo | Tipo | Regra | Cardinalidade |
| --- | --- | --- | --- |
| `role_id` | enum | O em ato futuro | 1 (`ROLE-REG`, `ROLE-CUS`, `ROLE-REV`, `ROLE-OPS`, `ROLE-AUD`) |
| `appointing_authority_ref` | string | C em indicação emitida | 1 |
| `authority_validation_ref` | string | C antes de aceite institucional eficaz | 1 |
| `nomination_decision_ref` | string/null | N até ato de nomeação | 0..1 |
| `nomination_scope` | string | C com indicação efetiva | 1 |
| `identity_evidence_ref_private` | string/null | C para verificação de identidade | 0..1 |
| `independent_verification_ref` | string/null | C antes de aceite validado | 0..1 |
| `acceptance_ref_private` | string/null | N até aceite individual | 0..1 |
| `acceptance_verified_at` | datetime/null | C com aceite verificado | 0..1 |
| `effective_at` / `expires_at` | datetime/null | C quando vigência estabelecida | 0..1 cada |
| `conflict_assessments` | array<object> | C antes de decisão de segregação | 0..N |
| `conflict_assessments[].role_a` / `role_b` | enum | O por avaliação | 1 cada |
| `conflict_assessments[].conflict_rule_ref` / `assessment_ref` | string | O por avaliação | 1 cada |
| `suspension_ref` / `revocation_ref` | string/null | C se ocorrer evento | 0..1 cada |

**Invariante:** indicação, prova de identidade, aceite, habilitação técnica e autorização B/C são fatos distintos. A existência de `role_id` não confere função ou privilégio.

## 5. F3 — BLK-E05: evidência, custódia e adjudicação
| Campo | Tipo | Regra | Cardinalidade |
| --- | --- | --- | --- |
| `evidence_items` | array<object> | O em parecer de evidência efetiva | 1..N |
| `evidence_items[].artifact_ref` | string | O por item | 1 |
| `evidence_items[].digest_algorithm` | string | C quando hash exigido | 1 |
| `evidence_items[].digest_expected` / `digest_observed` | string/null | C apenas após fonte e verificação adequadas | 0..1 cada |
| `evidence_items[].digest_verifier_ref` | string/null | C para hash observado | 0..1 |
| `evidence_items[].provenance_ref` | string | O por item | 1 |
| `evidence_items[].custody_location_ref_private` | string/null | C quando evidência estiver sob custódia | 0..1 |
| `evidence_items[].chain_of_custody_refs` | array<string> | C quando movimentações ocorrerem | 0..N |
| `custody_policy_ref` / `retention_period_ref` / `access_policy_ref` | string/null | C antes de custódia efetiva | 0..1 cada |
| `independent_reviewer_ref` | string/null | C antes de parecer independente | 0..1 |
| `review_disposition` | enum/null | N até parecer | 0..1 (`insufficient`, `requires_correction`, `accepted_for_scope`, `rejected`) |
| `disposition_ref` | string/null | N até decisão competente | 0..1 |

**Invariante:** um digest informado não equivale a hash verificado; cadeia de custódia descrita não comprova custódia implementada. Parecer favorável não aprova gate.

## 6. Aliases e depreciações documentais propostas
| Campo anterior | Destino canônico | Regra |
| --- | --- | --- |
| `review_record_id`, `nomination_record_id`, `evidence_review_id` | `record_id` | Adaptar apenas em futuros registros; não reescrever histórico |
| `acceptance_ref` | `acceptance_ref_private` em F2 | Distinguir aceite individual de aceite editorial |
| `reviewer_ref`, `independent_reviewer_ref` | `reviewer_role_ref` + prova de identidade | Exigir separação de papel e verificação |
| `artifact_digest` | `digest_expected` + `digest_observed` + verificador | Não presumir que o valor legado foi observado |
| `editorial_acceptance_ref` | Mantido em F1 | Não confundir com aceite de pessoa |
| `gate_decision_ref` | Mantido distinto | Nunca preencher por inferência |

Os aliases são recomendações; dependem de decisão técnica antes de qualquer migração ou schema definitivo.

## 7. Dependências e próxima decisão
Pendências a ratificar: política exata de tipos de referência e identificadores; serialização; limite superior de cardinalidade; campos obrigatórios por estágio; enum de estados; sigilo e localização de evidências; critérios de conflito; autoridade e retenção. **Não foram criados ou executados validadores JSON Schema.** 

**Próxima proposta — GAI-INT-62:** matriz de invariantes e regras condicionais do dicionário canônico, estritamente documental, antes de qualquer schema candidato.

## 8. Estado preservado
**15 bloqueadores** (7 P0, 7 P1, 1 P2), nenhum encerrado nesta etapa. **82 casos catalogados sem execução verificada. Pedido A concluído; B/C não autorizados; COMP-04-P condicionado e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Nenhuma nomeação, implantação, schema, runner, teste ou gate foi aprovado por este documento.
