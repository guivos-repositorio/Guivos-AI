# GAI-CAP-12 — API Especializada da Guivos AI
**Especificação de capacidade · Versão documental 2.4 · 31/10/2026**
**Estado:** proposta conceitual de contratos e governança. Não é API implementada, serviço operacional, disponibilidade comercial ou autorização de integração.

## 1. Propósito
Estabelecer a camada contratual de consumo das **capacidades especializadas da Guivos AI**, por serviços internos do ecossistema e, em escopos estritamente autorizados, por aplicações e profissionais parceiros. A API disponibilizará **resultados analíticos fundamentados** em vez de acesso indiscriminado ao histórico pessoal ou às bases canônicas.

A Guivos AI **não é um quarto modelo de linguagem fundacional**: ela usa métodos especializados e pode utilizar adaptadores de GPT, Claude e Gemini. **Guivos Intelligence** é o orquestrador da experiência da Jornada; as fontes canônicas do ecossistema são responsáveis por fatos, identidade, permissões e revisões.

## 2. Dois domínios de consumo distintos
| Dimensão | API interna Guivos Intelligence → Guivos AI | API especializada para parceiros |
| --- | --- | --- |
| Consumidor | Serviço autenticado do ecossistema | Aplicação, instituição ou profissional credenciado |
| Finalidade | Compreensão, exploração e validação na Jornada | Caso de uso contratado e explicitamente permitido |
| Autoridade | Identidade de serviço + autorização da Pessoa e política da finalidade | Identidade do parceiro + vínculo/escopo + autorização específica aplicável |
| Dados | Apenas contexto autorizado resolvido por serviço canônico | Respostas mínimas, segregadas por parceiro, propósito e Pessoa |
| Capacidades | Catálogo interno aprovado por capacidade | Subconjunto explicitamente licenciado/homologado |
| Apresentação | Guivos Intelligence valida com a Pessoa e gerencia estado | Parceiro deve cumprir obrigações de apresentação e limites |
| Revisões | Propagação de versões, invalidação e cancelamento | Eventos/consultas de status, expiração e revogação controladas |
| Segurança | Autenticação serviço a serviço, autorização por finalidade | Segregação de tenants, auditoria, escopos e limites de consumo |

**Mesma família especializada, superfícies contratuais diferentes.** Acesso interno não pode ser reutilizado como atalho para fornecer dados ao parceiro.

## 3. Fronteiras de autoridade e topologia proposta
1. **Pessoa/organização:** exerce direitos, informa contexto, valida escolhas e compartilha conforme regras aplicáveis.
2. **Serviços canônicos:** identidade, vínculos, autorizações, registros, oportunidades, revisões e retenção.
3. **Camada autorizada de contexto/memória:** recupera evidências, eventualmente com Neo4j como projeção relacional, sem promover grafo a autoridade universal.
4. **Guivos AI:** executa CAP-01 a CAP-11 conforme método e versões homologadas para o consumidor.
5. **Guivos Intelligence:** chama a API interna e orquestra interface, perguntas, validação e controles da Jornada.
6. **Gateway de parceiro:** autentica, autoriza e limita solicitações externas; nunca concede por si acesso a fatos que o serviço de autorização negou.

Provedores GPT/Claude/Gemini não recebem credenciais canônicas da Guivos, não consultam diretamente Neo4j e não se tornam controladores automáticos da memória.

## 4. Capacidades candidatas expostas
| Família | Uso possível | Restrições |
| --- | --- | --- |
| CAP-01/02 | Síntese de trajetória e momento | Finalidade, minimização, atribuição de fonte |
| CAP-03/09 | Suporte de afirmações e divergências | Fontes autorizadas e estado de revisão |
| CAP-04/06 | Condições e compatibilidade futura | Não atribuir déficit pessoal nem score humano |
| CAP-05/07 | Possibilidades e caminhos intermediários | Interesse a validar; não garantir sucesso |
| CAP-08 | Qualificação de oportunidade | Oferta/estoque/prazo precisam de fonte competente |
| CAP-10 | Status de validade e reavaliação | Propagar obsolescência e revogações |
| CAP-11 | Relatório de Trajetória e Possibilidades | Autorização separada para geração e entrega |

**Nenhuma capacidade está homologada.** Documentar rota candidata não significa criar endpoint operacional.

