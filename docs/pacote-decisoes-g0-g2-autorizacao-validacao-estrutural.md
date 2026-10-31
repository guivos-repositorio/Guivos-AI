# GAI-INT-21 — Pacote de Decisões Prioritárias de G0/G2 e Autorização de Validação Estrutural
**Versão documental 4.5 · 31/10/2026**
**Estado:** propostas prontas para deliberação; nenhuma decisão aprovada neste estudo, nenhum teste executado e nenhum gate liberado.

## 1. Objetivo
Converter as dependências priorizadas em [GAI-INT-20](matriz-dependencias-sequenciamento-entrada-implementacao.md) em perguntas concretas a serem respondidas por autoridades designadas. Preparar, **sem conceder autorização**, a possível primeira campanha de validação estrutural offline e estritamente sintética dos schemas da Guivos AI.

A concordância com a produção deste documento autoriza somente sua **publicação documental**. Não autoriza instalar dependências, disparar scripts, usar provedores externos, acessar dados reais ou modificar Replit/Neo4j. Guivos AI e GKR permanecem independentes.

## 2. Situação de partida
- 12 capacidades especializadas GAI-CAP-01 a 12, documentadas.
- 20 estudos integrados anteriores GAI-INT-01 a 20.
- 19 JSON Schemas candidatos sob `schemas/candidate-v1/`.
- 49 fixtures estruturais sintéticas (25 básicas e 24 tipadas), dois executores offline ainda sem run registrado.
- 16 decisões PND-01 a 16 ainda abertas.
- G0 parcialmente documental, G1–G6 pendentes.
- Integração ponta a ponta da Jornada/Replit, Guivos AI, Neo4j e modelos externos não comprovada por estes documentos.

Não usar contagem de artefatos como indicador de qualidade operacional.

## 3. Propostas prioritárias de G0
### D21-01 — Autoridade canônica (PND-01)
**Pergunta:** quem pode afirmar, alterar e revogar cada dado de identidade, contexto, declaração, evidência, oportunidade, disponibilidade, autorização e relatório?

**Alternativas:** (A) serviços canônicos especializados por domínio, com donos explícitos e eventos versionados; (B) base única centralizada com governança única; (C) autoridade híbrida não formalizada.

**Recomendação de estudo:** avaliar A como padrão arquitetural, sujeito a inventário real dos serviços e decisão de governança. Não atribuir autoridade geral ao Neo4j, Guivos Intelligence ou saída GPT/Claude/Gemini.

**Prova para decidir:** matriz campo → serviço proprietário → versão → origem → retenção → consumidor → evento de correção → mecanismo de reconciliação. **Status: `pending_decision`.**

### D21-02 — Alçadas e independência (PND-11)
**Pergunta:** quem revisa arquitetura, privacidade, contratos, testes, adjudicação e emissão de GateDecision?

**Alternativas:** (A) funções separadas com responsável e suplente; (B) atuação combinada, sujeita a compensações e revisão adicional; (C) papel indefinido.

**Recomendação:** A para riscos altos e críticos; exceções justificadas caso a caso, sem inventar pessoas, nomeações ou assinatura.

**Prova para decidir:** registro de autoridade formal, escopo, conflito de interesse, responsável por resposta a incidentes e instância de escalonamento. **Status: `pending_decision`.**

## 4. Propostas prioritárias de G2
### D21-03 — Finalidades e proteção de dados (PND-02)
**Pergunta:** quais bases e finalidades autorizam cada processamento, reprocessamento e eventual entrega, incluindo parceiros?

**Alternativas:** matriz por finalidade, sujeito, destinatário, tempo e base aplicável; ou autorização genérica indistinta.

**Recomendação:** matriz granular com revisão jurídica/privacidade. **Não presumir consentimento como única base legal nem considerar esta proposta parecer jurídico.** Provas: fluxos documentados, minimização, controle de acesso, retenção e tratamento de direitos. **Status: pendente.**

### D21-04 — Identidade, segregação e escopos (PND-03)
**Pergunta:** como autenticar e autorizar Pessoas, Organizações, Coletivos, serviços internos e consumidores B2B sem confundir conta, processamento e compartilhamento?

**Recomendação:** autorização verificada no serviço de origem e no ponto de uso, por finalidade e escopo; isolamento por tenant; nenhuma permissão herdada de uma resposta de IA. Provas: contrato de identidade, negativos entre tenants, revogação, tokens e perfis de leitura. **Status: pendente.**

### D21-05 — Revogação e retenção (PND-08)
**Pergunta:** como interromper novos acessos e usos não autorizados, revalidar derivados e aplicar políticas de retenção e exclusão sem alegar recolhimento de dados já entregues?

**Recomendação:** separar bloqueio de acesso, invalidação da análise, exclusão conforme política aplicável, retenção legítima e comunicação com destinatários. Provas: matriz de propagação, recibos efetivos, caches/relatórios, tratamento de concorrência e incidentes. **Status: pendente.**

**Nenhuma dessas recomendações fecha PND-01/02/03/08/11.**

## 5. Proposta delimitada de primeira campanha estrutural (PND-09, 10, 12)
O objetivo futuro **não é homologar a Guivos AI**: é executar, em ambiente offline controlado, os 49 casos sintéticos preparados e observar aceitação/rejeição estrutural dos 19 schemas candidatos.

