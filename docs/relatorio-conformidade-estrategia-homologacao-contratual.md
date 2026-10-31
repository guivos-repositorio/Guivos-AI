# GAI-INT-12 — Relatório de Conformidade e Estratégia de Homologação Contratual
**Guivos AI · Versão documental 3.6 · 31/10/2026**
**Estado:** relatório de prontidão documental, não relatório de execução. **Nenhuma suíte foi executada, nenhum gate foi homologado e nenhuma integração ou liberação foi autorizada.**

## 1. Propósito
Consolidar a situação dos contratos candidatos da Guivos AI, estabelecer evidências verificáveis para conformidade e definir um processo de homologação com responsáveis e decisões rastreáveis. Este documento **não transforma a publicação de schemas ou fixtures em aprovação técnica**.

Abrange GAI-CAP-01 a GAI-CAP-12, GAI-INT-01 a 11, os schemas `candidate-v1`, os dois catálogos de fixtures e os dois executores offline. Guivos Intelligence continua responsável por orquestrar a experiência e a validação da Pessoa; Guivos AI por métodos especializados; serviços canônicos por fatos, versões e autorizações.

## 2. Inventário e estado apurado documentalmente
| Ativo | Quantidade | Evidência existente | Estado real |
| --- | ---: | --- | --- |
| Especificações de capacidades | 12 | Documentos CAP-01–CAP-12 | Conceituadas; não homologadas |
| Estudos integrados anteriores | 11 | Documentos GAI-INT-01–11 | Publicados |
| Schemas de base INT-08 | 3 | JSON Schema Draft 2020-12 | Candidatos |
| Schemas INT-09 | 8 | Erros, recibos, dependências e 5 payloads | Candidatos |
| Schemas INT-11 | 8 | 7 payloads e 1 envelope tipado | Candidatos |
| **Total de schemas** | **19** | `schemas/candidate-v1/` | **Não homologados** |
| Fixtures básicas INT-10 | 25 | `tests/contracts/candidate-v1/cases.json` | Preparadas, sem run |
| Fixtures tipadas INT-11 | 24 | `tests/contracts/candidate-v1/typed-cases.json` | Preparadas, sem run |
| **Total de casos estruturais** | **49** | Dois arquivos de fixtures sintéticas | **Sem resultado observado** |
| Executores offline | 2 | Scripts Python em `tests/contracts/` | Publicados, não executados nesta etapa |
| Decisões G1–G6 | 0 aprovadas | Plano de gates INT-03 | Pendentes |

**Atenção:** esta tabela é inventário de arquivos e escopos documentais. A contagem não demonstra completude semântica, qualidade ou sucesso de testes. Não há logs de execução nem evidências de adjudicação a interpretar.

## 3. Hierarquia de evidências e estado de conformidade
| Nível | Significado | Prova mínima |
| --- | --- | --- |
| E0 — Proposto | Especificação ou contrato documentado | Caminho e versão |
| E1 — Preparado | Schema, fixture e executor criados | Arquivo identificável por commit e entradas sintéticas |
| E2 — Executado | Casos efetivamente rodados | Run ID, ambiente, comando, versões, saída e resumo de falhas |
| E3 — Revisado | Resultados avaliados por responsáveis | Revisão, rubrica, limitações, defeitos e assinaturas/atribuição |
| E4 — Adjudicado | Escopo aceito/rejeitado por autoridade designada | Registro formal de decisão e condições |
| E5 — Homologado para escopo | Gate aplicável concedido formalmente | GateDecision, controle de alterações e prazo de validade |

**Situação atual máxima: E1 para fixtures e schemas.** Os gates não avançam automaticamente com a contagem de artefatos. E2–E5 não existem nesta etapa.

## 4. Contrato lógico do relatório de execução futuro
Cada campanha deverá registrar, no mínimo:
- `campaign_id`, `run_id`, `executed_at` e `execution_status`;
- `repository_commit`, `schema_digests[]`, `fixture_catalog_digest`, `runner_digest`;
- `python_version`, `jsonschema_version`, `referencing_version`, `environment_ref`;
- `cases_total`, `cases_executed`, `cases_matched`, `cases_failed`, `cases_inconclusive`;
- `case_results[]`: `case_id`, `expected_valid`, `observed_valid`, `comparison_status`, `error_paths[]`, `limitations[]`;
- `security_review_status`, `semantic_review_status`, `review_refs[]`, `adjudication_ref` e `gate_decision_ref`.

