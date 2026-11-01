# GAI-INT-58 — Roteiro de Revisão de Completude e Segregação dos Instrumentos

**Data:** 31/10/2026 · **Estado:** roteiro documental candidato; sem revisão institucional realizada, aceite ou homologação.  
**Referência:** [GAI-INT-57](gai-int-57-instrumentos-aceite-parecer.md) e [GAI-INT-56](plano-obtencao-adjudicacao-evidencias-gai-int-56.md).

## 1. Escopo
Estabelecer critérios para futura revisão dos três formulários GAI-INT-57, preservando a separação entre **completude estrutural de modelo vazio**, **preenchimento futuro por autoridade competente**, **verificação de evidências**, **parecer** e **decisão de encerramento**. Este roteiro não certifica que uma verificação independente ocorreu.

## 2. Critérios transversais e critérios impeditivos

| ID | Critério | Evidência documental exigível no futuro | Resultado nesta publicação |
| --- | --- | --- | --- |
| REV58-T01 | Identificador do bloqueador e referência de formulário inequívocos | Código BLK, versão e localização do registro | Modelo documental identificável |
| REV58-T02 | Campos obrigatórios e condicionais distinguíveis | Especificação dos campos, null/pendente quando não há evento | Desenho publicado; preenchimento ausente |
| REV58-T03 | Separação entre proponente, emissor, verificador, revisor e decisor | Matriz de incompatibilidades e aceites | Segregação proposta; pessoas não designadas |
| REV58-T04 | Cadeia de integridade e temporalidade verificável | SHA/digest conferidos, fontes independentes, vigência/revogação | Sem conferência independente |
| REV58-T05 | Confidencialidade e controle de localização | Referência privada sem conteúdo sensível no GitHub público | Restrição documentada; custódia não implantada |
| REV58-T06 | Contradições, limitações, exceções e motivo do parecer | Registro específico e revisão de divergências | Nenhum parecer produzido |
| REV58-T07 | Gate separado de encerramento de bloqueador | `closure_decision_ref` e `gate_decision_ref` independentes | Ambos nulos nos modelos |
| REV58-T08 | Precedência documental e histórico preservado | Referências de decisão superveniente, diff e aceite editorial | Adendo disponível; aceite pendente |

**Impedimentos à emissão futura de parecer favorável:** identidade não verificada; ausência de competência; conflito de funções; evidência autodeclarada sem verificação independente; versão ou SHA incompatível; dados sensíveis em repositório público; conclusão sem escopo; alegação de execução sem autorização; gate inferido.

## 3. Revisão específica por formulário

### F1 — BLK-D01: precedência documental
**Instrumento:** [GAI-INT-57/F1](gai-int-57-formulario-revisao-blk-d01.md).  
Verificar que o formulário suporta uma linha por documento histórico, identificação de decisão superveniente, preservação do original, hash de cada versão, divergência e revisão independente quando aplicável. Para o conjunto GAI-INT-34/35/38/51, o formulário prevê os campos essenciais de revisão, mas não contém verificações realizadas. **Critério pendente:** esclarecer registro de aceite editorial e forma de registrar múltiplos documentos sem ambiguidade. Não encerrar BLK-D01.

### F2 — BLK-I01: indicação e aceite institucional
**Instrumento:** [GAI-INT-57/F2](gai-int-57-formulario-aceite-blk-i01.md).  
Verificar cobertura de DIR-C44-01..04: elegibilidade/identidade, independência/incompatibilidades, indicação e aceite individual, suspensão/substituição. O modelo contém referências separadas de nomeação, aceite e revisão. **Critérios pendentes:** autoridade verificável para o ato, matriz de incompatibilidades aprovada e mecanismo privado de preservação de comprovantes; não presumir que um campo `role_id` preenchido nomeia titular.

### F3 — BLK-E05: evidência e custódia
**Instrumento:** [GAI-INT-57/F3](gai-int-57-formulario-parecer-blk-e05.md).  
Verificar proveniência, artefato, digest, cadeia de custódia, segregação de revisor, limites, contradições, revogação e disposição. O modelo prevê campos centrais. **Critérios pendentes:** política de retenção, verificação de hash por referência independente, critérios de confiança e trilha de adjudicação segura; nenhum parecer real foi produzido.

## 4. Modelo de resultado de revisão futura
**Classificações candidatas:** `complete_for_documentary_design`, `requires_documentary_changes`, `cannot_be_assessed`, `rejected`. Nunca usar `approved_for_execution` como saída deste roteiro.  
Campos futuros: `review_id`, `form_id`, `form_blob_sha`, `criteria_evaluations`, `findings`, `missing_requirements`, `reviewer_identity_ref`, `independence_ref`, `decision_scope_ref`, `limitations`, `review_disposition`, `closure_decision_ref=null`, `gate_decision_ref=null`.

O conteúdo desta publicação é uma **análise preliminar de desenho por leitura**, e não um formulário preenchido de avaliação ou uma aceitação institucional.

## 5. Encaminhamento e ordem de tratamento
1. Preparar adendos específicos para as lacunas identificadas nos três formulários, **sem preencher dados pessoais nem alterar decisões históricas**.
2. Submeter o pacote documental à futura revisão por funções institucionalmente habilitadas, conforme GAI-DEC-013.
3. Distinguir claramente a revisão de template do uso real do template, que depende de autorização, custódia e aceites próprios.
4. Atualizar BLK-D01/I01/E05 apenas após decisões de encerramento específicas e comprovadas.

## 6. Limites e estado preservado
Pedidos B e C **não autorizados**; COMP-04-P **condicionado e inativo**; **82 casos sintéticos catalogados e nenhuma execução verificada**; **15 bloqueadores**, dos quais **7 P0, 7 P1 e 1 P2**, sem encerramento por este roteiro; **G0 parcial, G1–G6 pendentes, PND-01..16 abertas**. Não foram executados scripts, validações JSON Schema, consultas a sistemas privados, testes, inspeções, nomeações, credenciais ou gates.

**Próximo encaminhamento candidato — GAI-INT-59:** adendos documentais dos três formulários para os requisitos faltantes, preservando as versões originais e sem uso operacional.
