# GAI-INT-31 — Propostas de Correção Contratual dos Achados STA-01, STA-02 e STA-03
**Versão documental 5.8 · 31/10/2026**
**Estado:** propostas técnicas para deliberação; **nenhum schema vigente foi editado**, nenhum teste foi executado e nenhum gate foi aprovado.

## 1. Origem e autorização
A [revisão estática GAI-REV-001](relatorio-revisao-estatica-autorizada-pedido-a.md), autorizada pelo representante da direção exclusivamente para leitura de arquivos públicos, identificou três riscos de maior prioridade. O encaminhamento da direção permite preparar **propostas de correção**, mas não implica aprovação de mudança de contrato, execução do Pedido B ou inspeção do Pedido C.

## 2. STA-01 — Controle de compartilhamento dos relatórios
**Fonte:** `schemas/candidate-v1/cap11-report-result.schema.json`.

**Observação:** `sharing_scope_ref` existe, mas não é obrigatório; `report_status` admite `released_to_authorized_recipient` sem essa referência.

**Alteração candidata:** adicionar um `if/then` que exija `sharing_scope_ref` não vazia nos estados `ready_for_authorized_release` e `released_to_authorized_recipient`. Manter a referência opcional em `draft` e estados sem compartilhamento, caso o domínio confirme essa intenção. Avaliar exigência de `delivery_receipt_ref` e `authorized_recipient_ref` **apenas depois de consultar o serviço canônico de autorização e entrega**; não inventar semântica nem titulares.

**Casos negativos propostos:** relatório liberado sem `sharing_scope_ref`; escopo vazio; envio com escopo expirado/revogado (esta última é **regra semântica de serviço**, não validável pelo schema isoladamente). **Caso positivo:** rascunho sem escopo de compartilhamento, se a regra for ratificada.

**Compatibilidade:** respostas antigas com status de liberação sem `sharing_scope_ref` deixarão de ser válidas; requer versão de contrato e migração ou rejeição explícita. A mera presença do campo não prova consentimento ou direito de acesso.

## 3. STA-02 — Recibos de eventos e transições
**Fonte:** `schemas/candidate-v1/event-receipt.schema.json`.

**Observação:** enums `operation` e `result` são independentes; por exemplo, `event_received` + `applied` é aceito estruturalmente, sem demonstrar aplicação da mudança.

**Alteração candidata:** organizar os resultados por fase usando `if/then`, após validar semanticamente quais operações podem efetivamente retornar `applied`. Uma proposta mínima é **não permitir `applied` com `event_received` ou `event_validated`**, e exigir `aggregate_version` para `validity_applied` com resultado `applied`. Decidir separadamente se `impact_assessed`, `consumer_acknowledged` e demais operações têm significado de aplicação ou de confirmação.

**Casos propostos:** `event_received/applied` inválido; `event_received/inconclusive` ou `not_applied` válido conforme política; `validity_applied/applied` sem versão inválido; resultado de aplicação sem evidência de efeito ainda dependerá de verificação operacional.

**Compatibilidade:** consumidores que usam `applied` como sinônimo de "recebido" terão de mudar comportamento e registros. Um recibo não substitui evento assinado, auditoria de estado ou prova de persistência.

## 4. STA-03 — Escopos de eventos canônicos
**Fonte:** `schemas/candidate-v1/canonical-event.schema.json`.

**Observação:** `authorization_policy_ref` não está em `required`; `subject_scope_ref` e `tenant_scope_ref` são opcionais e podem ser nulos.

**Alteração candidata:** exigir `authorization_policy_ref` não vazia para eventos com impacto de autorização, especialmente `authorization_scope_revoked`, `authorization_scope_expired` e `report_access_restricted`. Para esses eventos, propor `subject_scope_ref` não nula e não vazia; exigir também `tenant_scope_ref` não nula se o contexto de multitenancy do serviço for confirmado. Não impor regra global cega a eventos de versão de método sem sujeito, sob risco de rejeitar eventos legítimos.

**Casos negativos propostos:** revogação sem política; `subject_scope_ref=null`; string vazia; tenant obrigatório ausente em evento multitenant. **Caso positivo:** evento global sem sujeito, desde que o tipo e o owner permitam. Garantir que revogação gere invalidação operacional é requisito fora do JSON Schema.

**Compatibilidade:** produtores precisarão fornecer identificadores e política; confirmar fonte autoritativa e contrato de revogação antes de endurecer schemas.

## 5. Especificações estruturadas candidatas
A [matriz JSON de patches](propostas-correcao-sta01-sta02-sta03.json) conserva **expressões JSON Schema Draft 2020-12 propostas**, com pré-condições e critérios de aceitação. **Não são schemas em produção, nem substituem os 19 contratos em `schemas/candidate-v1`.**

## 6. Ordem de deliberação
1. **Produto + autorização/privacidade:** confirmar quais estados de relatório exigem escopo e recibo real.
2. **Arquitetura + serviço emissor/consumidor de eventos:** ratificar semântica de cada fase de recibo.
3. **Proprietários de identidade e autorização:** ratificar escopos de revogação, tenant e sujeito.
4. **Gestão central de autorizações:** decidir se permite uma mudança em nova versão candidata separada e campanha sintética posterior. A aprovação de desenho **não** autoriza executar scripts.
5. **Revisor independente e autoridade de gate:** avaliar evidências produzidas em etapas separadas, sem aprovação presumida.

## 7. Situação preservada
A autorização concedida se restringiu ao Pedido A. Pedidos B e C continuam não autorizados. G0 segue parcial, G1–G6 pendentes; PND-01 a PND-16 não foram encerradas. Nenhuma alteração em Replit, Neo4j, provedores ou GKR.

## Evolução v5.9
Os três schemas candidatos separados foram publicados no [GAI-INT-32](schemas-candidatos-v2-propostas-sta01-sta02-sta03.md). Nenhuma homologação foi concedida.
