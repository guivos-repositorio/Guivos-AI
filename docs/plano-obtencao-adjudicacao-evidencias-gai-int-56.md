# GAI-INT-56 — Plano de Obtenção e Adjudicação de Evidências

**Data:** 31/10/2026 · **Estado:** plano documental candidato.  
**Fontes:** [GAI-INT-53](matriz-consolidada-bloqueadores-dependencias-gai-int-53.md), [GAI-INT-54](adendos-precedencia-historica-trilha-evidencias-gai-int-54.md), [GAI-INT-55](matriz-estruturada-evidencias-bloqueadores-gai-int-55.md), [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md).

## 1. Objetivo e limites
Definir a sequência, o tipo de evidência exigida, a forma de revisão e as condições de interrupção para os bloqueadores **BLK-D01, BLK-I01 e BLK-E05**, sem executar testes, nomear pessoas, coletar documentos privados ou conceder autorização operacional. O plano distingue **produzir uma especificação**, **obter uma evidência**, **verificar sua autenticidade** e **adjudicar um bloqueador**; nenhuma dessas etapas deve ser declarada concluída por inferência.

## 2. Ordem e dependências
| Fase | Bloqueador | Ação documental permitida agora | Dependência para obtenção futura | Evidência candidata | Critério de adjudicação |
| --- | --- | --- | --- | --- | --- |
| F1 — precedência | BLK-D01 (P2) | Revisar links e registrar notas sobre GAI-INT-34/35/38/51 e decisões posteriores sem alterar o histórico | Revisor documental competente e aceite explícito da atualização, quando exigido | Quadro de superveniência, diff editorial, SHAs e parecer | O texto histórico permanece íntegro; notas vinculadas a decisões corretas, links conferidos e revisão registrada |
| F2 — legitimidade | BLK-I01 (P0) | Preparar formulários vazios de papel, critérios de elegibilidade, segregação e aceite conforme DIR-C44-01..04 | Indicações individuais da direção, identidade institucional verificável, registrador e verificador independentes, aceites individuais | Atos específicos de designação, verificação externa, aceitações, declarações de conflito, vigência e revogação | Identidade, competência e independência demonstradas sem autodeclaração como prova suficiente |
| F3 — custódia e adjudicação | BLK-E05 (P1) | Especificar manifesto de evidências e checklist de revisão, sem emitir credenciais ou armazenar provas sensíveis em repositório público | Responsáveis e revisores competentes, ambiente/custódia aprovados, controles de assinatura, integridade e revogação | Manifesto versionado, hash real de artefatos, registros de custódia, parecer de revisão, trilha de divergências | Integridade, proveniência, controle de acesso, reprodução adequada e revisão independente comprovadas |

**Dependência central:** a fase F3 pode ser *especificada* antes de F2, mas evidências institucionais autenticadas e atos de adjudicação não podem ser considerados válidos sem a cadeia de legitimidade apropriada. BLK-D01 pode avançar documentalmente sem autorizar F2/F3.

## 3. Procedimento de adjudicação proposto
1. **Recebimento:** registrar ID do bloqueador, natureza da evidência e sua fonte; não aceitar conclusões embutidas no nome do arquivo.
2. **Integridade:** confrontar hashes, versão e origem com fonte independente; um SHA declarado pelo operador não basta.
3. **Pertinência:** verificar se a evidência prova o requisito específico, no período e no escopo delimitados.
4. **Autoridade e independência:** conferir competência de quem emitiu/revisou, segregação de funções, conflito de interesses e vigência.
5. **Contradições:** apontar fontes divergentes, versões superadas e ressalvas sem harmonização artificial.
6. **Parecer:** propor `insufficient`, `requires_correction`, `accepted_for_scope` ou `rejected`; a recomendação do revisor não substitui decisão competente.
7. **Disposição:** fechar o bloqueador somente por ato rastreável e específico. `gate_decision_ref` permanece nulo até gate independente.

**Sem coleta nesta fase:** a lista acima é especificação de processo, não afirmação de que evidências foram recebidas ou verificadas.

## 4. Requisitos mínimos por fase

### F1 — BLK-D01
- Inventariar quatro documentos históricos e as decisões/artefatos supervenientes, com links e datas.
- Diferenciar mudança de fato (arquivo candidato atualizado) de decisão normativa (GAI-DEC-012/015).
- Produzir notas editoriais anexas sem reescrever narrativa original ou alterar `candidate-v1`.
- Registro de aceite documental pendente. **Status permanece parcial_documental.**

### F2 — BLK-I01
- Aplicar a política DIR-C44-01..04 de GAI-DEC-013 sem antecipar designações.
- Campos futuros: `role_id`, `nomination_decision_ref`, `identity_verification_ref`, `independence_review_ref`, `acceptance_ref`, `effective_at`, `expires_at`, `revocation_ref`.
- Proibir preenchimento especulativo ou publicação de identificadores privados; identidade declarada em conversa não é verificação externa.
- Nenhum ROLE-REG/CUS/REV/OPS/AUD deve ser considerado ocupado por esta proposta. **Status permanece aberto.**

### F3 — BLK-E05
- Campos futuros: `evidence_id`, `blocker_id`, `artifact_sha`, `digest_algorithm`, `evidence_digest`, `custody_location_ref`, `chain_of_custody_refs`, `reviewer_ref`, `independence_ref`, `limitations`, `disposition_ref`, `gate_decision_ref`.
- Separar evidências públicas de identificadores e registros privados; o GitHub público só pode conter metadados aprovados.
- Não presumir confiança criptográfica sem âncora independente, nem segurança de ambiente por um campo booleano.
- Preparar controle de revogação, versões e preservação de contradições. **Status permanece aberto.**

## 5. Portas de decisão e proibições
**Porta D (documental):** conferência e aceite de precedência podem ser submetidos à direção sem teste.  
**Porta I (institucional):** cada nomeação e aceite exige ato específico, identidade externa e independência competente.  
**Porta E (evidências):** custódia, emissão e revisão efetivas exigem instrumentos autorizados; proposta de template não constitui implementação.  
**Portas B/C e gates:** permanecem bloqueadas; nenhuma transição acima constitui autorização de teste, inspeção operacional ou homologação.

**Condições de não início:** falta de autoridade verificável, revisão independente exigível, local de custódia apropriado, autorização delimitada ou integridade demonstrável. Não instalar ferramentas, consultar dados privados, contactar fornecedores ou executar scripts por força deste plano.

## 6. Saídas desta etapa e próxima proposta
**Saída efetiva:** ordem de tratamento F1→F2→F3 documentada, com critérios verificáveis e estados preservados. **Não saíram desta etapa:** atos de nomeação, credenciais, hashes verificados, atestações, relatórios de teste, decisões de fechamento ou evidências institucionais.

**GAI-INT-57 (candidato):** preparar somente os formulários documentais vazios de aceitação/parecer para BLK-D01, BLK-I01 e BLK-E05, preservando requisitos de privacidade e sem dar início às atividades restritas.

## 7. Estado inalterado
**15 bloqueadores:** 7 P0, 7 P1, 1 P2; nenhum declarado resolvido por este plano. **82 casos catalogados, zero execuções verificadas. Pedido A concluído; B e C não autorizados. COMP-04-P aprovado em princípio e inativo. G0 parcial; G1–G6 pendentes; PND-01–16 abertas.** Nenhum contrato foi homologado, nenhuma credencial emitida e nenhum gate aprovado.
