# GAI-INT-42 — Modelo Institucional de Emissão, Custódia e Revogação de Autorizações

**Versão documental 7.1 · 31/10/2026**  
**Estado:** proposta de governança para deliberação; não nomeia titulares nem constitui autorização de execução.

## 1. Âmbito e autoridade
A [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md) reconhece a declaração do representante inicial da direção como autoridade administrativa central para autorizações. Esse registro **não fornece prova externa de identidade** ou vínculo criptográfico. A presente proposta não transfere a autoridade decisória para um operador, revisor ou sistema automatizado.

Separar quatro atos: **(a)** comprovar identidade institucional; **(b)** aprovar uma concessão administrativa específica; **(c)** assinar/publicar a concessão; **(d)** verificar tecnicamente a concessão antes de execução. Nenhum desses atos supre os demais.

## 2. Papéis propostos e aceite pendente

| Código | Papel | Responsabilidade | Separação mínima | Situação |
| --- | --- | --- | --- | --- |
| ROLE-DIR | Direção autorizadora | Decidir escopo, duração, limites e revogação administrativa | Não ser o único verificador técnico da própria concessão | Autoridade declarada por GAI-DEC-011; identidade ainda não verificada externamente |
| ROLE-REG | Registrador institucional | Verificar identidade e vínculo de papel/chave, manter cadastro público mínimo de chaves e histórico | Não conceder autorizações | Titular e aceite pendentes |
| ROLE-CUS | Custodiante de chave | Proteger assinatura, realizar procedimentos de rotação e recuperação com dupla custódia | Não decidir sozinho o escopo aprovado | Titular e aceite pendentes |
| ROLE-REV | Revisor de segurança independente | Revisar controle de acesso, ameaças, isolamento e aprovação técnica do desenho | Não operar a campanha avaliada | Titular e aceite pendentes |
| ROLE-OPS | Operador do ambiente | Executar campanha somente com concessão verificável e ambiente isolado | Não emitir/assinar a própria concessão nem revisar a própria execução | Titular e aceite pendentes |
| ROLE-AUD | Auditor de evidências | Confirmar logs, revogação, cadeia de custódia e conclusão documental | Não ser o operador do mesmo ciclo | Titular e aceite pendentes |

**Não atribuir papéis a pessoas por inferência**, nem publicar CPF, e-mail privado, credenciais ou nome civil no repositório.

## 3. Fluxo institucional proposto
1. **Credenciamento:** registrador documenta método de verificação externa da identidade institucional da direção e de qualquer delegado, com evidências protegidas fora do GitHub público.
2. **Vinculação de chaves:** registrar chave pública/identificador, papel, validade, finalidade, autoridade de aprovação e evidência de posse. Chave privada nunca é publicada.
3. **Pedido específico:** operador solicita campanha delimitada; inventário de schemas, dados sintéticos, executor e ambiente é congelado com hashes.
4. **Revisão independente:** ROLE-REV avalia escopo, versão, ausência de rede/segredos, dependências, critérios de parada e risco residual; parecer não substitui decisão da direção.
5. **Aprovação da direção:** ROLE-DIR concede ou rejeita o Pedido B com referência inequívoca; eventual autorização é individual, limitada e revogável.
6. **Emissão assinada:** custodiante autorizado assina representação canônica da concessão aprovada; a relação entre aprovação e assinatura deve ser auditável.
7. **Distribuição e verificação:** verificador independente utiliza âncora previamente instalada, relógio confiável, revogação atual, controle de replay e integridade de todos os artefatos.
8. **Encerramento:** evidências são preservadas, concessão é consumida/expirada e auditor faz adjudicação separada. Nenhum resultado aprova gate automaticamente.

## 4. Custódia e ciclo de vida de chaves
- Recomenda-se chave distinta por finalidade (autorizações de campanha, snapshots de revogação e registros institucionais). Evitar chave única para todas as funções.
- Custódia com mínimo privilégio, proteção de hardware quando apropriada, inventário de chaves e registro de acessos; credenciais privadas não devem ser copiadas para scripts ou para o GitHub.
- Geração, importação, ativação, suspensão, rotação, recuperação e destruição exigem procedimento assinado, dupla verificação e trilha de auditoria.
- Políticas de assinatura, algoritmo, duração das chaves, expiração dos certificados e provedores **ainda precisam de aprovação técnica especializada**; não pressupor fornecedor.
- Comprometimento ou perda de custódia: suspender emissão, revogar chaves/concessões afetadas e avaliar evidências anteriores.

## 5. Revogação e modo offline
A direção poderá revogar concessão específica, papel ou chave. Como a campanha sintética é offline, a revogação deverá chegar ao verificador mediante snapshot assinado e previamente provisionado, com versão monotônica e janela curta de validade. Snapshot ausente, vencido, de emissor desconhecido ou inferior à versão conhecida: **negar execução**.

O snapshot offline não representa revogação instantânea. A tolerância máxima de defasagem, a proteção contra rollback e a frequência de atualização dependem de decisão de risco antes de qualquer implementação. Autorizações sensíveis podem exigir checagem prévia online em etapa segregada, ou não serem executadas offline.

## 6. Matriz de segregação de deveres
| Ação | Decisor | Executor material | Verificador obrigatório |
| --- | --- | --- | --- |
| Nomear registrador e custodiante | Direção | Administração institucional | Aceite explícito + avaliação independente |
| Vincular identidade/chave | Registrador segundo política aprovada | Registrador | Revisor independente |
| Aprovar Pedido B | Direção | Nenhum ato de execução é presumido | Registro formal e trilha institucional |
| Assinar concessão | Direção define autorização | Custodiante conforme alçada | Verificador criptográfico independente |
| Preparar ambiente | Responsável técnico nomeado | Operador | Revisor de segurança independente |
| Executar campanha | Somente após concessão específica | Operador | Verificador automatizado e controles externos |
| Revogar concessão | Direção | Administrador/custodiante autorizado | Registro íntegro, atualização de snapshot |
| Analisar evidências | Revisor/auditor independente | Auditor | Direção delibera sobre encaminhamento, não sobre resultado presumido |

## 7. Termo mínimo de aceite de função
Para cada papel: código da função, referência de identidade verificada (não dados privados), nomeação explícita, escopo, responsabilidades, incompatibilidades, método de custódia quando aplicável, data/hora, assinatura/aceite verificável, revisão, substituto e condições de desligamento. Sem aceite, papel permanece **vago**.

## 8. Decisões pendentes
- **INST-01:** quem exercerá ROLE-REG e quem verificará sua independência?
- **INST-02:** qual modelo de custódia e substituição para ROLE-CUS?
- **INST-03:** qual evidência externa liga ROLE-DIR à identidade institucional?
- **INST-04:** qual perfil criptográfico e âncora de confiança serão adotados?
- **INST-05:** como funcionará revogação assinada e proteção anti-rollback offline?
- **INST-06:** quais pessoas/entidades aceitarão ROLE-REV, ROLE-OPS e ROLE-AUD?
- **INST-07:** quais limites e custos de implementação poderão ser submetidos à direção?

## 9. Limites explícitos
Não há nomeações reais, aceites, chaves, certificados, assinatura, revogação operacional, verificador habilitado, autorização de execução ou inspeção. O runner endurecido permanece bloqueado. **Pedido B e Pedido C continuam não autorizados.** G0 parcial; G1–G6 pendentes; PND-01 a PND-16 abertas.

Referências: [GAI-INT-41](cadeia-confianca-autorizacoes-execucao-candidata.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md) · [GAI-INT-40](endurecimento-executor-v2-candidato-bloqueado.md).
