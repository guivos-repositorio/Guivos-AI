# GAI-CAP-08 — Qualificação de Oportunidades
**Especificação de capacidade · Versão documental 2.0 · 31/10/2026**
**Estado:** conceituada; critérios, contratos e testes propostos. Não implementada, testada, homologada ou liberada.

## 1. Finalidade e fronteira
A GAI-CAP-08 examina **ofertas concretas** e sua eventual pertinência a um caminho ou possibilidade, verificando origem, disponibilidade, prazo, requisitos, condições de acesso e limitações. Não fabrica oferta, não garante vaga ou resultado, não transforma uma categoria abstrata em publicação existente e não substitui a autoridade do serviço de oportunidades.

- **Possibilidade (CAP-05):** futuro concebível, não oferta comercial ou institucional.
- **Caminho (CAP-07):** percurso de aproximação com etapas propostas, não garantia de realização.
- **Oportunidade concreta:** iniciativa identificada de publicador conhecido, com evidência e status temporal verificável.
- **Qualificação da oferta:** avaliação da qualidade dos metadados, legitimidade verificável, vigência e requisitos declarados pela fonte.
- **Pertinência contextual:** relação fundamentada entre oferta e caminho, considerando CAP-02/04/06, sem declarar interesse da Pessoa.
- **Disponibilidade:** somente estado sustentado por fonte apropriada e verificação temporal. Uma publicação existente não prova vagas restantes ou capacidade efetiva.

## 2. Autoridades e fluxo
**Serviço de oportunidades do ecossistema:** autoridade pelo registro da oferta, publicador, alterações, publicação, prazos e eventos. Fontes externas devem ter proveniência e verificação específicas.

**Guivos AI:** interpreta e qualifica as evidências e a pertinência contextual da oferta.

**Guivos Intelligence:** solicita avaliação quando pertinente, apresenta limites e obtém validação da Pessoa.

**Neo4j:** possível projeção de relações entre oferta, requisitos, caminhos e evidências, consultada por serviços autorizados, sem acesso irrestrito dos modelos.

**GPT/Claude/Gemini:** processamento auxiliar, não sistemas de registro nem verificadores independentes por mera concordância.

## 3. Classes de supply
| Classe | Exemplos | Contribuição possível |
| --- | --- | --- |
| Direct Supply | Curso, vaga, mentoria, evento, atividade cultural, voluntariado, prática, comunidade | Experiência ou oportunidade diretamente associada ao caminho |
| Enabling Supply | Transporte, internet, equipamento, acessibilidade, cuidado infantil, documentação, mobilidade e infraestrutura | Redução de barreira externa que permite acesso a uma etapa |

O tipo de oferta não implica que ela seja adequada, aberta ou disponível para a Pessoa.

## 4. Dimensões de qualificação da oferta
| Dimensão | Informação exigida ou a verificar | Cuidado |
| --- | --- | --- |
| Identidade | ID da oportunidade, fonte, publicador e vínculo | Nome publicado não comprova autenticidade do publicador |
| Tipo | Categoria e classe Direct/Enabling | Não confundir oferta com possibilidade |
| Status | Rascunho, publicada, suspensa, encerrada, cancelada ou desconhecida | Não apresentar encerrada como ativa |
| Temporalidade | Início, término, inscrições, validade, timezone, última verificação | A ausência de prazo não significa validade indefinida |
| Requisitos | Obrigatórios, facilitadores, preferências e fonte | Evitar universalizar requisito de oferta específica |
| Condições de acesso | Gratuidade/preço, localidade, remoto/presencial, capacidade, elegibilidade | Não inventar custo, vagas ou disponibilidade |
| Acessibilidade | Recursos e adaptações informados, ou informação desconhecida | Não inferir adaptação existente |
| Fonte e comprovação | URL/registro interno, versão, data, integridade, disputas | Verificação de conteúdo não implica verificação de resultado |
| Relação contextual | Evidências de vínculo com possibilidade/caminho, condições e lacunas | Não declarar “match perfeito” |
| Interação | Recomendada, exibida, aberta, salva, inscrita, participante, resultado | Cada evento tem significado próprio |

## 5. Estados independentes
**Estado da publicação:** `draft`, `published`, `suspended`, `closed`, `cancelled`, `unknown`.

**Estado da verificação:** `verified_current`, `verified_historical`, `pending_verification`, `stale`, `conflicting_sources`, `unverifiable`.

**Estado da disponibilidade:** `confirmed_available` somente com evidência específica recente; `published_not_confirmed`; `not_available`; `unknown`.

**Pertinência:** `contextually_relevant`, `potentially_relevant`, `requires_information`, `not_relevant_for_this_path`, `not_assessable`.

Não colapsar esses estados: oferta publicada e relevante não é necessariamente ofertada com inscrição disponível. Estado técnico de aprovação de publicação no ecossistema não equivale à certificação independente de qualidade.

