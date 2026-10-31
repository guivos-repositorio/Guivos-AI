# GAI-INT-24 — Verificação de Administração do Repositório e Limites de Autoridade Institucional
**Versão documental 4.8 · 31/10/2026**
**Estado:** constatação de metadados GitHub e encaminhamento de governança. Não constitui nomeação institucional, autorização de testes ou aprovação de gate.

## 1. Objetivo
Verificar a natureza da administração do repositório Guivos AI e separar **permissão técnica sobre código/documentos** de **mandato institucional para fontes canônicas, privacidade, segurança e homologação**. Este documento complementa o [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md), sem alterar as decisões pendentes.

## 2. Constatação na conexão GitHub em 31/10/2026
A consulta de metadados ao repositório `guivos-repositorio/Guivos-AI` indicou:
- Identificador do repositório: `1440878620`.
- Proprietário: `guivos-repositorio`, identificado pelo GitHub como conta de tipo `User`, **não** `Organization`.
- Visibilidade: `public`.
- Branch padrão: `main`.
- Permissões informadas para a conexão autenticada: `admin=true`, `maintain=true`, `pull=true`, `push=true`, `triage=true`.
- Listagem de associações organizacionais da conexão: vazia.

**Limite da evidência:** os metadados não identificam a Pessoa física responsável pela conta, o proprietário jurídico da Guivos, contratos operacionais, colaboradores externos, governança interna, titulares dos serviços canônicos ou quem pode assinar uma decisão institucional. Associação organizacional vazia no GitHub **não prova ausência de uma organização no mundo real**.

## 3. Que poderes foram e não foram comprovados
| Poder | Evidência | Conclusão |
| --- | --- | --- |
| Criar/editar documentação nesse repositório | Permissão de administração e commits confirmados | Controle técnico do repositório acessível |
| Alterar arquivos em `main` | Commits verificados em rodadas anteriores | Operação técnica realizada |
| Decidir arquitetura conceitual da Guivos AI | Direcionamentos previamente documentados | Competência institucional específica não inferida de GitHub |
| Declarar autoridade sobre identidade, ofertas ou consentimento | Nenhum contrato/mandato verificado | **Não comprovado** |
| Nomear jurídico, segurança, revisores e donos canônicos | Nenhuma delegação verificada | **Não comprovado** |
| Autorizar testes/uso de dados reais/integrações externas | Nenhuma decisão específica neste documento | **Não autorizado aqui** |
| Homologar gates G0–G6 | Nenhuma autoridade formal verificada | **Não comprovado; gates inalterados** |

A permissão `admin=true` não deve ser convertida em `gate_authority=true` em qualquer registro ou automação.

## 4. Encaminhamento de governança
**Etapa 1 — Responsável institucional:** obter da instância legítima da Guivos a identificação de quem ratifica governança de dados e nomeações. O controle administrativo no GitHub pode servir para **publicar a decisão**, não para substituir a assinatura/autorização de origem.

**Etapa 2 — Serviços existentes:** verificar o inventário real de identidade, autorizações, oportunidades, contexto, evidências e entrega, distinguindo sistemas em operação de componentes ainda planejados.

**Etapa 3 — Mandatos formais:** registrar nomeação, aceite, escopo, vigência, conflitos de interesse e referência ao ato legítimo para cada função pertinente. Não publicar informações pessoais desnecessárias em repositório público.

**Etapa 4 — Deliberação D21-01/02:** somente após as provas, encaminhar as duas decisões à autoridade competente; não considerá-las encerradas com base na existência deste dossiê.

**Etapa 5 — Campanha estrutural:** decidir separadamente se haverá execução offline das 49 fixtures. A autorização deve especificar ambiente, versionamento, responsáveis e critérios; não decorre de controle do repositório.

## 5. Situação registrada após a verificação
- PND-01 e PND-11: direcionamentos conceituais existentes; ratificação formal pendente.
- Outras 14 PNDs: pendentes.
- Cadastro de 16 funções do GAI-INT-23: todos os titulares permanecem sem nomeação comprovada.
- G0: parcial; G1–G6: pendentes.
- 19 schemas, 49 fixtures e dois scripts offline: preparados; sem execução registrada.
- Sem alteração em Replit, Neo4j, GPT/Claude/Gemini ou GKR.

## 6. Próxima ação verificável
A próxima ação com potencial de desbloqueio real é **obter a definição institucional de quem ratifica D21-01/D21-02**. Sem essa informação, uma nova série de estudos apenas ampliaria documentação, não a capacidade de homologação.

**Referências:** [GAI-INT-23](dossie-ratificacao-responsaveis-autoridade-alcadas.md) · [GAI-INT-22](encaminhamento-decisoes-autoridade-canonica-alcadas-g0-g2.md) · [GAI-INT-21](pacote-decisoes-g0-g2-autorizacao-validacao-estrutural.md) · [Registro de Decisões](registro-decisoes.md).

**Verificação limitada a metadados GitHub; nenhuma ratificação, execução ou aprovação operacional.**
