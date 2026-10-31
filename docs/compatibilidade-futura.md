# Inteligência de Compatibilidade Futura — Guivos AI
**Versão 0.4 · 31/10/2026 · Estado: proposta conceitual, não implementada**

## 1. Objetivo
Avaliar como condições atuais de uma Pessoa se relacionam com requisitos de possibilidades futuras e quais mudanças ou oportunidades intermediárias poderiam viabilizar caminhos escolhidos. **Compatibilidade não é uma nota da Pessoa, previsão de sucesso ou juízo de mérito.** É uma avaliação específica, temporal e fundamentada de condições para um determinado caminho.

## 2. Princípios
- Uma Pessoa pode optar por não perseguir qualquer possibilidade; não há trajetória obrigatória.
- Cada futuro considerado deve indicar origem: declarado, adjacente, emergente ou exploratório.
- Distinguir requisito obrigatório, condição facilitadora, preferência e barreira externa.
- Diferenciar condição atendida, não atendida com evidência, desconhecida, não aplicável e condição contestada.
- Nunca declarar falta de capacidade quando só há falta de informação.
- Não supor que uma oportunidade exibida foi percebida ou recusada.
- Evidências devem ter fonte, data, finalidade autorizada e prazo de validade.
- Não inferir autossabotagem ou diagnóstico psicológico a partir de eventos de navegação.

## 3. Modelo de comparação
**Entrada A — Momento atual:** contexto validado, competências, recursos, agenda, preferências e condições de acesso.

**Entrada B — Possibilidade futura:** experiência ou objetivo explorável, escolhido ou aceito para análise pela Pessoa.

**Entrada C — Requisitos do caminho:** exigências reais de uma oferta, normas aplicáveis ou condições plausíveis explicitamente sinalizadas como hipótese.

**Processo:**
1. Identificar quais condições são relevantes para a possibilidade.
2. Verificar quais já possuem evidência suficiente.
3. Expor lacunas comprovadas sem confundí-las com dados desconhecidos.
4. Procurar caminhos intermediários, inclusive apoios habilitadores.
5. Comparar alternativas em custo, tempo, acessibilidade, esforço e reversibilidade, somente quando houver informação confiável.
6. Formular perguntas para resolver dúvidas.
7. Exibir a análise à Pessoa e, se autorizado, ao profissional.
8. Reavaliar quando novos registros, preferências ou requisitos surgirem.

## 4. Estados de compatibilidade por requisito
| Estado | Significado |
| --- | --- |
| Atendida | Evidência atual suficiente para um requisito específico. |
| Não atendida | Evidência adequada mostra ausência atual da condição exigida. |
| Desconhecida | Dados insuficientes; não caracterizar como lacuna confirmada. |
| Em verificação | Informação nova ou divergente requer confirmação. |
| Não aplicável | O requisito não incide no caminho avaliado. |

A apresentação não precisa de um percentual único de compatibilidade. Se houver métricas, devem representar somente requisitos verificáveis e nunca pontuar o valor ou o potencial da Pessoa.

## 5. Categorias de oportunidades intermediárias
- **Direct Supply:** formação, prática, mentoria, vagas, comunidades, atividades, experiências.
- **Enabling Supply:** transporte, acesso à internet, equipamentos, acessibilidade, documentação, cuidado infantil e infraestrutura.
- **Ajustes de contexto:** mudança de agenda, obtenção de informação, adaptação de formato ou apoio; não presumir que sejam viáveis ou desejados.

Uma oportunidade intermediária só pode ser chamada de **disponível** se tiver existência, requisitos e validade verificados. Caso contrário, indicar categoria de oportunidade a buscar.

## 6. Demonstração sintética
**Possibilidade:** participar de uma formação presencial de tecnologia em outro município.

**Momento atual:** interesse em tecnologia declarado; horário livre às terças relatado; deslocamento e custos não informados.

**Requisitos da oferta:** presença às quartas, matrícula até 15/11, transporte até o local. Os requisitos são hipotéticos neste exemplo.

**Análise:** incompatibilidade de horário potencial (a Pessoa só informou disponibilidade às terças); custo e transporte desconhecidos, não faltas confirmadas.

**Caminhos:** investigar turma em outro horário; verificar transporte e acessibilidade; considerar modalidade remota se existir oferta verificável.

**Perguntas:** “É possível participar às quartas?”; “Você deseja explorar turmas remotas?”; “Quais condições de deslocamento devem ser consideradas?”

Não afirmar que a Pessoa perdeu uma chance ou deixou de evoluir.

## 7. Relatório e API
Formato lógico proposto para uma unidade de análise:
- `possibility_id`, `origin`, `as_of`, `purpose`;
- `requirement_id`, `requirement_source`, `requirement_status`;
- `evidence_refs`, `evidence_age`, `uncertainties`;
- `intermediate_opportunities` com estado de verificação e validade;
- `alternative_paths`, `questions_to_validate`;
- `person_validation_status`, `professional_review_status`.

Não incluir dados pessoais no repositório público. Um contrato real de API será desenhado depois de definir permissões, proteção de dados e testes.

## 8. Avaliação antes de implementação comercial
Testar com casos sintéticos e revisão humana:
- Taxa de lacunas falsas por informação ausente;
- Acurácia dos requisitos atribuídos a cada oportunidade;
- Fidelidade das referências de evidência;
- Tratamento de mudanças no objetivo e nas condições;
- Existência e validade das oportunidades intermediárias;
- Capacidade de explicar alternativas sem induzir escolhas;
- Respeito às permissões, confidencialidade e revogação de acesso.

## 9. Limites e decisões pendentes
A utilidade comercial do motor, os requisitos técnicos, os segmentos prioritários e a forma de apresentação ainda dependem de validação. A Guivos AI apoia compreensão e escolha, não prevê resultados individuais nem substitui avaliação profissional.

**Repositório:** documentação exclusiva Guivos-AI, independente do GKR.
