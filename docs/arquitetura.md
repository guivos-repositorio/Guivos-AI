# Arquitetura conceitual — Guivos AI
**Estado:** proposta para investigação, não implementação concluída.

## Fronteira de sistemas
Guivos Intelligence consumirá Guivos AI. **Intelligence** coordena fluxos e experiência do ecossistema; **Guivos AI** desenvolve e entrega a especialização analítica em trajetórias, lacunas e possibilidades. A relação é de consumo de capacidades por interface controlada, não de identidade entre os componentes. Ver [documento de separação arquitetural](guivos-ai-vs-intelligence.md).

As camadas a seguir descrevem elementos de integração e não atribuem toda a orquestração ao serviço Guivos AI.

## Camadas
1. **Identidade e permissões** — Pessoa cadastrada, vínculo profissional, escopos e revogação de acesso.
2. **Fontes** — Jornada Guivos, interações com oportunidades e informações profissionais autorizadas.
3. **Memória e relações** — dados temporais, proveniência e grafo de relações; Neo4j é candidato conforme a POC da Guivos Intelligence.
4. **Integração e consumo** — Guivos Intelligence orquestra seus fluxos e consome os serviços especializados da Guivos AI; adaptadores para múltiplos modelos poderão existir em ambos conforme responsabilidade técnica.
5. **Análise** — retrospectiva, contexto atual, futuros possíveis, requisitos, lacunas e oportunidades intermediárias.
6. **Relatório/API** — apresentação para profissionais, evidências, limitações e hipóteses.

## Modelo mínimo de evidência
Cada afirmação deve, quando possível, vincular fonte, data, escopo autorizado, grau de confirmação, interpretação e incertezas. Inferências não podem ser armazenadas como fatos comprovados.

## Eventos de oportunidades
Disponibilizada != recomendada != exibida != percebida != consultada != aproveitada. A plataforma deve registrar exclusivamente eventos que consiga observar e identificar limitações.

## Ciclo cognitivo
Compreender → Identificar lacunas → Perguntar → Aprofundar → Reavaliar → Validar → Direcionar. Direcionamentos e oportunidades não pressupõem aceite da Pessoa.

## Componentes candidatos
Modelos GPT, Claude e Gemini; memória de grafo Neo4j; GKR como referência institucional controlada. A escolha e o uso efetivo de cada componente exigem validação técnica.
