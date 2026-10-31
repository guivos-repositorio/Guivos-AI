# GAI-INT-35 — Deliberação de Compatibilidade e Versionamento do Envelope v2
**Versão documental 6.2 · 31/10/2026**  
**Estado:** minuta executiva para deliberação da direção. Nenhuma opção foi ratificada por esta publicação.

## 1. Decisões que precisam ser tomadas
Com base no [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md), três questões devem ser decididas de forma explícita. O encaminhamento "de acordo, segue" autoriza preparar a minuta, mas não equivale a escolher uma opção de política.

### D35-A — Resultados parciais
- **A1 (recomendada para a primeira versão):** `result` somente quando `lifecycle_status=completed`; estados intermediários não incluem `result`. Informações de progresso podem ter canal separado, versionado e sem confundir hipótese com conclusão.
- **A2:** permitir `result` parcial em `processing` e `awaiting_review`, acompanhado de `result_completeness` e proveniência, mediante novo contrato explícito.
- **A3:** permitir `result` em `awaiting_review` apenas, com semântica distinta de publicação e validação da Pessoa.

**Critério:** simplicidade, representação de incertezas, compatibilidade com consumidores e não apresentação de progresso como resultado validado.

### D35-B — Falhas e cancelamentos
- **B1 (recomendada):** respostas com `failed` e `cancelled` não têm `result`; causas e códigos seguros seguem um contrato de erro ou mecanismo de status correlacionado por `request_id`, com identificação de falha/cancelamento sem dados sensíveis.
- **B2:** incluir um objeto `failure` no mesmo envelope, opcional somente para estado `failed`; exige revisão do envelope-base e do contrato de segurança.
- **B3:** manter status de falha sem causa estruturada no envelope; código disponível exclusivamente por API separada.

**Critério:** rastreabilidade de erro sem vazamento, compatibilidade de clientes e disponibilidade de evidências para suporte.

### D35-C — Versão de protocolo e migração
- **C1 (recomendada):** introduzir `candidate-2` apenas em envelope-base v2 independente; manter `candidate-1` imutável. O schema v2 já publicado, que referencia base v1, deverá ser revisado **antes** de ser tratado como contrato v2 completo.
- **C2:** manter o valor `candidate-1` para uma iteração de estrutura v2 isolada, sem habilitar consumidores; não declarar interoperabilidade.
- **C3:** adotar negociação explícita de versão por recurso/API depois de inventário dos consumidores e dependências.

**Critério:** evitar divergência entre `$id`, `api_contract_version` e URI de registry; prever dual-read/dual-write apenas se a realidade de serviços exigir e permitir.

## 2. Encaminhamento recomendado (não aprovado)
**Combinação candidata A1 + B1 + C1**, por reduzir risco de resultados parciais confundidos com conclusões e preservar os consumidores atuais.

Essa combinação é apenas recomendação. A direção deverá selecionar cada dimensão; nenhuma alternativa pode ser entendida como escolhida automaticamente.

## 3. Dependências de aprovação
- **Produto / Guivos Intelligence:** significado de progresso, revisão humana, validação e cancelamento.
- **Arquitetura / contratos:** versão, correlação, compatibilidade e registro de schemas.
- **Serviços de identidade, autorização e privacidade:** escopos válidos, separação de falha e dados sensíveis.
- **Revisão independente:** evidências e critérios de liberação.
- **Direção Guivos:** aprovação administrativa de cada decisão e de eventuais campanhas de teste.

Os representantes técnicos ainda não foram ratificados; a presença dessa lista não presume aceite ou assinatura.

## 4. Gates, permissões e condições
A deliberação de política **não autoriza por si só** alterar contratos atuais, executar `run_schema_cases.py`/`run_typed_cases.py`, instalar dependências, inspecionar Replit ou Neo4j, acessar dados, fazer chamadas a modelos ou aprovar G0–G6. Pedidos B e C continuam sem autorização. PND-01..16 permanecem abertas.

## 5. Registro e próxima etapa
As escolhas ficam como `null` em [registro estruturado candidato](deliberacao-compatibilidade-envelope-v2-candidata.json). Após a escolha explícita A/B/C pela direção, uma decisão delimitada poderá orientar nova revisão do schema em área candidata isolada, sem presumir implantação.

Referências: [GAI-INT-34](envelope-tipado-v2-politica-ciclo-vida-candidata.md) · [GAI-INT-33](compatibilidade-contrato-tipado-matriz-casos-v2.md) · [GAI-DEC-011](decisao-representante-direcao-autoridade-central-autorizacao.md).
