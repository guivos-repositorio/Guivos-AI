# GAI-INT-49 — Instrumento de Evidências e Parecer Independente da Alternativa A

**Versão documental 8.0 · 31/10/2026**  
**Estado:** instrumento e modelos em branco, não aplicado a fornecedores.

## 1. Escopo e limites
Materializa o método de avaliação documental da [GAI-INT-48](roteiro-avaliacao-alternativa-a-custodia-gerenciada.md), com pesos estabelecidos em [GAI-DEC-014](decisao-metodo-avaliacao-custodia-gai-dec-014.md). O instrumento **não substitui** a autorização COMP-04 para solicitar cotações, contatar fornecedores ou inspecionar sistemas. É vedado preencher notas, confirmar filtros ou emitir parecer de conformidade sem evidências obtidas em procedimento autorizado.

## 2. Unidade de evidência
Cada registro precisa identificar: código único, candidato/serviço (quando autorizado), requisito/critério correspondente, título descritivo, tipo da fonte, referência privada ou URL de fonte pública autorizada, emissor, data e versão da fonte, intervalo de validade, integridade quando pertinente, restrições de compartilhamento, responsável pela obtenção, método de verificação, achados e revisor independente.

A evidência deve ser conservada em ambiente apropriado, não anexada ao GitHub público quando contiver conteúdo confidencial ou identificável. Hash de documento pessoal não deve ser publicado como identificador reversível; metadados públicos devem ser minimizados.

## 3. Suficiência da evidência
| Dimensão | Condição para considerar suficiente |
| --- | --- |
| Autenticidade | Origem e autoria razoavelmente verificáveis; material não alterado sem controle |
| Rastreabilidade | Referência, versão e cadeia de obtenção preservadas |
| Atualidade | Fonte válida para a versão e período avaliados |
| Especificidade | Demonstra o controle no serviço, plano e configuração analisados |
| Completude | Cobre requisitos essenciais e suas exceções |
| Verificabilidade técnica | Permite conferência independente, não somente alegação comercial |
| Coerência | Não conflita com contrato, segurança, privacidade e demais fontes sem tratamento |
| Revisão independente | Parecer de pessoa distinta de quem coletou a evidência |

**Resultado por evidência:** `sufficient`, `partial`, `insufficient`, `contradictory` ou `not_evaluated`. O estado `sufficient` exige que as oito dimensões tenham sido avaliadas; lacuna desconhecida mantém o resultado em `not_evaluated` ou `partial`.

## 4. Classes de lacunas e tratamento
| Classe | Situação | Encaminhamento |
| --- | --- | --- |
| G-00 | Não avaliada / sem documento | Não calcular nota; registrar demanda de evidência |
| G-01 | Ausência ou incompletude não crítica | Solicitar complementação somente quando COMP-04 autorizar |
| G-02 | Evidência contraditória, desatualizada ou não verificável | Suspender julgamento do item e requerer esclarecimento independente |
| G-03 | Possível falha de requisito eliminatório | Bloquear recomendação até resolução comprovada |
| G-04 | Falha confirmada de requisito eliminatório | Desclassificar a alternativa/configuração para o escopo específico |
| G-05 | Risco residual conhecido, dentro de critério não eliminatório | Registrar mitigação, responsável e aceitação futura expressa |

**Desconhecido não equivale a aprovado nem a falha confirmada.** Nunca converter ausência de prova em nota zero para forçar resultado.

## 5. Regras de avaliação e decisão
1. Aplicar as sete categorias aprovadas, com pesos respectivos de 25, 20, 15, 15, 10, 10 e 5%.
2. Descrever documentos e conflitos por critério; evidência promocional isolada não comprova adequação técnica.
3. Revisar os oito filtros eliminatórios da GAI-INT-48 separadamente. `unverified` ou `unclear` impede seleção, enquanto `failed` comprovado desclassifica.
4. Exigir duas pessoas distintas para coleta e parecer, com conflitos de interesse declarados.
5. Somente atribuir nota de 0 a 5 após suficiência evidencial e revisão independente; calcular média ponderada apenas com os sete itens completos, sem penalidade automática por desconhecido.
6. Parecer `qualified` ou `not_qualified` só pode ser emitido após análise dos filtros; o status inicial deve ser `not_issued`.
7. Nenhum parecer seleciona fornecedor, aprova tratamento de dados reais, cria credenciais ou autoriza implantação.

## 6. Modelo de parecer independente
O parecer deve incluir: identidade institucional verificada do revisor; declaração de independência; objeto e versão do serviço; escopo e exclusões; inventário de evidências; avaliação de suficiência; lacunas G-00 a G-05; filtros eliminatórios; resumo financeiro TCO para 12/36 meses com fonte e data; riscos residuais e tratamento; divergências; conclusão justificada; condicionantes; data e aceite verificável.

Estados candidatos: `not_issued`, `insufficient_evidence`, `conditionally_qualified`, `qualified`, `not_qualified`. **Não confundir parecer técnico com deliberação da direção.**

## 7. Entregas e arquivos
- [Registro de evidências em branco](instrumento-evidencias-alternativa-a-custodia.json).
- [Modelo de parecer independente em branco](modelo-parecer-independente-custodia-a.json).
- [Roteiro GAI-INT-48](roteiro-avaliacao-alternativa-a-custodia-gerenciada.md).

## 8. Barreiras atuais
COMP-04 pendente. Sem responsáveis designados e aceitos para avaliação de fornecedores; sem cotação, contato, inspeção ou coleta de dados; sem fornecedor selecionado, notas ou parecer. O trabalho é exclusivamente documental. Pedidos B/C não autorizados, 82 casos sintéticos sem execução verificada, G0 parcial, G1–G6 pendentes e 16 PNDs abertas.
