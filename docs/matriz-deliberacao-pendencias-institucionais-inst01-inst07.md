# GAI-INT-43 — Matriz de Deliberação das Sete Pendências Institucionais

**Versão documental 7.2 · 31/10/2026**  
**Estado:** proposta para a direção, sem escolhas ratificadas, nomeações ou execução.

## 1. Objetivo
Organizar as sete pendências INST-01 a INST-07 da [GAI-INT-42](modelo-institucional-emissao-custodia-revogacao-autorizacoes.md) em decisões verificáveis. **A autorização para elaborar esta matriz não é aprovação das alternativas.** A autoridade administrativa da direção segue GAI-DEC-011, sem transformar autodeclaração em prova de identidade criptográfica.

## 2. Matriz de decisão
| ID | Questão | Natureza | Encaminhamento recomendado | Evidência de encerramento |
| --- | --- | --- | --- | --- |
| INST-01 | Registrador institucional | administrativa + aceite | A direção pode definir critérios e indicar candidato; independência e aceite exigem comprovação. | Nomeação e evidência de independência |
| INST-02 | Custódia e substituição | mista | A direção define segregação e alçada; revisão técnica determina mecanismo, recuperação e dupla custódia. | Plano de custódia avaliado e aceite |
| INST-03 | Identidade da direção | verificação externa | A autodeclaração GAI-DEC-011 não demonstra vínculo institucional verificável; autoridade de confiança independente deve validar. | Atestado institucional externo e registro protegido |
| INST-04 | Perfil criptográfico | técnica + aprovação | Algoritmo, serialização canônica, âncora, ciclo de chave e validade requerem parecer de segurança antes de aprovação. | Perfil revisado, interoperabilidade e ameaça modelada |
| INST-05 | Revogação offline | técnica + risco | Política de expiração de snapshot, anti-rollback, revogação e interrupção é decisão técnica sujeita ao apetite de risco aprovado pela direção. | Procedimento assinado e teste autorizado em etapa futura |
| INST-06 | Aceites ROLE-REV/OPS/AUD | administrativa + aceite | Direção pode indicar; cada função exige aceite explícito, comprovação de segregação e limites claros. | Termos de aceite e incompatibilidades verificados |
| INST-07 | Custos e limites de implantação | administrativa + orçamento | Preparar faixas de custo; aprovação de orçamento não equivale a autorização de aquisição, acesso ou execução. | Plano de custos e decisão financeira específica |

## 3. Ordem de deliberação
**Fase institucional:** definir critérios de nomeação, segregação e verificação externa (INST-01, INST-03, INST-06); o aceite do indicado permanece individual e independente da indicação.

**Fase técnica:** submeter custódia, assinatura, revogação e ambiente a avaliação de arquitetura/segurança (INST-02, INST-04, INST-05). A direção aprova somente depois do parecer; nenhuma assinatura ou chave deve ser criada nesta etapa.

**Fase financeira:** apresentar alternativas e limites de custo (INST-07). Aprovação de diretriz de orçamento não autoriza aquisição, despesa, conexão ou processamento.

## 4. Modelo de registro por decisão
Para cada INST: identificador, opções analisadas, proposta recomendada, aprovador, data, evidência da decisão, proprietário futuro (se aceito), revisão independente, dependências, limitações, condições de reconsideração e referências. **Não preencher aceites nem titularidade por inferência.**

## 5. Barreiras de governança
A GAI-INT-41 e a GAI-INT-42 continuam **especificações**. O verificador independente, o registrador e o custodiante não estão operacionais. O executor endurecido v2 permanece bloqueado. Pedido B (testes) e Pedido C (inspeção) não autorizados; 82 casos documentados, zero execuções verificadas, G0 parcial, G1–G6 pendentes, PND-01 a PND-16 abertas.

## 6. Próxima decisão solicitada
A direção deverá decidir **primeiro os critérios institucionais** para indicar registrador, custodiante e revisores — sem pressupor nomes — e definir a forma independente de comprovação de sua própria identidade institucional. O [registro estruturado das sete pendências](matriz-deliberacao-pendencias-institucionais-inst01-inst07.json) mantém todas as escolhas nulas até deliberação explícita.

Referências: [GAI-INT-42](modelo-institucional-emissao-custodia-revogacao-autorizacoes.md) · [GAI-INT-41](cadeia-confianca-autorizacoes-execucao-candidata.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md).
