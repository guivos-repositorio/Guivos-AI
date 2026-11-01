# GAI-INT-64 — Mapa de Cobertura INV62 × C63 e Lacunas de Deliberação

**Data:** 01/11/2026 · **Natureza:** reconciliação estática de rastreabilidade, sem execução de casos, homologação ou avaliação de gate.  
**Fontes conferidas:** [GAI-INT-62](gai-int-62-matriz-invariantes-regras-condicionais.md) (30 invariantes) e [GAI-INT-63](gai-int-63-matriz-casos-conceituais-condicoes-aceite-inv62.md) (24 casos conceituais).

## 1. Semântica de cobertura
- **Direta:** o caso nomeia ou concretamente representa a obrigação/proibição daquela regra.
- **Indireta:** o caso toca parte da obrigação, mas não a demonstra isoladamente e precisa de cenário adicional.
- **Sem cenário:** não existe caso C63 explicitamente associado à regra.
- **Cobertura é documental**, não validação, resultado observado, teste positivo ou aptidão operacional.

## 2. Matriz integral das 30 regras
| Regra INV62 | Casos C63 associados | Cobertura |
| --- | --- | --- |
| INV62-T01 | C63-T-P01 | direta |
| INV62-T02 | C63-T-P01, C63-T-N01 | direta |
| INV62-T03 | C63-T-P01 | direta |
| INV62-T04 | C63-T-N02, C63-T-C01 | direta |
| INV62-T05 | C63-T-N03 | direta |
| INV62-T06 | C63-T-N04 | direta |
| INV62-T07 | C63-T-C01 | indireta |
| INV62-T08 | C63-T-N04 | direta |
| INV62-T09 | C63-T-N05 | direta |
| INV62-T10 | — | sem cenário |
| INV62-D01 | C63-D-P01 | direta |
| INV62-D02 | C63-D-P01, C63-D-N01 | direta |
| INV62-D03 | C63-D-N02 | indireta |
| INV62-D04 | C63-D-C01 | direta |
| INV62-D05 | C63-D-C02 | direta |
| INV62-D06 | C63-D-N02 | direta |
| INV62-I01 | C63-I-P01 | direta |
| INV62-I02 | C63-I-P01 | direta |
| INV62-I03 | C63-I-N01 | direta |
| INV62-I04 | C63-I-C01 | direta |
| INV62-I05 | C63-I-N03 | direta |
| INV62-I06 | C63-I-N02 | direta |
| INV62-I07 | C63-I-C01 | direta |
| INV62-E01 | C63-E-P01 | direta |
| INV62-E02 | C63-E-P01, C63-E-N01 | direta |
| INV62-E03 | C63-E-N02 | direta |
| INV62-E04 | C63-E-C01 | direta |
| INV62-E05 | C63-E-N03 | direta |
| INV62-E06 | C63-E-N04 | direta |
| INV62-E07 | C63-E-C01, C63-E-C02 | direta |

**Total:** 30 invariantes; 27 com cobertura direta, 2 com cobertura apenas indireta, 1 sem cenário. **29 de 30 regras** têm alguma relação documental com C63, mas apenas **27** cobertura direta. As 24 situações C63 continuam **não executadas**; nenhum acréscimo aos 82 casos previamente catalogados.

## 3. Lacunas prioritárias
| Lacuna | Impacto | Complemento documental candidato |
| --- | --- | --- |
| INV62-T10 — alias não cria evento | Sem caso C63 | Propor caso negativo: conversão de `acceptance_ref` para `acceptance_ref_private` sem aceite individual real; expectativa: impedir inferência de aceite |
| INV62-T07 — vigência, escopo, revogação e autoridade | C63-T-C01 cobre sobretudo identidade externa, não temporalidade e revogação | Propor cenário condicionado de permissão com escopo e prazo, mas revogação não verificada |
| INV62-D03 — alcance da revogação histórica | C63-D-N02 aborda reescrita, mas não revogação integral sem fundamento | Propor cenário negativo de decisão posterior parcial tratada como revogação integral |
| INV62-D04 — multiplicidade e cardinalidade | C63-D-C01 existe, mas `precedence_links` ainda é proposto | Definir semântica/capacidade de múltiplas decisões por histórico |
| INV62-I07 — conflito por pares | C63-I-C01 evidencia lacuna, mas política de incompatibilidade não ratificada | Elaborar matriz candidata de papéis e autoridade competente, sem designações |
| INV62-E07 — política de retenção e algoritmos | Casos condicionados existentes; não há parâmetros aprovados | Preparar instrumento para deliberação de algoritmo, prazo e custódia sem fixar valores arbitrários |

**Importante:** as três primeiras lacunas de cobertura não significam ausência de políticas prévias; significam ausência de caso conceitual dedicado ou completo.

## 4. Cobertura por domínio
| Domínio | Direta | Indireta | Sem cenário | Total |
| --- | ---: | ---: | ---: | ---: |
| Transversal T | 8 | 1 | 1 | 10 |
| Documental D | 5 | 1 | 0 | 6 |
| Institucional I | 7 | 0 | 0 | 7 |
| Evidências E | 7 | 0 | 0 | 7 |
| **Total** | **27** | **2** | **1** | **30** |

A contagem representa **regras com ao menos uma associação**, não número de testes, evidências aceitas ou requisitos institucionalmente homologados.

## 5. Condições para eventual aceite documental
1. Manter vínculos bidirecionais entre identificadores INV62 e C63, sem reutilizar códigos para significados diferentes.
2. Revisar a pertinência de cada associação, registrando se cobre a obrigação integral ou apenas parte dela.
3. Não declarar cobertura de execução a partir de expectativas conceituais.
4. As decisões de desenho ainda não ratificadas (`P`) mantêm sua condição, mesmo que tenham cenário associado.
5. Preservar os documentos GAI-INT-62 e 63, publicar complementos como adendos rastreáveis quando aprovados documentalmente.
6. Qualquer encerramento de BLK-D01/I01/E05 exige evidência e ato competente separado; nenhum caso conceitual encerra bloqueadores.

## 6. Próxima etapa proposta
**GAI-INT-65 — Adendo de Cenários de Cobertura Residual**, concentrado em INV62-T10, T07 e D03, sem executar testes e sem alterar as 24 entradas originais de GAI-INT-63. Propostas de política para D04/I07/E07 deverão continuar condicionadas a futuras decisões expressas.

## 7. Limites e estado preservado
**15 bloqueadores** (7 P0, 7 P1, 1 P2) sem fechamento comprovado; **82 casos sintéticos anteriores sem execução verificada**; **24 cenários C63 conceituais não executados**. Pedido A concluído conforme registro; B/C não autorizados; COMP-04-P aprovado em princípio e inativo; G0 parcial; G1–G6 pendentes; PND-01..16 abertas. Nenhuma nomeação, credencial, implantação, schema, runner ou gate foi autorizado por esta matriz.
