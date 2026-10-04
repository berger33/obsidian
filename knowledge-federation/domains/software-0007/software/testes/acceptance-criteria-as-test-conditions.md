---
id: software.testes.acceptance-criteria.000001
tipo: conceito
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
aliases: ["Acceptance criteria as test conditions", "Critérios de aceitação podem ser tratados como condições de teste"]
lote: software-testes-2000-0001
---

# Critérios de aceitação podem ser tratados como condições de teste

## Em uma frase
Critérios de aceitação descrevem condições que uma implementação precisa cumprir para stakeholders aceitarem a história.

## Por que importa
Critérios explícitos ajudam a alinhar o que “pronto” significa e podem fornecer condições exercitáveis para testes. Sem eles, a equipe pode concluir a história com interpretações diferentes sobre sucesso.

## Como funciona
O CTFL observa que critérios de aceitação podem ser vistos como condições de teste. Eles costumam emergir da Conversation na história, mas precisam ser classificados e transformados em casos apropriados. Um critério pode cobrir regra funcional, dado, perfil, resultado ou limite, desde que possa ser verificado.

## Exemplo
Para upload de documento, critérios podem definir formatos aceitos, limite de tamanho, resposta a arquivo inválido e comportamento de reenvio. Os testes então selecionam exemplos, limites e combinações relevantes.

## Limites e trade-offs
Critérios não são necessariamente uma suíte completa nem substituem requisitos de segurança, desempenho ou acessibilidade quando aplicáveis. Uma coleção de critérios vagos também não resolve ambiguidade.

## Como verificar
Revise se cada critério é observável, relacionado ao valor da história, e se casos positivos e negativos estão cobertos; discuta exceções antes de automatizar.

## Conexões
- [[user-story-three-cs]] — situa critérios no modelo dos 3 Cs.
- [[test-entry-exit-criteria]] — distingue critério de aceitação de critérios de atividade.

## Fontes
- [ASTQB — CTFL §4.5.2, Acceptance Criteria](https://astqb.org/4-5-collaboration-based-test-approaches/) — critérios como condições de teste; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.5.2; acesso em 2026-10-01.
