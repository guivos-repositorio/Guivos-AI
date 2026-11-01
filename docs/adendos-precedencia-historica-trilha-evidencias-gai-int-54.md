# GAI-INT-54 — Adendos de Precedência Histórica e Trilha de Evidências

**Data:** 31/10/2026 · **Natureza:** adendo documental de rastreabilidade, sem alteração retroativa de decisões.  
**Base:** [GAI-INT-52](reconciliacao-estatica-estado-v83-gai-int-52.md) e [GAI-INT-53](matriz-consolidada-bloqueadores-dependencias-gai-int-53.md).  
**Estado:** publicação de orientação editorial e modelo de evidências; não constitui testes, homologação, autorização operacional ou gate.

## 1. Regra de precedência

A leitura do repositório deve preservar a redação histórica dos documentos, mas identificar explicitamente decisões e artefatos supervenientes. **Decisão posterior expressamente aprovada prevalece dentro de seu escopo; proposta técnica posterior não converte hipótese em regra normativa.** Divergências entre relato documental e conteúdo de arquivo são indicadas como pontos de reconciliação, não prova de execução.

## 2. Adendos de precedência (sem reescrever documentos históricos)

| Documento original | Formulação histórica | Precedência ou estado posterior | Interpretação correta |
| --- | --- | --- | --- |
| [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md) | Envelope v2 inicialmente referia base candidate-v1, com `api_contract_version=candidate-1`; A/B/C ainda em avaliação | [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md) aprova A1+B1+C1 para desenho; schemas posteriores `analysis-response.schema.json` e `analysis-response-typed.schema.json` candidatos referenciam base `candidate-2` | Priorizar a decisão e os arquivos candidatos atuais para descrição do desenho; nenhum contrato homologado |
| [GAI-INT-35](deliberacao-compatibilidade-versionamento-envelope-v2.md) | A1/B1/C1 eram alternativas não selecionadas | GAI-DEC-012 registra escolha expressa | A minuta permanece histórica; não caracterizar as opções como ainda não decididas, nem como autorizadas para execução |
| [GAI-INT-38](especificacao-executor-offline-33-casos-v2.md) | Executor v2 não implementado quando da especificação | [GAI-INT-39](implementacao-executor-offline-v2-nao-executado.md) registra implementação candidata; [GAI-REV-002](revisao-estatica-executor-offline-v2-rev002.md) aponta 11 achados; [GAI-INT-40](endurecimento-executor-v2-candidato-bloqueado.md) publica variante bloqueada | Existe código candidato, não executor validado/autorizado; mitigação parcial não encerra os 11 achados |
| [GAI-INT-51](instrumento-deliberacao-comp04-p-pesquisa-publica.md) | Pesquisa COMP-04-P sem decisão emitida | [GAI-DEC-015](decisao-aprovacao-condicionada-comp04-p-gai-dec-015.md) aprova somente em princípio, sujeita a cinco condições suspensivas | Estado atual: `operational_authorization=false`; nenhuma consulta COMP-04-P autorizada |

**Regra editorial:** manter conteúdo original e incluir, em futuras revisões documentais separadas, nota de superveniência com link, data, escopo e ressalvas. Nunca alterar retrospectivamente datas, decisões ou relatos de não execução.

## 3. Esquema lógico da trilha de evidências (proposto, não implantado)

Para cada bloqueador `BLK-*`, registrar os campos abaixo em artefato privado/institucional adequado quando autorizado:

