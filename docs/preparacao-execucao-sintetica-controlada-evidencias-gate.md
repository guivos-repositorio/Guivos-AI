# GAI-INT-15 — Plano de Preparação para Execução Sintética Controlada e Evidências de Gate
**Versão documental 3.9 · 31/10/2026**
**Estado:** preparação documental e modelo de manifesto, sem autorização de execução, runs, adjudicações ou gates aprovados.

## 1. Finalidade e limites
Definir como uma eventual campanha de avaliação sintética deve ser autorizada, isolada, reproduzida, auditada, revisada e submetida às autoridades responsáveis pelos gates G0–G6. A publicação deste documento **não é autorização para executar testes**, instalar dependências ou acessar Replit, Neo4j, modelos externos, dados reais, GKR ou ambientes operacionais.

O escopo inicial candidato contém os **19 JSON Schemas candidate-v1**, **49 fixtures sintéticas** (25 básicas + 24 tipadas) e **dois executores offline já documentados**. Não se presume que essas ferramentas estejam validadas, que executem sem falhas ou que suas fixtures cubram riscos de negócio, privacidade e IA.

## 2. Pré-condições para solicitação de execução
Antes de qualquer run, exigir:
1. **Responsável técnico e autoridade de autorização formalmente designados**, com registro da alçada.
2. **Escopo limitado**: repositório, commit, schemas, fixtures, runner, objetivo, riscos, duração, custo e restrições.
3. **Ambiente isolado** com conta/permissões mínimas, sem acesso a bases canônicas ou dados da Pessoa.
4. **Dados exclusivamente sintéticos e revisados**; não reproduzir documentos, prompts privados, segredos ou dados de usuários.
5. **Dependências aprovadas** e versões fixadas, com fonte confiável e revisão de cadeia de suprimentos.
6. **Política de saída/logs** sem conteúdo sensível, com retenção e acesso definidos.
7. **Critérios de parada** e política de resposta a anomalias, incluindo falhas de integridade e exposição indevida.
8. **Identificadores e checksums** de todos os artefatos congelados para a campanha.
9. **Critérios de aceite/reprovação definidos antes do run**, inclusive negativas esperadas e inconclusivos.
10. **Revisores e decisor de gate separados** de quem simplesmente executa os testes, sempre que aplicável.

Se alguma pré-condição crítica não estiver satisfeita, o estado deverá ser `blocked` ou `not_authorized`, e não `ready`.

## 3. Matriz de ambientes e proibições
| Ambiente candidato | Admissível na primeira campanha? | Condições |
| --- | --- | --- |
| Ambiente local/CI isolado de validação estrutural | Somente após autorização formal | Fixtures sintéticas, runner fixado, sem rede por padrão |
| Sandbox de integração com serviços falsos (mocks) | Etapa futura separada | Contratos e segurança revisados, fixtures próprias |
| Replit da Jornada da Pessoa | **Não** | Exige avaliação e autorização específica de inspeção/integração |
| Neo4j operacional ou com dados da Pessoa | **Não** | Requer política, autorização e controles de dados |
| OpenAI, Claude, Gemini reais | **Não** | Execução externa e custo não autorizados nesta etapa |
| API/parceiro B2B ou produção | **Não** | Depende de gates, privacidade e autorização de liberação |
| GKR | **Não alterar** | Governança independente; apenas referência conceitual controlada |

## 4. Pacote de campanha e congelamento
O pacote candidato deverá conter `campaign_ref`, `authorization_decision_ref`, `scope_ref`, `repository_commit_sha`, `schema_file_digests[]`, `fixture_file_digests[]`, `runner_file_digests[]`, `dependency_lock_ref`, `environment_spec_ref`, `approved_execution_window`, `maximum_budget`, `reviewer_roles[]`, `stop_conditions[]` e `retention_policy_ref`.

Um commit isolado **não** fixa ambiente de execução nem dependências; registrar ambos. Mudança em qualquer parte relevante exige nova versão ou nova campanha, sem reescrever evidências históricas.

## 5. Modelo de manifesto — não executado
O arquivo [manifesto candidato](../tests/contracts/candidate-v1/execution-readiness-manifest.json) apresenta um registro com status `not_authorized`, referências a suites e campos nulos para commits, autorização, ambiente e evidências ainda não determinadas.

**Não preencher com valores de execução inventados.** O catálogo de fixtures não representa saída observada; resultados `passed`, `failed` e `inconclusive` somente após run real.

## 6. Máquina de estados da campanha
```text
draft
  → awaiting_authorization
  → authorized_for_scoped_run
  → environment_prepared
  → execution_started
  → execution_completed | execution_failed | execution_aborted
  → evidence_collected
  → under_review
  → adjudicated
  → gate_decision_recorded
```
Transições alternativas: `not_authorized`, `blocked`, `cancelled`, `expired_authorization`. Nem `execution_completed` nem `evidence_collected` constituem aprovação de gate. A autorização deve corresponder à execução exata e estar válida no momento do disparo.

## 7. Procedimento técnico futuro, condicionado
1. Registrar e validar autorização formal da campanha.
2. Reconstituir cópia imutável/identificada dos arquivos aprovados e comparar checksums.
3. Isolar ambiente, proibir credenciais de produção e bloquear comunicação externa não necessária.
4. Fixar versões de Python, `jsonschema`, `referencing` e suas dependências transitivas.
5. Verificar confiabilidade e integridade dos dois executores **antes** do primeiro uso.
6. Executar separadamente os casos de `cases.json` e `typed-cases.json`, sem transformar casos não executados em `pass`.
7. Capturar código de saída, comparação esperado/observado, erros de validação não sensíveis e versões.
8. Registrar tentativas e retestes por `run_id` independente; falhas nunca desaparecem da trilha.
9. Revisar cobertura, falsos positivos/negativos e limitações; impedir que sucesso estrutural seja considerado prova semântica.
10. Emitir relatório de evidências; obter adjudicação e decisão formal de gate **em processos distintos**.

