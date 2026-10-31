# GAI-INT-32 — Schemas candidatos v2 isolados para STA-01/02/03
**Versão documental 5.9 · 31/10/2026**  
**Estado:** 3 arquivos candidatos publicados; nenhuma substituição de candidate-v1, execução de teste, aprovação técnica ou gate.

## 1. Escopo executado
A partir dos três arquivos fonte em `schemas/candidate-v1/`, foram publicados **três novos JSON Schemas** em `schemas/candidate-v2-proposed/`, sob `$id` exclusivos desse diretório. Trata-se da preparação documental/técnica solicitada pela direção após o GAI-INT-31. Não há aplicação em APIs ou sistemas operacionais.

| Achado | Schema original preservado | Schema novo proposto | Mudança |
| --- | --- | --- | --- |
| STA-01 | [cap11 v1](../schemas/candidate-v1/cap11-report-result.schema.json) | [cap11 v2 proposta](../schemas/candidate-v2-proposed/cap11-report-result.schema.json) | `allOf/if/then` exige `sharing_scope_ref` quando `report_status` indica liberação |
| STA-02 | [receipt v1](../schemas/candidate-v1/event-receipt.schema.json) | [receipt v2 proposta](../schemas/candidate-v2-proposed/event-receipt.schema.json) | Bloqueia `applied` em etapas de recebimento/validação e exige versão em `validity_applied/applied` |
| STA-03 | [event v1](../schemas/candidate-v1/canonical-event.schema.json) | [event v2 proposta](../schemas/candidate-v2-proposed/canonical-event.schema.json) | Exige `authorization_policy_ref` e `subject_scope_ref` não vazios para eventos de revogação, expiração de escopo ou restrição de relatório |

## 2. Compatibilidade e premissas a resolver
**STA-01:** respostas antigas de relatório liberado sem `sharing_scope_ref` não atenderão à proposta. O campo, por si só, não prova que o acesso foi autorizado. `delivery_receipt_ref` e identificação de destinatário exigem decisão posterior dos serviços canônicos.

**STA-02:** consumidores que registram `applied` para mera recepção terão de adequar seus estados. O contrato proposto ainda não comprova aplicação real de evento nem substitui log de auditoria; a tabela completa de estados depende dos proprietários de serviço.

**STA-03:** emissores de eventos afetados deverão carregar política e escopo do sujeito. `tenant_scope_ref` permanece inalterado até determinação do contexto multitenant. Não se deve exigir sujeito de todo tipo de evento sem decisão de domínio.

**Contrato envolvente:** `analysis-response-typed.schema.json` ainda aponta para `cap11-report-result.schema.json` da pasta candidate-v1. A proposta v2 não está integrada automaticamente ao registry nem à tipagem do envelope e **não deve ser tratada como válida em runtime sem integração própria posterior**.

## 3. Evidências e limite da verificação
Os três arquivos foram criados a partir da estrutura dos respectivos fontes e acrescidos de condições declarativas JSON Schema Draft 2020-12. Há confirmação de publicação no GitHub, não laudo de validação. Não foi executado Python, `jsonschema`, runner, teste sintético, instalação de dependências, ou integração externa.

Os 19 schemas do diretório `candidate-v1` continuam distintos dos 3 schemas **adicionais** da proposta; 22 arquivos em dois diretórios **não significam 22 contratos aprovados**.

## 4. Critérios para aprovação futura
1. Revisão da semântica por responsáveis técnicos de arquitetura, autorização, privacidade e serviços canônicos.
2. Avaliação de compatibilidade dos produtores/consumidores e estratégia de versão.
3. Validação estrutural e casos positivos/negativos mediante autorização **independente para Pedido B**, com executor e revisor.
4. Decisão explícita da direção sobre adoção, nunca inferida da publicação.
5. Evidências específicas e revisão antes de qualquer gate.

**Estado:** G0 parcial; G1–G6 pendentes. PND-01..16 permanecem abertas. Nenhum acesso a Replit, Neo4j, provedores, bancos ou GKR.

Referências: [GAI-INT-31](propostas-correcao-contratos-prioritarios-sta01-sta02-sta03.md) · [GAI-REV-001](relatorio-revisao-estatica-autorizada-pedido-a.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md).
