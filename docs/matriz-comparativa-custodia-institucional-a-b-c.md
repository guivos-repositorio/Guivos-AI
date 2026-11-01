# GAI-INT-47 — Matriz Comparativa de Custódia Institucional

**Versão documental 7.7 · 31/10/2026**  
**Estado:** comparação arquitetural proposta; sem seleção de alternativa, fornecedor, preços ou implantação.

## 1. Contexto e escopo
Esta matriz desenvolve a [GAI-INT-46](arquitetura-custodia-privada-evidencias-institucionais-candidata.md) e compara três abordagens de custódia **antes de existirem cotações, inspeções autorizadas ou provas técnicas**. Os atributos apresentados são **hipóteses e riscos típicos do modelo**, não resultados verificados de algum produto. Nenhuma pontuação é atribuída sem evidência.

## 2. Alternativas

| Aspecto | A — Privado gerenciado | B — Infraestrutura própria | C — Sistema existente |
| --- | --- | --- | --- |
| Segurança | Controles gerenciados podem reduzir esforço; exigir comprovação de configuração e responsabilidades compartilhadas | Maior controle técnico, com maior ônus de proteção e atualização | Controles e permissões atuais **desconhecidos** até avaliação |
| Privacidade | Exige DPA, avaliação de suboperadores, localidade e transferências | Guivos assume mais obrigações operacionais e contratuais com terceiros de infraestrutura | Reavaliar compatibilidade de finalidades e segregação |
| Auditoria | Verificar integridade, retenção e exportação dos logs | Projetar e operar trilha resistente a adulteração | Demonstrar granularidade, independência e preservação dos registros |
| Retenção/exclusão | Verificar exclusão, réplicas, snapshots e backups conforme contrato | Configuração mais controlável, mas requer operação comprovada | Verificar se políticas existentes atendem às novas classes |
| Custos | Licenças, volume, transferência, suporte, migração e saída | Infraestrutura, equipe, segurança, backup, manutenção e contingência | Custo incremental e adequações desconhecidos |
| Manutenção | Parte da operação pode ser fornecida; integrações e configuração permanecem responsabilidade Guivos | Elevada responsabilidade interna de correção, disponibilidade e recuperação | Pode reaproveitar operação existente; capacidade e riscos desconhecidos |
| Reversibilidade | Risco de formatos proprietários; exigir exportação e descarte após saída | Possível maior controle de formatos, mas migração ainda tem custo | Dependências e migração dependem do sistema atual |

## 3. Critérios ponderados — pesos propostos, não aprovados

| Critério | Peso candidato | Evidência de avaliação |
| --- | ---: | --- |
| Segurança e identidade | 25% | RBAC/ABAC e MFA; segregação de deveres; criptografia e custódia de chaves; gestão de incidentes |
| Privacidade e conformidade | 20% | base legal e minimização; acesso a direitos dos titulares; localização e transferências; suboperadores e DPA |
| Auditoria e evidências | 15% | trilha resistente a adulteração; logs mínimos e íntegros; exportação para auditor independente |
| Retenção e exclusão | 15% | regras por classe de dado; exclusão e confirmação; retenção de backup e litígio |
| Custo total de propriedade | 10% | implantação e licenças; armazenamento e transferência; equipe e suporte; saída e migração |
| Operação, manutenção e resiliência | 10% | responsável operacional; patching e monitoramento; backup e restauração; SLA/SLO |
| Portabilidade e reversibilidade | 5% | exportação completa; formatos interoperáveis; gestão de dependência do fornecedor; descarte após migração |
| **Total** | **100%** | |

Método proposto para fase futura: avaliar cada critério de 0 a 5 **somente com prova documentada**, calcular pontuação ponderada e publicar incertezas, limitações, custo total e análise de sensibilidade. Hoje, todas as pontuações são **não avaliadas**. Critério crítico sem evidência impede recomendação final, mesmo com pontuação agregada alta.

## 4. Evidência exigida por alternativa

### A — Repositório privado gerenciado
- evidência técnica de MFA/RBAC, criptografia e auditoria
- contrato, DPA, região e transferências
- cotações e custos de saída
- prova de restauração e exclusão

### B — Cofre sob infraestrutura própria
- modelo de ameaças e arquitetura
- plano de operação 24/7 e resposta a incidentes
- custos de equipe, infraestrutura e manutenção
- auditoria e ensaios autorizados em etapa futura

### C — Sistema institucional existente
- inventário e contratos mediante autorização
- avaliação independente de segregação e finalidade
- relatório de lacunas, retenção e exclusão
- custo incremental e plano de segregação

## 5. Filtros eliminatórios
Qualquer solução escolhida deverá comprovar: finalidade e base legal apropriadas; minimização e proteção dos direitos dos titulares; segregação de funções, MFA e menor privilégio; criptografia e custódia; auditoria independente; retenção e exclusão, inclusive ciclo dos backups; gestão de incidentes; exportação e plano de saída; e **autorização específica para eventual implantação**. Uma alternativa sem atendimento desses filtros não poderá vencer por preço.

## 6. Cenários e custo de propriedade
Solicitar, apenas quando houver autorização adequada, estimativas comparáveis para volume inicial/escala, arquivos por dossiê, armazenamento em 12/36 meses, acessos administrativos, exportação e recuperação, indisponibilidade, operação e encerramento. Usar **mesmas premissas em A, B e C**; registrar custos tributários e de câmbio se pertinentes. Nenhuma cifra de mercado ou preço foi afirmado nesta etapa.

## 7. Encaminhamento à direção
A GAI-INT-46 sugeriu priorizar **A para avaliação**, não contratação. Esta matriz mantém essa hipótese como primeira trilha de levantamento, sujeita à confirmação dos controles e à avaliação paralela de B e C. A direção poderá posteriormente aprovar **somente o método, pesos e ordem da avaliação**, em decisão separada; tal aprovação não escolherá fornecedor ou solução.

### Deliberações pendentes
- COMP-01: aprovar ou ajustar os sete critérios e pesos.
- COMP-02: aprovar ou ajustar filtros eliminatórios e metodologia de evidência.
- COMP-03: definir ordem de investigação das alternativas A, B e C.
- COMP-04: aprovar, de modo específico, eventual coleta de cotações/inventário, sem inspecionar sistemas por inferência.

## 8. Governança
Nenhum fornecedor foi selecionado, preço validado, cotação solicitada, sistema inspecionado ou ambiente privado criado; nenhum documento pessoal coletado. Pedidos B e C continuam não autorizados; 82 casos sintéticos catalogados e nenhuma execução verificada; G0 parcial, G1–G6 pendentes e 16 PNDs abertas.

[Registro comparativo em JSON](matriz-comparativa-custodia-institucional-a-b-c.json) · [GAI-INT-46](arquitetura-custodia-privada-evidencias-institucionais-candidata.md) · [GAI-DEC-013](decisao-aprovacao-criterios-institucionais-gai-dec-013.md).
