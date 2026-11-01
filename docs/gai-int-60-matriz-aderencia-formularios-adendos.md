# GAI-INT-60 — Matriz de Aderência entre Formulários, Roteiro e Adendos

**Data:** 31/10/2026 · **Natureza:** conferência estática documental de GAI-INT-57, GAI-INT-58 e GAI-INT-59. **Sem revisão institucional, preenchimento, execução ou homologação.**

## 1. Escopo e fontes
Foram lidos o [índice dos instrumentos GAI-INT-57](gai-int-57-instrumentos-aceite-parecer.md), o [roteiro GAI-INT-58](gai-int-58-roteiro-revisao-completude-segregacao.md) e os [três adendos GAI-INT-59](gai-int-59-adendos-completude-instrumentos.md). A análise verifica **cobertura documental prevista**, não efetividade, conformidade operacional nem validade institucional. Os formulários originais permanecem preservados.

**Convenção:** C = coberto no desenho por formulário e/ou adendo; P = parcialmente definido ou depende de decisão de política; N = não demonstrado por estes instrumentos. Nenhuma classificação C significa evidência verificada.

## 2. Matriz de cobertura transversal
| ID | Requisito GAI-INT-58 | F1 BLK-D01 | F2 BLK-I01 | F3 BLK-E05 | Ressalva |
| --- | --- | --- | --- | --- | --- |
| REV58-T01 | Identificador inequívoco, versão e referência | C | C | C | Identificação de modelo; registros reais não existem |
| REV58-T02 | Campos obrigatórios/condicionais; ausência explícita | P | P | P | Campos previstos, mas não há esquema formal que distinga todos os condicionais |
| REV58-T03 | Segregação de papéis e incompatibilidades | P | C | C | Matriz F2 candidata, sem ratificação e sem verificação de pessoas |
| REV58-T04 | Integridade, temporalidade e revogação | C | C | C | Hash e origem não conferidos; campos apenas preparados |
| REV58-T05 | Privacidade e localização de custódia | P | C | C | F1 não detalha localização/retenção; documentos não criam sistema privado |
| REV58-T06 | Contradições, limitações e razões do parecer | C | P | C | F2 dispõe de `review_findings` e `limitations`, mas não explicita `contradiction_refs` |
| REV58-T07 | Encerramento separado de decisão de gate | C | C | C | Referências de fechamento e gate permanecem nulas |
| REV58-T08 | Precedência e histórico preservados | C | N/A | N/A | Requisito diretamente aplicável a F1; GAI-INT-54 define regra geral |

**Síntese de aderência de desenho:** não existe requisito transversal demonstrado como operacionalmente verificado. A cobertura formal de T02 permanece parcial nos três instrumentos. N/A não constitui lacuna funcional quando o requisito não é aplicável ao instrumento.

## 3. Matriz específica por instrumento
| Instrumento | Cobertura identificada | Sobreposição ou duplicidade | Lacuna remanescente | Encaminhamento candidato |
| --- | --- | --- | --- | --- |
| F1 BLK-D01 | Múltiplos documentos, decisão superveniente, versão, diff, aceite editorial | `historical_document_ref`, `contradiction_refs` e revisão aparecem no formulário e no adendo | Estrutura formal de múltiplas entradas, critérios obrigatórios/condicionais e referência de custódia/retensão, se o registro contiver evidência restrita | Definir tabela/estrutura canônica e compatibilidade de campos sem alterar fatos históricos |
| F2 BLK-I01 | Autoridade, identificação externa, segregação, aceite, vigência, suspensão e custódia privada | `nomination_decision_ref`, `effective_at`, `expires_at`, `independent_verification_ref`/identidade se sobrepõem semanticamente | Regras ratificadas de conflito por par de papéis, tratamento explícito de contradições e vocabulário canônico de campos equivalentes | Preparar dicionário e matriz de conflito propostos, não designar ou habilitar titulares |
| F3 BLK-E05 | Proveniência, digests esperados/observados, verificador, custódia, retenção, revisão e adjudicação | Campos de digest, cadeia de custódia, limitações e revisão aparecem em duas camadas | Critérios de aceitação de algoritmos, política de retenção, confiança institucional, tratamento de exceções e decisão externa | Especificar dependências da política e semântica canônica sem executar verificações |

## 4. Duplicidades e normalização proposta
- **Identidade do registro:** manter um ID único por avaliação efetiva e referenciar o formulário e adendo como versão de desenho. Não usar IDs de documento como prova de uma avaliação.
- **Origem/autorização:** distinguir `appointing_authority_ref` (origem do ato), `authority_validation_ref` (prova externa), `nomination_decision_ref` (decisão específica), `acceptance_ref` (aceite da pessoa). Campos equivalentes com sufixo `_private` exigem política de localização, não duplicação de fato.
- **Integridade:** distinguir digest esperado, digest observado e identidade do verificador; o simples `artifact_digest` não demonstra comparação.
- **Revisão e decisão:** distinguir parecer preliminar, disposição por autoridade e fechamento do bloqueador; `gate_decision_ref` só pode ser definido por processo próprio.
- **Histórico:** adendos complementam os modelos; não substituem nem revogam documentos originais.

## 5. Incompatibilidades e dependências identificadas
1. **Vocabulário:** variações como `reviewer_ref`/`independent_reviewer_ref` e `acceptance_ref`/`acceptance_ref_private` exigem dicionário para evitar interpretações divergentes.
2. **Cardinalidade:** F1 prevê múltiplos documentos, mas o instrumento original é uma ficha singular; definir cardinalidade e estrutura de coleção antes de preenchimentos reais.
3. **Obrigatoriedade:** sem regras formais de campos obrigatórios por tipo de registro; o checklist sozinho não constitui contrato de dados.
4. **Privacidade:** referências a custódia privada são propostas, não localização aprovada nem garantia de segurança.
5. **Independência:** indicação, verificação, revisão e decisão têm papéis distintos ainda não formalmente ocupados.
6. **Semântica de aceite:** aceite documental, aceite de função, aceitação de evidência, encerramento de bloqueador e gate são atos separados.

## 6. Conclusão e critérios de aceite futuro
O conjunto **GAI-INT-57 + 58 + 59 fornece cobertura documental preliminar das três frentes**, com lacunas de semântica, cardinalidade, campos condicionais e autoridade. Não declarar os instrumentos completos em sentido institucional ou prontos para uso operacional.

Próxima etapa candidata: **GAI-INT-61 — Dicionário Canônico de Campos e Regras de Cardinalidade para Instrumentos**, como proposta documental. Qualquer normalização formal requer avaliação dos responsáveis competentes e manutenção da rastreabilidade histórica.

## 7. Estado e limites
**BLK-D01:** parcial documental; **BLK-I01 e BLK-E05:** abertos. Os 15 bloqueadores permanecem sem encerramento comprovado (7 P0, 7 P1, 1 P2). **82 casos catalogados, zero execuções verificadas; Pedido A concluído; B/C não autorizados; COMP-04-P condicionado e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Nenhuma nomeação, credencial, teste, inspeção, alteração de schema, runner, ambiente ou gate decorre deste documento.
