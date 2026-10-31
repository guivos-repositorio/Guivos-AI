# GAI-CAP-11 — Relatório de Trajetória e Possibilidades
**Especificação de capacidade · Versão documental 2.3 · 31/10/2026**
**Estado:** conceituada. Produto, contratos, fluxo de acesso e testes são propostas; sem implementação, homologação ou disponibilização comercial.

## 1. Finalidade do relatório
A CAP-11 integra resultados autorizados de capacidades especializadas da Guivos AI em um **relatório compreensível, verificável, contextual e revisável**, para apoiar a Pessoa e, quando expressamente autorizado, orientadores, mentores e outros profissionais legitimamente vinculados.

**Não é** laudo, diagnóstico psicológico/psiquiátrico, instrumento de seleção automática, avaliação de mérito, sentença sobre potencial humano ou promessa de evolução. A análise deverá representar alternativas, evidências, incertezas, limites de aplicação e escolhas da Pessoa.

O produto conceitual inicial é o **Relatório de Trajetória e Possibilidades**, já descrito em [relatorio.md](relatorio.md). Este documento detalha sua capacidade analítica e contratos de governança, sem revogar o estudo anterior.

## 2. Consumidores e papéis
| Ator | Papel permitido | Limite |
| --- | --- | --- |
| Pessoa | Contribuir, revisar, validar suas declarações e escolhas, contestar interpretação | Não ser obrigada a concordar com hipóteses ou direcionamento |
| Guivos Intelligence | Solicitar geração, conduzir validação e apresentação durante a Jornada | Não acessar informações fora da finalidade autorizada |
| Guivos AI | Integrar análises especializadas, consolidar proveniência e gerar o artefato lógico | Não se tornar autoridade sobre os fatos originais |
| Profissional autorizado | Ler conteúdo específico ao acompanhamento, registrar observações segregadas | Vínculo profissional não garante acesso total ou permanente |
| Serviços canônicos | Validar identidade, autorização, finalidade, fontes e versões | Devem controlar revogação e acesso |
| API comercial (futura) | Solicitar relatório conforme contrato e escopo específicos | Não pode obter histórico bruto ou dados de terceiros por padrão |

## 3. Estrutura lógica do relatório
A estrutura deve ser **modular**: nem toda seção será exibida ou preenchida quando o caso de uso, a autorização ou as fontes não justificarem.

1. **Identificação e finalidade:** identificador da Pessoa, consumidor, profissional (se houver), finalidade e janela temporal — preferir IDs pseudônimos conforme meio de entrega.
2. **Escopo autorizado:** fontes usadas, dados excluídos, versão e limitações de compartilhamento.
3. **Síntese do momento atual:** contexto, condições, preferências, objetivos e desconhecidos (CAP-02).
4. **Trajetória documentada:** acontecimentos e mudanças atribuídos às fontes e períodos (CAP-01).
5. **Evidências e graus de sustentação:** afirmações, fontes, justificativas e contraprovas, quando pertinentes (CAP-03).
6. **Lacunas contextuais:** requisitos, condições atendidas/não atendidas e informações desconhecidas (CAP-04).
7. **Possibilidades futuras:** declaradas, adjacentes, emergentes e exploratórias, sem atribuir desejo indevido (CAP-05).
8. **Compatibilidade condicional:** cenários e requisitos por caminho, sem pontuação global da Pessoa (CAP-06).
9. **Caminhos intermediários:** rotas opcionais, etapas, Direct/Enabling Supply e dependências (CAP-07).
10. **Oportunidades concretas:** somente ofertas verificadas, com fonte, status e limitações (CAP-08).
11. **Incertezas e contradições:** divergências substantivas e questões não resolvidas (CAP-09).
12. **Estado de atualização:** referências de versão, resultados substituídos e necessidade de reavaliação (CAP-10).
13. **Perguntas e aprofundamento:** perguntas não indutivas para Pessoa/profissional, com separação clara entre dúvida e hipótese.
14. **Validação, limites e próximos passos:** confirmações e correções da Pessoa, cautelas de uso e escolhas que permanecem abertas.

Um relatório não deve preencher lacunas com texto genérico para aparentar completude. Se informações fundamentais estiverem indisponíveis, declarar cobertura limitada ou não gerar determinada seção.