## 5. Operações lógicas candidatas — sem fixar URLs definitivas
- **Descobrir capacidades habilitadas:** catálogo por consumidor, versão e finalidade.
- **Solicitar análise:** capacidade, sujeito pseudônimo, finalidade, versão de contexto e escopos; preferir referências a dados brutos.
- **Consultar estado de processamento:** pendente, executando, aguardando revisão, finalizado, falhou, cancelado ou obsoleto.
- **Consultar resultado:** apenas se a autorização ainda é vigente, a versão é compatível e o destinatário pode acessar os campos.
- **Solicitar relatório:** CAP-11 sob autorização de processamento e de entrega separadas.
- **Consultar validade:** versão, expiração, invalidação ou substituição.
- **Cancelar processamento:** melhor esforço e bloqueio de publicação; observar tarefas já concluídas e políticas de retenção.
- **Receber aviso de alteração:** evento autenticado, limitado ao que o parceiro está autorizado a saber; alternativamente consulta de status.
- **Consultar consumo:** métricas de serviço e cobrança agregada, sem expor outros sujeitos.

**Revogar consentimento não é endpoint sob autoridade autônoma da Guivos AI:** o serviço competente recebe e decide a revogação; a Guivos AI propaga os efeitos analíticos via CAP-10.

## 6. Fluxo de chamada interno proposto
1. A Jornada obtém contribuições da Pessoa pelos serviços canônicos.
2. Guivos Intelligence identifica tarefa e capacidade especializada, valida finalidade e versão.
3. Serviço de identidade/autorização verifica acesso e limites da solicitação.
4. Camada de contexto fornece conjunto mínimo de fontes autorizadas.
5. Guivos AI executa capacidade homologada, podendo chamar provedores através de adaptadores controlados.
6. CAP-03/09 qualificam suporte e conflitos; CAP-10 controla atualidade e invalidação.
7. Resposta contém estado, versão de contexto, referências, incertezas e limites.
8. Guivos Intelligence rejeita respostas obsoletas, pergunta e valida direcionamento com a Pessoa.

O diagnóstico v0.7 da Jornada indica que esse encadeamento **não está operacional na interface pública atual do Replit**.

## 7. Fluxo de parceiro e autorização
1. Parceiro é autenticado e sua organização/aplicação é identificada.
2. Contrato de finalidade e capacidades permitidas é verificado.
3. Vínculo profissional e acesso individual são avaliados pelo serviço canônico.
4. Autorização de processamento é verificada **por solicitação**, com prazo e escopo; para relatório, autorização de compartilhamento/entrega é separada.
5. Gateway aplica isolamento de tenant, rate limits, custo/uso, minimização e logs apropriados.
6. Guivos AI executa somente capacidade homologada para esse escopo.
7. Resposta é filtrada para o consumidor e nunca inclui registro de outro tenant.
8. Correção/revogação invalida acesso e derivados segundo política, inclusive caches e entregas futuras.

**Cadastro ou contrato comercial de parceiro não equivale à autorização da Pessoa.**

## 8. Envelope lógico de requisição — exemplo sintético
```json
{
  "request_id": "synthetic-request-001",
  "api_contract_version": "proposed-v1",
  "capability": "GAI-CAP-02",
  "capability_version": "approved-version-if-any",
  "purpose": "current_moment_understanding",
  "consumer_ref": "synthetic-internal-service",
  "subject_ref": "pseudonymous-person-ref",
  "processing_authorization_ref": "server-validated-scope-ref",
  "context_version": "revision-101",
  "as_of": "2026-10-31T13:00:00-03:00",
  "requested_output_scope": ["summary", "unknowns", "limitations"],
  "idempotency_key": "synthetic-idempotency-key"
}
```
O envelope é apenas ilustrativo. Campos declarados pelo consumidor não comprovam autorização; gateway e serviços autorizados devem verificar contexto e vínculos. Nenhuma credencial é incluída.

## 9. Envelope lógico de resultado — exemplo sintético
```json
{
  "request_id": "synthetic-request-001",
  "analysis_id": "synthetic-analysis-101",
  "api_contract_version": "proposed-v1",
  "capability": "GAI-CAP-02",
  "context_version": "revision-101",
  "status": "needs_person_validation",
  "validity": "valid_for_recorded_context",
  "result": {
    "summary": "Síntese contextual limitada aos relatos disponíveis.",
    "claim_refs": ["synthetic-claim-1"],
    "unknowns": ["Preferência de modalidade não informada"],
    "limitations": ["Não houve verificação externa da declaração."]
  },
  "generated_at": "2026-10-31T13:00:00-03:00",
  "method_version": "proposed-1",
  "authorization_checked": "at_request",
  "delivery_status": "not_released"
}
```
Os valores exemplificam o **formato desejado**, não uma execução real. O retorno deverá ser filtrado e reautorizado antes de qualquer recuperação por destinatário.