## 6. Critérios mínimos para afirmar “oportunidade disponível”
1. Fonte e publicador identificados no domínio competente.
2. Registro ou publicação verificado, sem evidência atual de encerramento/cancelamento.
3. Janela de participação/inscrição válida **na data de referência**, caso aplicável.
4. Indicação específica de disponibilidade confirmada, quando essa afirmação exigir consulta a estoque/vagas/capacidade.
5. Requisitos relevantes e barreiras conhecidos ou explicitamente desconhecidos.
6. Identificadores, versão, timestamp de verificação e limite de validade da confirmação.

Sem evidência suficiente, informar **publicada, disponibilidade não confirmada** ou **desconhecida**. Não calcular disponibilidade com base apenas em data futura, anúncios antigos ou texto gerado por modelo.

## 7. Processo conceitual de qualificação
1. Receber finalidade, sujeito, contexto, autorização e referência da oferta.
2. Verificar a autorização com serviços apropriados, sem confiar em escopo autoafirmado.
3. Resolver registro da oferta e publicador na fonte competente, com versão e status.
4. Conferir janela temporal, atualidade, dados essenciais, elegibilidade e condições de acesso.
5. Diferenciar requisitos obrigatórios, facilitadores e preferências.
6. Verificar sinais de desatualização, duplicação, divergência e restrições.
7. Avaliar pertinência a possibilidade/caminho específico, utilizando CAP-03/04/06/07 quando autorizado.
8. Distinguir Direct e Enabling Supply e explicar como a oferta **poderia** apoiar uma etapa.
9. Preparar resultado fundamentado, estados independentes e perguntas por desconhecido.
10. Devolver Guivos Intelligence com versões, validade e limites; não efetuar inscrição/compra automaticamente.
11. Revisar após alteração, expiração, revogação, mudança de contexto ou nova fonte.

## 8. Contrato lógico de solicitação (sintético)
```json
{
  "capability": "GAI-CAP-08",
  "method_version": "proposed-1",
  "purpose": "qualify_concrete_opportunity",
  "subject_ref": "synthetic-person",
  "authorization_ref": "server-verified-reference",
  "context_version": "revision-52",
  "opportunity_ref": "synthetic-opportunity",
  "path_ref": "optional-path-ref",
  "as_of": "2026-10-31T12:00:00-03:00",
  "requested_checks": ["identity", "status", "requirements", "access", "contextual_relevance"]
}
```

## 9. Contrato lógico de resposta (sintético)
```json
{
  "capability": "GAI-CAP-08",
  "analysis_id": "synthetic-analysis",
  "opportunity_ref": "synthetic-opportunity",
  "source_version": "offer-v3",
  "context_version": "revision-52",
  "publication_status": "published",
  "verification_status": "verified_current",
  "availability_status": "published_not_confirmed",
  "relevance_status": "requires_information",
  "supply_class": "direct",
  "requirements": [
    {
      "requirement_ref": "schedule-wednesday",
      "kind": "mandatory_for_offer",
      "person_condition": "unknown",
      "evidence_refs": ["offer-rule-source"]
    }
  ],
  "verified_as_of": "2026-10-31T12:00:00-03:00",
  "valid_until": null,
  "unknowns": ["Vagas disponíveis", "Disponibilidade da Pessoa às quartas"],
  "limitations": ["A publicação não confirma vaga ou participação."],
  "questions_for_person": ["Você teria disponibilidade às quartas?"],
  "method_version": "proposed-1"
}
```
Campos são **propostas**, não contrato implementado. A publicação estar confirmada não permite declarar vaga disponível. `valid_until: null` exige regra de revalidação antes de alegação de atualidade contínua.

## 10. Semântica dos eventos de interação
| Evento | O que confirma | O que não confirma |
| --- | --- | --- |
| Oferta disponível no catálogo | Registro publicável segundo fonte e data | Pessoa tomou conhecimento |
| Recomendada | Motor selecionou para recomendação | Pessoa visualizou |
| Exibida | Interface apresentou segundo evento | Leitura consciente |
| Aberta | Pessoa acessou detalhes | Interesse confirmado |
| Salva | Ação de salvar registrada | Inscrição ou comparecimento |
| Inscrita | Registro de inscrição aceito pela fonte | Presença ou benefício |
| Participação | Evento de participação confirmado pela fonte relevante | Aprendizagem ou evolução automaticamente |
| Resultado | Resultado específico registrado com evidência | Causalidade exclusiva daquela oferta |

Não interpretar não inscrição como rejeição deliberada, desinteresse ou autossabotagem.

## 11. Exemplo sintético
Uma formação aparece como **publicada** no registro do ecossistema, com inscrição até 15/11 e encontros às quartas. A fonte não confirma vagas restantes. A Pessoa declarou tempo livre às terças, mas nada sobre quartas.

**Resultado permitido:** oferta publicada com prazo informado, disponibilidade de vagas **não confirmada**, adequação de horário **desconhecida**. Sugestão de verificar vagas e perguntar sobre quartas.

**Não permitido:** “vaga garantida”, “100% compatível”, “Pessoa ignorou a oferta” ou “curso disponível para inscrição com vaga confirmada”.

