---
id: software.testes.tranche22.001608
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://jqwik.net/docs/current/user-guide.html", "https://search.maven.org/search?q=g:net.jqwik"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# jqwik: shrinking, discard ratio e dados fixos

## Em uma frase
O shrinking tenta encontrar amostras menores que ainda falsificam a propriedade; o guia cobre modo integrado, desligar (ShrinkingMode.OFF), modo full e trocar o alvo do shrink, com exemplos onde a string "LVtyB" encolhe para "AA".

## Por que importa
Contraexemplo mínimo é a diferença entre um bug que se reproduz em um case e um que morre na triagem; desligar shrinking para acelerar feedback cobra esse preço.

## Como funciona
Com Assumptions, o try pode ser descartado por não satisfazer premissas: maxDiscardRatio limita a razão entre tries e checks — default 5 — e estourá-la reporta a property como falha, com override em junit-platform.properties.

## Exemplo
Propriedades data-driven (@ForAll com @DataPoints) recebem dados na ordem fornecida, tries limita quantos data points rodam, apenas a primeira falsificação é reportada e não há shrinking — o jqwik não conhece as restrições dos dados externos.

## Limites e trade-offs
Dados dirigidos por exemplo antigo do JUnit (parameterized) dão falsa sensação de propriedade; sem shrinking, o report é o case bruto que falhou, do jeito feio que veio.

## Como verificar
Force um filtro absurdo (assume true com probabilidade 1/100) e veja a falha por discard ratio explodir mesmo sem bug no código.

## Conexões
- [[jqwik-provide]] — Veja também: jqwik: @Provide e o catálogo Arbitraries.
- [[jqwik-config-modules]] — Veja também: jqwik: configuração central e módulos de nicho.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
