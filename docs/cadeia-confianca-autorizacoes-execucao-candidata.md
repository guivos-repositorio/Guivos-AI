# GAI-INT-41 — Cadeia de Confiança de Autorizações para Execução

**Versão documental 7.0 · 31/10/2026**  
**Estado:** proposta de arquitetura, não implementação nem autorização de execução.

## 1. Princípio institucional
A [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md) preserva a direção Guivos como autoridade administrativa central para qualquer autorização. **A identidade do declarante na conversa ainda não possui verificação externa registrada.** Uma assinatura criptográfica, isoladamente, comprova posse da chave privada, não a legitimidade institucional do titular: o vínculo entre identidade, papel e chave precisa de validação independente.

**Proposta:** uma autorização específica e verificável para o Pedido B poderá ser emitida somente por uma identidade de direção previamente vinculada, de maneira independente, a uma chave autorizadora. O executor nunca deve aceitar autodeclaração, simples `approved=true`, arquivo produzido pelo operador ou assinatura de chave não cadastrada.

## 2. Papéis e separação de competências
| Papel | Atribuição proposta | Limite |
| --- | --- | --- |
| Direção Guivos | Aprova escopo e concessão/revogação administrativa do Pedido B | Não substitui revisão técnica, segurança ou gate |
| Registrador institucional de confiança | Verifica identidade e registra vínculo entre direção, papel e chave pública | Não concede autorização de teste |
| Custodiante da chave privada | Assina somente concessões formalmente aprovadas, preferencialmente em hardware protegido | Não publica segredo nem controla unilateralmente revisão |
| Operador da campanha | Executa apenas após verificação de autorização, ambiente e escopo | Não emite, assina ou modifica autorização |
| Revisor técnico independente | Confere escopo, isolamento, artefatos e evidências | Não pode ser o próprio operador |
| Verificador confiável externo | Verifica assinatura, cadeia de confiança, validade, revogação e vínculo com artefatos | Não deve aceitar decisão de liberação apenas do arquivo recebido |

Nenhum titular técnico, registrador ou custodiante foi formalmente nomeado ou aceitou atribuições por este documento.

## 3. Artefato de concessão proposto
Para uma futura campanha sintética offline, o objeto assinado deverá conter ao menos:

- `authorization_id` único; `issuer_identity_ref`, `issuer_role_ref`, `key_id`, `trust_anchor_version`;
- `scope=offline_synthetic_B` e lista exata de catálogos/casos permitidos;
- `repository_commit_sha`, manifestos de schemas e fixtures com SHA-256, registry congelado, runner hash e `dependency_lock_digest`;
- `environment_ref`, `operator_ref`, `independent_reviewer_ref` e política de isolamento;
- `issued_at`, `not_before`, `expires_at`, `nonce`, `authorization_sequence`;
- `max_runs`, `campaign_id`, limites de evidências e políticas de interrupção;
- envelope de assinatura digital sobre representação canônica e versão do formato.

**Regra:** assinatura e payload devem ser protegidos contra troca de conteúdo e uso cruzado entre ambientes. Escolha e perfil de assinatura, serialização canônica, algoritmo e gestão de chaves dependem de revisão especializada. Não armazenar chave privada, segredo, token ou identificador pessoal sensível no repositório público.

## 4. Verificação antes de qualquer operação
1. Verificar identidade da chave emissora a partir de **âncora de confiança pré-provisionada e independente do pacote de execução**. Recusar chave que venha apenas dentro da concessão.
2. Conferir integridade da assinatura, perfil criptográfico aceito, papel do emissor e escopo da delegação.
3. Validar horário com relógio confiável, vigência e limite máximo de execução; negar se horário confiável indisponível.
4. Consultar registro de revogação autenticado e atualizado. Em modo offline, usar snapshot assinado, pré-carregado, com validade curta, `sequence` monotônica e política de expiração. Ausente, vencido ou inconsistente: **falhar fechado**.
5. Bloquear replay: `authorization_id`/`nonce`/`campaign_id` consumidos em armazenamento confiável, persistente e protegido contra rollback; `max_runs` controlado por autoridade do ambiente, não por contador alterável no JSON.
6. Confrontar o checkout e todos os digests reais do runner, schemas, fixtures e dependências com os valores autorizados.
7. Exigir operador e revisor distintos, sandbox isolada externamente (sem rede, Secrets, dados reais ou serviços), logs íntegros e política de interrupção.
8. Só depois do sucesso integral dos controles permitir que um **executor aprovado futuramente** seja invocado.

**O executor atualmente publicado não implementa essa cadeia e sua variante endurecida permanece deliberadamente bloqueada.**

## 5. Revogação, rotação e incidentes
- A direção deverá ter mecanismo verificável para suspender ou revogar concessões e chaves.
- Revogação de autorização ou comprometimento da chave invalida novas campanhas; campanhas em andamento devem ser interrompidas segundo política externa.
- Rotações requerem dupla custódia/revisão, registro de época de chave e período controlado de transição.
- Offline não permite presumir revogação em tempo real: um snapshot válido apenas delimita risco residual. Para autorizações de maior risco, exigir verificação online prévia em fase separada, fora da execução isolada, ou não permitir execução offline.
- Auditoria precisa registrar concessão, consumo, revogação, tentativas negadas e evidências sem publicar dados secretos.

## 6. Cenários de negação obrigatória
Autorização autodeclarada, assinatura inválida, chave desconhecida, chave revogada, emissor sem papel válido, vigência expirada, ausência de relógio confiável, revogação indisponível, repetição de nonce, SHA divergente, operador igual ao revisor, ambiente não isolado, dependências divergentes, acesso indevido a rede/Secrets ou limite de execução ultrapassado devem resultar em **negação sem teste**.

## 7. Fronteiras e condições de aceitação
A definição institucional, o vínculo de chave, o verificador independente e o ambiente offline devem ser aprovados e revisados separadamente. Esta especificação **não é uma autorização do Pedido B ou C** nem autoriza implementar serviços de autenticação, adquirir HSM, emitir chaves, criar credenciais, executar scripts ou alterar gates.

**Pendências:** titularidade do registrador/custodiante, prova externa de identidade, âncora inicial, política de revogação offline, perfil de assinatura, ambiente confiável, revisão de ameaças, orçamento e autorização específica para implementação.

**Estado mantido:** 82 casos catalogados, zero execuções verificadas, Pedido B e C não autorizados, G0 parcial, G1–G6 pendentes e PND-01 a PND-16 abertas.

Referências: [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md) · [GAI-REV-002](revisao-estatica-executor-offline-v2-rev002.md) · [GAI-INT-40](endurecimento-executor-v2-candidato-bloqueado.md).
