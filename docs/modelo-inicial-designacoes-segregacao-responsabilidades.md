# GAI-INT-25 — Modelo Inicial de Designações e Segregação de Responsabilidades
**Versão documental 5.0 · 31/10/2026**
**Estado:** matriz proposta à direção da Guivos. Nenhuma nomeação pessoal, mandato técnico, aprovação de gate ou execução de teste.

## 1. Decisão de origem e limite
A [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) já estabeleceu a administração da Guivos, representada inicialmente por sua direção, como instância de **nomeações e decisões estratégicas iniciais**. Esta publicação **não substitui** um ato específico de nomeação. Ela organiza quais funções podem ter coordenação estratégica inicial, quais exigem titulares técnicos e quais devem receber revisão independente.

Os 16 slots em [GAI-INT-23](registro-ratificacao-titulares-alcadas-candidato.json) continuam sem indicação nominal. A classificação proposta abaixo não concede alçadas automaticamente.

## 2. Modelo de responsabilidade progressiva
| Categoria | Participação inicial possível da direção | Condição para atuação operacional |
| --- | --- | --- |
| Estratégia e prioridades | Definir agenda, riscos, orçamento proposto e decisões de produto | Registro de decisão dentro de competência institucional |
| Coordenação arquitetural | Patrocinar e designar responsável, inclusive temporário | Revisão técnica das ADRs e limites de dados |
| Serviços canônicos existentes | Identificar o titular real de cada serviço | Inventário técnico e aceite do proprietário |
| Identidade e autorização | Solicitar desenho e controles | Responsável de segurança + revisão de finalidades |
| Privacidade e bases legais | Definir prioridade e contratar/indicar análise | Parecer competente, não substituível por decisão comercial |
| Contratos e engenharia | Indicar equipe e critérios | Capacidade técnica verificada e controles de qualidade |
| Execução de testes | Autorizar somente escopo específico em decisão separada | Executor capacitado, ambiente isolado e evidências |
| Revisão independente | Nomear revisor apropriado | Ausência de conflito relevante e parecer documentado |
| Gate G0/G2/G5/G6 | Definir alçadas e escalonamento | Evidência própria de cada gate, revisão e decisão formal |

**Direção como instância de designação ≠ direção automaticamente responsável por todas as funções técnicas.**

## 3. Priorização de designações
**Grupo P0 — imediatamente necessário para evoluir G0:** instância da direção já definida; confirmar responsável de arquitetura, responsável por inventário de dados/serviços e responsável por governança de decisões. D21-01/PND-01 e D21-02/PND-11 só poderão encerrar quando os titulares, mandatos, provas de competência e aceites estiverem registrados.

**Grupo P1 — antes de qualquer fluxo com dados reais ou gate G2:** proprietário do serviço de identidade/autorização, segurança e parecer jurídico/privacidade. Distinguir processamento de compartilhamento, finalidade, tenant, revogação e retenção.

**Grupo P2 — antes de qualquer campanha de testes autorizada:** responsável por contratos e schemas, curadoria de fixtures, executor QA e revisor independente; obter autorização de campanha específica, com ambiente e critérios congelados.

**Grupo P3 — antes de integração ou disponibilização:** responsáveis por supply, evidências, relatórios/entrega, operação, observabilidade, incidentes e autoridades específicas de gates. Algumas responsabilidades existem em múltiplas ondas, mas o requisito de alçada não desaparece.