## 4. Categorias de afirmações no relatório
| Tipo de conteúdo | Formulação admissível | Vedação |
| --- | --- | --- |
| Fato observado no sistema | “Há registro de abertura da oferta em...” | Abertura = participação ou interesse confirmado |
| Declaração atribuída | “A Pessoa relatou...” | Converter relato em verificação externa automática |
| Interpretação fundamentada | “Os registros sugerem..., considerando...” | Apresentar como verdade definitiva |
| Hipótese exploratória | “Uma possibilidade a investigar é...” | Atribuir desejo oculto |
| Lacuna confirmada | “O requisito X não é atendido nesta condição...” | Tratar como deficiência pessoal |
| Informação desconhecida | “Não há dados suficientes sobre...” | Inferir ausência de experiência/capacidade |
| Oportunidade qualificada | “A oferta está publicada; disponibilidade não confirmada.” | Prometer vaga, acesso ou resultado |
| Decisão da Pessoa | “A Pessoa optou por explorar/adiar...” | Interpretar recusa como autossabotagem |

A forma de linguagem deverá variar segundo público e finalidade, mas não deverá alterar a classificação epistêmica ou apagar limitações.

## 5. Requisitos de rastreabilidade e integridade
Cada seção/afirmação relevante deverá associar:
- `claim_id`, `source_refs`, `source_versions` e classe epistêmica;
- `analysis_id`, `capability_id`, `method_version`, `context_version`;
- data e período de validade, quando aplicáveis;
- status de revisão, contradição, consentimento ou autorização;
- grau de suporte descritivo e explicação verificável;
- referência de substituição/invalidação, quando houver.

Não incluir raciocínio privado oculto de modelos; apresentar **justificativa concisa verificável com evidências**, adequada ao leitor autorizado. Uma mesma evidência não ganha independência por ter sido resumida por vários modelos.

## 6. Processo conceitual de geração
1. **Solicitação:** Guivos Intelligence ou consumidor autorizado apresenta finalidade, público, seções solicitadas, horizonte e versão de contexto.
2. **Autorização:** serviço competente valida identidade, relação, consentimentos/bases aplicáveis, finalidade, prazo e escopo de dados.
3. **Composição:** Guivos AI recebe somente resultados de capacidades elegíveis e suas referências, com versões e limitações.
4. **Verificação:** CAP-03/09 examinam afirmações, contradições, informações desconhecidas e vínculos com fontes.
5. **Atualidade:** CAP-10 impede reutilizar resultados vencidos ou incompatíveis com `context_version` corrente.
6. **Minimização:** remover conteúdo não necessário ao propósito ou não permitido ao destinatário; segregar notas de profissionais.
7. **Geração lógica:** produzir seções estruturadas, com distinção entre fatos, relatos, hipóteses e possibilidades.
8. **Revisão:** considerar verificação técnica/humana conforme criticidade e critérios futuros.
9. **Validação da Pessoa:** apresentar as interpretações relevantes à Pessoa quando aplicável e registrar concordância, correção, contestação ou escolha sem coerção.
10. **Entrega:** disponibilizar somente versão e seções autorizadas ao destinatário, com rastreabilidade e restrições.
11. **Atualização:** mudanças posteriores podem tornar relatório obsoleto, provocar revisão ou bloquear acesso.

**Gerar não significa publicar.** Composição, revisão, validação e entrega são estados separados.

## 7. Estados do relatório e validação
| Estado | Significado |
| --- | --- |
| `draft` | Em preparação, não distribuível |
| `awaiting_evidence_review` | Necessita revisão de evidência/método |
| `awaiting_person_validation` | Necessita confirmação ou contestação relevante da Pessoa |
| `ready_for_authorized_release` | Elegível segundo gates e autorização atual, mas ainda não entregue |
| `released_to_authorized_recipient` | Entrega registrada ao destinatário autorizado |
| `under_revision` | Em atualização ou contestação |
| `stale` | Não representa o contexto vigente |
| `superseded` | Substituído por versão posterior |
| `access_blocked` | Uso bloqueado por autorização/política |
| `failed` | Geração ou verificação não concluída |

**Validação:** confirmar um relato pessoal não comprova automaticamente requisitos externos. Aprovação de uma seção não significa aceite de todas as hipóteses ou autorização irrestrita de compartilhamento.

