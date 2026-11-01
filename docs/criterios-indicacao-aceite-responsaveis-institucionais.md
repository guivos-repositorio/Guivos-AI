# GAI-INT-44 — Critérios Institucionais de Indicação e Aceite

**Versão documental 7.3 · 31/10/2026**  
**Estado:** minuta submetida à direção; critérios propostos, não ratificados. Nenhum titular nomeado.

## 1. Decisão que esta minuta prepara
A Guivos deve estabelecer critérios verificáveis para **indicar, aceitar, revisar, substituir e desligar** os responsáveis pela cadeia de confiança antes de nomear pessoas. O "de acordo, segue" desta etapa autoriza o desenvolvimento documental, não aprova os critérios nem concede autorização operacional.

A [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md) preserva a autoridade administrativa central da direção, mas **não constitui prova externa de identidade**. Uma função de controle não pode autenticar unilateralmente a própria nomeação.

## 2. Condições mínimas gerais
1. **Indicação expressa:** decisão administrativa da direção com papel, alçada, duração, limites e referência documental.
2. **Identidade verificada:** evidência institucional verificável, protegida fora do repositório público; sem assumir identidade a partir de nome de usuário ou conversa.
3. **Aceite individual:** declaração verificável de ciência de deveres, conflito de interesses, independência, confidencialidade, substituição e revogação.
4. **Competência compatível:** experiência ou qualificação comprovável conforme o papel, com revisão independente em funções técnicas.
5. **Segregação:** responsável por operar campanha não pode revisar a própria execução, emitir sua própria autorização nem alterar a cadeia de confiança.
6. **Menor privilégio e duração limitada:** alçadas, permissões e mandatos explicitados, renovação dependente de avaliação.
7. **Auditabilidade e saída:** nomeação, aceite, alteração de função, afastamento, suspensão e substituição documentados; nenhuma função permanece ativa após revogação.

## 3. Critérios específicos por papel
| Papel | Requisitos de indicação propostos | Evidências e impedimentos |
| --- | --- | --- |
| ROLE-REG — Registrador institucional | Independência do operador, capacidade de validar vínculo institucional e administrar inventário público mínimo de chaves | Método externo de verificação, trilha de revisão e aceite; não autoriza campanhas |
| ROLE-CUS — Custodiante de chaves | Competência operacional em custódia e recuperação, dupla verificação, separação entre aprovador e assinante | Plano de custódia, rotação, recuperação, aceite; sem chave privada no GitHub |
| ROLE-REV — Revisor de segurança | Competência em segurança de aplicações, identidade, assinatura, isolamento e controle de evidências | Independência do executor, declaração de conflitos, parecer formal |
| ROLE-OPS — Operador de campanha | Competência no ambiente offline e nos runners, treinamento para interrupção e registro de incidentes | Acesso mínimo e prazo limitado; não emite autorização ou aprova gate |
| ROLE-AUD — Auditor de evidências | Competência em auditoria de integridade e rastreabilidade | Não ser operador da campanha auditada; parecer registrável |
| ROLE-DIR — Direção | Autoridade administrativa central reconhecida no registro GAI-DEC-011 | Vinculação institucional e identidade ainda exigem comprovação independente para confiança criptográfica |

## 4. Fluxo de indicação e aceite
**Etapa 1 — critérios:** direção aprova ou revisa esta política, sem designar pessoas automaticamente.

**Etapa 2 — indicação:** direção indica um candidato por função, com mandato, escopo e justificativa.

**Etapa 3 — verificação:** verificadores independentes conferem identidade, competência e conflito de interesses. A direção não pode usar uma autorização autodeclarada como prova única.

**Etapa 4 — aceite:** o candidato confirma formalmente a função. Sem aceite, o campo `accepted` permanece falso e o posto continua vago.

**Etapa 5 — habilitação separada:** designação e aceite não emitem chaves, não ativam sistemas e não autorizam testes. Eventuais acessos dependerão de decisões específicas e controles técnicos aprovados.

**Etapa 6 — reavaliação:** mandato e aceites devem ser reavaliados na expiração, alteração de escopo, incidente, mudança de pessoa ou conflito de interesse.

## 5. Incompatibilidades e substituição
É proibido que o mesmo responsável seja simultaneamente operador e revisor da mesma campanha ou opere a própria emissão/revogação de autorização. Acúmulo de funções institucionais somente pode ser analisado caso a caso, com justificativa, revisão independente e controles compensatórios; funções incompatíveis não são acumuláveis.

Desligamento, perda de mandato ou comprometimento impõem suspensão imediata das permissões relacionadas, revogação de credenciais quando existirem, custódia de evidências e nomeação de sucessor mediante novo aceite. A ausência de sucessor mantém a função suspensa, sem bypass automático.

## 6. Critérios de deliberação e evidência
**DIR-C44-01:** aprovar ou revisar os sete critérios gerais.  
**DIR-C44-02:** aprovar ou revisar os impedimentos entre funções.  
**DIR-C44-03:** aprovar ou revisar o fluxo de indicação, verificação e aceite.  
**DIR-C44-04:** aprovar ou revisar a política de suspensão, substituição e reavaliação.

As quatro escolhas estão **pendentes** no [registro JSON](criterios-indicacao-aceite-responsaveis-candidatos.json). A aprovação de política não é nomeação, aceite, autorização B/C ou implantação.

## 7. Limites
Não existe registrador, custodiante, revisor, operador ou auditor nomeado/aceito por este documento. Nenhuma chave, credencial, serviço ou infraestrutura foi ativada. Pedidos B e C não autorizados; 82 casos catalogados, nenhum teste executado; G0 parcial, G1–G6 pendentes; PND-01 a PND-16 abertas.

Referências: [GAI-INT-43](matriz-deliberacao-pendencias-institucionais-inst01-inst07.md) · [GAI-INT-42](modelo-institucional-emissao-custodia-revogacao-autorizacoes.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md).