## 4. Matriz dos 16 slots e modalidade candidata
| Slot | Função | Encaminhamento |
| --- | --- | --- |
| ROLE-01 | Arquitetura | Direção pode coordenar e designar titular; revisão técnica necessária |
| ROLE-02 | Identidade | Especialista e proprietário de serviço a verificar |
| ROLE-03 | Contexto da Pessoa | Direção pode indicar coordenador temporário, sem autoridade factual implícita |
| ROLE-04 | Autorização e políticas | Especialista; controles de privacidade/segurança |
| ROLE-05 | Supply e oportunidades | Direção pode indicar coordenador temporário; fonte e disponibilidade devem ser verificadas |
| ROLE-06 | Evidências | Responsabilidade técnica de proveniência e integridade |
| ROLE-07 | Relatórios e entrega | Direção pode indicar coordenador; entrega requer autorização própria |
| ROLE-08 | Privacidade/jurídico | Parecer especializado e independente conforme risco |
| ROLE-09 | Segurança | Responsabilidade técnica especializada |
| ROLE-10 | Contratos | Engenharia especializada; revisão de schema e compatibilidade |
| ROLE-11 | QA executor | Executor técnico independente da decisão de aprovação |
| ROLE-12 | Revisor independente | Obrigação de independência e de avaliação de conflitos |
| ROLE-13 | Autoridade G0 | Direção deve definir alçada documental e evidências |
| ROLE-14 | Autoridade G2 | Alçada formal condicionada a pareceres técnicos/privacidade |
| ROLE-15 | Autoridade G5 | Alçada formal, distinta de revisão autoatribuída |
| ROLE-16 | Autoridade G6 | Alçada formal com critérios de liberação e rollback |

A [matriz JSON de alocação](matriz-designacoes-segregacao-candidata.json) conserva `nominee_ref=null` e `ratification_status=pending` para todos os slots.

## 5. Procedimento de designação pela direção
1. Registrar **qual função** será designada, seu domínio e escopo.
2. Identificar **pessoa/equipe indicada**, por referência controlada fora de dados pessoais publicamente expostos.
3. Verificar habilitação, eventual conflito e limitações de competência.
4. Registrar **aceite, mandato e prazo de vigência**, com alternativa de substituto.
5. Publicar somente decisão resumida e referências não sensíveis; manter documentos internos no sistema apropriado.
6. Atualizar `ratification_status` e PNDs apenas após evidência verificável, sem declarar gates aprovados.
7. Reavaliar nomeações quando o serviço, função ou autoridade mudar.

## 6. Matriz de segregação: quem propõe, executa, revisa e aprova
| Ato | Propõe | Executa | Revisa | Decide |
| --- | --- | --- | --- | --- |
| Arquitetura/contrato | Arquitetura | Engenharia | Responsável técnico e segurança quando aplicável | Alçada designada pela direção |
| Base/finalidade de processamento | Produto/dono do domínio | Serviço canônico | Privacidade e segurança | Autoridade competente, respeitadas obrigações legais |
| Fixture sintética e runner | QA/contratos | Executor autorizado | Revisor independente | Autoridade da campanha, se designada |
| Gate G2 | Segurança/owner de dados | Equipes técnicas | Segurança/privacidade e evidências | Autoridade G2 ratificada |
| Gate G5 | QA/governança | Responsáveis por avaliações | Revisor independente/adjudicador | Autoridade G5 ratificada |
| Gate G6/release | Operações/produto | Engenharia/operadores | Segurança, privacidade, QA e operação | Autoridade G6 ratificada |

**Não é obrigatório formar equipes separadas para cada linha**, mas exceções de independência devem ser formalmente tratadas. Não se considera aceitável a única pessoa executar, revisar e aprovar evidência crítica sem controle compensatório aprovado.

## 7. Condições materiais de evolução
- **GAI-DEC-009 está confirmada** em seu escopo de governança estratégica.
- **PND-01 e PND-11 estão abertas**, porque ainda não há ratificação de proprietários e alçadas específicas.
- As outras 14 decisões pendentes não são alteradas.
- G0 permanece parcial; G1–G6 permanecem pendentes.
- Os 19 schemas e 49 fixtures sintéticas permanecem sem execução verificada. Não foi concedida autorização para testar, usar dados reais ou acessar sistemas externos.

## 8. Próxima ação verificável
A direção poderá **indicar formalmente a primeira função de coordenação técnica/arquitetural** e a função responsável pelo inventário dos serviços canônicos, associando os respectivos mandatos e aceites. Uma vez identificados, será possível verificar as fontes reais e reduzir bloqueios de G0, sem confundir isso com implantação.

**Referências:** [GAI-DEC-009](decisao-instancia-governanca-direcao-guivos.md) · [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md) · [GAI-INT-22](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md) · [Registro de Decisões](registro-decisoes.md).

**Nenhuma alteração operacional no Replit, Neo4j, provedores ou GKR.**