## 8. Consentimento, finalidade, acesso e revogação
- Separar **autorização de processamento** e **autorização de compartilhamento/entrega** ao profissional, instituição ou parceiro.
- A autorização deve especificar finalidade, destinatário, categorias/seções, validade e possibilidade de revogação quando aplicável.
- Notas privadas de profissionais não passam automaticamente ao relatório visível na Jornada ou a outros profissionais.
- Não disponibilizar dados brutos, clínicos ou sensíveis por padrão; situações clínicas exigem governança e análise jurídica/técnica próprias.
- Registro de entrega não concede acesso perpétuo a futuras versões.
- Revogação deve bloquear novos usos incompatíveis e disparar o tratamento de versões e caches segundo serviços responsáveis; não presumir exclusão física onde existam regras legítimas de retenção.
- Não publicar relatórios individuais neste repositório/documentação pública.

## 9. Contrato lógico de solicitação (exemplo sintético)
```json
{
  "capability": "GAI-CAP-11",
  "method_version": "proposed-1",
  "purpose": "trajectory_and_possibilities_report",
  "subject_ref": "synthetic-person",
  "requester_ref": "authorized-professional",
  "recipient_refs": ["authorized-professional"],
  "processing_authorization_ref": "server-validated-processing-scope",
  "sharing_authorization_ref": "server-validated-sharing-scope",
  "context_version": "revision-81",
  "as_of": "2026-10-31T13:00:00-03:00",
  "sections_requested": ["current_moment", "trajectory", "possibilities", "limitations"],
  "analysis_refs": ["synthetic-cap01", "synthetic-cap02", "synthetic-cap05"],
  "output_locale": "pt-BR"
}
```
Essas referências são ilustrativas; campos recebidos do cliente não constituem prova de autorização.

## 10. Contrato lógico de resposta (exemplo sintético)
```json
{
  "capability": "GAI-CAP-11",
  "report_id": "synthetic-report",
  "report_version": "1",
  "context_version": "revision-81",
  "status": "awaiting_person_validation",
  "purpose": "trajectory_and_possibilities_report",
  "recipient_scope_ref": "authorized-sharing-scope",
  "sections": [
    {
      "section_id": "trajectory",
      "state": "draft",
      "summary": "A Pessoa relatou mudanças em atividades ao longo do período.",
      "claim_refs": ["synthetic-claim-1"],
      "limitations": ["Histórico parcial"]
    },
    {
      "section_id": "possibilities",
      "state": "draft",
      "summary": "Possibilidade adjacente a explorar, sem interesse confirmado.",
      "claim_refs": ["synthetic-claim-2"],
      "limitations": ["Não constitui recomendação obrigatória"]
    }
  ],
  "unknowns": ["Disponibilidade atual a confirmar"],
  "person_validation": {"status": "pending"},
  "evidence_review": {"status": "pending"},
  "delivery": {"status": "not_released"},
  "method_version": "proposed-1"
}
```
O exemplo não contém relatório real, não define schema técnico final e não representa execução concluída.

## 11. Exemplo de linguagem responsável
**Registro:** uma Pessoa consultou duas oportunidades e não há evento de participação confirmado.

**Formulação admissível:** “Existem registros de consulta a duas oportunidades. Não há evidências suficientes para afirmar se ocorreu participação ou quais fatores influenciaram a continuidade.”

**Pergunta possível:** “Houve alguma condição de horário, acesso ou interesse que você gostaria de esclarecer?”

**Formulação proibida:** “A Pessoa sabotou seu próprio desenvolvimento”, “não possui comprometimento” ou “recusou conscientemente as oportunidades”.

## 12. Formas de apresentação e contrato de produto
A CAP-11 define um **artefato lógico estruturado**; PDF, interface web, exportação autorizada e visualização pelo profissional são modalidades futuras de apresentação, não provas de implementação.

Uma modalidade de entrega deverá:
- preservar identificadores e versões;
- distinguir visualmente fato, relato, hipótese e desconhecido;
- permitir localizar evidências autorizadas;
- deixar claro quem recebeu, quando e para qual finalidade;
- oferecer correção e contestação conforme permissões;
- evitar impressão de validade contínua após alteração do contexto;
- registrar geração e entrega como eventos distintos.