## 10. Estados assíncronos, consistência e idempotência
Estados candidatos: `accepted`, `queued`, `processing`, `awaiting_review`, `completed`, `failed`, `cancelled`, `stale`, `blocked_by_authorization`.

- Solicitações repetidas com a mesma chave dentro do escopo definido não devem provocar duplicidade indevida.
- Reprocessamento deve indicar nova versão e dependências.
- Resposta antiga não pode substituir contexto recente.
- Timeout de gateway não prova que tarefa foi cancelada; consultar estado, se permitido.
- Falha de provedor não autoriza resposta fabricada nem fallback a modelo sem aprovação para aquela finalidade.
- Falhas parciais devem indicar cobertura e limitações, sem mascarar ausência de fontes.
- Retentativas, TTLs e timeouts permanecem parâmetros a definir e testar.

## 11. Segurança e privacidade
**Controles propostos:** autenticação forte de serviço/aplicação; autorização por ação/finalidade/sujeito/tenant; escopos mínimos; segregação de dados profissionais; proteção contra acesso a objetos de outros usuários; prevenção de replay; rotação de credenciais; limites de uso e custo; logs minimizados; criptografia em trânsito e repouso conforme arquitetura aprovada; políticas de retenção e descarte.

Requisitos adicionais:
- Não aceitar URLs de fontes fornecidas pelo parceiro como acesso irrestrito a rede interna/arquivos.
- Validar schema, tamanho, formato e content-type de entradas; tratar anexos como dados não confiáveis.
- Nunca usar prompts ou documentos como instruções de autoridade para conceder acesso, ignorar escopo ou modificar estado.
- Não devolver mensagens de erro com dados de outras Pessoas, segredos, tokens ou configuração interna.
- Classificar e controlar dados sensíveis; usos clínicos exigem governança separada.
- Evitar armazenamento de conteúdo pessoal bruto em telemetria e repositório de documentação.
- Não comercializar acesso a dados pessoais: monetização poderá abranger capacidades analíticas contratadas, conforme legislação e consentimentos/bases pertinentes.

## 12. Erros e respostas de segurança
| Tipo | Significado | Comportamento |
| --- | --- | --- |
| `unauthenticated` | Identidade do serviço não comprovada | Negar solicitação |
| `forbidden` | Finalidade, vínculo ou acesso não permitido | Negar sem revelar dados |
| `capability_not_enabled` | Capacidade não homologada/habilitada | Não executar |
| `invalid_contract` | Dados/versão/escopo inválidos | Retornar erro sanitizado |
| `context_version_conflict` | Contexto não corresponde à versão | Não promover resultado obsoleto |
| `rate_limited` | Consumo acima do limite autorizado | Adiar/rejeitar conforme contrato |
| `upstream_unavailable` | Serviço canônico, modelo ou contexto indisponível | Falha segura, sem inventar resultado |
| `needs_review` | Resultado não elegível a entrega | Exigir revisão, não publicar |
| `access_revoked` | Revogação válida | Bloquear novas leituras e encaminhar efeitos à CAP-10 |

Códigos HTTP, formatos exatos, mensagens de erro, SLAs e garantias de entrega serão definidos em contrato técnico futuro.

## 13. Versionamento e compatibilidade
Distinguir:
- **`api_contract_version`:** forma externa da requisição e resposta;
- **`capability_version`:** comportamento funcional da capacidade;
- **`method_version`:** implementação/metodologia analítica;
- **`context_version`:** versão do contexto autorizado;
- **`analysis_version`:** revisão do resultado;
- **`source_versions`:** versões dos fatos/requisitos associados.

Mudanças incompatíveis exigirão estratégia de migração e descontinuação com notificação, testes de compatibilidade e consumidores identificáveis. Não presumir que todos os produtos suportam sempre as mesmas versões.

## 14. Observabilidade e economia unitária
Métricas candidatas, separadas por capacidade, consumidor e tenant autorizado: sucesso técnico, latência, custo por análise, tokens/provedores, erros, bloqueios de autorização, respostas obsoletas suprimidas, revisões humanas, custo de armazenamento e taxa de invalidação.

Não incluir dados identificáveis em dashboards agregados e não comparar valor da Pessoa por métricas operacionais. Preços, quotas, metas, disponibilidade comercial e acordos de nível de serviço permanecem hipóteses.

