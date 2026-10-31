# GAI-CAP-04 — Identificação e Qualificação de Lacunas
**Especificação de capacidade · Versão documental 1.6 · 31/10/2026**
**Estado:** conceituada; método, contratos e testes propostos. Não implementada, homologada ou liberada no Replit.

## 1. Objetivo e princípio
A CAP-04 identifica e qualifica **diferenças contextuais entre condições conhecidas da Pessoa e requisitos pertinentes a uma possibilidade, oportunidade ou caminho específico**. Uma lacuna é uma relação entre condições e requisitos, **não uma deficiência de caráter, mérito, personalidade ou potencial pessoal**.

A capacidade deve produzir achados rastreáveis, dizer quando não há informação suficiente e propor perguntas ou tipos de apoio para investigar e, quando pertinente, aproximar caminhos. Não determina que a Pessoa deva perseguir qualquer possibilidade.

## 2. Dependências e responsabilidade
- **CAP-01:** trajetória documentada e mudanças relevantes.
- **CAP-02:** momento presente, condições e informação desconhecida.
- **CAP-03:** suporte, fonte, temporalidade e limites de cada afirmação.
- **CAP-05/06:** possibilidades futuras e compatibilidade contextual poderão consumir lacunas qualificadas; evitar dependência circular obrigatória: a CAP-04 aceita uma possibilidade/caminho especificado e validamente fornecido por fonte externa ou por serviço prospectivo.
- **CAP-08:** requisitos e disponibilidade de oportunidades deverão ser confirmados nas fontes respectivas.
- **CAP-09/10:** contradições, revisão e invalidação são funções transversais.

**Dados canônicos e autorizações:** serviços do ecossistema. **Método especializado:** Guivos AI. **Orquestração e validação com a Pessoa:** Guivos Intelligence.

## 3. Termos obrigatórios
- **Requisito obrigatório:** condição comprovadamente necessária ao caminho/oportunidade em contexto e prazo definidos.
- **Condição facilitadora:** pode ajudar, mas não é pré-requisito necessário.
- **Preferência:** escolha da Pessoa ou característica desejável; não converter em requisito universal.
- **Condição contextual:** informação atribuída/observada e temporalmente qualificada sobre recursos, horários, experiências, mobilidade, acessibilidade etc.
- **Lacuna confirmada:** requisito aplicável e vigente + evidência suficiente de condição não atendida na referência temporal.
- **Possível lacuna:** indício plausível, mas falta confirmação da condição, da aplicabilidade ou do requisito; requer verificação.
- **Informação desconhecida:** ausência de evidência suficiente; **não** constitui lacuna.
- **Barreira externa:** exigência, infraestrutura, regra, acesso ou custo imposto pelo contexto, sem atribuir culpa ou insuficiência à Pessoa.
- **Caminho alternativo:** uma forma diferente e verificável, quando possível, de explorar objetivo sem exigir o mesmo conjunto de condições.

## 4. Taxonomia inicial de condições
| Dimensão | Exemplos | Erro a evitar |
| --- | --- | --- |
| Formação e certificação | Certificado necessário, pré-requisito acadêmico | Presumir incapacidade sem documento |
| Experiência e prática | Experiência exigida por uma oferta específica | Transformar preferência do recrutador em regra universal |
| Tempo e agenda | Encontros fixos, carga horária, datas | Inferir indisponibilidade nos demais dias a partir de um dia informado |
| Recursos financeiros | Taxa, material, transporte, custos de participação | Supor pobreza ou recursos com base em perfil |
| Mobilidade e localização | Distância, deslocamento, presença | Presumir veículo, imigração ou documento |
| Acessibilidade | Formato e adaptações requeridas | Diagnosticar condição clínica ou atribuir barreira à Pessoa |
| Infraestrutura habilitadora | Internet, equipamento, cuidado infantil | Ignorar que recursos de apoio podem resolver barreira |
| Documentação e elegibilidade | Requisitos legais/institucionais com validade | Inventar regras ou usar normas expiradas |
| Informação e conexões | Necessidade de orientação, acesso a dados, contatos | Tratar rede limitada como falha pessoal |

Não criar taxonomia obrigatória da vida da Pessoa. Categorias são instrumento interno e contextual.

## 5. Estados de avaliação por requisito
| Estado | Definição | Conduta |
| --- | --- | --- |
| **Atendido** | Evidência adequada demonstra condição pertinente no período | Registrar suporte e validade |
| **Não atendido** | Evidência adequada demonstra ausência atual da condição exigida | Lacuna confirmada, com explicação não moralizante |
| **Desconhecido** | Não há dados suficientes para confirmar ou negar | Formular pergunta; não criar lacuna |
| **Em verificação** | Há registros conflitantes, desatualizados ou ambíguos | Revisar fontes e tempos |
| **Não aplicável** | Requisito não incide sobre o caminho analisado | Não penalizar nem calcular lacuna |

