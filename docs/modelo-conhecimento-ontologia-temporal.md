# Modelo de Conhecimento e Ontologia Temporal — Guivos AI
**Documento de arquitetura v0.9 · 31/10/2026**
**Estado:** especificação conceitual proposta para análise e validação; não é esquema Neo4j implementado nem autorização para mudanças operacionais no Replit.

## 1. Objetivo e fronteira
Representar, de modo rastreável, como Pessoas vivenciam Momentos, declaram Objetivos, encontram Oportunidades, exploram Possibilidades e enfrentam Condições ou Lacunas. O modelo deve sustentar análises retrospectivas, contextuais e prospectivas, sem confundir fatos observáveis com interpretações.

**Autoridades:** serviços do ecossistema preservam os registros canônicos e permissões; Guivos AI mantém métodos e análises derivadas; Guivos Intelligence orquestra a experiência e consome resultados. Neo4j é candidato à representação de relações, não autorização para acesso direto e indiscriminado dos motores de linguagem.

## 2. Vocabulário conceitual — entidades
| Entidade | Função | Cuidados de representação |
| --- | --- | --- |
| Pessoa | Sujeito da Jornada | Identificador pseudonimizado nas interfaces internas; identidade sob serviço apropriado |
| Momento | Recorte temporal de contexto, circunstâncias e prioridades | Não é rótulo fixo de personalidade |
| Declaração | Relato textual/voz estruturado ou corrigido pela Pessoa | Preservar fonte e versão; não assumir veracidade universal |
| Objetivo | Intenção expressamente validada | Pode mudar, ser suspensa ou abandonada |
| Possibilidade | Futuro explorável ou experiência concebível | Origem declarada, adjacente, emergente ou exploratória |
| Oportunidade | Oferta ou iniciativa concreta, temporalmente verificável | Requisitos, validade, provedor e evidência da oferta |
| Requisito | Condição específica de um caminho ou oportunidade | Obrigatório, facilitador ou preferência; fonte verificável |
| CondiçãoContextual | Situação ou recurso conhecido relativo à Pessoa | Atendida, não atendida, desconhecida, em verificação, não aplicável |
| EventoDeInteração | Acontecimento observável relacionado à oportunidade | Diferenciar recomendar, exibir, abrir, salvar, inscrever, participar |
| Experiência | Acontecimento vivido ou relatado com evidência apropriada | Distinguir autodeclaração de participação confirmada |
| Evidência | Referência de suporte a uma afirmação | Fonte, data, versão, permissão, validade e contestação |
| Fonte | Origem da informação | Pessoa, profissional, serviço de oportunidades, parceiro ou inferência |
| Lacuna | Distância contextual entre condição atual demonstrada e requisito pertinente | Não imputar déficit quando dado está ausente |
| Hipótese | Interpretação plausível ainda não confirmada | Nunca sobrescrever fato ou ser tratada como diagnóstico |
| Análise | Resultado versionado da Guivos AI | Possui escopo, método, data, referências e incertezas |
| Caminho | Sequência alternativa de condições, ações e oportunidades | Não é prescrição ou garantia de evolução |
| Autorização | Permissão e finalidade específica para processamento/acesso | Revogação, expiração, revisão e auditoria |
| VínculoProfissional | Relação autorizada entre Pessoa e profissional | Não concede, sozinho, acesso a todos os dados |
| Revisão | Correção, confirmação, contestação ou atualização | Histórico e efeitos de invalidação registrados |

## 3. Relações sugeridas (vocabulário inicial)
- Pessoa **VIVENCIA** Momento; Pessoa **DECLARA** Declaração; Declaração **EXPRESSA** Objetivo.
- Pessoa **VALIDA** Possibilidade; Possibilidade **EXIGE** Requisito; Requisito **REFERENCIA** Evidência.
- Pessoa **POSSUI_CONDICAO** CondiçãoContextual; CondiçãoContextual **ATENDE_OU_NAO** Requisito com estado e referência temporal.
- Oportunidade **PODE_APOIAR** Possibilidade/Caminho quando houver fundamentação; Oportunidade **ESTABELECE** Requisito.
- Pessoa **TEM_EVENTO** EventoDeInteração; EventoDeInteração **REFERE_SE_A** Oportunidade.
- Pessoa **RELATA** Experiência; Experiência **E_REFERENCIADA_POR** Evidência.
- Análise **UTILIZA** Evidência; Análise **PROPOE** Hipótese/Lacuna/Possibilidade/Caminho.
- Análise **DERIVA_DE_VERSAO** Momento/Declaração/registro canônico autorizado.
- Autorização **DELIMITA** finalidade, escopo, sujeito, destinatário e período; VínculoProfissional **EXIGE** autorização pertinente.
- Revisão **ATUALIZA_OU_CONTESTA** registro e **INVALIDA** análise derivada quando necessário.

Relações são conceituais, não Cypher ou contratos prontos. Não presumir correspondência 1:1 com nós e arestas Neo4j. Distinguir relações declaradas, observadas e inferidas no armazenamento.

## 4. Temporalidade e versionamento
Cada fato e relação sensível ao tempo deve guardar, quando necessário:
- **occurred_at:** momento em que o evento aconteceu;
- **recorded_at:** momento em que o sistema recebeu o registro;
- **valid_from / valid_to:** intervalo em que a condição se aplica, quando conhecido;
- **source_version:** versão do registro de origem;
- **analysis_as_of:** instante de referência do processamento;
- **supersedes / superseded_by:** encadeamento das revisões.

