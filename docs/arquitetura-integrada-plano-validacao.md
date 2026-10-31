# GAI-INT-01 — Arquitetura Integrada e Plano de Validação
**Versão documental 2.5 · 31/10/2026**
**Estado:** estudo de coerência CAP-01–CAP-12. Não executado, não homologado, sem autorização operacional.

## 1. Síntese arquitetural
**Guivos Intelligence** orquestra a Jornada, perguntas e validação da Pessoa. **Guivos AI** executa análises especializadas e devolve resultados rastreáveis. **Serviços canônicos** controlam fatos, autorização, versões e oportunidades. **Neo4j** poderá projetar relações autorizadas, sem ser autoridade universal. **GPT/Claude/Gemini** são provedores técnicos, não fontes de verdade nem sistemas de memória. **GKR** é repositório independente.

A inspeção Replit v0.7 não demonstrou integração ponta a ponta da Jornada pública com cognição real e memória durável. Os testes sintéticos isolados não equivalem à homologação das capacidades.

## 2. Fluxos distintos
**Interno:** Pessoa → Jornada → Guivos Intelligence → autorização e contexto canônico → Guivos AI CAP-01–11 → Intelligence valida versão e apresenta à Pessoa.

**Externo:** parceiro autenticado → gateway CAP-12 → autorização por Pessoa/finalidade/tenant → Guivos AI homologada para o escopo → resposta mínima e rastreável.

Guivos Intelligence pode utilizar GPT/Claude/Gemini para funções gerais sem passar pela Guivos AI. Os modelos não recebem credenciais ou acesso direto irrestrito a Neo4j.

## 3. Dependências integradas
| Capacidades | Dependência | Cuidado |
| --- | --- | --- |
| CAP-01/02 | Contexto autorizado, versões, CAP-03/09 como controles | Não tratar ausência de registro como ausência do fato |
| CAP-03 | Claims, evidências e proveniência | Não usar consenso de modelos como fonte independente |
| CAP-04 | Condições CAP-02 + requisito identificado + CAP-03 | Não depender obrigatoriamente de CAP-05 |
| CAP-05 | CAP-01/02/03; CAP-04 opcional | Não exigir lacuna para gerar possibilidade |
| CAP-06 | Possibilidade CAP-05 ou declarada; CAP-04, evidências | Avaliar requisitos, não pessoas |
| CAP-07 | CAP-04/05/06; oferta CAP-08 opcional | Categoria não é oferta real |
| CAP-08 | Serviço canônico de oportunidades; CAP-03 | Publicação, verificação e disponibilidade são estados distintos |
| CAP-09 | Evidências CAP-03 e fontes | Classificar divergência sem votação entre modelos |
| CAP-10 | Eventos canônicos, versões e dependências | Invalidar derivadas impactadas, sem reprocessamento irrestrito |
| CAP-11 | Subconjunto pertinente CAP-01–10 | Gerar, validar e entregar são etapas separadas |
| CAP-12 | Capacidades habilitadas, autorização e isolamento | API interna não transfere privilégios ao parceiro |

CAP-03 e CAP-09 são verificações transversais, não exigências recursivas mútuas. CAP-10 governa validade do resultado, sem se tornar fonte canônica.

## 4. Achados da revisão documental
| ID | Achado | Tratamento proposto |
| --- | --- | --- |
| INT-01 | Referências CAP-04↔CAP-05↔CAP-06 podem formar ciclo | CAP-05 independente de lacuna; CAP-04 avalia requisito fornecido; CAP-06 integra |
| INT-02 | CAP-03/09 podem duplicar tratamento de conflito | CAP-03 avalia suporte; CAP-09 trata divergência |
| INT-03 | Estados de análise não são uniformes | Envelope e taxonomias por domínio |
| INT-04 | “Publicada”, “verificada”, “disponível” não são equivalentes | Estados separados na CAP-08 |
| INT-05 | Validação da Pessoa e consentimento de entrega não são equivalentes | Guardar eventos e autorizações distintos |
| INT-06 | Análises podem sobreviver a revisões | Dependências e invalidação CAP-10 |
| INT-07 | Consumo interno/B2B tem fronteiras diferentes | Identidade, finalidade, tenant e gateways separados |
| INT-08 | Memória Neo4j pode ser confundida com fato canônico | Mapear autoridade por tipo de dado |
| INT-09 | Respostas convergentes podem compartilhar fonte | Manter origem e linhagem |
| INT-10 | Contratos são exemplos, não schemas homologados | Formalizar e testar contratos |
| INT-11 | Gate da POC pode ser confundido com liberação especializada | Impedir promoção sem evidência de execução |
| INT-12 | Relatórios podem vazar conteúdo entre destinatários | Filtrar por escopo e reautorizar ao consultar |

