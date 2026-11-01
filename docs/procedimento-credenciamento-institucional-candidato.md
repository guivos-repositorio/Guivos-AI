# GAI-INT-45 — Procedimento Candidato de Credenciamento Institucional

**Versão documental 7.5 · 31/10/2026**  
**Estado:** procedimento e modelos documentais preparados; nenhum credenciamento efetuado.

## 1. Autoridade e base
Este procedimento operacionaliza documentalmente a política de elegibilidade, segregação, aceite e substituição aprovada pela [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md). A autorização desta etapa alcança **somente o desenho dos procedimentos e modelos**, não a indicação de titulares, coleta de documentos pessoais, criação de credenciais ou operação.

A direção conserva a decisão de nomear. Um registrador verificará vinculação institucional quando formalmente designado, e um revisor independente avaliará conflito e qualificação. Sem registrador ou revisor formalmente aceitos, os fluxos são **não iniciáveis**.

## 2. Sequência proposta e condições de bloqueio

| Etapa | Responsabilidade futura | Evidência mínima | Bloqueio |
| --- | --- | --- | --- |
| P-01 Solicitar indicação | Direção | Ato com papel, escopo, duração, justificativa e referência | Sem assinatura/autoria institucional verificável |
| P-02 Proteger documentação | Administração autorizada | Canal privado apropriado, acesso mínimo, prazo de retenção | GitHub público ou meios não aprovados |
| P-03 Verificar identidade | Registrador independente | Comprovação institucional externa, evidência armazenada fora do repositório | Verificação exclusivamente autodeclarada |
| P-04 Avaliar competência e conflitos | Revisor independente | Parecer, incompatibilidades, qualificações pertinentes | Operador e revisor coincidentes |
| P-05 Obter aceite | Indicado | Aceite individual, ciência de deveres e mandato | Falta ou recusa de aceite |
| P-06 Registrar a nomeação | Direção + registrador | Decisão específica e trilha de auditoria; referência pública pseudônima | Documentos P-03 a P-05 incompletos |
| P-07 Avaliar habilitação | Segurança/arquitetura | Projeto de acesso aprovado em ato separado | Nomeação usada como autorização de acesso |
| P-08 Reavaliar ou substituir | Direção + controles independentes | Revisão periódica, revogação e encerramento de acessos | Sucessor considerado ativo antes do aceite |

**Não coletar** nesta etapa CPF, documentos, biometria, contatos privados ou dados de candidatos. A política de privacidade/retenção do futuro ambiente de credenciamento deverá ser definida antes de qualquer coleta.

## 3. Três modelos separados

1. [Modelo de indicação](modelo-indicacao-institucional-candidato.json): ato administrativo proposto, sem nomeação preenchida.
2. [Modelo de verificação independente](modelo-verificacao-institucional-candidato.json): apenas referências a evidências mantidas em canal seguro, parecer ainda não emitido.
3. [Modelo de aceite individual](modelo-aceite-institucional-candidato.json): aceite ainda não concedido, sem assinatura ou dados identificadores.

Todos os modelos utilizam `state=draft_unfilled`, `nominee_ref=null` e marcadores de aprovação vazios. É vedado interpretar os modelos como nomeações.

## 4. Requisitos de completude do futuro dossiê
Um dossiê válido deverá apresentar: indicação específica; comprovação institucional externa; verificação de independência e conflitos; aceite expresso; mandato e escopo; protocolo de acesso mínimo; substituto (quando aplicável); custódia de evidência em meio privado; possibilidade de revogação e trilha de auditoria. **Mesmo um dossiê completo não autoriza execução do Pedido B/C.**

## 5. Controles de proteção e integridade
- No repositório público, conservar somente referências não identificadoras, versões de modelo e status.
- Evidências pessoais e provas de vínculo institucional ficam em repositório privado autorizado, com controles de acesso, retenção e descarte.
- O verificante não deve ser indicado por quem busca burlar o controle, nem auditar atos que praticou.
- Aceite é revogável; suspensão de papel deve impedir novas autorizações.
- Publicação dos formulários não ativa chaves, certificados, contas, serviços ou permissões.

## 6. Decisões que permanecem pendentes
A direção ainda precisa selecionar e formalizar titulares, mecanismos de verificação externa, método de aceite verificável, local de guarda das evidências, critérios de retenção e processo de revisão independente. INST-01 a INST-07 não se encerram apenas com este procedimento.

## 7. Estado de execução
**Nenhum dossiê preenchido; nenhuma nomeação ou aceite; nenhuma chave criada; nenhum teste executado.** Pedido B e Pedido C não autorizados. G0 parcial; G1–G6 pendentes; PND-01 a PND-16 abertas. 82 casos sintéticos catalogados.

Referências: [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md) · [GAI-INT-44](criterios-indicacao-aceite-responsaveis-institucionais.md) · [GAI-INT-42](modelo-institucional-emissao-custodia-revogacao-autorizacoes.md).
