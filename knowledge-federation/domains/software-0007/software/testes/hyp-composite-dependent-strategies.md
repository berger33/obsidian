---
id: software.testes.tranche12.000561
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/strategies.html", "https://hypothesis.readthedocs.io/en/latest/reference/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: estratégias próprias com `@composite`

## Em uma frase
`@composite` permite combinar draws de estratégias em um gerador reutilizável cuja saída depende dos valores já sorteados.

## Por que importa
Esse padrão expressa objetos estruturados com invariantes entre campos, sem gerar combinações inválidas e descartá-las depois por meio de muitas precondições.

## Como funciona
Defina uma função decorada com `@composite`, receba `draw` e solicite cada componente às estratégias apropriadas; derive campos relacionados a partir de draws anteriores e retorne o objeto final.

## Exemplo
Uma estratégia pode sortear uma data de início e depois gerar uma data de fim igual ou posterior, produzindo intervalos que satisfazem o contrato do construtor.

## Limites e trade-offs
Um gerador customizado pode introduzir enviesamento se sempre escolher uma das ramificações ou se esconder regras relevantes do domínio. Combinadores prontos são mais simples quando já descrevem o caso.

## Como verificar
Experimente a estratégia em um teste e inspecione exemplos representativos; inclua limites em que cada ramificação muda e verifique se a propriedade ainda pode encontrar violações.

## Conexões
- [[hypothesis-strategy-combinators]] — Veja também: Hypothesis: map, flatmap e filter em estratégias.
- [[hyp-data-draw-dinamico]] — Veja também: Hypothesis: draws dinâmicos com `data()`.

## Fontes
- [Hypothesis — Strategies Reference](https://hypothesis.readthedocs.io/en/latest/reference/strategies.html) — estratégias primitivas, compositores, builds, coleções, exemplos e filtros; consultado em 2026-10-02.
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
