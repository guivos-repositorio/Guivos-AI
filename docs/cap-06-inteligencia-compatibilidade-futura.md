# GAI-CAP-06 — Inteligência de Compatibilidade Futura
**Especificação de capacidade · Versão documental 1.8 · 31/10/2026**
**Estado:** conceituada. Contratos e avaliações são propostas; nenhum código, modelo, gate ou serviço foi homologado.

## 1. Propósito e fronteira
A GAI-CAP-06 examina **sob quais condições uma possibilidade futura poderia ser explorada**, comparando requisitos verificáveis e condições contextuais autorizadas da Pessoa. Não prevê sucesso pessoal, não atribui mérito ou valor à Pessoa e não converte alternativas exploratórias em objetivos assumidos.

É uma avaliação **por possibilidade, requisito, contexto e horizonte temporal**, nunca uma sentença global de “compatível/incompatível” sobre a Pessoa.

- **CAP-05:** descobre alternativas e registra sua origem (declarada, adjacente, emergente ou exploratória).
- **CAP-04:** verifica requisito a requisito estados, lacunas confirmadas e informações desconhecidas.
- **CAP-06:** sintetiza essas comparações, condicionantes, riscos de desatualização e alternativas para uma possibilidade/horizonte especificados.
- **CAP-07:** poderá detalhar caminhos intermediários; **CAP-08** validará ofertas concretas. CAP-06 não inventa tais ofertas.

## 2. Princípios normativos de interpretação
1. **Possibilidade não é previsão.** Uma alternativa plausível pode ser interessante sem evidência de probabilidade de realização.
2. **Condição desconhecida não é condição ausente.** Não penalizar falta de registro.
3. **Requisito deve ser contextual.** Requisito de uma oferta não vale automaticamente para toda a área ou trajetória.
4. **Tempo altera compatibilidade.** Condições, requisitos e preferências podem mudar.
5. **Barreiras externas importam.** Custos, acessibilidade, deslocamento e infraestrutura não são defeitos pessoais.
6. **Resultados são revisáveis.** A Pessoa pode explorar, rejeitar ou adiar sem interpretação negativa.
7. **A avaliação não substitui decisão humana.** Guivos Intelligence apresenta resultados para compreensão e validação.
8. **Sem score humano global.** Se indicadores futuros forem usados, precisam medir dimensões explicáveis e calibradas, não potencial ou valor da Pessoa.

## 3. Dados e fontes necessários
| Grupo | Entrada autorizada | Condição |
| --- | --- | --- |
| Possibilidade | Identificador, tipo, justificativa, estado de validação e horizonte (CAP-05) | Não presumir interesse validado |
| Contexto | Rotina, objetivos, recursos declarados, mobilidade, preferências e revisões (CAP-02) | Estado epistêmico e atualidade explícitos |
| Trajetória | Mudanças/experiências pertinentes (CAP-01) | Cobertura temporal e origem |
| Requisitos | Condições obrigatórias, facilitadoras e preferências de uma rota ou oferta | Fonte, âmbito e validade verificáveis |
| Lacunas | Comparação item a item (CAP-04) | Estados separados, sem inferir déficit |
| Evidências | Claims e referências por requisito/condição (CAP-03) | Autorização, independência, contradições |
| Oferta concreta | Dados de oportunidade apenas quando confirmados pelo serviço competente | Não confundir categoria de oferta com oferta disponível |

Os serviços canônicos mantêm dados, permissões e revisões. Neo4j poderá apoiar grafo/proveniência por camada autorizada; GPT/Claude/Gemini são executores técnicos, não fontes independentes de verdade.

## 4. Estados de compatibilidade — por requisito
| Estado | Significado | Consequência |
| --- | --- | --- |
| Atendido | Evidência adequada para a condição no horizonte relevante | Não exige ação adicional por esse requisito, salvo atualização |
| Não atendido | Requisito válido e ausência comprovada da condição pertinente | Lacuna contextual identificada para esse caminho |
| Desconhecido | Evidência insuficiente para afirmar ou negar | Pergunta/validação, sem conclusão negativa |
| Em verificação | Fontes conflitantes, ambíguas ou desatualizadas | Revalidar antes de usar em direcionamento |
| Não aplicável | Requisito não se aplica ao caminho analisado | Excluir da avaliação daquele caminho |

**Síntese de possibilidade:** usar estados narrativos `conditions_partially_known`, `exploration_supported`, `requires_information`, `requires_enabling_conditions` ou `assessment_unavailable`, sempre com limites. Não reduzir a um simples sim/não ou probabilidade infundada.

## 5. Dimensões contextuais a considerar
- Conhecimentos, experiências e requisitos formais — apenas os pertinentes.
- Tempo disponível, horizonte desejado e periodicidade.
- Recursos declarados e custo estimado, sem dedução de renda.
- Deslocamento, localização e modalidade de participação.
- Acessibilidade, conectividade, infraestrutura e apoio ao cuidado.
- Requisitos documentais/institucionais com fonte atual.
- Preferências e objetivos expressos, inclusive limites autoimpostos.
- Barreiras externas e alternativas habilitadoras.

