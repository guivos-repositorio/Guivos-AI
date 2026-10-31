# GAI-CAP-09 — Gestão de Incertezas e Contradições
**Especificação de capacidade · Versão documental 2.1 · 31/10/2026**
**Estado:** conceituada. Não implementada, testada, homologada ou autorizada para produção.

## 1. Propósito e fronteiras
A CAP-09 é uma capacidade **transversal** para reconhecer, classificar e encaminhar informação insuficiente, ambiguidades, divergências e contradições em análises da Guivos AI. Protege a integridade epistêmica das CAP-01 a CAP-08 e das futuras CAP-10/11/12.

**Princípio:** divergência não é automaticamente erro, e concordância não comprova verdade. A Guivos AI não fabrica consenso entre GPT, Claude e Gemini, não interpreta silêncio como recusa nem usa incerteza para atribuir defeitos à Pessoa.

**Guivos AI** qualifica conflitos e limites; **Guivos Intelligence** coordena perguntas, validação e exibição; **serviços canônicos** preservam fatos, versões, consentimento e origens. CAP-09 não é árbitro automático de decisões humanas.

## 2. Vocabulário
| Termo | Definição | Tratamento |
| --- | --- | --- |
| Desconhecido | Não há evidência suficiente para responder | Registrar ausência e, se útil, perguntar |
| Ambiguidade | Registro comporta mais de uma interpretação razoável | Preservar interpretações e solicitar contexto |
| Divergência | Fontes/modelos produzem respostas distintas | Comparar por afirmação, fonte e escopo |
| Contradição aparente | Diferenças explicáveis por período, conceito, modalidade ou contexto | Não classificar como conflito real |
| Contradição substantiva | Afirmações incompatíveis sobre o mesmo atributo, sujeito, período e escopo | Sinalizar e qualificar impacto |
| Fonte obsoleta | Fonte expirou, foi corrigida ou perdeu atualidade | Invalidação/reverificação |
| Conflito de evidências | Suportes válidos apontam para respostas mutuamente incompatíveis | Suspender conclusão dependente ou apresentar limites |
| Incerteza de método | Extração, classificação ou interpretação é insuficientemente validada | Não promover a achado confirmado |

A origem da informação e seu tipo epistêmico permanecem visíveis: evento observado, relato atribuído, registro profissional, documento externo e inferência de IA.

## 3. Tipologia de divergências
- **Temporal:** a Pessoa relata disponibilidade em datas diferentes; pode representar evolução.
- **Semântica:** palavras idênticas têm significados/contextos diferentes.
- **De fonte:** documento externo e declaração divergem sobre requisito.
- **De extração:** transcrição ou leitura de anexo contém possível erro.
- **De autorização:** uma fonte existe, mas não pode ser utilizada nesta finalidade; ausência de acesso não é ausência do fato.
- **Entre modelos:** GPT/Claude/Gemini produzem inferências diferentes sobre a mesma evidência.
- **De versão:** um resultado foi produzido sobre contexto já revisado.
- **De horizonte:** requisito válido hoje não necessariamente será válido na data futura.
- **De granularidade:** relato amplo não contradiz automaticamente evento pontual.

Nenhum tipo de divergência autoriza inferência psicológica ou causal automática.

## 4. Regras de comparação de afirmações
Antes de classificar conflito, verificar:
1. A identidade do sujeito e o isolamento de dados;
2. O atributo/conceito de que se trata;
3. O período ao qual cada afirmação se refere (`occurred_at`, `recorded_at`, `valid_from`, `as_of`);
4. A finalidade e o escopo autorizados;
5. Origem, versão, independência e limites da fonte;
6. Tipo epistêmico (fato técnico, relato, hipótese);
7. Natureza da incompatibilidade e sua relevância para a decisão.

Respostas de três modelos derivadas de um único documento contam como **uma origem de dados**, ainda que três métodos produzam interpretações.

## 5. Estados e encaminhamento
- `consistent_with_available_evidence`: coerência limitada às evidências acessíveis.
- `unknown`: insuficiência de dados.
- `ambiguous`: múltiplos sentidos possíveis.
- `apparent_conflict_temporally_explained`: divergência explicável pelo tempo.
- `unresolved_conflict`: incompatibilidade substantiva pendente.
- `model_disagreement`: divergência entre interpretações dos modelos.
- `stale`: informação/análise sem validade para o momento.
- `requires_human_review`: revisão qualificada necessária.
- `blocked_by_authorization`: não permitido analisar ou revelar a fonte.

