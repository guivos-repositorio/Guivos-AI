# GAI-INT-05 — Autoridade de Dados, Consentimentos e Fluxos de Revogação
**Versão documental 2.9 · 31/10/2026**
**Estado:** estudo de governança e arquitetura proposto. Não é parecer jurídico, política operacional aprovada, integração implementada ou autorização para processar dados reais.

## 1. Objetivo
Especificar quem pode registrar, interpretar, consultar, compartilhar, corrigir, restringir e eventualmente eliminar informações no ecossistema Guivos, distinguindo **autoridade sobre fatos**, **responsabilidade por análises**, **controle de acesso**, **consentimento quando aplicável** e **direitos da Pessoa**.

**Guivos Intelligence consome Guivos AI.** A AI fornece métodos e resultados especializados, não substitui o serviço canônico nem decide autonomamente como utilizar informações pessoais. **Neo4j é infraestrutura candidata de relações e proveniência**, não fonte universal de verdade; GPT/Claude/Gemini não são proprietários nem autoridades dos dados. O GKR permanece independente.

## 2. Matriz de autoridade e responsabilidade
| Informação ou função | Autoridade funcional proposta | Consumidores autorizáveis |
| --- | --- | --- |
| Identidade, vínculo, papéis e sessão | Serviço de identidade e vínculos | Intelligence, AI e gateway conforme ação |
| Finalidade, permissão, restrição e revogação | Serviço de autorização/privacidade | Serviços demandantes após verificação |
| Declarações, anexos e revisões da Pessoa | Serviço canônico de contexto | Intelligence/AI mediante finalidade e minimização |
| Eventos de interação e validação | Serviço da Jornada e eventos canônicos | Intelligence/AI sob regras de proveniência |
| Publicador, requisitos, preço, prazo e status de oferta | Serviços de oportunidades | CAP-08 e consumidores elegíveis |
| Relações temporais e evidência projetada | Serviço de contexto/memória; Neo4j candidato | Consultas mediadas, nunca LLM irrestrito |
| Claims, lacunas, possibilidades e relatórios derivados | Guivos AI como autora metodológica; armazenamento com governança própria | Intelligence e destinatários autorizados |
| Apresentação, perguntas, aceite, adiamento e escolha | Guivos Intelligence e Pessoa | Superfícies e serviços pertinentes |
| Entrega a profissional/parceiro | Serviço de compartilhamento/autorização e canal contratado | Destinatário expressamente autorizado |

Autoridade funcional não equivale à condição jurídica de controlador, operador ou titular; os papéis legais e as bases adequadas exigem análise específica por tratamento.

## 3. Consentimento não é sinônimo de qualquer autorização
O tratamento poderá depender de diferentes bases legais conforme finalidade e contexto; **não presumir consentimento como base universal**. Quando o consentimento for a base aplicável, deverá ser específico, demonstrável, informado e revogável conforme legislação. O serviço deverá distinguir:
- autorização operacional de sessão/acesso ao serviço;
- base legal e finalidade de tratamento de dados;
- permissão de leitura de fontes determinadas;
- permissão de executar uma capacidade;
- permissão de reprocessar ou atualizar uma análise;
- permissão de compartilhar/entregar a destinatário identificado;
- obrigação legal ou retenção legítima que eventualmente subsista após uma revogação.

Nenhuma das permissões acima deve ser inferida automaticamente de outra. Aceitar explorar uma possibilidade não autoriza compartilhamento de relatório a um profissional; contratar plano B2B não autoriza acesso a uma Pessoa.

## 4. Objeto lógico de autorização (proposta)
Campos: `authorization_ref`, `subject_ref`, `controller_or_responsible_ref`, `consumer_ref`, `tenant_ref`, `purpose_code`, `legal_basis_ref`, `allowed_actions[]`, `source_scopes[]`, `data_categories[]`, `recipient_refs[]`, `valid_from`, `valid_until`, `issued_at`, `revoked_at`, `authorization_version`, `decision_provenance_ref` e `policy_version`.

**A emissão, comprovação e verificação são externas à Guivos AI.** Referências fornecidas por clientes não provam legitimidade. Uma resposta de autorização deve ser revalidada conforme a sensibilidade da operação e antes de entrega a terceiro.

