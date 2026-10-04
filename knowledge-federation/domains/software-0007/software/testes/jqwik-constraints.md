---
id: software.testes.tranche22.001606
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

# jqwik: restringindo a geração aleatória

## Em uma frase
A geração padrão conhece os tipos (strings, inteiros, listas, mapas, arrays, funcionais) e é ajustada por anotações de restrição nos parâmetros: @IntRange(min = -5, max = 5) delimita inteiros, @AlphaChars restringe o alfabeto, e a seção homônima do guia enumera limites de tamanho de string, char sets, nullabilidade e unicidade.

## Por que importa
Gerar "qualquer coisa" produz falsos positivos inúteis quando o contrato do domínio é estreito; restrições declaram o espaço de amostragem sem sair da anotação.

## Como funciona
Shrinking e restrição combinam: o exemplo do guia usa @AlphaChars numa string que deve encolher para "AA", mostrando o shrinker respeitando o espaço alfabético.

## Exemplo
Para regras próprias, o guia demonstra anotações caseiras empilhando restrições — o exemplo GermanText combina @NumericChars, @AlphaChars, @Chars e @StringLength num único @interface.

## Limites e trade-offs
Filtrar demais (withFilter/assumptions) derruba o discard ratio e a property pode ser reportada como falha mesmo sem bug — restrição tem de nascer do domínio, não do medo.

## Como verificar
Gere amostras de um @IntRange estreito usando a geração direta de streams e confirme que edge cases (mín/max) aparecem na amostra.

## Conexões
- [[jqwik-example-annotation]] — Veja também: jqwik: @Example é uma property de um try.
- [[jqwik-provide]] — Veja também: jqwik: @Provide e o catálogo Arbitraries.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
