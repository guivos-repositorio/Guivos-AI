# GAI-INT-08 — Catálogo Formal de Schemas e Compatibilidade entre Serviços
**Versão documental 3.2 · 31/10/2026**
**Estado:** três schemas candidatos em JSON Schema Draft 2020-12 publicados para revisão técnica. Não homologados, não utilizados por serviços e não validados em integração.

## 1. Objetivo
Converter a parte comum dos contratos lógicos definidos em [GAI-INT-02](normalizacao-contratos-estados-compartilhados.md), [GAI-INT-07](contratos-eventos-projecao-dependencias.md) e [CAP-12](cap-12-api-especializada-guivos-ai.md) em **artefatos JSON Schema versionados, legíveis e passíveis de validação por ferramentas futuras**. Um schema candidato valida estrutura, **não comprova autorização, veracidade, segurança ou compatibilidade semântica do resultado**.

## 2. Catálogo inicial, candidate-v1
| Artefato | Responsabilidade | Caminho |
| --- | --- | --- |
| AnalysisRequest | Envelope de solicitação de capacidade, versão do contrato, finalidade, referências e contexto | [analysis-request.schema.json](../schemas/candidate-v1/analysis-request.schema.json) |
| AnalysisResponse | Envelope de resultado e estados independentes de execução, validade e evidências | [analysis-response.schema.json](../schemas/candidate-v1/analysis-response.schema.json) |
| CanonicalEvent | Eventos originados em serviços canônicos, com origem, agregado, versão e payload restrito | [canonical-event.schema.json](../schemas/candidate-v1/canonical-event.schema.json) |

**Versão:** `candidate-1` indica contrato não aprovado, distinto da versão documental 3.2. Os `$id` são identificadores propostos, sem garantia de hospedagem operacional nem publicação como API.

## 3. Contratos e limites
### AnalysisRequest
Campos exigidos: `request_id`, `api_contract_version`, `capability_id`, `consumer_ref`, `subject_ref`, `purpose`, `authorization_scope_ref`, `context_version`, `as_of`, `input_refs`.

O schema exige presença e formato básico; o backend deverá verificar autorização, identidade, relação entre consumidor e Pessoa, finalidade, versões e escopo. Uma referência fornecida pelo cliente não concede permissão.

### AnalysisResponse
Campos exigidos: `request_id`, `analysis_id`, `api_contract_version`, `capability_id`, `context_version`, `lifecycle_status`, `validity_status`, `support_status`, `claims`, `limitations`, `generated_at`.

Execução concluída não equivale a informação comprovada, atual ou autorizada para exibição. Claims carregam tipo epistêmico e suporte. `result` ainda é objeto extensível: **não há schema completo por CAP**, que precisa ser desenvolvido separadamente.

### CanonicalEvent
Campos exigidos: `event_id`, `event_type`, `schema_version`, `producer_service_ref`, `aggregate_ref`, `aggregate_version`, `occurred_at`, `recorded_at`, `payload_ref`.

O schema não autentica emissor nem comprova legitimidade do evento. `payload_ref` deve ser resolvido por serviço autorizado, não pelo modelo de linguagem.

## 4. Convenções e política de compatibilidade proposta
- **Evolução aditiva:** novos campos opcionais poderão ser tolerados apenas se as políticas de validação e os consumidores os suportarem. Nesta primeira candidatura, `additionalProperties:false` nos envelopes exige revisão explícita; portanto adicionar campo pode exigir nova versão.
- **Quebra incompatível:** renomear campo obrigatório, alterar enum, mudar significado de estado ou enfraquecer restrição de autorização exige nova versão, migração e testes.
- **`schema_version` vs `api_contract_version`:** contratos de eventos e contratos de análise possuem ciclos separados.
- **Versionamento semântico:** versões de método, contexto, fonte, análise e relatório não substituem versões de contrato.
- **Temporalidade:** timestamps seguem `date-time`; validadores deverão ativar verificação de formato e exigir offset/fuso de forma normativa.
- **Ausência, nulo e desconhecido:** são distintos; uso de `null` está permitido somente em campos específicos do candidato.
- **Projeções Neo4j:** schemas de eventos não são schemas físicos do grafo.

