# GAI-INT-50 — Proposta de Autorização COMP-04 por Escopos Segregados

**Versão documental 8.1 · 31/10/2026**  
**Estado:** proposta para decisão futura; nenhuma das permissões foi concedida.

## 1. Objetivo e alcance do acordo
A deliberação [GAI-DEC-014](decisao-metodo-avaliacao-custodia-gai-dec-014.md) aprovou critérios COMP-01/02/03, mantendo **COMP-04 pendente**. Esta entrega estrutura os atos de autorização necessários para preencher o [instrumento GAI-INT-49](instrumento-avaliacao-evidencias-parecer-alternativa-a.md). O acordo para elaborar esta proposta **não aprova os escopos** abaixo, não expande o Pedido C e não habilita execução.

## 2. Três permissões mutuamente independentes
| Escopo | Ato que poderá ser autorizado | Requisitos mínimos de concessão | Estado |
| --- | --- | --- | --- |
| COMP-04-P — Consulta pública | Acesso documental a informações **publicadas abertamente** por fornecedores, incluindo especificações, políticas e preços públicos | Lista de fontes/URLs ou categorias permitidas, responsável, período, critérios de registro e limites | **Pendente** |
| COMP-04-C — Contato comercial | Contato dirigido a fornecedores e solicitação de informações ou cotações | Empresas e destinatários, mensagem aprovada, limites de informação, custos e responsabilidades, prazo | **Pendente** |
| COMP-04-I — Inspeção privada | Visualização controlada de sistemas internos e evidências privadas | Autoridade específica sobre o ambiente, escopo, identidade do operador, privilégios, supervisão, logs e condições de parada | **Pendente** |

**Proibição de inferência:** autorizar P não autoriza C ou I; autorizar C não autoriza I; nenhuma permissão autoriza implantação, despesa, aquisição, extração de dados reais, autenticação ou testes do Pedido B. Pedido C permanece uma autorização separada, não satisfeita por COMP-04-I.

## 3. COMP-04-P — Consulta a informações públicas
Permissões possíveis, após ato expresso: visitar URLs públicas e consultar documentação comercial/técnica disponível sem autenticação; registrar nome e versão do serviço, evidências e respectivas datas; comparar preços públicos com premissas declaradas.

Exclusões: acesso a painéis protegidos, testes de endpoints ou configurações, login com credenciais, coleta massiva, scraping que viole restrições, coleta de dados pessoais, captura de segredos, divulgação pública de documentos privados e afirmação de conformidade sem prova.

**Condição para concessão:** registrar fontes permitidas, responsável, janela de execução e método de auditoria. Mesmo fontes públicas podem exigir revisão de termos e tratamento de dados antes de usar automação.

## 4. COMP-04-C — Contato comercial
Permissões possíveis, após ato expresso: encaminhar perguntas do roteiro GAI-INT-48, obter cotação vinculada a volumes e escopo e coletar documentação autorizada para avaliação.

Exclusões: assinatura de contrato, aquisição, implantação, inclusão de dados reais, criação de contas, pagamento, consentimento a termos em nome da Guivos ou promessa comercial sem autorização distinta.

**Condição para concessão:** fornecedores, nomes institucionais dos contatos, mensagem aprovada, canais, prazo, limite de custos, política de confidencialidade, tratamento de dados e retenção das respostas. Nunca publicar contatos pessoais ou propostas confidenciais no repositório público.

## 5. COMP-04-I — Inspeção de sistemas privados
Permissões possíveis, após autorização separada: leitura restrita de configurações e evidências não públicas de **sistemas expressamente nomeados** por titular legitimado, com prazo, papel e revisão independente.

Exclusões: alteração de configurações, testes ativos, exportação de dados, transferência de credenciais, inspeção de Neo4j/Replit/GPT/Claude/Gemini por inferência, instalação, ativação de serviços e qualquer ato pertencente ao Pedido B. A autorização do Pedido C também permanece necessária quando o objeto coincidisse com seu escopo.

**Condição para concessão:** identificar sistema, ambiente, proprietário, acesso mínimo, método de logging, medidas de proteção, parecer técnico, prova de autoridade e mecanismo de revogação. Ausência de qualquer item → negar.

## 6. Campos obrigatórios para futura autorização
Ato futuro deve indicar `authorization_id`, `scope_code` (P, C ou I), `issuer_ref`, `authority_proof_ref`, `specific_assets_or_sources`, `operator_ref`, `reviewer_ref`, `permitted_actions`, `prohibited_actions`, `not_before`, `expires_at`, `cost_limit`, `data_protection_constraints`, `evidence_location`, `revocation_method` e `decision_ref`. **Sem comprovação independente da identidade institucional, nenhum arquivo JSON basta para a autorização operacional.**

## 7. Encaminhamento proposto
Apresentar **primeiro a COMP-04-P à direção para deliberação separada**, com escopo estritamente documental, sem contatos e sem inspeção. COMP-04-C e COMP-04-I deverão aguardar necessidades concretas, nomeações/aceites pertinentes e novas decisões independentes. Isso é uma recomendação de sequência, **não uma concessão**.

## 8. Registro verificável
Os três formulários permanecem em `pending_explicit_authorization`, sem destinatários, ativos, titulares ou decisão de emissão. [Registro estruturado de permissões em branco](proposta-autorizacao-comp04-escopos-segregados.json).

**Estado preservado:** nenhuma consulta externa executada nesta etapa, fornecedor contatado ou sistema privado inspecionado; nenhum preço verificado, contratação ou dado real; Pedido B/C não autorizados; 82 casos sintéticos não executados; G0 parcial, G1–G6 pendentes; PND-01 a PND-16 abertas.

Referências: [GAI-DEC-014](decisao-metodo-avaliacao-custodia-gai-dec-014.md) · [GAI-INT-49](instrumento-avaliacao-evidencias-parecer-alternativa-a.md) · [GAI-INT-48](roteiro-avaliacao-alternativa-a-custodia-gerenciada.md).
