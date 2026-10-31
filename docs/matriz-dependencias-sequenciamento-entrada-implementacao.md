# GAI-INT-20 — Matriz de Dependências, Sequenciamento de Decisões e Critérios de Entrada na Implementação
**Versão documental 4.4 · 31/10/2026**
**Estado:** backlog arquitetural e matriz de dependências candidatos. Nenhuma decisão PND encerrada, responsável formalmente designado, implementação autorizada, teste executado ou gate aprovado.

## 1. Propósito
Transformar a visão integrada do [GAI-INT-19](consolidacao-arquitetura-prontidao-implementacao.md) em um backlog de decisões, com pré-requisitos, sequência racional, evidências necessárias, riscos e condição de autorização para o trabalho futuro.

O planejamento envolve Guivos Intelligence, Guivos AI, serviços canônicos, eventual Neo4j, provedores de modelos, API CAP-12 e consumidores do ecossistema. **Planejamento de implementação não constitui ordem de execução.** Replit e GKR não serão alterados automaticamente.

## 2. Estado de partida verificável
- GAI-CAP-01–12: 12 capacidades documentadas.
- GAI-INT-01–19: 19 estudos integrados publicados.
- Contratos: 19 JSON Schemas `candidate-v1`; não homologados.
- Testes: 49 fixtures estruturais sintéticas, dois scripts offline; sem execução registrada.
- Decisões: 16 PNDs abertas, conforme [GAI-INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md).
- Gates: G0 documental parcial; G1–G6 pendentes.
- Sem validação ponta a ponta da POC Replit/Neo4j e sem autorização operacional nesta rodada.

A nova [matriz estruturada do sequenciamento](matriz-dependencias-sequenciamento-candidato.json) contém **16 itens GAI-BLK-01..16** associados individualmente às PNDs. Todos têm `status=proposed_not_authorized` e `authorization_required=true`.

## 3. Dependências do backlog por domínio
| ID | Entrega/decisão candidata | Depende de | Função candidata | Gate |
| --- | --- | --- | --- | --- |
| BLK-01 | Autoridade canônica, fontes, proveniência | — | Dados | G0, G2 |
| BLK-11 | Owners, alçadas e governança dos gates | — | Governança | G0, G5 |
| BLK-02 | Finalidades, bases legais e limites de processamento | 01, 11 | Privacidade/jurídico | G2 |
| BLK-03 | Identidade, tenant, consentimento/escopos | 01, 02, 11 | Segurança | G2 |
| BLK-08 | Revogação, retenção, derivados e entrega | 02, 03 | Privacidade | G2 |
| BLK-04 | Papel físico do Neo4j e reconciliação | 01, 03 | Arquitetura de dados | G1, G4 |
| BLK-05 | Normalização de envelopes, claims e schemas | 01, 03 | Engenharia de contratos | G1 |
| BLK-06 | Versionamento, compatibilidade e migração | 05 | Integração | G1 |
| BLK-07 | Eventos, recibos e invalidação propagada | 03, 04, 05 | Integração/segurança | G2, G4 |
| BLK-09 | Revisão das 49 fixtures e rubricas | 05, 11 | QA/qualidade de IA | G3 |
| BLK-12 | Severidades, métricas e condições de parada | 09, 11 | QA/segurança | G3, G5 |
| BLK-10 | Decisão sobre campanha sintética controlada | 03, 09, 11, 12 | Governança técnica | G3 |
| BLK-13 | Autorização de inspeção do Replit/Jornada | 03, 04, 06, 07, 11 | Produto/arquitetura | G4 |
| BLK-14 | Política de adaptadores, fallback e custos | 03, 05, 09 | Arquitetura de IA | G4, G6 |
| BLK-15 | Observabilidade, incidentes e rollback | 07, 10, 12 | Operações/segurança | G6 |
| BLK-16 | Condições de oferta API/B2B | 02, 03, 06, 11, 13, 14, 15 | Produto/jurídico | G6 |

**As dependências são recomendações de sequenciamento, não restrições aprovadas por owners.** Uma decisão pode ser aprofundada documentalmente antes de pré-requisitos, mas sua execução depende de controles e autorização aplicáveis.

