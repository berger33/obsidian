---
id: software.testes.atdd.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/4-5-collaboration-based-test-approaches/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Acceptance test-driven development", "ATDD deriva testes de critérios de aceitação"]
lote: software-testes-2000-0001
---

# ATDD deriva testes de critérios de aceitação

## Em uma frase
Acceptance test-driven development (ATDD) define casos de teste antes da implementação de uma história, colaborativamente entre diferentes perspectivas.

## Por que importa
Critérios escritos apenas depois do código podem refletir o que foi construído em vez de esclarecer o que stakeholders precisam. A conversa prévia reduz interpretações incompatíveis e cria uma base concreta para validação.

## Como funciona
O CTFL descreve ATDD como test-first: membros com perspectivas distintas — por exemplo, clientes, desenvolvedores e testers — criam casos antes de implementar a história. Esses casos podem ser executados manual ou automaticamente. Critérios de aceitação podem ser tratados como condições de teste que precisam ser exercitadas, mas a equipe ainda deve decidir quais dados e resultados demonstram cada condição.

## Exemplo
Para uma história sobre cancelamento de reserva, representantes acordam quando há reembolso, quais estados permitem cancelamento e que confirmação o usuário recebe. Os casos são definidos antes de codificar e usados para orientar a implementação e a avaliação posterior.

## Limites e trade-offs
ATDD não exige transformar toda conversa em uma suíte gigante. Critérios vagos, impossíveis de observar ou contraditórios precisam ser esclarecidos antes de automatizar.

## Como verificar
Confira se critérios foram acordados antes da implementação, cobrem exemplos relevantes e têm resultado observável; preserve decisões e exceções.

## Conexões
- [[acceptance-testing-validation]] — situa aceitação no nível de validação.
- [[test-oracles-resultados-esperados]] — critérios ajudam a decidir resultados esperados.

## Fontes
- [ASTQB — CTFL §4.5, Collaboration-based Test Approaches](https://astqb.org/4-5-collaboration-based-test-approaches/) — ATDD, critérios e colaboração; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.5.3; acesso em 2026-10-01.
