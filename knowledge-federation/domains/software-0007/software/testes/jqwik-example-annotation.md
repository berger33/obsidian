---
id: software.testes.tranche22.001605
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

# jqwik: @Example é uma property de um try

## Em uma frase
Testes baseados em exemplo não ficam de fora: @Example marca o caso clássico, e internamente o jqwik trata exemplos como propriedades com tries hardcoded em 1 — tudo que funciona para @Property funciona para eles, inclusive geração com @ForAll.

## Por que importa
Manter exemplos e propriedades no mesmo motor preserva as ferramentas (tags, discovery, relatórios) e elimina o "outro lugar" onde metade do time escreve testes.

## Como funciona
Um @Example void anExample() roda uma vez; um método @Property com @ForAll recebe valores aleatórios mesmo sem corpo de laço — a distinção é apenas o número de tries.

## Exemplo
A mesma classe de ciclo de vida do guia mistura @Example void anExample() e @Property(tries = 5) para mostrar as duas vidas lado a lado.

## Limites e trade-offs
Como exemplo é property de try único, configurações globais que afetam properties (como defaults de atributos) alcançam @Example de formas inesperadas em debugging.

## Como verificar
Converta um @Test do Jupiter para @Example apontando o mesmo motor jqwik e confirme contagem de 1 execução no report.

## Conexões
- [[jqwik-lifecycle]] — Veja também: jqwik: instância nova, hooks e closeables.
- [[jqwik-constraints]] — Veja também: jqwik: restringindo a geração aleatória.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
