---
id: software.testes.tranche22.001604
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

# jqwik: instância nova, hooks e closeables

## Em uma frase
A suíte roda com isolamento por desenho: para cada property ou example é criada uma nova instância da classe contêiner, e cada property executa de 1 a n tries cujos argumentos são bindados nos parâmetros @ForAll.

## Por que importa
O estado mutável entre tries é o assassino clássico de testes de propriedades; saber que a instância renova a cada propriedade (e o que não renova entre tries) define onde guardar fixtures.

## Como funciona
Um arsenal de anotações cobre as granularidades: @BeforeContainer/@AfterContainer (estáticos, por classe), @BeforeProperty/@AfterProperty e @BeforeTry/@AfterTry, além de AutoCloseable implementado pela classe de teste como pós-cada-execução.

## Exemplo
No exemplo SimpleLifecycleTests, o construtor imprime "Before each" e o close() imprime "After each" ao redor de um @Property(tries = 5) que roda o corpo cinco vezes.

## Limites e trade-offs
A simetria com Jupiter (sem @BeforeEach por try automático) confunde migração: no jqwik cada try da MESMA property compartilha a instância, e é aí que estado pode vazar.

## Como verificar
Coloque um contador de instância em campo estático e um em campo de instância num @Property(tries = 3) e confira qual zera a cada execução.

## Conexões
- [[jqwik-failure-report]] — Veja também: jqwik: anatomia do relatório de falsificação.
- [[jqwik-example-annotation]] — Veja também: jqwik: @Example é uma property de um try.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