## 15. Avaliação sintética — casos candidatos não executados
| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| CAP12-E01 | Intelligence solicita capacidade aprovada e escopo válido | Contrato e autorização verificados |
| CAP12-E02 | Parceiro autenticado sem vínculo autorizado com Pessoa | Acesso negado |
| CAP12-E03 | Parceiro possui contrato, mas sem autorização de finalidade | Acesso negado |
| CAP12-E04 | Relatório gerado sem autorização de compartilhamento | Entrega bloqueada |
| CAP12-E05 | Pedido em capacidade não homologada | `capability_not_enabled` |
| CAP12-E06 | IDs de outro tenant em requisição | Bloqueio sem vazamento |
| CAP12-E07 | Alteração do contexto durante execução | Resultado antigo não promovido |
| CAP12-E08 | Revogação entre execução e recuperação | Nova verificação e acesso bloqueado |
| CAP12-E09 | Chamada repetida com mesma chave idempotente | Sem efeito duplicado |
| CAP12-E10 | Timeout com job ainda executando | Status explícito, sem afirmar cancelamento |
| CAP12-E11 | Neo4j/serviço canônico indisponível | Falha segura |
| CAP12-E12 | GPT falha; fallback não autorizado | Não substituir silenciosamente por outro modelo |
| CAP12-E13 | API tenta obter histórico bruto sem escopo | Negar |
| CAP12-E14 | Saída contém afirmação sem suporte | CAP-03/09 impedem apresentação como fato |
| CAP12-E15 | Relatório antigo acessado após invalidação | Informar estado ou bloquear uso atual |
| CAP12-E16 | Dado clínico não necessário em payload | Minimizar/rejeitar |
| CAP12-E17 | Entrada contém instrução maliciosa em documento | Tratar como dado, não autoridade |
| CAP12-E18 | Parceiro ultrapassa quota/custo | Aplicar limite |
| CAP12-E19 | Versionamento incompatível de contrato | Erro tipado/migração apropriada |
| CAP12-E20 | Cancelamento enquanto job conclui | Resolver estado sem publicação não autorizada |
| CAP12-E21 | Callback com assinatura inválida | Rejeitar |
| CAP12-E22 | Status de oportunidade expirou | CAP-08/10 impedem alegação vigente |
| CAP12-E23 | Telemetria recebe dados pessoais indevidos | Bloquear e registrar falha de privacidade |
| CAP12-E24 | Profissional tenta ler notas segregadas de outro vínculo | Bloquear por escopo |

Antes de homologação: definir autoridade dos gates, contrato formal, requisitos de segurança, testes de isolamento, avaliação semântica, testes de carga, custo, observabilidade, regressão, rollback e revisão humana. Nenhum dos 24 casos foi executado.

## 16. Dependências e decisões pendentes
- Identidade, vínculos e consentimentos/autorização por finalidade;
- Fonte canônica, contexto versionado, acesso controlado a memória e Neo4j;
- Capacidades CAP-01 a CAP-11 homologadas por uso específico;
- Publicação/expiração de oportunidades no serviço competente;
- Política de armazenamento e revisão de relatórios;
- Gateway, filas, mecanismos de reprocessamento, métricas e controle de custos;
- Contrato para eventos de invalidação e revogação;
- Contratos comerciais e obrigações de parceiros;
- Autoridade dos gates e critérios para transição da POC à operação.

## 17. Revisão integrada após as 12 capacidades
Com a CAP-12, completa-se a **primeira rodada documental das doze capacidades GAI-CAP-01 a 12**, sem caracterizar implementação. Próximo estudo recomendado: **arquitetura integrada e plano de validação**, com dependências, contratos comuns, cenários ponta a ponta e definição explícita de gates antes de desenvolver ou conectar produção.

**Referências:** [Documento Mestre](index.md) · [Matriz](matriz-capacidades-guivos-ai.md) · [Produto e API](produto-api.md) · [CAP-11](cap-11-relatorio-trajetoria-possibilidades.md) · [Papéis AI/Intelligence](guivos-ai-vs-intelligence.md) · [Autoridade de Dados](autoridade-dados-memoria-contexto.md) · [Integração Replit](integracao-replit-intelligence-ai-neo4j.md) · [Avaliação](avaliacao-validacao-qualidade.md).

**GKR e Replit permanecem inalterados. Não existe API externa operacional autorizada por este documento.**
