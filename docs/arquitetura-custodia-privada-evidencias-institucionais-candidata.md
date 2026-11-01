# GAI-INT-46 — Arquitetura Candidata de Custódia Privada de Evidências Institucionais

**Versão documental 7.6 · 31/10/2026**  
**Estado:** especificação técnica e de governança para deliberação; nenhum ambiente provisionado e nenhum dado coletado.

## 1. Objetivo e fronteira
Proteger evidências de identidade, vínculo institucional, verificação independente e aceite individual do procedimento [GAI-INT-45](procedimento-credenciamento-institucional-candidato.md). O repositório público Guivos AI guarda **somente documentos de política, modelos vazios e referências abstratas**. Documentos pessoais, imagens, biometria, CPF, contatos, evidências identificáveis, tokens, credenciais e chaves privadas não devem ser publicados no GitHub nem incorporados à documentação.

A [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md) aprovou critérios de governança, não a coleta de informações ou implantação de infraestrutura. Este documento não autoriza operar um cofre, contratar serviços ou gerar identidades.

## 2. Alternativas arquiteturais para avaliação
| Alternativa | Características | Limitação | Situação |
| --- | --- | --- | --- |
| A — Repositório privado gerenciado de evidências | Armazenamento criptografado, autorização por papel, trilha de auditoria e retenção configurável | Verificar capacidades reais do fornecedor, localidade, contratos, exportação e exclusão de backups | **Referência candidata** |
| B — Cofre de documentos sob infraestrutura própria | Maior controle sobre infraestrutura, chaves, acesso e auditoria | Exige equipe, operação, resiliência e segurança contínua | Não descartada |
| C — Sistema institucional existente validado | Reduz duplicidade se houver controles comprovados | Não presumir conformidade, isolamento ou direitos de acesso | Sujeita a inventário autorizado |

**Recomendação para desenho:** priorizar A como hipótese comparativa, sem escolher fornecedor, plano, região ou serviço. A seleção depende de avaliação de risco, privacidade, custo e aceite técnico.

## 3. Separação física e lógica
**Camada pública:** políticas, modelos vazios, identificadores de especificação e status genérico sem referência reversível a pessoas.  
**Camada privada de identidade:** documentos e evidências necessárias, minimizadas por finalidade, cifradas e vinculadas a um identificador interno opaco.  
**Camada privada de decisões:** evidências de indicação, verificações, aceites, revogações e mandatos com versão e trilha auditável.  
**Camada de chaves:** gestão separada, com rotação, controle de uso, acesso restrito e sem chaves privadas no código.  
**Camada de auditoria:** eventos imutáveis ou resistentes a adulteração, protegidos contra edição por operadores da custódia.  
**Camada de metadados públicos:** apenas status documental não identificador; não reproduzir links privados ou hashes previsíveis de documentos pessoais.

## 4. Identidade, autorização e acesso
- Aplicar menor privilégio, negação por padrão, autenticação forte (MFA resistente a phishing, quando viável) e acesso just-in-time com aprovação para atividades sensíveis.
- Separar ROLE-REG (validação de vínculo), ROLE-CUS (custódia), ROLE-REV (revisão), ROLE-AUD (auditoria), ROLE-OPS (ambiente), ROLE-DIR (deliberação administrativa).
- ROLE-DIR aprova a política e atos específicos; isto **não equivale** a acesso irrestrito ao conteúdo de todos os dossiês.
- Compartilhamento de documento por link público, permissões anônimas, exportação irrestrita e credenciais compartilhadas devem ser proibidos.
- Toda consulta deve ter finalidade, fundamento, responsável e prazo; acessos excepcionais exigem registro e revisão.
- Alteração ou revogação de papel devem interromper permissões, sessões e concessões ativas conforme mecanismo validado.

## 5. Minimização, retenção e exclusão
**Antes da coleta:** registrar finalidade, necessidade de cada categoria de evidência, base legal aplicável, aviso de privacidade, titular responsável, prazo ou critério de retenção e obrigações legais. Requer avaliação de privacidade e LGPD por responsável qualificado.

**Durante uso:** preferir atestados e referências internas a cópias integrais; proibir dados excessivos; permitir retificação, contestação e registro da origem.

**Retenção:** sem prazo arbitrário aprovado. Propor matriz por classe (identificação, aceites, pareceres, logs, revogações), com evento inicial, período proposto, base legal, responsável e aprovação formal. Até essa decisão, **não iniciar coleta**.

**Exclusão:** ao término da finalidade e ausente obrigação válida de conservação, revogar acesso, apagar objetos principais e réplicas controladas, registrar resultado, gerenciar backups por ciclo documentado e controlar retenção de logs minimizados. Não prometer eliminação instantânea de backups imutáveis sem confirmar tecnicamente. Exceções por retenção legal ou litígio exigem fundamento, prazo e revisão.

## 6. Auditoria e resposta a incidentes
Os registros de auditoria devem conter identificador de evento, ator pseudônimo, ação, finalidade, referência interna não pública, data/hora confiável, decisão de acesso, resultado, correlação de sessão e integridade da trilha. Não registrar conteúdo integral da evidência ou credenciais no log. Alertar e revisar acessos anômalos, exportações, mudança de permissões, revogações e falhas de integridade. Definir responsáveis, comunicação e resposta a incidente antes de operar.

## 7. Segurança e ciclo de vida
- Criptografia em trânsito e repouso com mecanismos reconhecidos; segredos e chaves em serviço de custódia separado.
- Políticas de backup, recuperação, retenção de snapshots e testes de restauração condicionadas a autorização própria.
- Segregar produção, desenvolvimento e qualquer ambiente de teste; não usar dossiês reais nos 82 casos sintéticos.
- Avaliar residência/transmissão internacional e suboperadores antes da contratação.
- Registrar riscos de fornecedor, disponibilidade, portabilidade, término contratual e comprovação de exclusão.

## 8. Gates documentais antes de qualquer implementação
**EVD-01:** arquitetura de armazenamento e classificação de dados revisadas.  
**EVD-02:** política de identidade e acesso aprovada; titulares aceitos e segregados.  
**EVD-03:** avaliação jurídica e de privacidade (incluindo LGPD) e matriz de retenção concluídas.  
**EVD-04:** modelo de criptografia/custódia de chave e recuperação revisado.  
**EVD-05:** política de auditoria, incidentes e direitos dos titulares aprovada.  
**EVD-06:** análise de fornecedor/custo/região e saída contratual registrada.  
**EVD-07:** autorização institucional específica para eventual provisionamento, distinta de Pedidos B e C.

Nenhum item EVD constitui gate G0–G6 automaticamente.

## 9. Proposta de deliberação futura
A direção deverá escolher **somente o caminho de avaliação** (A, B ou C), definir responsável por avaliação de privacidade e selecionar critérios de retenção, acesso e auditoria antes de discutir implementação. A publicação desta matriz **não equivale à aprovação de alternativa**.

**Estado preservado:** modelos de indicação, verificação e aceite em branco; titulares ROLE-REG/CUS/REV/OPS/AUD não nomeados; nenhum ambiente privado criado, nenhuma evidência pessoal coletada, chaves não emitidas; Pedido B/C não autorizados; 82 casos sintéticos catalogados, nenhum executado; G0 parcial, G1–G6 pendentes, 16 PNDs abertas.

Referências: [GAI-INT-45](procedimento-credenciamento-institucional-candidato.md) · [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md) · [GAI-INT-41](cadeia-confianca-autorizacoes-execucao-candidata.md).
