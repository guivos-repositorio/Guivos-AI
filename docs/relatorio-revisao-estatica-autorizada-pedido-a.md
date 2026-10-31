# GAI-REV-001 — Relatório de Revisão Estática Autorizada (Pedido A)
**Data:** 31/10/2026 · **Escopo:** exclusivamente arquivos públicos `guivos-repositorio/Guivos-AI` · **Snapshot GitHub:** `aad703416ca2a413f032f2d7180ef494296ee058`.
**Autorização:** declaração explícita da direção: “Autorizo o pedido A, exclusivamente para revisão estática dos arquivos públicos da Guivos AI.”
**Status:** leitura e inspeção estática concluídas; **nenhum runner executado, nenhuma dependência instalada, nenhuma integração ou gate validado**.

## 1. Evidência examinada
- Diretório `schemas/candidate-v1/`: **19 schemas** presentes, sendo 12 resultados de capacidades e 7 envelopes/contratos auxiliares.
- `tests/contracts/candidate-v1/cases.json`: **25 casos**, 11 esperados válidos e 14 esperados inválidos, IDs únicos no catálogo.
- `tests/contracts/candidate-v1/typed-cases.json`: **24 casos**, 12 esperados válidos e 12 esperados inválidos, IDs únicos no catálogo.
- Dois runners: `run_schema_cases.py` e `run_typed_cases.py`.
- Manifesto `execution-readiness-manifest.json`: `status=not_authorized`, sem commit de execução, ambiente, runs ou gate.
- Templates de pacote de evidências e revisão de gate: não preenchidos.

Os arquivos foram lidos via GitHub; não foram executados comandos Python nem validadores JSON Schema. A soma documental dos catálogos é **49 casos** (23 positivos e 26 negativos). IDs foram contados apenas dentro de cada catálogo, não comparados transversalmente.

## 2. Achados documentais
| Ref | Prioridade proposta | Evidência observável no código | Risco/decisão necessária |
| --- | --- | --- | --- |
| STA-01 | Alta | `cap11-report-result.schema.json` declara `sharing_scope_ref` em `properties`, mas não em `required`; permite `report_status=released_to_authorized_recipient` sem esse campo | Exigir prova de escopo de compartilhamento e recibo aplicável no estado de entrega, sem supor que schema substitui autorização |
| STA-02 | Alta | `event-receipt.schema.json` combina `operation` e `result` com enums independentes, sem condições entre fases | Pode representar `event_received` com `result=applied` sem prova de aplicação; criar restrição/contrato de máquina de estados e casos negativos |
| STA-03 | Alta | `canonical-event.schema.json` define `authorization_policy_ref`, mas não o exige; `subject_scope_ref` e `tenant_scope_ref` são opcionais | Definir exigências por tipo de evento e escopo, em particular revogação; campos opcionais não asseguram isolamento ou autorização |
| STA-04 | Média | `analysis-response.schema.json` aceita `claims[].additionalProperties=true` e `result` como objeto livre; `analysis-response-typed` usa `allOf` e condicionais por `capability_id` | O envelope isolado não impõe validação especializada; documentar que consumidores devem usar schema tipado nos resultados aplicáveis e controlar extensões |
| STA-05 | Média | `cap07-path-result.schema.json` não fecha `additionalProperties` no item `steps`, nem exige `minLength` para `step_ref`, `path_ref` e `possibility_ref` | Contratos de jornada podem aceitar campos imprevistos e referências vazias; decidir política e propor testes |
| STA-06 | Média | `analysis-response-typed.schema.json` impõe `result` para todos os 12 `capability_id`, mesmo com status `accepted`, `queued`, `processing` ou `failed` permitidos pelo envelope | Definir se resposta parcial/falha deve ter outro schema ou condicionar resultado à conclusão; risco de contradição entre protocolo de ciclo de vida e tipagem |
| STA-07 | Média | `run_schema_cases.py` valida schemas e usa `FormatChecker`; `run_typed_cases.py` usa registry local; ambos comparam `expected_valid` com validação e imprimem resumo | Não geram por si pacote imutável de evidências, hash/ambiente/resultado persistido, assinatura/revisão, nem cobrem autorização, semântica ou integração |
| STA-08 | Média | 25 casos gerais cobrem 11 schemas distintos; os 24 casos tipados são contra uma única resposta tipada com 12 condições | A presença de caso não prova cobertura de todas as invariantes: incluir matriz de campos obrigatórios, combinações, fronteiras, eventos/recibos e negativos de autorização |
| STA-09 | Baixa | Strings de identificação em alguns contratos não impõem formato estrito, e `format: date-time` valida formato, não ordem temporal | Requerer regras semânticas, versionamento, ordenação `occurred_at`/`recorded_at` e tratamento de relógios |
| STA-10 | Baixa | Schemas incluem `$id` absoluto e o schema tipado usa `$ref` relativos; runner tipado constrói registry local com URI base | Estratégia está documentada e tem correspondência textual de nomes, mas **resolução em runtime não foi testada**; congelar versão e executar somente mediante pedido B autorizado |

**Classificação de severidade:** hipótese para triagem pela direção e revisores técnicos, não parecer independente nem demonstração de exploração.

## 3. Limitações e critérios de conclusão
- O conteúdo é **proposta candidate-v1**, não contrato homologado.
- Não se afirma que os 49 casos passam, nem que algum falha. Não se executou Python, jsonschema ou testes.
- A leitura não valida autorização de dados reais, qualidade epistêmica, coerência de negócio, segurança operacional, Neo4j, Replit ou APIs.
- O repositório pode mudar após o snapshot indicado; revalidação deve utilizar commit fixo e artefatos versionados.
- Os achados STA-01 a STA-10 exigem decisão de correção, exceção justificada ou teste posterior com evidência.

## 4. Plano de correção proposto, sem execução
**P1:** resolver STA-01/02/03 e definir requisitos condicionais por operação/estado; incluir testes negativos candidatos de escopo de compartilhamento, recibo e eventos de revogação.

**P2:** resolver STA-04/05/06 e especificar distinção entre envelope de status e resultado concluído; avaliar compatibilidade dos consumidores.

**P3:** ampliar matriz de cobertura STA-07/08/09/10, preparar artefatos de evidência com digest, commit, ambiente e revisão independente.

Alterar schemas, fixtures ou runners depende de nova decisão de implementação/documentação; **o Pedido A concedeu revisão estática, não execução de testes ou modificação automática dos contratos**.

## 5. Conclusão
**Pedido A — revisão estática:** realizado dentro do escopo autorizado, com achados para triagem. **Pedido B:** não autorizado. **Pedido C:** não autorizado. **G0 parcial; G1–G6 pendentes. PND-01 a PND-16 não foram encerradas.**

Referências diretas: [Schemas candidatos](../schemas/candidate-v1/) · [Casos gerais](../tests/contracts/candidate-v1/cases.json) · [Casos tipados](../tests/contracts/candidate-v1/typed-cases.json) · [Runner geral](../tests/contracts/run_schema_cases.py) · [Runner tipado](../tests/contracts/run_typed_cases.py) · [Pedido A/B/C](solicitacoes-autorizacao-a-b-c.md).