## 5. Fluxos autorizados
### A — Contribuição e compreensão na Jornada
1. Pessoa acessa a Jornada; serviço competente valida identidade, finalidade e escopo.
2. Contexto canônico registra contribuição e versão com proveniência.
3. Intelligence solicita à AI somente os elementos necessários à capacidade requerida.
4. AI entrega claims e limites vinculados à versão/contexto/autorização.
5. Intelligence solicita validação da Pessoa sem transformar hipótese em fato canônico.
6. Correções são registradas pela fonte competente; CAP-10 sinaliza análises afetadas.

### B — Profissional autorizado
1. Profissional e vínculo são verificados; contrato institucional não é suficiente por si.
2. Finalidade, dados, destinatário, período e condições de compartilhamento são avaliados.
3. CAP-11 pode gerar relatório conforme escopo de processamento.
4. Entrega exige **verificação separada do escopo de compartilhamento**.
5. Leitura posterior deverá respeitar vigência, revogação, versões e eventuais restrições.

### C — Parceiro API
Gateway CAP-12 identifica aplicação e tenant; serviço de autorização verifica Pessoa e finalidade; AI produz apenas resultado autorizado; resposta é minimizada e filtrada por consumidor. **Não transferir direitos do canal interno ao parceiro**.

## 6. Semântica da revogação e restrição
**Evento válido:** solicitação ou determinação autenticada recebida pelo serviço competente, com sujeito, fundamento, finalidade, alcance, instante de efeito e versão.

**Efeitos candidatos distintos:**
- cessar novos acessos para operações incompatíveis;
- cancelar ou isolar tarefas futuras/pedidos em andamento quando exigido;
- impedir recuperação de derivados e relatórios não mais compartilháveis;
- invalidar análises cujas fontes não podem mais ser utilizadas;
- notificar caches, relatórios e consumidores alcançados pela política;
- considerar eliminação, anonimização ou retenção excepcional mediante política e análise jurídica;
- preservar evidência mínima e segura da revogação sem expor o conteúdo dos dados.

**Revogação não significa exclusão física automática**, nem reprocessamento irrestrito, nem possibilidade de recuperar documentos já entregues fora do controle técnico direto; obrigações dos destinatários e medidas posteriores requerem governança contratual.

## 7. Fluxo proposto de propagação
```text
Pessoa ou autoridade competente
  → serviço de autorização: registra decisão e versão
  → emite evento autenticado de alteração/revogação
  → consumidores autorizados recebem escopo mínimo do evento
  → bloquear leitura e entrega incompatíveis
  → CAP-10 sinaliza derivações e dependências afetadas
  → Intelligence/API/caches aplicam restrições e revalidam estado
  → serviços de armazenamento executam retenção/exclusão conforme política
  → auditoria registra resultado, falhas e pendências sem conteúdo excessivo
```
**Prioridade:** aplicar bloqueios de autorização antes de qualquer nova execução ou tentativa de correção analítica. Um evento pode ser repetido ou chegar fora de ordem; exigir idempotência, versões e reconciliação.

## 8. Contrato ilustrativo de evento (dados sintéticos)
```json
{
  "event_id": "synthetic-revocation-001",
  "event_type": "access_scope_revoked",
  "subject_ref": "synthetic-person",
  "authorization_ref": "opaque-scope-001",
  "authorization_version": "revision-8",
  "affected_purposes": ["professional_report_sharing"],
  "affected_recipient_refs": ["synthetic-professional"],
  "effective_at": "2026-10-31T13:00:00-03:00",
  "emitted_at": "2026-10-31T13:00:02-03:00",
  "origin_service_ref": "canonical-authorization",
  "retention_action": "evaluate_under_policy",
  "processing_status": "not_executed"
}
```
Contrato não implementado. Nenhuma integração, eliminação de dados ou revogação real foi executada.

## 9. Distinção entre estados
- `authorization_status`: `authorized`, `denied`, `revoked`, `expired`, `requires_reverification`, decidido por serviço competente.
- `processing_status`: `not_started`, `running`, `stopped`, `failed`, `completed`, sob rastreabilidade operacional.
- `validity_status`: `valid_for_recorded_context`, `revalidation_required`, `stale`, `invalidated`, `blocked_by_authorization`, segundo CAP-10.
- `delivery_status`: `not_released`, `released_to_authorized_recipient`, `access_blocked`; entrega histórica não prova leitura.
- `retention_disposition`: `pending_policy_review`, `retained_under_applicable_rule`, `deleted_when_due`, `not_applicable`, exigindo decisão competente.

Não substituir esses conceitos por um único `status` e não exibir “excluído” sem prova da operação real.