**Regra de publicação:** nenhuma conclusão decisiva dependente de conflito substantivo sem resolução deve ser apresentada como fato confirmado. Pode-se apresentar uma síntese com limites, ou interromper o resultado específico.

## 6. Processo lógico
1. Receber pedido, finalidade, versão, autorização e claims candidatos.
2. Recuperar evidências mínimas pertinentes sob controle de acesso.
3. Normalizar sujeito, conceito, período, versão e tipo de fonte.
4. Detectar possíveis divergências sem concluir conflito prematuramente.
5. Examinar se diferenças são temporais, semânticas ou de escopo.
6. Verificar suporte de cada afirmação com CAP-03.
7. Comparar interpretações GPT, Claude e Gemini **por afirmação e fundamento**, nunca por votação.
8. Produzir classificação, evidências a favor/contra, limites e impacto.
9. Propor perguntas neutras ou revisão humana quando pertinente.
10. Sinalizar claims dependentes a CAP-10 para invalidação futura.
11. Entregar ao Guivos Intelligence apenas o que for autorizado, com versão e estado.

## 7. Regras de decisão
- **Conflito resolvido por fonte verificável:** registrar por que uma fonte é aplicável, sem apagar o registro histórico divergente.
- **Diferença temporal legítima:** registrar mudança ao longo do tempo, não acusar inconsistência da Pessoa.
- **Modelos discordam e evidências não resolvem:** preservar alternativas, declarar incerteza e solicitar mais informações.
- **Dados faltantes:** perguntar em vez de supor.
- **Fonte não autorizada:** não utilizá-la como prova nem insinuar conteúdo confidencial.
- **Alto impacto ou sensibilidade:** revisão humana qualificada, respeitando critérios específicos ainda a definir.
- **Modelo indisponível:** reportar indisponibilidade; não gerar resultado fingindo execução múltipla.

## 8. Contrato lógico de solicitação (sintético, não implementado)
```json
{
  "capability": "GAI-CAP-09",
  "method_version": "proposed-1",
  "purpose": "assess_uncertainty_and_conflicts",
  "subject_ref": "synthetic-person",
  "authorization_ref": "server-verified-reference",
  "context_version": "revision-61",
  "as_of": "2026-10-31T13:00:00-03:00",
  "claim_refs": ["claim-1", "claim-2"],
  "source_refs": ["source-1", "source-2"],
  "model_result_refs": ["optional-gpt", "optional-claude", "optional-gemini"]
}
```
O campo de autorização é apenas referência: a verificação é realizada pelo serviço competente, não pelo próprio cliente. Dados do exemplo são sintéticos.

## 9. Contrato lógico de resposta (sintético)
```json
{
  "capability": "GAI-CAP-09",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-61",
  "status": "needs_clarification",
  "findings": [
    {
      "finding_id": "f-1",
      "state": "apparent_conflict_temporally_explained",
      "claim_refs": ["claim-1", "claim-2"],
      "supporting_refs": ["source-1", "source-2"],
      "explanation": "Os relatos se referem a meses diferentes e podem representar mudança de rotina.",
      "impact_on_decision": "revalidate_current_availability",
      "questions_for_person": ["Qual disponibilidade corresponde à sua rotina atual?"],
      "requires_human_review": false
    }
  ],
  "unresolved_claim_refs": [],
  "limitations": ["A síntese está limitada às fontes autorizadas."],
  "method_version": "proposed-1"
}
```
Contratos, estados e identificadores são **propostas conceituais**, não APIs reais ou resultados de execução.

## 10. Exemplo sintético com modelos distintos
A Pessoa relatou mudança recente de horário. GPT sugere indisponibilidade para curso, Claude aponta falta de informação e Gemini propõe possível participação online.

**Análise correta:** a condição deve ser verificada com a Pessoa e o requisito do curso com fonte confiável. A hipótese de formato online requer oferta confirmada. Nenhum modelo pode ser eleito vencedor apenas por concordância ou confiança textual.

**Não afirmar:** “A Pessoa é contraditória”, “está evitando estudar” ou “a maioria dos modelos confirma que não pode participar”.

## 11. Escalonamento e revisão humana
Propor revisão humana quando:
- divergência altera substancialmente recomendação de alto impacto;
- fontes autorizadas permanecem incompatíveis e não há regra de resolução;
- risco de exposição de dado sensível ou compartilhamento profissional inadequado;
- interpretação aparenta diagnóstico psicológico/clínico;
- a Pessoa contesta síntese substantiva;
- regra de elegibilidade tem efeito relevante e não está comprovada.

