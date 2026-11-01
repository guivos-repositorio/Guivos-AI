# GAI-INT-59/F2 — Adendo de Completude BLK-I01

**Vinculado a:** [GAI-INT-57/F2](gai-int-57-formulario-aceite-blk-i01.md). **Natureza:** modelo, sem designações ou aceites.

## 1. Comprovação institucional
Campos futuros: `appointing_authority_ref`, `authority_validation_ref`, `nomination_decision_ref`, `nomination_scope`, `identity_evidence_ref_private`, `independent_verification_ref`, `acceptance_ref_private`, `acceptance_verified_at`, `effective_at`, `expires_at`, `suspension_ref`, `revocation_ref`.

Verificação da identidade do representante da direção e de cada nomeado deve ocorrer por fonte externa apropriada; declaração em conversa ou assinatura sem vínculo comprovado não é suficiente.

## 2. Segregação e incompatibilidades
Prever matriz com `role_a`, `role_b`, `conflict_rule_ref`, `assessment_ref`, `independent_reviewer_ref`, `mitigation_ref`, `decision_ref`. Examinar explicitamente segregação entre registrador, custodiante, operador, revisor e auditor. O preenchimento de papéis não autoriza credenciais nem supera conflitos automaticamente.

## 3. Custódia privada de comprovantes
Definir somente referências opacas em documentação pública. Política futura de custódia deverá especificar acesso mínimo, retenção, integridade, revogação e rastreabilidade; não registrar dados pessoais ou segredos no GitHub.

## 4. Checklist futuro
- [ ] Autoridade e papel institucional foram verificados independentemente.
- [ ] Indicação, verificação, aceite e habilitação são atos distintos.
- [ ] Incompatibilidades foram analisadas e julgadas por responsável competente.
- [ ] Comprovantes estão em custódia apropriada e o prazo de validade é definido.
- [ ] Mecanismos de suspensão e substituição estão registrados.

**Estado:** `nomination_decision_ref=null`, `acceptance_ref_private=null`, `closure_decision_ref=null`, `gate_decision_ref=null`. Sem nomeações; BLK-I01 aberto; Pedido B/C não autorizado.