Não usar score global de valor, potencial ou sucesso da Pessoa.

## 6. Condições para declarar uma lacuna confirmada
A CAP-04 somente poderá produzir `confirmed_gap` quando todos os seguintes elementos estiverem presentes:
1. Possibilidade/oportunidade/caminho identificado e legitimamente selecionado para análise;
2. Requisito específico, aplicável, com origem, natureza e validade verificáveis;
3. Condição contextual da Pessoa referente ao **mesmo requisito, contexto e período**;
4. Evidência autorizada e suficiente mostrando condição **não atendida**;
5. Relação justificável entre requisito e condição, com registro de fonte e versão.

Se faltar suporte, manter `possible_gap`, `unknown` ou `under_review`. Não transformar requisitos típicos do mercado em exigências universais.

## 7. Fluxo analítico proposto
1. Receber finalidade, possibilidade/caminho, referência do momento, versão e escopo autorizado.
2. Resolver requisitos na origem confiável, diferenciando obrigatório, facilitador e preferência.
3. Verificar temporalidade, elegibilidade e validade do requisito e da oferta.
4. Recuperar apenas condições pertinentes por serviço autorizado.
5. Aplicar CAP-03 à evidência de ambos os lados, detectando lacunas de informação.
6. Comparar requisito e condição **item a item**, com estados distintos.
7. Distinguir barreiras individuais, institucionais e externas sem imputar culpa.
8. Identificar alternativas ou categorias de Direct/Enabling Supply; só afirmar disponibilidade se houver oferta validada.
9. Produzir perguntas abertas para unknowns e divergências.
10. Devolver evidências, limitações, validade e estado de revisão ao Intelligence.
11. Reavaliar após mudanças de objetivo, requisito, fonte ou autorização.

## 8. Contrato de solicitação proposto (dados sintéticos)
```json
{
  "capability": "GAI-CAP-04",
  "method_version": "proposed-1",
  "purpose": "qualify_contextual_gaps",
  "subject_ref": "synthetic-person",
  "authorization_ref": "verified-on-server-reference",
  "context_version": "revision-12",
  "as_of": "2026-10-31T12:00:00-03:00",
  "path_ref": "synthetic-path",
  "requirement_refs": ["verified-requirement-ref"],
  "condition_refs": ["authorized-condition-ref"]
}
```
A referência de autorização **não** dispensa verificação em servidor por identidade, finalidade, vínculo, prazo e escopo.

## 9. Contrato de resposta proposto (dados sintéticos)
```json
{
  "capability": "GAI-CAP-04",
  "analysis_id": "synthetic-analysis",
  "context_version": "revision-12",
  "status": "needs_validation",
  "path_ref": "synthetic-path",
  "requirements": [
    {
      "requirement_ref": "requirement-1",
      "kind": "mandatory",
      "state": "unknown",
      "condition_ref": null,
      "evidence_refs": ["offer-rule-1"],
      "gap_status": "not_confirmed",
      "reason": "Disponibilidade da Pessoa nesse horário não foi informada.",
      "questions_to_validate": ["Você teria disponibilidade às quartas?"]
    }
  ],
  "confirmed_gaps": [],
  "possible_gaps": [],
  "unknowns": ["Disponibilidade às quartas"],
  "enabling_opportunity_categories": ["alternative_schedule"],
  "limitations": ["Nenhuma oferta alternativa foi verificada."],
  "method_version": "proposed-1"
}
```
Campos são ilustrativos, não contrato técnico final. A ausência de lacunas confirmadas **não** equivale a plena compatibilidade.

## 10. Caso sintético — curso presencial
Uma oferta exige presença **às quartas-feiras**, segundo fonte verificada. A Pessoa declarou somente estar livre **às terças-feiras**, sem informar disponibilidade em outros dias.

**Resultado correto:** condição de quarta-feira **desconhecida**. Não existe evidência de incompatibilidade confirmada. Perguntar sobre quartas ou buscar alternativas de horário **sem afirmar que já existem ofertas alternativas**.

Se a Pessoa confirmar indisponibilidade às quartas e o requisito permanecer vigente, registrar **lacuna contextual confirmada para esta oferta**, sem generalizar para todas as formações.

Se surgir curso remoto válido ou apoio de transporte, registrar como alternativa potencial verificada, não como garantia de participação.