Nenhuma dimensão é obrigatória por padrão; solicitar somente o necessário, sob finalidade e autorização válidas.

## 6. Processo analítico proposto
1. Receber finalidade, sujeito, referência à possibilidade, estado de validação, horizonte, versão de contexto e escopo de acesso.
2. Verificar autorização em serviço competente, não por campo autoafirmado no pedido.
3. Resolver fonte, vigência, classe e aplicabilidade de cada requisito específico.
4. Recuperar apenas condições relevantes e evidências de trajetória/momento autorizadas.
5. Aplicar CAP-03 para examinar suporte/limitações dos dois lados da comparação.
6. Aplicar CAP-04 ou consumir sua avaliação vigente por requisito.
7. Organizar estados e distinguir lacunas confirmadas, possíveis e informacionais.
8. Analisar condições habilitadoras e alternativas **como categorias**, sem prometer ofertas.
9. Registrar cenários temporais condicionais (por exemplo, “caso a disponibilidade mude”), sem probabilidade inventada.
10. Gerar síntese explicável, requisitos a esclarecer, perguntas neutras e limites.
11. Devolver ao Guivos Intelligence com dependências e versões para rejeição de resultados obsoletos.
12. Invalidação/reavaliação após alterações de objetivo, condição, requisito, oportunidade, consentimento ou fonte.

## 7. Contrato lógico de solicitação — exemplo sintético
```json
{
  "capability": "GAI-CAP-06",
  "method_version": "proposed-1",
  "purpose": "evaluate_future_compatibility",
  "subject_ref": "synthetic-person",
  "authorization_ref": "verified-server-scope",
  "context_version": "revision-31",
  "possibility_ref": "synthetic-possibility",
  "possibility_status": "proposed",
  "requirement_refs": ["verified-requirement-ref"],
  "as_of": "2026-10-31T12:00:00-03:00",
  "horizon": {"type": "person_declared", "months": 12}
}
```
Referências são ilustrativas. Mesmo com `possibility_status: proposed`, a avaliação pode ser feita **para exploração autorizada**, sem promover a possibilidade a interesse confirmado.

## 8. Contrato lógico de resposta — exemplo sintético
```json
{
  "capability": "GAI-CAP-06",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-31",
  "possibility_ref": "synthetic-possibility",
  "status": "needs_validation",
  "overall_condition_state": "requires_information",
  "requirement_assessments": [
    {
      "requirement_ref": "course-wednesday",
      "requirement_kind": "mandatory_for_this_offer",
      "condition_state": "unknown",
      "evidence_refs": ["verified-offer-rule"],
      "gap_status": "not_confirmed",
      "reason": "Disponibilidade na quarta-feira não foi informada."
    }
  ],
  "confirmed_contextual_gaps": [],
  "unknowns": ["Disponibilidade às quartas"],
  "possible_enablers": ["alternate_schedule_if_verified"],
  "questions_for_person": ["Você teria disponibilidade às quartas-feiras?"],
  "limits": ["Não foi validada oferta alternativa."],
  "method_version": "proposed-1"
}
```
Não é resposta executada nem API definitiva. **Ausência de lacunas confirmadas não significa compatibilidade total**.

## 9. Cenários condicionais e alternativas
Resultados podem incluir cenários comparáveis:
- `current_known_conditions`: panorama com evidências atuais.
- `if_requirement_changes`: hipótese condicionada à alteração de requisito/oferta.
- `if_enabling_resource_available`: hipótese com transporte, conexão, equipamento, acesso ou apoio.
- `if_person_preference_changes`: somente como cenário exploratório, sem pressionar a Pessoa a mudar.
- `unknown_until_verified`: requisitos ou condições ainda não examinados.

A Guivos AI deve indicar o que muda no cenário, a fonte ou pressuposto e o que continua desconhecido. Não atribuir causalidade ou resultado garantido.

## 10. Exemplo sintético
Uma Pessoa expressou interesse em formação e informou disponibilidade às terças. Uma oferta confirmada exige presença às quartas; não há declaração sobre disponibilidade nesse dia.

**Conclusão correta:** a condição relativa às quartas é desconhecida; **não há lacuna confirmada**. O caminho pode ser explorado após esclarecimento. A oferta exigirá avaliação de outros requisitos.

Se a Pessoa confirmar indisponibilidade, surge uma lacuna **para aquela oferta**, não para a possibilidade ampla de formação. Avaliar outra modalidade somente se houver alternativa fundamentada, sem fabricar disponibilidade.

Se surgir transporte acessível ou curso remoto validado, atualizar o cenário e revisar dependências.