Modelos de precificação e planos comerciais permanecem em estudo; não alegar que produto está à venda.

## 13. Indicadores de avaliação e bloqueios
**Métricas candidatas:** fidelidade factual por afirmação, cobertura de evidências, taxa de claims sem suporte, separação fato/hipótese, atualidade do contexto, isolamento de dados, correção do escopo por destinatário, utilidade avaliada por Pessoa/profissional, compreensão de limites, custo e latência.

**Bloqueios críticos:** informação de outra Pessoa, compartilhamento sem base/autorização, diagnóstico automatizado impróprio, relatório obsoleto apresentado como atual, exposição de notas segregadas e fabricação de histórico ou oferta.

Os limiares numéricos, autoridade de adjudicação, público-piloto e gates ainda precisam de decisões específicas; nenhum teste foi executado.

## 14. Cenários sintéticos propostos (não executados)
| ID | Cenário | Comportamento esperado |
| --- | --- | --- |
| CAP11-E01 | Pessoa relata experiência não confirmada externamente | Atribuir corretamente o relato |
| CAP11-E02 | Histórico sem intervalo completo | Exibir limite temporal |
| CAP11-E03 | CAP-05 sugere opção não validada | Identificar hipótese, não objetivo |
| CAP11-E04 | CAP-04 registra desconhecido | Não transformá-lo em lacuna confirmada |
| CAP11-E05 | Oferta exibida e não aberta | Não inferir desinteresse |
| CAP11-E06 | Inscrição sem participação | Não declarar resultado |
| CAP11-E07 | Oferta expira após preparação do relatório | Marcar seção/versão afetada obsoleta |
| CAP11-E08 | Pessoa contesta interpretação | Registrar contestação e revisão |
| CAP11-E09 | Profissional sem compartilhamento autorizado | Bloquear entrega |
| CAP11-E10 | Nota profissional segregada | Não expor indevidamente |
| CAP11-E11 | Autorização de processamento sem autorização de entrega | Não liberar a terceiro |
| CAP11-E12 | Revogação após entrega | Bloquear novos acessos/atualizações conforme política |
| CAP11-E13 | Dados de outra Pessoa no contexto | Falha crítica de isolamento |
| CAP11-E14 | Modelo inventa certificado | Rejeitar claim sem fonte |
| CAP11-E15 | Dois modelos discordam sobre causa de comportamento | Não atribuir causa sem evidência |
| CAP11-E16 | Novo contexto chega durante geração | Descartar ou sinalizar versão obsoleta |
| CAP11-E17 | Falha Neo4j/provedor | Não simular relatório atualizado |
| CAP11-E18 | Relatório com dado clínico desnecessário | Minimizar/bloquear |
| CAP11-E19 | Seção sem informação suficiente | Marcar incompleta, não inventar conteúdo |
| CAP11-E20 | Versão histórica autorizada para auditoria | Não apresentá-la como avaliação atual |
| CAP11-E21 | Aprovação de um relato pela Pessoa | Não converter todas as hipóteses em validadas |
| CAP11-E22 | Entrega registrada ao profissional | Não confundir entrega com leitura/aceite |

## 15. Dependências e decisões pendentes
**Dependências:** CAP-01 a CAP-10 conforme conteúdo requerido, serviços de identidade/contexto/autorização, evidências, governança, observabilidade e consumidor autorizado. Não exigir todas as capacidades para gerar um relatório limitado e honesto; exigir fontes e avaliações necessárias ao conteúdo efetivamente produzido.

**Pendências:** matriz de seções por público; contrato de processamento versus entrega; perfil de revisores e autoridade; regras de retenção; renderização e exportação; registro de validação da Pessoa; política de relatórios históricos; custos por análise; riscos de alta consequência e condições de eventual comercialização.

**Referências:** [Documento Mestre](index.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [Estudo inicial do Relatório](relatorio.md) · [CAP-03](cap-03-interpretacao-fundamentada-evidencias.md) · [CAP-05](cap-05-descoberta-possibilidades-futuras.md) · [CAP-09](cap-09-gestao-incertezas-contradicoes.md) · [CAP-10](cap-10-reavaliacao-invalidacao-analises.md) · [Avaliação](avaliacao-validacao-qualidade.md).

**Guivos AI e GKR seguem independentes; Replit, Neo4j e provedores não são modificados.**
