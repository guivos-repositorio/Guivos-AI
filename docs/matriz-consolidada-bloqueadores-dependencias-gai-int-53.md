# GAI-INT-53 — Matriz Consolidada de Bloqueadores e Dependências de Liberação

**Data:** 31/10/2026 · **Base:** [GAI-INT-52](reconciliacao-estatica-estado-v83-gai-int-52.md), Documento Mestre v8.3 e decisões vigentes.  
**Natureza:** planejamento e revisão documental, sem autorização para execução, implementação operacional, homologação ou gates.

## 1. Critérios de classificação
**P0 (impeditivo):** ausência impede iniciar a atividade regulada (execução B, inspeção C, pesquisa COMP-04-P ou gate). **P1 (alto):** incompatibilidade ou evidência essencial ainda não resolvida para adoção. **P2 (documental):** rastreabilidade histórica e clareza, sem criar permissão operacional.  
Status: **aberto** = sem evidência de encerramento; **parcial** = solução candidata preparada, sem validação independente; **condicionado/inativo** = política aprovada em princípio, mas não ativada. Responsáveis indicados por função são **candidatos**, não nomeações.

## 2. Matriz de bloqueadores
| ID | Prioridade | Dimensão | Bloqueador e impacto | Dependência | Responsabilidade candidata | Evidência necessária para encerramento | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BLK-C01 | P1 | Contratos | STA-01: referência de compartilhamento não comprova autorização vigente; risco de liberação indevida | Serviço canônico de autorização, semântica de escopo/entrega | Produto + identidade/privacidade | Decisão semântica, contrato versionado e evidência de validação autorizada | Parcial |
| BLK-C02 | P1 | Contratos | STA-02: estado `applied` não comprova persistência; consumidores podem usar semântica anterior | Proprietários de emissor/consumidor e auditoria | Arquitetura + serviços de eventos | Tabela de estados ratificada, migração e evidência de efeito | Parcial |
| BLK-C03 | P1 | Contratos | STA-03: escopos de eventos de revogação não demonstram invalidação efetiva | Autoridade de políticas, sujeito, tenant e consumidores | Identidade + serviços canônicos | Matriz de eventos, referências válidas, provas de aplicação e revisão | Parcial |
| BLK-C04 | P1 | Contratos | Envelope candidate-2 e payloads v1/v2 coexistem sem compatibilidade operacional demonstrada | Registry local versionado, negociação de versão, inventário de consumidores | Arquitetura de contratos | Inventário, rastreabilidade dos `$ref`, plano de migração e validação autorizada | Aberto |
| BLK-C05 | P1 | Contratos | Política B1 prevê erros correlacionados, mas contrato candidate-2 de erro ainda não está definido | Especificação de request_id, falhas seguras e consumidores | Produto + arquitetura + segurança | Contrato separado revisado e critérios de compatibilidade | Aberto |
| BLK-E01 | P0 | Executor | REV2-01: arquivo de autorização autodeclarado não é autoridade confiável | Âncora e vínculo institucional, assinatura/revogação, verificador independente | Direção + registrador + segurança | Cadeia de confiança aprovada e demonstrada em revisão autorizada | Aberto; variante bloqueada |
| BLK-E02 | P0 | Executor | REV2-02/05/11: commit, entradas e registry sem comparação integral com manifesto congelado | Repositório/artefatos fixados, allowlist e hashes | Arquitetura + operador futuro | Manifesto imutável, verificação real e revisão independente | Parcial |
| BLK-E03 | P0 | Executor | REV2-03/04: dependências e isolamento sem prova técnica; risco de rede/Secrets | Lockfile com hashes, sandbox externa, controle de ambiente | Segurança + operação | Ambiente offline atestado e integridade efetiva, sob autorização específica | Aberto |
| BLK-E04 | P1 | Executor | REV2-06/07/08/10: fragmentos, origem sintética, erros e saída de evidência insuficientes | Parser de registry, política de fixtures, I/O seguro | Engenharia + revisor independente | Correções revisadas e evidência futura autorizada | Parcial |
| BLK-E05 | P1 | Evidências | REV2-09: digest, assinatura e adjudicação do pacote de resultados incompletos | Custódia segura, revisor e registro imutável | Governança de evidência + revisão | Manifesto de evidência, atestação, segregação e parecer | Aberto |
| BLK-I01 | P0 | Institucional | Identidade, nomeação, aceite e independência não formalizados para papéis críticos | GAI-DEC-011/013; PND-01 e PND-11 e demais competências | Direção e registrador a designar | Ato de designação, aceite verificável e matriz de segregação | Aberto |
| BLK-I02 | P0 | Autorizações | Pedido B/C sem concessão específica executável; risco de confundir concordância documental com permissão | BLK-I01, cadeia de confiança e delimitadores de escopo | Direção + verificador independente | Decisão explícita separada, válida, verificável e revogável | Não autorizado |
| BLK-I03 | P0 | Custódia | COMP-04-P com cinco condições suspensivas não satisfeitas; pesquisa deve permanecer bloqueada | Operador, fontes, prazo, evidências/revisão, ato de ativação | Direção + revisor institucional | Registro das cinco condições e autorização de ativação individualizada | Condicionado/inativo |
| BLK-G01 | P0 | Gates | G0 parcial, G1–G6 pendentes, PND-01..16 abertas; sem base para homologação | Responsáveis, avaliações, evidências e decisões por gate | Direção + autoridades de gate a ratificar | Atas específicas, evidências auditáveis e decisão independente por gate | Aberto |
| BLK-D01 | P2 | Documentação | Documentos GAI-INT-34/35/38/51 contêm descrições históricas superadas por decisões posteriores | Adendos editoriais com referências de precedência | Governança documental | Notas de superveniência, histórico preservado, revisão de links | Aberto |