| Dimensão | Limite candidato |
| --- | --- |
| Entrada | Schemas `candidate-v1`, `cases.json` e `typed-cases.json` |
| Execução | `run_schema_cases.py` e `run_typed_cases.py` após revisão |
| Dados | Exclusivamente sintéticos, previamente examinados |
| Ambiente | Sandbox offline isolada, sem credenciais/segredos |
| Integrações externas | Nenhuma |
| Replit, Neo4j, GKR | Nenhum acesso, alteração ou leitura operacional |
| GPT, Claude, Gemini | Nenhuma chamada ou custo |
| Evidências | Commit congelado, hashes, versões e resultados reais por case_id |
| Aprovação | Autoridade formal por designar |
| Estado real | **`not_authorized`**, sem run registrado |

### D21-06 — Revisão de fixtures (PND-09)
**Pré-requisito:** revisores verificam que os 49 casos são sintéticos, consistentes, não sensíveis e suficientemente representativos da validação estrutural inicial. Casos semanticamente perigosos exigirão suites separadas. Status: pendente.

### D21-07 — Aceite, severidade e parada (PND-12)
**Critério candidato:** 49/49 comparações com expectativa estrutural correspondente, zero casos `not_run` ou inconclusivos na campanha delimitada; diferenças abrem defeito e reteste. **Este é um critério proposto, não um resultado obtido.** Resultados corretos de testes negativos contam como sucesso apenas quando o validador os rejeitar.

Condições de parada: dados não sintéticos, integridade divergente, rede/credencial proibida, falha de ferramenta ou dependência, autorização inválida, vazamento, inconsistência crítica de fixtures. Status: pendente.

### D21-08 — Autorização de execução (PND-10)
**Pedido futuro:** autorizar especificamente execução offline controlada, após aprovação do escopo, ambiente, dependências, revisores, limite financeiro, janela e registro de evidências. **Nenhuma autorização é solicitada como ato automático pela leitura do documento.** Deve existir decisão posterior inequívoca registrada.

## 6. Registro estruturado candidato
A [proposta machine-readable](pacote-decisoes-g0-g2-autorizacao-estrutural-candidato.json) conserva o escopo da campanha e oito itens prioritários de decisão, todos pendentes. O campo `execution_authorized=false`; `runs=[]`; `gate_decision_ref=null`.

O JSON é **registro de proposta**, não sistema de permissões e não substitui autoridade formal. Não preencher datas, owners, orçamento ou IDs de autorização sem fonte legítima.

## 7. Critérios de entrada para a deliberação
1. Questão, alternativas, recomendação e riscos documentados.
2. Dados e finalidade delimitados, sem acesso implícito ao Replit.
3. Responsável competente e alçada formalmente identificados.
4. Evidências e consequências para G0/G2 e G1/G3 identificadas.
5. Critérios objetivos e restrições de execução.
6. Decisão registrada como `approved_with_scope`, `rejected` ou `deferred` por autoridade autorizada; ausência de decisão permanece pendente.
7. Mudança real exige decisão de execução/implantação separada, mesmo depois de um gate documental.

## 8. Sequenciamento sugerido
**Primeiro:** deliberar autoridade de dados e alçadas (D21-01/02), com foco em fronteiras e responsáveis.

**Depois:** esclarecer finalidades, identidade, escopos e revogação (D21-03/04/05); essas decisões condicionam sistemas com dados reais, mas não constituem autorização técnica de integração.

**Em paralelo documental:** revisar fixtures e aprovar critérios da primeira campanha (D21-06/07), sem executá-la.

**Somente após as aprovações relevantes:** submeter D21-08, congelar pacote e, se autorizada, executar campanha offline. Resultados devem ser capturados como observados e revisados independentemente. Gates G1/G3 continuariam exigindo deliberação própria.

## 9. Bloqueios explícitos
| Bloqueio | Resultado |
| --- | --- |
| Sem autoridade ou responsável designado | Nenhuma aprovação de gate |
| Sem autorização explícita de execução | Não executar scripts |
| Dependências ou fonte das fixtures não revisadas | Manter campanha bloqueada |
| Sem isolamento/offline verificável | Não iniciar run |
| Resultados só esperados, não observados | Não declarar conformidade |
| Falha de segurança/revogação | Impede evolução para dados reais |
| Divergência de provedores | Não substitui evidência canônica |
| Gate estrutural isolado | Não autoriza API, B2B, Jornada ou release |

## 10. Encaminhamento conceitual D21-01/D21-02
O [GAI-INT-22](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md) consolida autoridade por domínio e segregação de alçadas como direcionamentos arquiteturais. Permanecem pendentes a ratificação formal, a nomeação de responsáveis e toda autorização de execução.

## 11. Próximo avanço preferencial
Ao contrário de criar indefinidamente novos estudos, a etapa seguinte mais útil será **deliberar formalmente os pontos D21-01 e D21-02** e identificar a autoridade capaz de decidir sobre uma campanha offline estritamente sintética.

Um eventual **GAI-INT-22 — Registro das Deliberações de G0/G2 e Plano de Validação Autorizada** só deve registrar decisões realmente tomadas; caso persistam pendências, manter o registro como não aprovado.

**Referências:** [GAI-INT-20](matriz-dependencias-sequenciamento-entrada-implementacao.md) · [GAI-INT-19](consolidacao-arquitetura-prontidao-implementacao.md) · [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [GAI-INT-15](preparacao-execucao-sintetica-controlada-evidencias-gate.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [GAI-INT-05](autoridade-dados-consentimentos-revogacao.md).

**Sem execução, integração, alteração de sistemas ou aprovação de gates.**