## 12. Revisão, revogação e falhas
- Oferta expira/cancela: atualizar publicação, retirar indicação de disponibilidade e invalidar análises dependentes.
- Requisito muda: reavaliar lacunas e compatibilidade; preservar versão histórica.
- Publicador sem comprovação: declarar verificação pendente, não afirmar confiança garantida.
- API/Neo4j indisponível: devolver estado `unverifiable`/`assessment_unavailable`; não fabricar dados.
- Duplicatas: distinguir registros do mesmo publicador e versões sem contar como múltiplas ofertas.
- Autorização revogada: bloquear consulta ao contexto individual, revisar relatórios/caches.
- Custo, localidade, acessibilidade desconhecidos: destacar desconhecidos, não preencher por inferência.
- Ofertas fraudulentas ou perigosas: encaminhar para verificação e controles apropriados; não certificar publicador por geração textual.
- Resultados de modelos divergentes: conferir fonte e data, não votar.
- Informações sensíveis: não expor em recomendações sem finalidade legítima.

## 13. Cenários sintéticos de avaliação (não executados)
| ID | Caso | Resultado esperado |
| --- | --- | --- |
| CAP08-E01 | Publicação existe, vagas não verificadas | Disponibilidade não confirmada |
| CAP08-E02 | Prazo encerrado | Encerrada/não disponível |
| CAP08-E03 | Oferta cancelada após recomendação | Invalidar recomendação vigente |
| CAP08-E04 | Fonte informa requisito desatualizado | Exigir revalidação |
| CAP08-E05 | Quarta exigida; terça relatada | Horário da Pessoa desconhecido |
| CAP08-E06 | Oferta exibida sem abertura | Não inferir percepção |
| CAP08-E07 | Oferta aberta sem inscrição | Não afirmar participação |
| CAP08-E08 | Inscrição sem presença | Não afirmar experiência |
| CAP08-E09 | Falta valor/preço | Não inventar custo |
| CAP08-E10 | Publicador não verificado | Sem afirmação de autenticidade |
| CAP08-E11 | Oferta duplicada por fontes derivadas | Consolidar proveniência |
| CAP08-E12 | Oferta externa sem informação de acessibilidade | Declarar desconhecido |
| CAP08-E13 | Transporte habilitador para curso | Identificar Enabling Supply |
| CAP08-E14 | Categoria de “curso” sem publicação | Não gerar oferta fictícia |
| CAP08-E15 | Pessoa recusa sugestão | Respeitar escolha, sem julgamento |
| CAP08-E16 | Autorização revogada durante consulta | Impedir acesso e invalidar conforme política |
| CAP08-E17 | Resultado de versão antiga chega atrasado | Não substituir estado recente |
| CAP08-E18 | Modelo inventa vagas disponíveis | Rejeitar alegação sem fonte |
| CAP08-E19 | Escopo profissional distinto | Não cruzar dados de Pessoas/profissionais |
| CAP08-E20 | Oferta tem requisitos alternativos | Não transformar “ou” em requisitos cumulativos |

Métricas, critérios mínimos, classificação de gravidade e gates devem ser definidos e adjudicados segundo [Modelo de Avaliação](avaliacao-validacao-qualidade.md). Nenhum teste da lista foi executado.

## 14. Integração com Intelligence, Mall, Travel e outros serviços
A Guivos AI **não se torna o sistema de cadastro, pagamento, inscrição ou distribuição das oportunidades**. Serviços pertinentes do ecossistema continuam responsáveis por seus fatos operacionais; Guivos Intelligence coordena a Jornada. CAP-08 devolve interpretação especializada, rastreável e limitada.

Ofertas poderão pertencer a diferentes unidades do ecossistema, quando concretamente disponíveis e autorizadas. O modelo não presume que todas as unidades já estejam integradas, nem mistura autorização comercial com acesso à trajetória pessoal.

A API externa poderá expor qualificação de oportunidades sob contrato específico, sem disponibilizar histórico bruto, dados sensíveis ou informações profissionais indevidas.

## 15. Dependências e decisões pendentes
**Dependências:** CAP-02/03/04/06/07 conforme caso, CAP-09/10 para revisão, serviços de oportunidade, identidade, contexto, governança e observabilidade.

**Pontos a decidir:**
1. Fonte de verdade e schema canônico da oferta por unidade/ecossistema;
2. Estados oficiais de publicação versus vagas/capacidade e critérios de frescor por tipo;
3. Procedimentos para autenticação de publicadores e fontes externas;
4. Política de atualização, expiração e revalidação;
5. Permissões e finalidade de consultas por Pessoa e profissional;
6. Padrão de relação oferta↔requisito↔caminho no grafo;
7. Métricas de erro factual, ofertas expiradas e falso match;
8. Quem autoriza liberar CAP-08 para consumo real.

**Referências:** [Documento Mestre](index.md) · [Matriz](matriz-capacidades-guivos-ai.md) · [CAP-04](cap-04-identificacao-qualificacao-lacunas.md) · [CAP-06](cap-06-inteligencia-compatibilidade-futura.md) · [CAP-07](cap-07-caminhos-intermediarios.md) · [Modelo de Evidências](modelo-evidencias-rastreabilidade.md).

**Nenhuma alteração operacional no Replit, Neo4j, provedores ou GKR é autorizada por esta especificação.**