A autoridade e os critérios formais de revisão ainda devem ser definidos pela governança. Revisão humana não equivale a consentimento nem autoriza acesso fora de escopo.

## 12. Interação com CAP-10
CAP-09 identifica inconsistências e dependências. CAP-10 será responsável por coordenar **invalidação, atualização e reavaliação** de análises afetadas após novos registros, mudança de condição, revisão de requisito ou revogação. Uma resposta obsoleta não deve substituir resultado de contexto mais recente no Intelligence.

## 13. Segurança, privacidade e falhas
- Revogação durante análise: interromper novas leituras e aplicar políticas de invalidação/retenção.
- Fonte de outra Pessoa/instituição: bloquear acesso e não revelar conteúdo.
- Documento/áudio não interpretado: declarar limite, não completar lacunas por suposição.
- Neo4j ou provedor indisponível: retornar estado degradado ou indisponível, sem fabricar comparações.
- Evidência antiga corrigida: não manter conflito desatualizado como atual.
- Referências de fonte em relatório: mostrar somente as que o consumidor está autorizado a conhecer.
- Falta de registro de inscrição/participação: não inferir rejeição consciente.
- Divergência entre modelos: registrar versões/métodos sem expor segredos ou dados indevidos.

## 14. Avaliação sintética inicial — nenhum teste executado
| ID | Cenário | Comportamento esperado |
| --- | --- | --- |
| CAP09-E01 | Mudança de disponibilidade entre meses | Alteração temporal, não contradição automática |
| CAP09-E02 | Duas afirmações incompatíveis do mesmo período | Conflito não resolvido |
| CAP09-E03 | Dados insuficientes | Unknown, não suposição |
| CAP09-E04 | GPT/Claude/Gemini discordam | Revisão por evidência, sem votação |
| CAP09-E05 | Três modelos repetem fonte única | Não contar como fontes independentes |
| CAP09-E06 | Documento expirado diverge de atualização | Fonte atual qualificada sem apagar histórico |
| CAP09-E07 | Transcrição ambígua | Solicitar confirmação |
| CAP09-E08 | Informação de profissional fora de escopo | Não acessar/revelar |
| CAP09-E09 | Oportunidade apenas exibida | Não concluir consciência ou rejeição |
| CAP09-E10 | Contexto revisado durante análise | Resultado antigo obsoleto |
| CAP09-E11 | Pessoa contesta interpretação | Encaminhar revisão sem rotular Pessoa |
| CAP09-E12 | Dois conceitos semanticamente diferentes | Evitar falso conflito |
| CAP09-E13 | Dados de outra Pessoa aparecem no envelope | Rejeitar por isolamento |
| CAP09-E14 | Revogação de autorização | Bloquear acesso e seguir política |
| CAP09-E15 | Neo4j indisponível | Não fabricar consulta ao histórico |
| CAP09-E16 | Contradição de alto impacto | Revisão humana quando exigida |
| CAP09-E17 | Requisito mudou de obrigatório para opcional | Preservar versão e reavaliar conclusão |
| CAP09-E18 | Modelos concordam em afirmação falsa | Rejeitar pela evidência |
| CAP09-E19 | Possibilidades diferentes, ambas plausíveis | Não classificar como contradição |
| CAP09-E20 | Ausência de documentação sobre experiência | Não afirmar inexistência da experiência |

**Maturidade:** definir posteriormente rubricas, métricas de falsos conflitos, resolução por fontes, transparência, segurança, testes adversariais e autoridade dos gates. Falhas críticas de privacidade, diagnóstico impróprio ou certeza fabricada impedem homologação.

## 15. Dependências e questões abertas
Dependências de CAP-03 (suporte), CAP-01/02 (tempo/contexto), CAP-04/06/08 (requisitos/ofertas), CAP-10 (invalidação), serviços canônicos de identidade/autorização/contexto e auditoria. Não requer que GPT/Claude/Gemini sejam sempre executados em conjunto.

Pendências: taxonomia final de severidade, mecanismo de resolução por domínio, critérios de revisão humana, métricas de qualidade, esquema de registro das divergências, política de retenção e limites de exposição por consumidor.

**Documentos relacionados:** [Documento Mestre](index.md) · [Matriz](matriz-capacidades-guivos-ai.md) · [CAP-03](cap-03-interpretacao-fundamentada-evidencias.md) · [Modelo de Evidências](modelo-evidencias-rastreabilidade.md) · [Avaliação e Validação](avaliacao-validacao-qualidade.md).

**GKR, Replit e Neo4j permanecem inalterados.**