Não usar `pass` para casos ainda não executados. A execução de validação estrutural não altera automaticamente `security_review_status` ou `semantic_review_status`.

**Modelo de estado sintético, não execução:**
```json
{
  "report_type": "contract_conformance_readiness",
  "document_version": "3.6",
  "candidate_catalog": "candidate-v1",
  "schema_count": 19,
  "planned_fixture_count": 49,
  "execution_status": "not_executed",
  "observed_cases": null,
  "review_status": "not_reviewed",
  "adjudication_status": "not_adjudicated",
  "gate_approval": null
}
```

## 5. Estratégia de compatibilidade
Matriz proposta:
| Origem / mudança | Consumidor atual | Consumidor candidato | Exigência futura |
| --- | --- | --- | --- |
| Evento `candidate-v1` | Validador de evento atual | Validador novo | Verificar preservação da semântica, versão, emissor e escopo |
| AnalysisResponse original | Consumer que aceita `result` extensível | Envelope tipado INT-11 | Verificar impacto de exigir `result` e associação CAP |
| Payload especializado | Consumidor por CAP | Payload revisto | Recusar alteração silenciosa de enum/obrigatoriedade |
| ErrorResponse | Consumidor de falhas | Nova união sucesso/erro | Falha não pode ser interpretada como análise bem-sucedida |
| EventReceipt | Serviço de propagação | Novo modelo de recibos | Recebimento não se confunde com aplicação |
| DependencyEdge | Projeção/indexador | Nova versão de vínculo | Preservar proveniência, isolamento, versão e reconciliação |

Os testes devem cobrir **velho produtor → novo consumidor**, **novo produtor → velho consumidor**, contratos incompatíveis, migração e rollback. Adicionar campo pode ser incompatível com `additionalProperties: false`. Não designar versão “estável” sem validação.

## 6. Bloqueios e lacunas prioritárias
| ID | Lacuna | Severidade candidata | Tratamento antes de homologação |
| --- | --- | --- | --- |
| HOM-01 | Nenhum run das 49 fixtures | Alta | Executar testes em ambiente isolado, após autorização |
| HOM-02 | Sem evidência de compatibilidade cruzada | Alta | Criar matriz automatizável de versões e consumidores |
| HOM-03 | Envelope tipado não substitui automaticamente contrato original | Alta | Definir política de adoção e migração |
| HOM-04 | Falhas e sucesso ainda não formam união tipada normativa | Alta | Especificar e validar contrato de discriminador |
| HOM-05 | Payloads CAP são mínimos estruturais, não contratos completos | Alta | Revisar semântica e exemplos por responsáveis de domínio |
| HOM-06 | Autorizações e isolamento não são verificáveis por JSON Schema | Crítica em caso de exposição | Executar testes de serviço e revisão de segurança específicos |
| HOM-07 | Regras de eventos, ordenação e revogação não estão verificadas operacionalmente | Crítica em caso de uso indevido | Cenários de concorrência, recibos e bloqueio |
| HOM-08 | Faltam rubricas quantitativas homologadas e adjudicadores designados | Alta | Designar responsabilidades e critérios por risco |
| HOM-09 | Não existem resultados de latência/custo/segurança de integração | Alta | Medição futura em ambiente isolado |
| HOM-10 | Sem política aprovada de monitoramento, rollback e incidentes | Alta | Aprovar plano antes de G6 |

Severidades são **classificações documentais propostas**, não incidentes comprovados. A resolução de uma lacuna deve citar evidência, teste e decisão; nunca apenas a atualização do texto.

## 7. Critérios de aceite sugeridos
### G1 — Contratos
Inventário e owners aprovados; schemas validados por ferramenta compatível com Draft 2020-12; fixtures negativas efetivamente rejeitadas; cobertura por CAP revisada; plano de migração documentado; erros e estados sem ambiguidades. Exige evidência de run, não publicação isolada.