A ausência de data confiável deve ser visível, e não completada pela IA. Corrigir uma declaração não deve apagar automaticamente a trilha das análises históricas permitidas, mas deve impedir que uma versão obsoleta se apresente como vigente. Retenção/exclusão obedecem às finalidades e requisitos aplicáveis.

## 5. Proveniência e epistemologia
Uma afirmação deve ser tipada:
1. **Observação de sistema:** evento comprovável de uma interface ou serviço, limitado ao que o evento realmente mede.
2. **Relato da Pessoa:** declaração do próprio sujeito.
3. **Registro profissional:** anotação identificada, com acesso e finalidade restritos.
4. **Informação externa:** requisito ou oferta com fonte e data verificáveis.
5. **Inferência de IA:** hipótese ou relação derivada que requer rastreabilidade e pode ser contestada.

**Regra:** exibição de oportunidade não comprova percepção; consulta não comprova compreensão; ausência de inscrição não comprova recusa; ausência de registro não comprova ausência de experiência.

## 6. Estados de compatibilidade e lacunas
Para cada par (CondiçãoContextual, Requisito), utilizar estados **atendido**, **não atendido com evidência**, **desconhecido**, **em verificação**, **não aplicável**. Lacuna confirmada exige requisito pertinente e evidência sobre condição não atendida; ausência de dado gera pergunta, não lacuna confirmada. Incluir barreiras externas e oportunidades habilitadoras, não somente formação e habilidades.

## 7. Exemplo sintético de trajetória
- Pessoa P declara objetivo de trabalhar em determinada área.
- Possibilidade B: participar de formação relacionada, ainda não escolhida.
- Oportunidade O: curso com inscrição e requisitos publicados.
- Requisito R: presença às quartas.
- Condição C: Pessoa informou disponibilidade às terças; quartas não foram avaliadas.
- Evento E: curso foi exibido na interface. Isso **não** significa que P o percebeu.
- Análise A: há **informação desconhecida** sobre disponibilidade às quartas, não incompatibilidade comprovada.
- Pergunta: “Você teria disponibilidade às quartas?”
- Revisão: após resposta, atualizar a condição, invalidar a inferência antiga e reavaliar as alternativas.

Nenhuma informação real de usuários deve integrar os exemplos no repositório público.

## 8. Como Guivos Intelligence consome Guivos AI
Intelligence encaminha solicitação especializada com finalidade, escopo autorizado, referência temporal e versão do contexto; Guivos AI consulta os serviços autorizados, executa análise e retorna: possibilidades, requisitos, lacunas qualificadas, hipóteses, evidências, limites e questões de aprofundamento. Intelligence verifica a atualidade e apresenta o resultado sem transformá-lo em decisão automática.

GPT, Claude e Gemini são mecanismos que podem apoiar tarefas nos dois componentes; não são fontes canônicas de fatos. Neo4j não deve ser acessado diretamente pelo navegador ou por provedores externos.

## 9. Uso por API comercial
O contrato de relatório pode expor identificadores de análise, evidências autorizadas, categorias de lacuna e alternativas, sem liberar o grafo inteiro ou o histórico bruto. Separar dados de acompanhamento profissional de dados compartilhados na Jornada. A Pessoa cadastrada pode revisar permissões; conta ativa não é consentimento automático.

## 10. Regras de integridade (candidatas)
- Toda análise tem identificador, versão, data de referência e fontes suficientes para auditoria.
- Uma inferência não pode substituir um fato declarado.
- Mudanças do contexto podem invalidar recomendações e relatórios anteriores.
- Requisitos externos expiram ou precisam de reconfirmação.
- Acesso ao grafo e evidências respeita sujeito, finalidade, vínculo, prazo e autorização.
- Não criar classificação global do valor humano, de potencial de vida ou diagnóstico psicológico automatizado.
- Uma Pessoa pode rejeitar possibilidade sem ser marcada como resistente ou incapaz.

## 11. Avaliações antes de decisão de implementação
Testes sintéticos: duplicidade de eventos, registros contraditórios, ausência de fonte, relógios divergentes, mudança de objetivo, expiração de oferta, correção/revogação de autorização, relação indevida entre Pessoas e vazamento entre profissionais. Critérios: consistência temporal, integridade referencial, rastreabilidade, recuperação autorizada, inexistência de falsas lacunas e invalidação de análises obsoletas.

## 12. Decisões pendentes
- Fronteira exata entre dados transacionais, grafo projetado e armazenamento de documentos.
- Nomenclatura/IDs globais e modelo de identidade.
- Estratégia de versionamento de nós, arestas e evidências.
- Cardinalidades e política de duplicação/deleção.
- Políticas de leitura entre Intelligence, AI e parceiros.
- Qual entidade representa a autoria e validação de hipóteses profissionais.
- Estratégia de validação de fontes externas e qualidade das oportunidades.

## 13. Estado e conexões documentais
**Esta versão é conceitual**, ainda não um schema de banco homologado. Não altera o Replit nem abre gates de cognição ou memória. Ver [Documento Mestre](index.md), [Autoridade de Dados e Memória](autoridade-dados-memoria-contexto.md), [Integração Replit](integracao-replit-intelligence-ai-neo4j.md) e [Compatibilidade Futura](compatibilidade-futura.md). GKR permanece independente.
