---
id: software.testes.tranche22.001607
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

# jqwik: @Provide e o catálogo Arbitraries

## Em uma frase
Quando anotação não basta, o método provedor resolve: um @Provide retorna o Arbitrary para o parâmetro nomeado, e o guia trata ainda suppliers de Arbitrary, providers para tipos embutidos e o catálogo static Arbitraries.* (strings com char ranges, filtros, pesos, embaralhamento).

## Por que importa
Arbitraries são valores de primeira classe: o mesmo Arbitrary de um teste vira tooling de produção (dados sintéticos, property reutilizável entre módulos) sem depender de anotação.

## Como funciona
O caso clássico publicado: provider method retornando Arbitraries.strings().withCharRange('a','z').ofMinLength(1).ofMaxLength(10).filter(s -> s.endsWith("h")) ligado ao @ForAll("first").

## Exemplo
Para gerar você mesmo, randomValue(Function<Random,T>) produz valores que não podem ser shrunk, enquanto fromGenerator(RandomGenerator<T>) mantém o shrinking e deixa o try influenciar a geração.

## Limites e trade-offs
Provider com nome errado quebra só em discovery, e valores vindos de Random puro perdem shrinking e edge cases — o preço da liberdade do randomValue é um relatório pior.

## Como verificar
Troque fromGenerator por randomValue num gerador que falha e observe o Shrunk Sample desaparecer do relatório de falha.

## Conexões
- [[jqwik-constraints]] — Veja também: jqwik: restringindo a geração aleatória.
- [[jqwik-shrinking-assumptions]] — Veja também: jqwik: shrinking, discard ratio e dados fixos.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
