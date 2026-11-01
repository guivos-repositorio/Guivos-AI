# GAI-INT-62 — Matriz de Invariantes e Regras Condicionais dos Instrumentos

**Data:** 01/11/2026 · **Estado:** especificação documental candidata, não contrato homologado.  
**Base:** [GAI-INT-61](gai-int-61-dicionario-canonico-campos-cardinalidade.md), [GAI-INT-60](gai-int-60-matriz-aderencia-formularios-adendos.md) e instrumentos [GAI-INT-57](gai-int-57-instrumentos-aceite-parecer.md) a [GAI-INT-59](gai-int-59-adendos-completude-instrumentos.md).

## 1. Legenda e semântica
Esta matriz registra **regras propostas para revisão humana futura**, sem executar validador, rodar fixtures ou implementar JSON Schema. `R` = condição exigível quando o evento correspondente existir; `F` = combinação proibida por princípio de governança; `P` = condição ainda dependente de ratificação técnica ou institucional.

A ausência de evidência não deve ser interpretada como aprovação. Um documento pode satisfazer uma regra de forma *estrutural* sem comprovar autenticidade, legalidade, integridade ou eficácia. Identidade, atribuições e escopos de autorização requerem verificação externa.

## 2. Invariantes transversais
| ID | Regra candidata | Condição / negação | Estado |
| --- | --- | --- | --- |
| INV62-T01 | Identificador de ocorrência único | Registro real deve ter `record_id` não vazio, `record_kind`, `blocker_id` e referências de modelo | R |
| INV62-T02 | Vínculo tipo–bloqueador | `documentary_review` só se vincula a BLK-D01; `institutional_nomination` a BLK-I01; `evidence_adjudication` a BLK-E05 | R |
| INV62-T03 | Origem e limitações | Registro efetivo exige `source_document_refs` com pelo menos um item e `limitations` explícito (pode ser lista vazia) | R |
| INV62-T04 | Revisão não autodeclarada | `record_status=reviewed` exige referência de revisor e comprovação independente de identidade/competência conforme política aplicável | R |
| INV62-T05 | Separação entre decisões | `closure_decision_ref` não pode ser produzido pelo simples preenchimento ou revisão do instrumento; `gate_decision_ref` depende de ato próprio | F |
| INV62-T06 | Falha fechada para autorização | `approved=true`, papel preenchido ou arquivo assinado sem vínculo institucional verificável não autorizam execução B/C ou COMP-04-P | F |
| INV62-T07 | Vigência e revogação | Qualquer afirmação de permissão eficaz exige verificação de prazo, escopo, revogação e autoridade | R |
| INV62-T08 | Sigilo | Referências `*_private` são opacas; conteúdo sensível não pode ser copiado para GitHub público | F |
| INV62-T09 | Consistência temporal | `effective_at` e `expires_at` só podem ser confrontados quando ambos definidos e validados; `expires_at` anterior a `effective_at` é incompatível | R |
| INV62-T10 | Alias não comprova evento | Converter um nome legado para nome canônico não cria ato, evidência ou resultado observado | F |

## 3. F1 — Precedência documental (BLK-D01)
| ID | Condição | Regra ou combinação inválida | Estado |
| --- | --- | --- | --- |
| INV62-D01 | Registro de revisão constituído | `historical_entries` deve conter 1..N objetos com `historical_document_ref` e `interpretation_note` | R |
| INV62-D02 | `supersession_type=normative_decision` | Exigir `supervening_decision_ref` e `decision_scope` não vazios | R |
| INV62-D03 | Precedência histórica declarada | Proibir alegação de revogação integral sem decisão expressa que cubra todo o escopo | F |
| INV62-D04 | Um documento com múltiplas decisões posteriores | Usar `precedence_links` 0..N; uma única referência escalar não deve ocultar demais decisões | P |
| INV62-D05 | Aceite editorial declarado | Exigir referência de revisão competente, conferência de links/versão e `editorial_acceptance_ref` real | R |
| INV62-D06 | Texto original preservado | Proibir atualização retroativa da narrativa do documento histórico como se fosse fato da data original | F |