### G2 — Segurança e autoridade
Serviços canônicos de identidade/autorização mapeados; permissão por finalidade/sujeito/tenant verificada no backend; revogação e expiração testadas; minimização de logs; sem acesso direto irrestrito de modelos ou parceiros às fontes.

### G3 — Avaliação sintética
Runs versionados e reprodutíveis; casos negativos e adversariais; defeitos classificados; nenhum bloqueador crítico aberto para o escopo; revisões independentes registradas.

### G4 — Integração controlada
Contratos de Intelligence ↔ Guivos AI ↔ serviços autorizados testados em ambiente separado com dados sintéticos; respostas obsoletas suprimidas; rollback e isolamento demonstrados.

### G5 — Adjudicação
Rubricas e avaliadores designados; resultados e divergências revisados; decisão formal, limites e duração registrados.

### G6 — Liberação
Aprovação explícita por responsáveis autorizados, escopo restrito, observabilidade, custos, segurança, retenção e resposta a incidentes.

**Estado: G0 parcial; G1–G6 pendentes.** Critérios ainda sujeitos à deliberação de governança.

## 8. Matriz de responsabilidades — sem nomeações
| Função | Evidência sob responsabilidade | Decisão |
| --- | --- | --- |
| Engenheiro de contratos | Schemas, fixtures e regressões | Recomenda conformidade técnica |
| Engenharia de integração | Compatibilidade e fluxos | Recomenda aprovação de integração |
| Segurança/privacidade | Identidade, escopo, isolamento e revogação | Bloqueia falhas críticas |
| Responsável pelos dados | Proveniência, versões e fatos | Valida escopo canônico |
| Revisão da qualidade de IA | Claims, hipóteses, qualidade e vieses | Parecer semântico |
| Governança designada | Pacote de evidências e exceções | Decide gate conforme competência formal |

Não presumir nomes, designação, alçada legal nem poderes de aprovar produção.

## 9. Protocolo de adjudicação futura
1. Congelar commit, fixtures e schemas para a campanha.
2. Executar apenas após autorização própria e registrar ambiente.
3. Consolidar resultados esperados e observados, sem eliminar falhas.
4. Classificar defeitos; retestes geram novos `run_id`.
5. Submeter evidências desidentificadas aos revisores competentes.
6. Registrar divergências e condições pendentes.
7. Propor decisão de gate com escopo, restrições, evidências e validade.
8. Obter aprovação explícita por autoridade designada ou manter gate pendente.

**É vedado declarar aprovação automática por taxa de casos positivos**, por concordância dos modelos GPT/Claude/Gemini ou por integração parcial do Neo4j.

## 10. Roadmap documental de fechamento
**F1 — Conformidade:** preparar pacote de execução controlada de contratos e ampliar casos negativos.

**F2 — Compatibilidade:** estabelecer versões, adaptações e depreciação com consumidores definidos.

**F3 — Governança:** nomear papéis, critérios de revisão, segurança e política de autorização.

**F4 — Integração:** somente após autorização explícita, comparar esquemas com os serviços efetivamente existentes no Replit e outros componentes.

**F5 — Decisão:** documentar evidências e adjudicar gates por escopo, separando homologação de autorização comercial.

## 11. Próxima etapa recomendada
[**GAI-INT-13 — Plano de Compatibilidade, Migração e Evolução de Contratos**](plano-compatibilidade-migracao-evolucao-contratos.md), publicado para aprofundar cenários producer/consumer, versionamento e rollout/rollback sem presumir operação real.

**Referências:** [GAI-INT-11](cobertura-contratos-especializados-integracao-schemas.md) · [GAI-INT-10](conformidade-schemas-casos-contrato-compatibilidade.md) · [GAI-INT-09](schemas-especializados-erros-recibos-eventos.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md) · [GAI-INT-08](catalogo-formal-schemas-compatibilidade-servicos.md).

**Nenhuma execução, homologação ou alteração operacional foi realizada. Replit, Neo4j, provedores e GKR mantêm seus estados anteriores.**
