# GAI-REV-002 — Revisão Estática do Executor Offline v2

**Versão documental 6.8 · 31/10/2026**  
**Objeto:** `tests/contracts/run_candidate_v2_cases.py`, blob SHA `a1835dfbf511ff43f7f5abd637f10c18e131c2d4`.  
**Método:** leitura do código público, sem executar Python, instalar pacotes ou validar fixtures. **Não é laudo de teste.**

## Resultado executivo
O executor implementa a estrutura de leitura de dois catálogos, registro local de schemas e comparação de expectativas, mas **não está pronto para execução autorizada**. Foram identificados controles declarativos insuficientes, problemas de integridade de artefatos e riscos de tratamento de erros. Os achados abaixo são inferências de inspeção estática, sujeitos à revisão de responsável técnico.

## Achados prioritários
| ID | Prioridade | Local | Achado / efeito | Correção candidata |
| --- | --- | --- | --- | --- |
| REV2-01 | Crítica | `check_authorization` | O JSON de autorização é controlado pelo chamador: `approved=true` e `offline_isolation_confirmed=true` são apenas afirmações, sem autenticação, assinatura, validade ou consulta a autoridade confiável. | Autorização externa verificável; tratar arquivo apenas como configuração auxiliar; bloquear execução sem evidência independente |
| REV2-02 | Alta | `--repo-sha` | Verifica correspondência entre dois valores fornecidos pelo próprio chamador, mas **não calcula o SHA do checkout real**. Pode operar com arquivos diferentes dos declarados. | Verificação local do commit e árvore/artefatos congelados antes de carregar schemas |
| REV2-03 | Alta | `dependency_lock_digest` | Campo exigido, porém não há comparação com dependências instaladas, lockfile ou wheels. | Pinning e hashes verificáveis em ambiente controlado |
| REV2-04 | Alta | `offline_isolation_confirmed` | Flag booleana não estabelece bloqueio de rede, filesystem ou Secrets; a ausência de chamadas HTTP explícitas não prova isolamento. | Sandbox externa sem rede, Secrets e dados reais, com evidências independentes |
| REV2-05 | Alta | `build_registry` | Confere schema e `$id`, mas não compara digests/allowlist com manifesto aprovado antes da leitura dos casos. | Manifesto de entradas com SHA-256 e versão imutável, validado antes da execução |
| REV2-06 | Média | `build_registry.walk` | Extrai fragmento de `$ref` e valida apenas documento destino; não valida se JSON Pointer ou âncora interna é existente. | Resolver referências com suporte explícito a fragmentos, `$anchor`/`$dynamicRef` conforme escopo |
| REV2-07 | Média | `normalize_cases` | Presença de `instance` não verifica se é sintético, nem revisão de conteúdo; `case_id` aceita string vazia. | Política de origem e revisão humana de fixtures, ID não vazio e esquema de catálogo |
| REV2-08 | Média | `main` | Captura exceções limitadas; erros de resolução da biblioteca ou de formato de recurso podem gerar stack trace não classificado. | Categorias de erro previsíveis, saída sanitizada e parada segura |
| REV2-09 | Média | `evidence` | Não grava `evidence_digest`, `campaign_id`, duração ou confirmação de revisor; `matched=33` pode gerar interpretação excessiva. | Evidência assinável, trilha de revisão e status de gate sempre separado |
| REV2-10 | Média | escrita de evidência | Verifica `exists()` e depois abre `x`, mas não há garantia contra troca de caminhos/symlinks por agente local; `parent.mkdir` é efeito no filesystem. | Diretório de evidências pré-aprovado, caminho fixado, permissões e atomicidade |
| REV2-11 | Média | política de schema | Reconhece `$ref` e diretórios esperados, mas não usa allowlist de nomes/hashes exatos de todos os schemas. Adições posteriores à árvore poderiam alterar o conjunto. | Registry congelado por manifesto de arquivos, não `glob` aberto |

## Pontos positivos observados apenas no código
- Não há chamada explícita a Replit, Neo4j, modelos de IA ou APIs externas.
- O executor consulta dois catálogos e exige 15 + 18 casos, com IDs únicos.
- Usa `Registry` local e nomes lógicos explícitos para os três schemas da compatibilidade.
- A opção de saída em arquivo exclusivo recusa sobrescrita já existente e mantém `gate_decision_ref=null`.
- O runner atual da versão v1 permanece separado.

## Adjudicação e encaminhamento
**Situação:** onze achados abertos; não atribuir aprovação técnica nem maturidade de campanha. Propor correções em arquivo/branch candidato separado, revisão independente e novo congelamento de commit antes de qualquer campanha.

**Sem autorização:** Pedido B (execução de testes), Pedido C (inspeção operacional), instalação de dependências, acesso a dados, implantação ou liberação de gates. G0 parcial; G1–G6 pendentes; PND-01–16 abertas.

Referências: [GAI-INT-39](implementacao-executor-offline-v2-nao-executado.md) · [GAI-INT-38](especificacao-executor-offline-33-casos-v2.md) · [GAI-DEC-012](decisao-politica-envelope-v2-a1-b1-c1.md).