## 10. Falhas e riscos de arquitetura
| Risco | Controle proposto |
| --- | --- |
| Cache mantém relatório após revogação | Revogação propagada e reautorização na leitura |
| Modelo recebe contexto fora de escopo | Recuperação mediada com minimização e validação do serviço |
| Resposta antiga chega depois do bloqueio | CAP-10 e gateway rejeitam publicação/entrega |
| Profissional acessa notas de outro vínculo | Isolamento por Pessoa, tenant, finalidade e destinatário |
| Fonte é apagada, mas grafo conserva projeção | Política de projeções, invalidação e retenção coordenada |
| Consentimento genérico é reutilizado para novo produto | Verificação de finalidade e base legal por uso |
| Evento forjado dispara exclusão | Autenticidade de origem, versão e autoridade |
| Revogação é confundida com obrigação universal de apagar | Procedimento de retenção e direitos por finalidade |
| Dados pessoais entram em logs e fixtures | Minimização, separação e revisão de evidências |
| Serviço de autorização indisponível | Falha segura para operações sensíveis |

## 11. Cenários sintéticos candidatos (não executados)
| ID | Cenário | Oráculo mínimo |
| --- | --- | --- |
| INT05-A01 | Pessoa autoriza análise e não entrega a profissional | Relatório não é compartilhado |
| INT05-A02 | Parceiro tem contrato, mas não vínculo individual | Negar acesso |
| INT05-A03 | Vínculo expirado | Revalidar, não presumir renovação |
| INT05-A04 | Revogação entre geração e consulta | Bloquear nova consulta incompatível |
| INT05-A05 | Revogação durante tarefa assíncrona | Cessar uso indevido e não entregar |
| INT05-A06 | Evento de revogação duplicado | Idempotência |
| INT05-A07 | Evento chega fora de ordem | Aplicar versão canônica vigente |
| INT05-A08 | Informação autorizada apenas para sessão | Não reter como memória permanente sem política |
| INT05-A09 | Neo4j contém projeção de fonte revogada | Aplicar política de acesso e revisão de projeção |
| INT05-A10 | Profissional de outra instituição | Sem vazamento de existência ou conteúdo |
| INT05-A11 | Base legal não depende de consentimento | Não inventar fluxo de revogação de consentimento; avaliar direitos e base adequados |
| INT05-A12 | Retenção legal continua aplicável | Restringir uso incompatível sem declarar exclusão concluída |
| INT05-A13 | Dados pessoais em log de execução | Impedir telemetria excessiva |
| INT05-A14 | Modelo tenta ampliar escopo via prompt | Negar instrução não confiável |
| INT05-A15 | Pessoa corrige dado, sem revogar uso | Versionar fonte e invalidar análises dependentes |
| INT05-A16 | Gateway recebe referência de autorização forjada | Recusar solicitação |
| INT05-A17 | Serviço de autorização indisponível | Falha segura, sem autorização presumida |
| INT05-A18 | Relatório já entregue anteriormente | Registrar limite de controle e obrigações de destinatário sem afirmar recolhimento |

**Estado:** `planned` para todos os casos; resultados técnicos e adjudicações inexistentes.

## 12. Governança e pontos pendentes
**Decisões ainda necessárias:**
1. Determinar controladores, operadores e responsabilidades legais conforme cada produto e fluxo.
2. Catalogar finalidades e bases legais por categoria de dado e consumidor.
3. Aprovar política de consentimento quando aplicável, direitos da Pessoa e retenção.
4. Definir esquema canônico de autorização e autenticidade de eventos.
5. Identificar proprietário técnico de bloqueio, cache, Neo4j e auditoria.
6. Estabelecer tempos de propagação, compensação e tratamento de falhas.
7. Definir política para relatórios compartilhados e parceiros externos.
8. Formalizar responsáveis, evidências e gates G1/G2/G3 antes de integração.

**Próximo estudo recomendado:** **GAI-INT-06 — Modelo de Dependências, Eventos e Propagação de Invalidação**, para detalhar interações CAP-10 e contratos de eventos canônicos, ainda sem execução.

**Referências:** [Autoridade de Dados e Memória v0.8](autoridade-dados-memoria-contexto.md) · [GAI-INT-01](arquitetura-integrada-plano-validacao.md) · [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md) · [GAI-INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md) · [CAP-11](cap-11-relatorio-trajetoria-possibilidades.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Não houve processamento de dados pessoais, mudança em Replit, Neo4j, provedores ou GKR.**
