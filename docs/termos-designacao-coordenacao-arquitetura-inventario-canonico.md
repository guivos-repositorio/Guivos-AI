# GAI-INT-27 — Termos de Designação P0-A/P0-B e Critérios de Aceite
**Versão documental 5.2 · 31/10/2026**
**Estado:** termos candidatos para a direção da Guivos, sem indicação de titulares, aceites, delegações de gate ou autorização operacional.

## 1. Resultado
O [GAI-INT-26](inventario-tecnico-inicial-designacoes-p0.md) verificou no GitHub os artefatos documentais e candidatos, mas não comprovou serviços em operação. A [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) confirmou a direção da Guivos como instância de nomeações estratégicas. Este estudo prepara **dois atos de nomeação distintos** para assinatura ou ratificação posterior, sem preenchê-los ficticiamente.

## 2. Termo P0-A — Coordenação de arquitetura
**Objeto:** organizar o inventário de contratos, dependências e fronteiras de confiança Guivos Intelligence/Guivos AI/serviços canônicos, preservando o Neo4j como projeção não autoritativa salvo decisão canônica específica.

**Responsabilidades propostas:** revisar o mapa de componentes; relacionar 12 capacidades a contratos; registrar ADRs candidatos; identificar owners e incompatibilidades; apresentar relatório de lacunas com fonte e versão.

**Entregável inicial:** mapa versionado de componentes e contratos com riscos, suposições, evidências e itens não verificados.

**Não inclui:** acesso automático a dados de Pessoas, autorização de execução de testes, atribuição de competência jurídica, homologação de G0–G6 ou alteração de sistemas operacionais.

**Campos do ato futuro:** `nominee_ref`, `appointment_decision_ref`, `scope_ref`, `acceptance_ref`, `effective_at`, prazo/condição de revisão e eventual `substitute_ref`.

**Condição de aceite:** titular indicado confirma escopo e limitações; direção ratifica e registra decisão verificável. **Estado: aguardando indicação.**

## 3. Termo P0-B — Inventário dos serviços canônicos
**Objeto:** verificar os serviços reais de identidade, autorização, contexto, oportunidades, evidências e entrega, distinguindo implementação, deploy e operação comprovada.

**Responsabilidades propostas:** identificar `service_ref`, repositório/ambiente, proprietário técnico, domínio de autoridade, finalidade, versão de contrato, política de correção/revogação, dependências, prova de existência e limitações.

**Entregável inicial:** inventário de serviços com `lifecycle_state` em `proposed|code_present|deployed_unverified|running_verified|unknown`, links de evidências e origem verificada.

**Não inclui:** consultar banco ou dados pessoais sem autorização, concluir que proprietário do GitHub detém autoridade canônica, executar procedimentos Neo4j/Replit ou conceder aprovação de gates.

**Campos do ato futuro:** os mesmos de P0-A, acrescidos de delimitação de fontes e permissões de consulta necessárias.

**Condição de aceite:** indicação, escopo de inspeção autorizado e aceitação formal. **Estado: aguardando indicação.**

## 4. Critérios e segregação entre P0-A e P0-B
| Aspecto | P0-A | P0-B |
| --- | --- | --- |
| Foco | Arquitetura e contratos | Serviços reais e fonte de autoridade |
| Evidências | ADR, versões, interfaces | Serviço, owner, estado e contrato efetivo |
| Pode relatar serviço não verificado | Sim, como incerteza | Sim, como `unknown` |
| Pode declarar autorização de dados | Não | Não |
| Pode executar testes sem decisão separada | Não | Não |
| Pode homologar G2 | Não | Não |

Os papéis podem eventualmente ser acumulados, mas a decisão deverá documentar capacidade, conflito de interesse, revisores independentes e medidas compensatórias.

## 5. Protocolo para a direção ratificar os dois atos
1. Identificar a Pessoa ou equipe que assumirá P0-A e P0-B, com referência interna apropriada, sem expor dados pessoais sensíveis em repositório público.
2. Definir escopo, limites de acesso, duração e entregáveis de cada mandato.
3. Obter aceite do indicado, com registro auditável.
4. Registrar decisão de nomeação e referência documental; nenhuma nomeação é válida apenas porque o template foi criado.
5. Atualizar o cadastro de 16 papéis do GAI-INT-23, sem promover automaticamente as PND-01/11 a concluídas.
6. Abrir solicitação separada se for necessário inspecionar sistemas privados, bancos, dados reais ou executar scripts.

## 6. Evidência e estados
[Termos estruturados P0-A/P0-B](termos-designacao-p0-candidatos.json) registram `nominee_ref=null`, `appointment_decision_ref=null`, `acceptance_ref=null`, `status=awaiting_nomination` para ambos. Isso demonstra a existência do modelo, não dos atos formais.

A matriz GAI-DEC-009 continua sendo decisão estratégica confirmada. PND-01 e PND-11 permanecem abertas; G0 parcial e G1–G6 pendentes. O inventário técnico do GAI-INT-26 continua restrito ao GitHub.

## 7. Próximo avanço material
A direção deve **indicar o responsável por P0-A e o responsável por P0-B** para preencher os termos, confirmar aceites e autorizar expressamente qualquer futura inspeção operacional. Sem essas indicações não há base para registrar nomeações reais.

**Referências:** [GAI-INT-26](inventario-tecnico-inicial-designacoes-p0.md) · [GAI-INT-25](modelo-inicial-designacoes-segregacao-responsabilidades.md) · [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md) · [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md).

**Nenhum teste foi executado, nenhum gate foi aprovado e nenhum sistema operacional foi alterado.**