## 3. Ordem recomendada de trabalho (não autorização)
**Trilha documental imediata:** (1) notas de precedência histórica BLK-D01; (2) matriz de responsáveis/competências sem nomeações automáticas BLK-I01; (3) critérios de evidência e fechamento BLK-E05; (4) especificação dos contratos e riscos C01–C05.  
**Trilha institucional condicionada:** resolver a identidade/autoridade, segregação e cadeia de confiança I01/E01 antes de discutir concessão B; preparar os cinco campos COMP-04-P sem pesquisar fornecedores ou ativar a autorização.  
**Trilha técnica posterior:** qualquer alteração de runner, validação, uso de sandbox, inspeção de sistemas ou campanha sintética demanda deliberação própria, com revisão, congelamento de SHA e limites explícitos.

## 4. Critério de fechamento de bloqueador
Um bloqueador só pode passar a **resolvido** com: identificador e escopo da decisão; responsável formalmente competente; artefato versionado com SHA; evidência pertinente e verificável; parecer de revisão independente quando aplicável; confirmação de não ampliação de autoridade; atualização documental. **Publicação de proposta ou afirmação de conformidade não é prova de fechamento.** Não encerrar pendências institucionais ou gates por inferência.

## 5. Fronteiras preservadas
**82 casos catalogados** (49 v1 e 33 v2), **zero execuções verificadas**. **Pedido A concluído** conforme registro; **B/C não autorizados**. **COMP-04-P aprovado em princípio, inativo**; C/I não concedidos. **G0 parcial; G1–G6 pendentes; PND-01–16 abertas**. Nenhuma nomeação, pesquisa de fornecedor, consulta COMP-04-P, teste, instalação, inspeção, implantação, uso de segredo ou decisão de gate decorre deste documento.

## 6. Próximo encaminhamento candidato
**GAI-INT-54 — Adendos de precedência histórica e trilha de evidências**, sem alterar decisões originais. Exige encaminhamento documental separado; não implica início de testes.

Referências: [GAI-INT-52](reconciliacao-estatica-estado-v83-gai-int-52.md) · [GAI-REV-002](revisao-estatica-executor-offline-v2-rev002.md) · [GAI-INT-40](endurecimento-executor-v2-candidato-bloqueado.md) · [GAI-INT-41](cadeia-confianca-autorizacoes-execucao-candidata.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md) · [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md) · [GAI-DEC-015](decisao-aprovacao-condicionada-comp04-p-gai-dec-015.md).
