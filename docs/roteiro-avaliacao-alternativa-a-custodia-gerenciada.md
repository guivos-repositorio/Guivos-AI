# GAI-INT-48 — Roteiro de Avaliação Documental da Alternativa A

**Versão documental 7.9 · 31/10/2026**  
**Estado:** roteiro de avaliação, sem contato com fornecedores, preços verificados ou inspeção.

## 1. Objeto e autoridade
Preparar perguntas e evidências necessárias à avaliação de um **repositório privado gerenciado** para documentos de identidade, vínculo institucional e aceite individual. A [GAI-DEC-014](decisao-metodo-avaliacao-custodia-gai-dec-014.md) aprovou os critérios/pesos COMP-01, os filtros COMP-02 e a ordem A→B→C COMP-03. **COMP-04 permanece pendente.** Não se permite solicitar cotações, contatar fornecedores, inventariar sistemas ou coletar dados pessoais por consequência deste roteiro.

## 2. Questionário técnico e evidências esperadas
### Segurança e identidade — peso 25%
1. Há MFA resistente a phishing para funções administrativas?
2. É possível segregação RBAC/ABAC e revisão periódica de permissões?
3. Como são gerenciadas chaves, criptografia e acessos emergenciais?
4. Que evidências auditáveis existem sobre incidentes e recuperação?

**Evidências futuras:** arquitetura de segurança; descrição verificável de controles de identidade; política de chaves e incidentes.

### Privacidade e conformidade — peso 20%
1. Quais papéis contratuais e bases legais são necessários?
2. Onde dados, backups e suboperadores estão localizados?
3. Como responder a direitos dos titulares e limitar finalidade?
4. O fornecedor aceita cláusulas de proteção de dados e portabilidade?

**Evidências futuras:** DPA/minuta contratual; mapa de dados e suboperadores; documento de transferências internacionais; processo de direitos dos titulares.

### Auditoria e evidências — peso 15%
1. Há logs de acesso, exportação, alteração e exclusão?
2. Logs são protegidos de adulteração por administradores comuns?
3. É possível entregar evidências a auditor independente?

**Evidências futuras:** dicionário de eventos; política de integridade e retenção de logs; descrição de exportação de auditoria.

### Retenção e exclusão — peso 15%
1. Retenção é configurável por classe e base legal?
2. Como funciona exclusão de objetos, réplicas e backups?
3. São possíveis suspensão legal e comprovação do descarte?

**Evidências futuras:** matriz de retenção configurável; política de backup e exclusão; procedimento de confirmação de descarte.

### Custo total — peso 10%
1. Quais cobranças fixas, por usuário, armazenamento, operações e tráfego?
2. Quais custos de implantação, suporte, auditoria e integração?
3. Quais custos de saída e variação por volume?

**Evidências futuras:** estrutura de preços por unidade; premissas de volume; condições comerciais e de cancelamento.

### Operação e resiliência — peso 10%
1. Quais SLA, RPO/RTO e responsabilidades de configuração?
2. Como operam patching, monitoramento e resposta a incidentes?
3. Quais limites de API e capacidade?

**Evidências futuras:** SLA e divisão de responsabilidade; documentação de continuidade; política de suporte.

### Reversibilidade — peso 5%
1. É possível exportar todos os documentos, metadados e trilhas pertinentes?
2. Quais formatos são usados e quais restrições existem?
3. Como confirmar fim de processamento e descarte após migração?

**Evidências futuras:** especificação de exportação; condições de saída; plano de migração e descarte.

## 3. Filtros eliminatórios
Avaliação de finalidade/base legal e LGPD; identidade e segregação; criptografia/custódia; auditoria íntegra; retenção, exclusão e backups; resposta a incidentes; portabilidade e plano de saída; autorização de implantação específica. Falha comprovada em filtro obrigatório impede seleção independentemente da pontuação. **Status atual de todos: não avaliado.**

## 4. Método de pontuação
Os sete pesos aprovados somam 100%. Cada critério só recebe nota de 0 a 5 após evidência verificável e revisão independente. Fórmula futura: `nota_ponderada = Σ(peso_percentual × nota_criterio / 5)`, resultando em 0–100, sem substituir gates. Itens sem evidência permanecem **desconhecidos**, nunca zero inventado ou nota presumida; nesse caso não calcular resultado final.

## 5. Modelo de custo total — TCO
Planejar comparações para **12 e 36 meses**, com premissas idênticas entre fornecedores e cenários base, crescimento e saída. Nenhum número foi preenchido ou estimado.

| Componente | Driver | Fórmula conceitual |
| --- | --- | --- |
| fixed license | BRL/month | `monthly_fixed_fee * months` |
| users | BRL/user/month | `licensed_users * unit_price_per_user_month * months` |
| storage | BRL/GB/month | `average_stored_gb * price_per_gb_month * months` |
| operations | BRL/1000_ops | `monthly_ops / 1000 * price_per_1000_ops * months` |
| egress | BRL/GB | `monthly_egress_gb * price_per_gb * months` |
| implementation | BRL/once | `one_time_setup_cost` |
| security privacy review | BRL/once | `one_time_review_cost` |
| support | BRL/month | `monthly_support_cost * months` |
| internal operations | BRL/hour | `hours_per_month * internal_hourly_cost * months` |
| backup recovery | BRL/month | `monthly_backup_recovery_cost * months` |
| exit migration | BRL/once | `one_time_exit_migration_cost` |

Regras: apresentar impostos, implantação, suporte, revisão de privacidade/segurança, custo interno, armazenagem, requisições, transferência, backup/restauração e migração final. Se houver moeda estrangeira, registrar data e origem da taxa de câmbio e riscos de variação; não inventar conversões. Evitar dupla contagem e explicitar itens incluídos em licenças.

## 6. Critérios de comparação e qualidade da evidência
A futura ficha de fornecedor deverá indicar fonte, data, validade, versão do produto, abrangência, lacunas e revisor independente. Comparar opções com os mesmos volumes e requisitos de LGPD. Materiais promocionais isolados não provam segurança, exclusão ou portabilidade; verificar termos contratuais e documentos técnicos na etapa autorizada.

## 7. Entregáveis posteriores, sujeitos a COMP-04
- Inventário autorizado de candidatos da alternativa A, sem presumir aderência.
- Coleta formal de informações públicas e cotações, com escopo e responsável aprovados.
- Matriz de evidências, lacunas e riscos para cada fornecedor.
- TCO em 12/36 meses com cotações e premissas verificáveis.
- Parecer independente e decisão de eventual aprofundamento de B/C.

## 8. Estado preservado
**Nenhum fornecedor escolhido ou contatado, nenhuma cotação solicitada, nenhum preço verificado, nenhuma inspeção ou armazenamento criado.** Nenhum documento pessoal coletado. Pedido B/C não autorizados; 82 casos sintéticos catalogados e sem execução verificada; G0 parcial, G1–G6 pendentes e PND-01 a PND-16 abertas.

[Modelo estruturado em JSON](roteiro-avaliacao-alternativa-a-custodia-gerenciada.json) · [GAI-INT-47](matriz-comparativa-custodia-institucional-a-b-c.md) · [GAI-INT-46](arquitetura-custodia-privada-evidencias-institucionais-candidata.md).