**Status:** achados e propostas documentais, não decisões normativas aprovadas.

## 5. Envelope compartilhado proposto
Campos comuns: `request_id`, `capability_id`, `api_contract_version`, `method_version`, `subject_ref`, `consumer_ref`, `purpose`, `authorization_scope_ref`, `context_version`, `source_versions`, `as_of`, `analysis_id`, `claims`, `evidence_refs`, `unknowns`, `limitations`, `dependencies`, `generated_at` e `valid_until` quando aplicável.

**Estados separados:** execução (`lifecycle_status`), atualidade (`validity_status`), sustentação (`support_status`), escolha da Pessoa (`person_validation_status`), publicação da oferta (`publication_status`) e disponibilidade (`availability_status`). Não criar “status único” com semântica ambígua.

## 6. Cenários ponta a ponta propostos — não executados
| Caso | Fluxo | Critério crítico |
| --- | --- | --- |
| E2E-01 | Contribuição sintética → contexto versionado → CAP-01/02/03 → Intelligence | Pessoa pode corrigir; CAP-10 marca resposta antiga obsoleta |
| E2E-02 | CAP-05 sugere alternativa não declarada | Não atribuir desejo; recusa não significa incapacidade |
| E2E-03 | CAP-04/06 analisam requisito com condição desconhecida | Não declarar lacuna confirmada |
| E2E-04 | CAP-08 verifica oferta que depois expira | Não manter disponibilidade vigente nem descartar possibilidade geral |
| E2E-05 | CAP-11 gera relatório sem autorização de entrega | Bloquear compartilhamento ao terceiro |
| E2E-06 | Parceiro tenta acessar outra Pessoa/tenant via CAP-12 | Bloquear sem revelar informação |
| E2E-07 | Modelos divergem usando mesma fonte | Não resolver por votação nem contar cópias como evidências |
| E2E-08 | Revogação e nova revisão durante execução | Bloquear leitura e resposta obsoleta |

## 7. Gates de maturidade propostos
| Gate | Evidência requerida | Estado |
| --- | --- | --- |
| G0 | Autoridade e dependências revisadas | Parcial; pendências registradas |
| G1 | Schemas, versionamento e estados aprovados | Pendente |
| G2 | Autorizações, fontes, retenção e isolamento validados | Pendente |
| G3 | Fixtures sintéticas executadas com relatório e métricas | Pendente |
| G4 | Integração controlada ponta a ponta | Pendente |
| G5 | Revisão humana e adjudicação de riscos | Pendente |
| G6 | Aprovação explícita, observabilidade, rollback e custos | Pendente |

Nenhum gate é aprovado pela documentação isoladamente.

## 8. Decisões ainda não ratificadas
**INT-DEC-P01:** schema comum e taxonomia de estados; **P02:** autoridade por tipo de dado; **P03:** finalidade/revogação; **P04:** seleção multi-modelo e fallback; **P05:** invalidação entre capacidades; **P06:** atualidade das oportunidades; **P07:** revisão humana e homologação; **P08:** contratos B2B, retenção e privacidade.

Não incluir esses itens no registro de decisões como aprovados sem deliberação expressa.

## 9. Próximo trabalho
Recomenda-se **normalizar os contratos compartilhados e construir a matriz de testes e gates**, antes de qualquer desenvolvimento. Posteriormente, somente mediante autorização específica, comparar contratos ao código do Replit e propor integração em ambiente isolado.

**Referências:** [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [Fronteira AI/Intelligence](guivos-ai-vs-intelligence.md) · [Autoridade de Dados](autoridade-dados-memoria-contexto.md) · [Diagnóstico Replit](integracao-replit-intelligence-ai-neo4j.md) · [Avaliação](avaliacao-validacao-qualidade.md) · [CAP-12](cap-12-api-especializada-guivos-ai.md).

**GKR, Replit, Neo4j e gates permanecem inalterados.**