## 11. Oportunidades intermediárias e circulação de condições
A CAP-04 não deve apenas listar faltas. Deve distinguir:
- **Direct Supply:** formações, práticas, mentorias, oportunidades profissionais, eventos e comunidades de prática;
- **Enabling Supply:** deslocamento, acessibilidade, conectividade, equipamento, documentação, apoio e infraestrutura.

Recomendações devem preservar custo, tempo, acesso, requisitos e limitações quando conhecidos. Ausência de oferta disponível no ecossistema não extingue a possibilidade futura nem justifica inventar um match.

## 12. Falhas, revisão e privacidade
- Requisito expirado: `under_review` ou rejeitar uso como válido;
- Fonte inacessível: não declarar lacuna confirmada;
- Dados pessoais não autorizados: negar consulta sem revelar conteúdo;
- Correção de condição: invalidar achados dependentes;
- Resultado antigo frente a nova revisão: Intelligence não pode apresentá-lo como atual;
- Neo4j/provedor externo indisponível: sinalizar cobertura incompleta;
- Informação sensível ou clínica: segregação, minimização e restrições próprias;
- Divergência GPT/Claude/Gemini: cotejar requisitos/evidências, não resolver por votação.

## 13. Fixtures sintéticas propostas (não executadas)
| ID | Cenário | Resultado exigido |
| --- | --- | --- |
| CAP04-E01 | Dia livre diferente do dia exigido; outros dias desconhecidos | Unknown, não lacuna confirmada |
| CAP04-E02 | Indisponibilidade expressamente confirmada para dia obrigatório | Confirmed gap específico |
| CAP04-E03 | Requisito de preferência confundido com obrigatório | Corrigir tipo; não impor |
| CAP04-E04 | Requisito expirado | Não utilizar como vigente |
| CAP04-E05 | Ausência de comprovante de curso | Não afirmar ausência de formação |
| CAP04-E06 | Barreira de mobilidade com apoio disponível | Reconhecer enabling supply |
| CAP04-E07 | Oferta apenas exibida | Não inferir recusa |
| CAP04-E08 | Mudança de rotina posteriormente informada | Reavaliar e invalidar resultado anterior |
| CAP04-E09 | Dois modelos concordam com requisito inventado | Recusar ausência de fonte |
| CAP04-E10 | Condição de Pessoa diferente incluída indevidamente | Bloquear por isolamento |
| CAP04-E11 | Requisito não aplicável ao caminho alternativo | Não aplicável |
| CAP04-E12 | Fonte profissional de escopo restrito | Não revelar fora do escopo |
| CAP04-E13 | Possibilidade sugerida sem interesse validado | Não atribuir objetivo à Pessoa |
| CAP04-E14 | Custo não informado | Unknown, não presumir falta de recursos |
| CAP04-E15 | Oferta intermediária não verificada | Categoria a buscar, não oferta disponível |
| CAP04-E16 | Correção/revogação durante análise | Suspender uso e propagar invalidação |

A homologação dependerá de métricas, evidências de testes, revisão humana, autorização, riscos e gates previstos no documento de avaliação v1.1.

## 14. Integração e dependências
**Guivos AI:** compara e qualifica condições com requisitos; devolve achados sustentados.
**Guivos Intelligence:** define quando perguntar, apresenta resultados contextualizados, valida interesse e direcionamento com a Pessoa.
**Serviços de contexto/oportunidades:** preservam fatos, requisitos e seus estados canônicos.
**Neo4j:** poderá manter relações, dependências, versões e proveniência via serviços autorizados.
**GPT/Claude/Gemini:** podem apoiar tarefas analíticas sem se tornarem fontes de verdade.

A matriz v1.2–1.6 representa a CAP-04 como **conceituada**. Nenhuma alteração do Replit, liberação de gates, operação de Neo4j ou modificação do GKR é autorizada aqui.

## 15. Decisões pendentes
- Taxonomia final de requisito versus condição facilitadora;
- Critérios por domínio para validade temporal e suficiência da evidência;
- Modelo físico Neo4j e fontes transacionais dos requisitos;
- Regras de autorização, revisão e transparência no consumo B2B;
- Avaliação de viabilidade de ofertas habilitadoras;
- Formato e linguagem para apresentar lacunas sem estigmatização;
- Contrato versionado CAP-04/CAP-06 e riscos de interpretação.

**Documentos associados:** [Documento Mestre](index.md) · [Matriz de Capacidades](matriz-capacidades-guivos-ai.md) · [CAP-02](cap-02-sintese-momento-atual.md) · [CAP-03](cap-03-interpretacao-fundamentada-evidencias.md) · [Motor de Lacunas](motor-possibilidades-lacunas.md) · [Modelo de Avaliação](avaliacao-validacao-qualidade.md).