## 4. F2 — Identidade e aceite institucional (BLK-I01)
| ID | Condição | Regra ou combinação inválida | Estado |
| --- | --- | --- | --- |
| INV62-I01 | Indicação formal emitida | `nomination_decision_ref`, `appointing_authority_ref` e `nomination_scope` precisam identificar atos distintos | R |
| INV62-I02 | Aceite individual declarado | Exigir `acceptance_ref_private`, `independent_verification_ref` e prova de autoridade do ato antes de declarar aceite verificável | R |
| INV62-I03 | Papel indicado | Não presumir habilitação técnica ou permissão operacional a partir de `role_id` | F |
| INV62-I04 | Funções incompatíveis na mesma pessoa | Exigir avaliação de conflito e decisão competente; incompatibilidade não é sanada apenas preenchendo `mitigation_ref` | R |
| INV62-I05 | Aceite com prazo | Verificar coerência temporal e revogação; não manter aceite eficaz depois de expiração/revogação aplicável | R |
| INV62-I06 | Identidade sem verificação externa | Proibir declaração de autoridade verificada com base somente em nome, mensagem ou assinatura não vinculada | F |
| INV62-I07 | Política de conflito por pares de papéis | Critérios específicos ainda dependem de ratificação; não inferir que todos os pares são permitidos | P |

## 5. F3 — Evidências e custódia (BLK-E05)
| ID | Condição | Regra ou combinação inválida | Estado |
| --- | --- | --- | --- |
| INV62-E01 | Parecer sobre evidência efetiva | `evidence_items` deve conter 1..N itens com `artifact_ref` e `provenance_ref` | R |
| INV62-E02 | `digest_observed` declarado | Requer `digest_algorithm`, `digest_verifier_ref` e método documentado de comparação com referência apropriada | R |
| INV62-E03 | Integridade afirmada | Proibir conclusão de hash conferido quando valor esperado e observado são apenas autodeclarados pelo mesmo interessado | F |
| INV62-E04 | Custódia efetiva afirmada | Requer política de acesso, referência de retenção e trilha de custódia adequada; detalhes privados não devem ser publicados | R |
| INV62-E05 | `review_disposition=accepted_for_scope` | Requer revisão independente verificável, escopo delimitado, contradições e limitações tratadas | R |
| INV62-E06 | Parecer favorável | Não preenche automaticamente `disposition_ref`, `closure_decision_ref` ou `gate_decision_ref` | F |
| INV62-E07 | Retenção/algoritmo de hash | Prazo, algoritmo aceito e critérios de confiança dependem de decisão própria e não são definidos nesta matriz | P |

## 6. Exemplos negativos conceituais — não são fixtures executadas
| Caso | Entrada conceitual | Expectativa de desenho |
| --- | --- | --- |
| C62-N01 | `record_kind=institutional_nomination` com `blocker_id=BLK-E05` | Incompatível |
| C62-N02 | `record_status=reviewed` sem revisor verificável | Incompatível |
| C62-N03 | F1 declara precedência normativa sem `supervening_decision_ref` | Incompatível |
| C62-N04 | F2 apresenta `role_id` e deduz permissão para Pedido B | Incompatível |
| C62-N05 | F3 declara `digest_observed` sem verificador | Incompatível |
| C62-N06 | F3 marca `accepted_for_scope` sem revisão independente | Incompatível |
| C62-N07 | Encerramento de bloqueador automaticamente usado como gate | Incompatível |

Nenhum exemplo foi avaliado por código; expectativas são derivadas de regras candidatas. Casos adicionais, valores permitidos, formatos e semântica dos estados precisam de deliberação técnica antes de transformar esta matriz em schemas.

## 7. Dependências e próxima etapa
Pontos pendentes: catálogo de conflitos por função; cardinalidade definitiva para precedência; regra de serialização; obrigatoriedade por estado; autoridade e âncora de confiança; política de retenção e algoritmos aceitos; integração com custódia privada; critérios de fechamento. **Próxima etapa proposta: GAI-INT-63 — Matriz de Casos Conceituais e Condições de Aceite das Regras INV62**, sem execução, sem schema e sem alterar os 82 casos já catalogados.

## 8. Estado
**15 bloqueadores** (7 P0, 7 P1, 1 P2), nenhum encerrado por esta publicação. **82 casos sintéticos catalogados anteriormente, zero execuções verificadas. Pedido A concluído; Pedidos B/C não autorizados; COMP-04-P condicionado e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Não houve testes, instalação, inspeção, nomeação, credencial, implantação, adoção contratual ou gate.
