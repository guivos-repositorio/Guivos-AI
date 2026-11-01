# GAI-INT-55 — Matriz Estruturada de Evidências por Bloqueador

**Data:** 31/10/2026 · **Natureza:** inventário documental candidato, sem execução ou homologação.  
**Bases:** [GAI-INT-53](matriz-consolidada-bloqueadores-dependencias-gai-int-53.md) e [GAI-INT-54](adendos-precedencia-historica-trilha-evidencias-gai-int-54.md).

## 1. Objetivo
Vincular os **15 bloqueadores** a documentos identificáveis e a evidências **ainda necessárias**, preservando a distinção entre prova documental existente, proposta de solução e verificação independente. **Referência a documento não comprova eficácia de controle.** Responsabilidades abaixo são **funções candidatas não designadas**, salvo formalização específica superveniente.

## 2. Matriz rastreável

| Bloqueador | Classe | Documentação de referência (não prova de resolução) | Evidência ausente / dependência | Função candidata | Critério de encerramento | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| BLK-C01 | P1 | GAI-INT-31/32; cap11-report-result v2 | Decisão de política/escopo e validade operacional; validação independente | Produto; identidade/privacidade | Semântica ratificada; evidência de autorização válida e avaliação de compatibilidade | parcial |
| BLK-C02 | P1 | GAI-INT-31/32; event-receipt v2 | Prova de efeito/persistência e compatibilidade de consumidores | Arquitetura; serviços de eventos | Tabela de transições ratificada, auditoria e validação autorizada | parcial |
| BLK-C03 | P1 | GAI-INT-31/32; canonical-event v2 | Prova de revogação efetiva; semântica de sujeito e tenant | Identidade; serviços canônicos | Políticas ratificadas, efeito verificável e revisão | parcial |
| BLK-C04 | P1 | GAI-INT-33/34/36; GAI-DEC-012; schemas v2 | Registry congelado, inventário de consumidores, migração e compatibilidade demonstrada | Arquitetura de contratos | Resolução de referências e evidências de integração autorizadas | aberto |
| BLK-C05 | P1 | GAI-DEC-012; GAI-INT-36 | Contrato B1 de erro separado e correlação segura | Produto; arquitetura; segurança | Especificação revisada e compatibilidade avaliada | aberto |
| BLK-E01 | P0 | GAI-REV-002 REV2-01; GAI-INT-40/41 | Vínculo institucional de emissor/chave, verificador e revogação confiáveis | Direção; registrador; segurança | Cadeia de confiança aprovada e verificada independentemente | aberto_bloqueado |
| BLK-E02 | P0 | GAI-REV-002 REV2-02/05/11; GAI-INT-40 | Manifesto congelado e conferência real de SHA/hashes de entradas e registry | Arquitetura; operador | Atestação de integridade independente | parcial |
| BLK-E03 | P0 | GAI-REV-002 REV2-03/04; GAI-INT-37/40 | Dependências imutáveis e sandbox sem rede/segredos, com atestação externa | Segurança; operação | Lockfile verificado e isolamento demonstrado sob autorização | aberto |
| BLK-E04 | P1 | GAI-REV-002 REV2-06/07/08/10; GAI-INT-40 | Revisão de fragmentos, fixtures, falhas e saída atômica | Engenharia; revisor | Correções e revisão técnica independente | parcial |
| BLK-E05 | P1 | GAI-REV-002 REV2-09; GAI-INT-54 | Digest/assinatura, custódia, registro imutável e adjudicação | Custódia; revisão | Pacote de evidências verificável, com parecer separado | aberto |
| BLK-I01 | P0 | GAI-DEC-011/013; GAI-INT-42/45 | Nomeações, aceites e prova institucional independente | Direção; registrador | Atos e aceites verificáveis; segregação demonstrada | aberto |
| BLK-I02 | P0 | GAI-DEC-011; GAI-INT-41; GAI-INT-53 | Autorização individualizada B/C; limites, revogação e prova da autoridade | Direção; verificador | Concessão específica independente, com controle de validade | nao_autorizado |
| BLK-I03 | P0 | GAI-DEC-015; GAI-INT-50/51 | Cinco condições suspensivas e ato de ativação | Direção; operador; revisor | Identidade/aceite, fontes, prazo, custódia/revisão, ato expresso | condicionado_inativo |
| BLK-G01 | P0 | GAI-INT-14; GAI-INT-53; registro-decisoes | Ratif. funções, fechamento de PNDs e parecer próprio por gate | Direção; autoridades de gate | Evidências adjudicadas e decisão individual de gate | aberto |
| BLK-D01 | P2 | GAI-INT-52/54; GAI-INT-34/35/38/51 | Revisão editorial/links e aceite competente sem reescrita histórica | Governança documental | Adendos conferidos, links e aceite documental | parcial_documental |

**Conferência de categorias:** 7 P0, 7 P1 e 1 P2; 15 bloqueadores no total. Os estados `parcial` e `parcial_documental` não significam encerramento. Para todos os registros, `closure_decision_ref=null` e `gate_decision_ref=null`.

## 3. Modelo de registro de evidência (não preenchido)
Campos candidatos: `blocker_id`, `source_document_refs`, `decision_ref`, `decision_scope`, `artifact_ref`, `artifact_commit_sha`, `artifact_digest`, `evidence_kind`, `evidence_ref`, `evidence_digest`, `issuer_role_ref`, `issuer_identity_verification_ref`, `reviewer_ref`, `independence_attestation_ref`, `observed_at`, `effective_at`, `expires_at`, `limitations`, `contradiction_refs`, `disposition`, `disposition_ref`, `gate_decision_ref`.

**Campos sem evidência permanecem nulos ou ausentes; nunca inserir valores fictícios para simular fechamento.** Identificadores individuais, credenciais, segredos e material sensível não devem ser expostos no repositório público. O presente documento não institui sistema de custódia.

## 4. Regras de verificação futura
1. Conferir se a evidência é pertinente ao bloqueador e ao **escopo aprovado**, com integridade e origem confiáveis.
2. Separar revisão documental de teste de validação, inspeção operacional e homologação.
3. Exigir operador/revisor institucionalmente competentes e independentes quando aplicável; não presumir atribuição a partir do nome de uma função.
4. Registrar contradições e expiração/revogação, e impedir que versões superadas sejam tomadas como atuais.
5. Encerrar somente por decisão explícita e revisada, preservando trilha de auditoria; nenhum fechamento implica aprovação automática de gates.

## 5. Próxima priorização documental
**GAI-INT-56 (candidato):** plano de obtenção e adjudicação de evidências, começando por BLK-D01, BLK-I01 e BLK-E05, com dependências e ordem de aprovação, **sem nomear titulares nem coletar dados privados**. Qualquer autorização de execução, inspeção, pesquisa COMP-04-P ou ativação exige ato separado.

## 6. Restrições
**Pedido A concluído** segundo registros anteriores. **B/C não autorizados. COMP-04-P condicionado e inativo. 82 casos catalogados sem execução verificada. G0 parcial; G1–G6 pendentes; PND-01..16 abertas.** Esta matriz não altera schemas, runners, ambientes, chaves, decisões ou gates.
