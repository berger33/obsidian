---
id: software.testes.tranche22.001603
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

# jqwik: anatomia do relatório de falsificação

## Em uma frase
O bloco de falha do jqwik é um diagnóstico completo: tentativas e checks, modo de geração (RANDOMIZED), política after-failure (SAMPLE_FIRST), quando-fixed-seed (ALLOW), modo e contagem de edge cases (MIXIN, totals e tried) e o seed reproduzível.

## Por que importa
Entre o barulho de stack trace, as duas linhas que salvam são a do seed — para reproduzir exatamente a sequência — e o par Shrunk Sample versus Original Sample, que mostra o menor contraexemplo encontrado e o bruto original.

## Como funciona
Um exemplo publicado reporta tries = 16, checks = 16, edge-cases#total = 4, seed = -2370223836245802816, e exibe a string Unicode gigante do Original Sample encolhida para "" "" no Shrunk Sample.

## Exemplo
Os footnotes (Adding Footnotes to Failure Reports) permitem anotar valores derivados no relatório, como a diferença calculada entre dois números da falha.

## Limites e trade-offs
O cabeçalho muda entre versões do guia — campos como when-fixed-seed refletem configuração global; comparar relatórios entre builds com versões diferentes cobra atenção.

## Como verificar
Reproduza uma falha local, cole o seed num teste duplicado com @Property(seed) e confirme que o mesmo Shrunk Sample reaparece.

## Conexões
- [[jqwik-property-forall]] — Veja também: jqwik: @Property, @ForAll e os mil tries.
- [[jqwik-lifecycle]] — Veja também: jqwik: instância nova, hooks e closeables.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