Os comandos `python tests/contracts/run_schema_cases.py` e `python tests/contracts/run_typed_cases.py` são **referências a executores candidatos**, não instrução para execução automática desta etapa.

## 8. Contrato do resultado observado
| Campo mínimo | Uso |
| --- | --- |
| `run_id`, `campaign_ref`, `executed_at` | Identificação da execução |
| `authorized_scope_ref`, `authorization_checked_at` | Escopo efetivamente autorizado |
| `repository_commit_sha`, `artifacts_sha256[]` | Rastreabilidade e integridade |
| `environment_fingerprint`, `dependency_versions` | Reprodutibilidade |
| `suite_ref`, `case_id`, `expected_valid`, `observed_valid` | Comparação por caso |
| `comparison_status` | `pass`, `fail`, `inconclusive`, `not_run` |
| `error_paths[]`, `runner_exit_code`, `limitations[]` | Diagnóstico sem conteúdo sensível |
| `review_ref`, `adjudication_ref`, `gate_decision_ref` | Separação entre execução e decisão |

A preservação de logs deve respeitar minimização e política aprovada; hashes não substituem autorização. Não publicar evidência confidencial em GitHub público.

## 9. Pontos de controle específicos
| Controle | Verificação requerida | Bloqueio |
| --- | --- | --- |
| Segurança do ambiente | Sem secrets nem rede externa indevida | Não executar |
| Origem das fixtures | Sintéticas e revisadas | Isolar/remover caso indevido |
| Schema/runner | Arquivos congelados e íntegros | Invalidar run divergente |
| Dependências | Versões e origem revisadas | Não executar |
| Negativos esperados | Rejeições avaliadas como sucesso **apenas se rejeitadas corretamente** | Abrir defeito |
| Referências `$ref` | Registry local e resolução consistente | Caso inconclusivo ou defeito |
| `FormatChecker` | Perfil temporal e comportamento conhecido | Registrar limitação |
| Semântica e autorização | Não simuladas como prova real | Manter G2 pendente |
| Revisão humana | Independência e autoridade documentadas | Não adjudicar |
| Evidência | Registro verificável e retenção definida | Não solicitar gate |

## 10. Severidade e interrupção propostas
- **S0 — crítico:** risco de exposição de dados, elevação de acesso, uso de credencial proibida, revogação ignorada ou evidência forjada; interromper, preservar evidência mínima e seguir resposta a incidentes aplicável.
- **S1 — alto:** schema incompatível em operação essencial, divergência de validade, cobertura crítica incompleta; bloquear aprovação do escopo.
- **S2 — moderado:** falha delimitada e recuperável sem dados pessoais; abrir defeito e retestar.
- **S3 — baixo:** inconsistência editorial sem alteração contratual; corrigir com registro.

As classes são propostas; não relatam falhas observadas. Nenhum gatilho foi testado.

## 11. Evidência por gate e dependência das decisões PND
| Gate | Evidência para submissão | Dependências prioritárias | Estado atual |
| --- | --- | --- | --- |
| G0 | Escopo, donos, alçadas e riscos ratificados | PND-01, PND-11 | Parcial |
| G1 | Schemas revisados + runs estruturais e compatibilidade observados | PND-05, PND-06 | Pendente |
| G2 | Testes de identidade, autorização, escopos, revogação e segregação | PND-01/02/03/07/08 | Pendente |
| G3 | Fixtures executadas, rubricas, defeitos e adjudicação de avaliação | PND-09/10/12 | Pendente |
| G4 | Fluxos integrados e rollback em sandbox autorizada | PND-04/07/13/14 | Pendente |
| G5 | Revisão independente e decisões formais | PND-11/12 | Pendente |
| G6 | Liberação delimitada, observabilidade e incidentes aprovados | PND-14/15/16 | Pendente |

O preparo do ambiente não resolve automaticamente nenhuma das 16 pendências e **não autoriza passar de dados sintéticos para reais**.

## 12. Checklist de prontidão para a futura campanha
- [ ] Autoridade designada e autorização formal da campanha registrada
- [ ] Escopo, critérios de aceite e limites financeiros formalizados
- [ ] Commits e hashes congelados
- [ ] Fixtures revisadas como estritamente sintéticas
- [ ] Ambiente isolado e controle de rede/segredos aprovado
- [ ] Dependências fixadas e verificadas
- [ ] Scripts revisados para execução segura
- [ ] Evidências e política de retenção aprovadas
- [ ] Critérios de parada e incidente aprovados
- [ ] Revisores e avaliadores designados
- [ ] Relatório de runs e sistema de defeitos preparados
- [ ] Procedimento formal de adjudicação e gate definido

**Nenhum item é marcado como concluído nesta etapa sem registro de prova.**

## 13. Próxima etapa recomendada
[**GAI-INT-16 — Modelo de Pacote de Evidências, Revisão Independente e Adjudicação de Gates**](pacote-evidencias-revisao-independente-adjudicacao-gates.md), para detalhar formulários lógicos, critérios de decisão e proveniência de evidências sem pressupor que testes já foram executados.

**Referências:** [INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [INT-10](conformidade-schemas-casos-contrato-compatibilidade.md) · [INT-11](cobertura-contratos-especializados-integracao-schemas.md) · [INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [INT-05](autoridade-dados-consentimentos-revogacao.md).

**Guivos AI e GKR mantêm governanças independentes. Nenhuma alteração operacional no Replit, Neo4j, provedores, API ou demais sistemas.**