## 4. Caminho crítico lógico proposto
```text
BLK-01 (fontes) ─────┐
                     ├──> BLK-02 (finalidades) ─> BLK-03 (escopos) ─> BLK-08
BLK-11 (alçadas) ────┘                             │
                                                   ├──> BLK-05 (contratos)
                                                   │        ├─> BLK-06 (versões)
                                                   │        └─> BLK-09 (fixtures)
                                                   │                 └─> BLK-12 (critérios)
                                                   │                        └─> BLK-10 (autorização testes)
                                                   └──> BLK-04 (Neo4j)
                                                              └─> BLK-07 (eventos)
BLK-03/04/06/07/11 ────────────────────────────────> BLK-13 (Replit)
BLK-03/05/09 ──────────────────────────────────────> BLK-14 (modelos)
BLK-07/10/12 ──────────────────────────────────────> BLK-15 (observabilidade)
BLK-02/03/06/11/13/14/15 ─────────────────────────> BLK-16 (B2B)
```
Isto não é cronograma nem cálculo de caminho crítico por duração, pois não foram estimadas durações, recursos ou capacidades de equipes.

## 5. Pacotes de decisão por onda
**Onda A — Fundamentos de confiança:** BLK-01 e BLK-11, depois BLK-02/03/08. Entregas: mapa de autoridade, responsabilidades, autorização por finalidade e segregação. Pode haver estudo paralelo, mas não liberar processamento real sem governança e privacidade.

**Onda B — Contratos e dependências:** BLK-04/05/06/07. Entregas: ADRs, contratos revisados, política de versão, eventos, fonte canônica e reconciliação de projeções.

**Onda C — Validação isolada:** BLK-09/12/10. Entregas: fixtures revisadas, rubricas, critérios de parada e *eventual* autorização formal de campanha. Sem autorização, estado permanece `not_authorized`.

**Onda D — Integração e operação preparatória:** BLK-13/14/15. Somente após autorizações específicas, avaliações de integração e riscos. A existência de contrato não é prova de integração.

**Onda E — Oferta e expansão:** BLK-16. Condicionada ao valor real para consumidores, autorização, dados permitidos e gates aplicáveis; não presumir viabilidade comercial de CAP-12.

## 6. Critérios de entrada na implementação
Uma unidade de trabalho só pode ser submetida para autorização de implementação quando houver:
1. ID de backlog, dono da decisão e alçada formal.
2. Escopo e componentes exatos, dados envolvidos e finalidades autorizadas.
3. Contrato candidato revisado e semântica definida; dependências classificadas.
4. Plano de evidência: fixtures, negativos, segurança, temporalidade, custo, qualidade e rollback.
5. Ambiente aprovado e limites de rede/acesso, segredos e retenção.
6. Critérios objetivos de aceite e parada, aprovados antes da execução.
7. Estratégia de falha segura, revalidação, rastreabilidade e observabilidade.
8. Aprovação específica do experimento/implementação, sem inferir do consenso sobre o documento.
9. Gates e PNDs aplicáveis identificados, com bloqueios críticos resolvidos.
10. Limite claro entre hipótese, projeto aprovado, execução, revisão e release.

**Prontidão para solicitar autorização ≠ autorização concedida ≠ implementação validada.**

## 7. Definition of Ready / Definition of Done — propostas
**Ready documental:** problema delimitado; responsabilidade candidata; fontes e contratos mapeados; riscos de privacidade identificados; alternativas registradas. Não significa `ready_to_build`.

**Ready to execute (futuro):** autorização formal; owner e ambiente aprovados; artefatos fixados; fixtures sintéticas revisadas; critérios definidos; segurança, custo, stop conditions e registro de evidência habilitados.

**Done técnico (futuro):** implementação verificada por testes reproduzíveis e revisão; defeitos identificados; limites comunicados; autorizações e retenção cumpridas; rollback avaliado. Não significa gate aprovado por si só.

**Done de gate (futuro):** decisão formal, escopo, validade, alçada e condições registradas. G6 não pode ser inferido a partir do fechamento de G1.