## 5. Lacunas conhecidas no catálogo
| ID | Lacuna | Encaminhamento |
| --- | --- | --- |
| SCH-01 | `result` não tipado por CAP-01–11 | Definir schemas específicos antes de G1 |
| SCH-02 | Claims permitem propriedades extras | Formalizar esquema de afirmação e referência |
| SCH-03 | Permissões verificadas somente semanticamente | Definir contratos com serviços canônicos e testes de acesso |
| SCH-04 | Enumeração de eventos limitada ao catálogo atual | Revisar donos dos domínios e extensibilidade |
| SCH-05 | Contrato de recibo/event acknowledgment ausente | Especificar `EventReceipt` e reconciliação |
| SCH-06 | Contrato de dependência/projeção ausente | Especificar `DependencyEdge` antes de banco físico |
| SCH-07 | Erros e resultado parcial não têm schema próprio | Criar erros tipados e política de `oneOf` |
| SCH-08 | Não há OpenAPI/AsyncAPI homologada | Gerar somente após decisões normativas |
| SCH-09 | Timestamps com formato sem regra operacional de offset | Definir perfil de validação restritivo |
| SCH-10 | Não existem suites automatizadas de conformidade | Preparar fixtures e execução sob gate próprio |

Essas lacunas são **achados documentais**, não bugs observados em produção.

## 6. Matriz de compatibilidade proposta
| Origem → destino | Contrato candidato | Teste obrigatório futuro |
| --- | --- | --- |
| Intelligence → Guivos AI | AnalysisRequest | Escopo, versão, método, contexto e identidade |
| Guivos AI → Intelligence | AnalysisResponse | Separação entre validade, suporte, execução e validação da Pessoa |
| Parceiro → gateway → Guivos AI | AnalysisRequest filtrado | Isolamento por tenant, vínculo, finalidade e limite de capacidade |
| Guivos AI → gateway → parceiro | AnalysisResponse filtrado | Não expor claims/fontes não autorizadas |
| Serviços canônicos → consumidor de eventos | CanonicalEvent | Emissor autenticado, idempotência e ordenação por agregado |
| CAP-10 → consumidores/caches | Futuro contrato de recibo | Comprovar aplicação, não só recebimento |

## 7. Cenários de conformidade — ainda não executados
| ID | Verificação esperada |
| --- | --- |
| INT08-S01 | Requisição com `request_id` ausente falha validação |
| INT08-S02 | Capacidade fora de CAP-01–12 falha validação |
| INT08-S03 | Versão de contrato diferente de candidate-1 falha |
| INT08-S04 | Campo extra na requisição é recusado |
| INT08-S05 | Resposta sem `support_status` é recusada |
| INT08-S06 | `completed` + `unsupported` passa estruturalmente mas não habilita afirmação factual |
| INT08-S07 | Evento sem origem ou versão é recusado |
| INT08-S08 | Event ID repetido passa esquema, mas deve falhar/ser deduplicado na camada operacional |
| INT08-S09 | Escopo forjado passa formato, mas deve falhar autorização |
| INT08-S10 | Resultado de outro tenant passa forma, mas é bloqueado na camada de domínio |
| INT08-S11 | Offset temporal ausente é analisado conforme perfil estrito futuro |
| INT08-S12 | Evento de revogação não implica exclusão sem política |
| INT08-S13 | Resposta antiga não substitui nova mesmo quando ambas são válidas estruturalmente |
| INT08-S14 | Oferta publicada não é automaticamente disponível |
| INT08-S15 | Compartilhamento CAP-11 exige autorização própria |
| INT08-S16 | Evolução de enum é testada quanto a incompatibilidade |
| INT08-S17 | Provedor indisponível produz erro seguro, não JSON de sucesso fabricado |
| INT08-S18 | Entrada de outro sujeito não autoriza consulta de fontes |

Nenhum cenário foi executado. Os casos S06 e S08–S18 ilustram que **validação estrutural não é validação semântica, de segurança ou operacional**.

## 8. Critérios para aprovação futura (G1–G3)
- Revisão de modelos de dados e enumerações por donos de domínio;
- Testes automatizados de schema em validador Draft 2020-12;
- Análise de compatibilidade com consumidores internos e externos;
- Schemas tipados de claims, erros, eventos, recibos, dependências e payloads especializados;
- Revisão de segurança de referências, autenticação, isolamento e revogação;
- Fixtures sintéticas com resultados observados e adjudicação humana;
- Aprovação explícita por responsáveis nomeados.

**G1, G2, G3 e posteriores continuam pendentes.** A criação de JSONs de schema não demonstra a passagem de nenhum gate.

## 9. Próxima etapa
**GAI-INT-09 — Schemas Especializados, Contratos de Erro e Recibos de Eventos** é o próximo estudo recomendado para completar os campos específicos das capacidades, contratos de falha e confirmação de propagação, mantendo o escopo documental.

**Referências:** [INT-02](normalizacao-contratos-estados-compartilhados.md) · [INT-07](contratos-eventos-projecao-dependencias.md) · [INT-03](matriz-testes-integrados-criterios-aceite-gates.md) · [INT-04](catalogo-fixtures-rubricas-adjudicacao.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**Nenhum endpoint foi ativado, nenhuma integração ao Replit/Neo4j foi realizada e o GKR permanece independente.**
