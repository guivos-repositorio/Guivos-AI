# GAI-DEC-012 — Política de Desenho A1 + B1 + C1

**Aprovada pela direção em 31/10/2026.** Escopo exclusivamente documental e de versionamento candidato.

- **A1:** o campo `result` é reservado a respostas concluídas (`completed`); respostas intermediárias não carregam resultado final.
- **B1:** respostas com falha ou cancelamento não carregam `result`; os erros utilizam um mecanismo separado e correlacionado, a especificar.
- **C1:** contrato-base `candidate-2` independente, preservando `candidate-1`.

**Limites:** não foram autorizados testes (Pedido B), inspeção operacional (Pedido C), execução de código, implantação, migração de consumidores, acesso a dados ou gates G0–G6. A aprovação da política não equivale à validação técnica dos schemas candidatos.

O registro estruturado das três escolhas está em [GAI-INT-35](deliberacao-compatibilidade-envelope-v2-candidata.json). G0 continua parcial, G1–G6 pendentes e as PNDs seguem abertas.