| Campo | Obrigatoriedade proposta | Semântica |
| --- | --- | --- |
| `blocker_id` | Obrigatório | ID de GAI-INT-53, sem ambiguidade |
| `decision_ref`, `decision_scope` | Obrigatório para fechamento | Decisão explícita com escopo, não concordância inferida |
| `artifact_ref`, `artifact_commit_sha`, `artifact_digest` | Obrigatório quando há artefato | Identificação imutável, integridade e localização |
| `evidence_kind`, `evidence_ref`, `evidence_digest` | Obrigatório para fechamento | Prova específica e verificável, não texto promocional |
| `issuer_role_ref`, `issuer_identity_verification_ref` | Conforme natureza do ato | Papel e vínculo institucional verificados fora do próprio JSON |
| `reviewer_ref`, `independence_attestation_ref` | Onde exigir revisão | Separação comprovada entre execução e julgamento |
| `observed_at`, `effective_at`, `expires_at` | Conforme evento | Distinguir observação, vigência e revogação |
| `limitations`, `contradiction_refs` | Obrigatório | Ausências, ressalvas e incompatibilidades |
| `disposition`, `disposition_ref` | Obrigatório para encerramento | Decisão formal: permanecer aberto, parcialmente mitigado, resolvido ou rejeitado |
| `gate_decision_ref` | Nulo até gate separado | Encerramento de bloqueador não aprova G0–G6 |

**Estados de evidência propostos:** `not_collected`, `documented_unverified`, `under_independent_review`, `accepted_for_specific_scope`, `rejected`, `superseded`, `revoked`. Eles não são equivalentes a status de gate.

## 4. Critérios negativos de encerramento
Não é prova suficiente: (i) publicação em GitHub; (ii) `approved=true` preenchido pelo operador; (iii) SHA informado pelo próprio interessado sem verificação independente; (iv) fixture com expectativa positiva; (v) runner criado ou bloqueado; (vi) assinatura sem identidade e âncora confiável; (vii) declaração de isolamento sem barreira externa; (viii) aprovação em princípio de COMP-04-P. A ausência de prova mantém o bloqueador aberto ou parcial.

## 5. Trilha de revisão por dimensão
- **Contratos BLK-C01–C05:** decisão de semântica, diff versionado, inventário de produtores/consumidores, referências, avaliação de compatibilidade e evidência de verificação futura devidamente autorizada.
- **Executor/evidências BLK-E01–E05:** cadeia de confiança institucional, manifestos congelados, hashes efetivamente comparados, isolamento atestado, resultados de revisão e pacote de evidências íntegro. Nenhuma dessas verificações é declarada realizada por este documento.
- **Institucional BLK-I01–I03:** nomeação/aceite verificáveis, condições e atos separados, prazo, revogação, custódia e independência; COMP-04-P permanece inativo.
- **Gates BLK-G01:** critérios e parecer próprios por gate, com decisão expressa; G0 parcial e G1–G6 pendentes.
- **Documentação BLK-D01:** esta matriz de precedência fornece referência para futura revisão editorial, mas **não encerra automaticamente BLK-D01** sem conferência de links e aceite documental competente.

## 6. Pendências e próxima recomendação
1. Preparar tabela estruturada de evidências candidatas por bloqueador, **sem inventar SHA, operadores, documentos privados ou resultados**.
2. Revisar institucionalmente a precedência GAI-INT-34/35/38/51 e definir quando adendos locais devem ser inseridos, preservando texto original.
3. Avaliar modelo de fechamento e segregação de assinaturas por responsáveis ainda a designar.
4. Não executar quaisquer testes ou consultas sob rótulo de documentação.

## 7. Limites expressos
**Pedido A:** concluído segundo registro. **Pedidos B/C:** não autorizados. **COMP-04-P:** aprovado em princípio, inativo, cinco condições suspensivas pendentes. **Casos:** 82 catalogados, zero execuções verificadas. **G0:** parcial; **G1–G6:** pendentes; **PND-01 a PND-16:** abertas. Nenhum gate é aprovado, nenhuma credencial emitida e nenhum serviço operacional alterado.

Referências complementares: [GAI-INT-41](cadeia-confianca-autorizacoes-execucao-candidata.md) · [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md) · [GAI-DEC-015](decisao-aprovacao-condicionada-comp04-p-gai-dec-015.md).