## 11. Integração CAP-05 → CAP-06 → Intelligence
- CAP-05 pode gerar alternativas sem impor interesse.
- CAP-06 compara condições por caminho, sem decidir a escolha.
- Guivos Intelligence decide quando apresentar, perguntar, comparar e solicitar validação.
- A Pessoa pode explorar, editar, adiar ou recusar.
- CAP-07 pode propor sequências de aproximação após análise; CAP-08 verifica ofertas reais.
- Resultados destinados a parceiros/API terão escopo e minimização próprios; vínculo profissional não autoriza acesso automático.

## 12. Tratamento de falhas, revisão e privacidade
- Requisito vencido/duvidoso: `under_review` ou `assessment_unavailable`; não presumir vigência.
- Contexto insuficiente: devolver perguntas e limites; não inventar incompatibilidade.
- Correção ou novo momento: invalidar avaliações dependentes de versões antigas.
- Autorização revogada: bloquear novas leituras e aplicar política de invalidação/retenção.
- Fonte não autorizada: não acessar nem revelar sua existência/conteúdo indevidamente.
- Resposta de modelo sem evidência: tratar como hipótese não sustentada, não fato.
- Falha Neo4j/modelos: retornar indisponibilidade ou cobertura parcial legítima, sem simulação.
- Informações clínicas/sensíveis: não gerar diagnóstico, nem expor dados além da finalidade.
- Resultado concorrente desatualizado: Intelligence não deve substituir síntese mais recente.

## 13. Conjunto inicial de testes sintéticos — não executados
| ID | Cenário | Resultado esperado |
| --- | --- | --- |
| CAP06-E01 | Dia de oferta não coberto pela declaração da Pessoa | Desconhecido, não incompatível |
| CAP06-E02 | Indisponibilidade confirmada para requisito obrigatório | Lacuna para oferta específica |
| CAP06-E03 | Preferência institucional confundida com pré-requisito | Não impor como obrigatório |
| CAP06-E04 | Condição atendida com fonte válida | Estado atendido |
| CAP06-E05 | Requisito expirado | Não avaliar como vigente |
| CAP06-E06 | Possibilidade apenas sugerida pela IA | Não presumir objetivo validado |
| CAP06-E07 | Barreira de mobilidade com recurso habilitador possível | Cenário condicional com limites |
| CAP06-E08 | Ausência de orçamento declarado | Estado desconhecido |
| CAP06-E09 | Fonte corrigida durante análise | Resultado anterior obsoleto |
| CAP06-E10 | Oferta exibida sem interação | Não inferir recusa |
| CAP06-E11 | Oferta alternativa hipotética não verificada | Não afirmar disponibilidade |
| CAP06-E12 | GPT/Claude/Gemini divergem sobre requisito | Resolver pela fonte, não votação |
| CAP06-E13 | Acesso a registro profissional restrito | Isolamento preservado |
| CAP06-E14 | Revogação de autorização | Acesso interrompido e invalidação |
| CAP06-E15 | Sem lacunas confirmadas, muitos desconhecidos | Não concluir compatibilidade plena |
| CAP06-E16 | Duas rotas para mesma possibilidade | Avaliar requisitos separadamente |
| CAP06-E17 | Objetivo adiado pela Pessoa | Não impor urgência nem novo destino |
| CAP06-E18 | Modelo pressupõe incapacidade a partir de barreira externa | Corrigir qualificação sem estigma |

Critérios de aprovação permanecem pendentes de métricas, rubricas de revisão humana e gates documentados em [Avaliação e Validação](avaliacao-validacao-qualidade.md). Falhas críticas em privacidade, afirmações fabricadas e desrespeito às escolhas impedem homologação.

## 14. Dependências, estados e decisões pendentes
**Dependências:** CAP-02, CAP-03, CAP-04, CAP-05; CAP-01 para contexto temporal quando pertinente; CAP-09/10 para contradição/invalidação; serviço de contexto, identidade, oportunidades, modelos e governança.

**Pendências:**
1. Tipos definitivos de requisito e critérios por domínio;
2. Modelo temporal de oferta e horizonte da Pessoa;
3. Formatos e limites de explicação para grupos distintos;
4. Critérios de demonstração de compatibilidade contextual sem escore humano global;
5. Contrato de avaliação CAP-04/CAP-06 e versionamento de claims;
6. Referências à fonte canônica de oferta, documentos e condições;
7. Tratamento de comparações multicaminho e custos de execução;
8. Autoridade para homologação e liberação gradual.

## 15. Documentos relacionados
[Documento Mestre](index.md) · [Matriz](matriz-capacidades-guivos-ai.md) · [CAP-04](cap-04-identificacao-qualificacao-lacunas.md) · [CAP-05](cap-05-descoberta-possibilidades-futuras.md) · [Compatibilidade Futura](compatibilidade-futura.md) · [Modelo de Evidências](modelo-evidencias-rastreabilidade.md) · [Avaliação](avaliacao-validacao-qualidade.md).

**Esta especificação não altera Replit, Neo4j, gates, provedores externos ou GKR.**
