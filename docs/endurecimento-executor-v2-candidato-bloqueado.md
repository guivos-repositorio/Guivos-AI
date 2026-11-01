# GAI-INT-40 — Endurecimento Candidato do Executor Offline v2
**Versão documental 6.9 · 31/10/2026**  
**Estado:** arquivo alternativo publicado para revisão estática; **intencionalmente bloqueado para execução**.

## Entrega
Novo arquivo [`run_candidate_v2_cases_hardened_proposed.py`](../tests/contracts/run_candidate_v2_cases_hardened_proposed.py) criado em paralelo ao runner anterior `run_candidate_v2_cases.py`, preservado sem alterações.

O código inclui um bloqueio explícito logo no início de `check_authorization`: levanta `CampaignError` antes de aceitar qualquer autorização fornecida pelo usuário. **O código permanece não operacional até que um verificador de autorização independente e confiável seja implementado e revisado.** A presença de código abaixo desse bloqueio não demonstra que os fluxos seguintes funcionem.

## Resposta aos achados GAI-REV-002

| Achado | Progresso realizado | Estado |
| --- | --- | --- |
| REV2-01 Autorização autodeclarada | Bloqueio incondicional de autorização sem verificador confiável | Mitigação de não execução; **controle definitivo pendente** |
| REV2-02 SHA não verificado | Função candidata consulta `git rev-parse HEAD` e verifica checkout sem alterações | Código preparado, **não executado** |
| REV2-03 Dependências | Mantida exigência declarativa de digest, sem verificação real | **Aberto** |
| REV2-04 Isolamento offline | Limitação explicitada; isolamento exige sandbox fora do script | **Aberto** |
| REV2-05 Integridade de schema | SHA-256 é registrado no catálogo local, mas não comparado com manifesto confiável congelado | **Aberto** |
| REV2-06 Fragmentos de referência | Resolução continua limitada a documentos e não valida todos os fragmentos ou âncoras | **Aberto** |
| REV2-07 Catálogos | `case_id` vazio passa a ser rejeitado na normalização | Melhoria candidata; revisão pendente |
| REV2-08 Exceções | Inclusão de `TypeError` e `subprocess.SubprocessError`; mensagem de erro genérica evita exposição direta do detalhe | Mitigação parcial; auditoria estruturada pendente |
| REV2-09 Evidências | Campo `campaign_id` proposto e `evidence_digest=null`; assinatura e digest real não implementados | **Aberto** |
| REV2-10 Saída e symlink | Sem proteção final contra substituição de diretório de saída | **Aberto** |
| REV2-11 Registry congelado | Permanece baseado em varredura de diretórios, sem allowlist de hashes aprovada | **Aberto** |

## Critérios antes de outra versão
1. Especificar cadeia de confiança da autorização B: origem verificável da direção, integridade/assinatura, validade temporal, escopo, revogação e verificador independente do arquivo de campanha. Nunca substituir bloqueio por simples flag autodeclarada.
2. Estabelecer sandbox externa sem rede, sem segredos e sem dados reais, com evidência audível de configuração; o script sozinho não garante isolamento.
3. Implementar verificação efetiva de lockfile e hashes de dependências e schemas previamente aprovados, com registry congelado.
4. Tratar referências, identificadores, erros de infraestrutura, concorrência da saída e digests de evidência.
5. Submeter todo o código a revisão independente e autorização de teste específica antes de qualquer execução.

**Conclusão:** existe uma segunda versão em código com endurecimentos parciais e um bloqueio seguro. Não houve execução, validação, instalação, acesso operacional, inspeção B/C ou aprovação de gates. G0 parcial; G1–G6 pendentes; PND-01 a PND-16 abertas.

Referências: [GAI-REV-002](revisao-estatica-executor-offline-v2-rev002.md) · [GAI-INT-39](implementacao-executor-offline-v2-nao-executado.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md).
