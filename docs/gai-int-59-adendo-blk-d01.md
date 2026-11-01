# GAI-INT-59/F1 — Adendo de Completude BLK-D01

**Vinculado a:** [GAI-INT-57/F1](gai-int-57-formulario-revisao-blk-d01.md). **Natureza:** campos candidatos; não preenchido.

## 1. Controle de múltiplos documentos
Prever uma entrada independente por documento histórico: `historical_document_ref`, `historical_blob_sha`, `historical_date`, `supervening_document_ref`, `supervening_decision_ref`, `decision_scope`, `effective_from`, `supersession_type` (decisão, correção factual, adendo), `interpretation_note` e `contradiction_refs`. Não inferir que versões posteriores revogam integralmente normas anteriores.

## 2. Aceite e rastreabilidade
Prever `editorial_review_id`, `link_check_refs`, `diff_ref`, `editorial_reviewer_ref`, `reviewer_competence_ref`, `independence_required`, `editorial_acceptance_ref`, `accepted_scope`, `acceptance_date` e `limitations`. Conferir integridade de links e preservação histórica antes do aceite, sob revisão competente.

## 3. Checklist futuro
- [ ] Cada documento possui referência e versão próprias.
- [ ] A superveniência tem alcance material e temporal explícito.
- [ ] Histórico foi preservado; nenhuma narrativa reescrita retroativamente.
- [ ] Decisões normativas e artefatos propostos foram distinguidos.
- [ ] Diff, links, ressalvas e parecer documental foram examinados.
- [ ] Aceite editorial independente, quando exigível, foi registrado.

**Campos de decisão:** `editorial_acceptance_ref=null`; `closure_decision_ref=null`; `gate_decision_ref=null`. Não assinalar itens antes da revisão. Este adendo não encerra BLK-D01.