## 8. Registro de riscos e interdependências
| Risco de sequência | Consequência | Bloqueio |
| --- | --- | --- |
| Construir grafo antes da autoridade de fontes | Memória de projeção tratada como fonte | Ratificar BLK-01/03/04 |
| Testar serviços reais sem segregação | Acesso impróprio, custo não autorizado | BLK-02/03/10 e escopo explícito |
| Construir API antes dos contratos | Acoplamento e versões incompatíveis | BLK-05/06 |
| Expor oportunidade como disponível por publicação | Direcionamento sem suporte factual | Autoridade canônica e CAP-08 |
| Publicar relatório antes de checar entrega | Violação de escopo | BLK-03/08 |
| Liberar antes de revisar eventos e caches | Resultado antigo usado como vigente | BLK-07/15 |
| Confundir testes de schema com qualidade da IA | Inferências falsas apesar do JSON válido | BLK-09/12/14 |
| Escalar para B2B antes de gates | Risco de dados, reputação e custo | BLK-16 condicionado |

## 9. Evidências mínimas por gate
| Gate | Entrada candidata | Evidência ainda faltante |
| --- | --- | --- |
| G0 | Mapa de papéis e alçadas (BLK-01/11) | Ratificação de responsáveis |
| G1 | Contratos, versões e projeções (BLK-04/05/06) | Testes e aprovação formal |
| G2 | Finalidades, escopos, revogação, eventos (BLK-02/03/07/08) | Prova de segurança e autorização |
| G3 | Fixtures e campanha sintética (BLK-09/10/12) | Runs observados, revisão e defeitos |
| G4 | Integração isolada (BLK-04/07/13/14) | Autorização e teste ponta a ponta |
| G5 | Revisão independente (BLK-11/12) | Designações, pareceres e adjudicação |
| G6 | Operação e consumidores (BLK-14/15/16) | Monitoramento, custos, rollout e GateDecision |

O estado permanece **G0 parcial e G1–G6 pendentes**. Nenhum teste, gate ou owner foi aprovado pela presente publicação.

## 10. Como utilizar a matriz JSON
A [matriz machine-readable](matriz-dependencias-sequenciamento-candidato.json) declara:
- `GAI-BLK-XX` e vínculo a `PND-XX`;
- `depends_on[]` com referências internas;
- `owner_role_candidate`, `priority_candidate` e `gates[]`;
- `acceptance_evidence` como resultado a comprovar;
- `status=proposed_not_authorized` e `authorization_required=true` para todos os 16 itens.

**A matriz não é sistema de tickets, não cria tarefas automáticas e não afirma execução ou designação de pessoas.** Alterações em dependências necessitam rastreabilidade de versão e revisão.

## 11. Decisões necessárias antes da próxima fase
- Confirmar se as dependências e prioridades propostas representam a governança desejada.
- Designar formalmente autoridades de G0/G2 e donos de dados, identidade e contratos.
- Decidir escopo inicial mínimo de uma campanha estritamente sintética.
- Ratificar requisitos de qualidade e revisão; diferenciar autorização para testes de autorização para implementação.
- Determinar quando e como a inspeção da POC Replit/Neo4j pode ocorrer, sem presumir acesso autorizado.
- Avaliar se o próximo avanço deve priorizar **validação observável dos 49 casos** após autorização, em vez de gerar apenas novos estudos.

## 12. Próxima etapa sugerida
[**GAI-INT-21 — Pacote de Decisões Prioritárias de G0/G2 e Autorização de Validação Estrutural**](pacote-decisoes-g0-g2-autorizacao-validacao-estrutural.md), com propostas prontas para deliberar, sem declarar nenhuma aprovação. Recomenda-se fechar as escolhas fundamentais antes de continuar ampliando indefinidamente documentação.

**Referências:** [INT-19](consolidacao-arquitetura-prontidao-implementacao.md) · [INT-14](registro-decisoes-pendentes-plano-fechamento-gates.md) · [INT-15](preparacao-execucao-sintetica-controlada-evidencias-gate.md) · [INT-12](relatorio-conformidade-estrategia-homologacao-contratual.md) · [INT-05](autoridade-dados-consentimentos-revogacao.md) · [INT-03](matriz-testes-integrados-criterios-aceite-gates.md).

**Sem execução de testes, contratação de serviços, alteração no Replit/Neo4j/provedores/API ou modificação do GKR.**
