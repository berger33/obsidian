---
id: software.testes.tranche22.001600
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

# jqwik: um engine de properties na plataforma JUnit

## Em uma frase
O jqwik é um motor de teste alternativo para a plataforma do JUnit 5: roda standalone ou ao lado de qualquer outro engine, como Jupiter (o padrão) e Vintage (JUnit 4), basta declará-los no mesmo testImplementation.

## Por que importa
Propriedades e exemplos convivendo com a suíte JUnit existente significa adoção incremental — nenhum projeto precisa escolher entre o time de testes unitários e o de testes de propriedades.

## Como funciona
O mínimo exigido é JUnit Platform 1.14.4; releases no Maven Central (grupo net.jqwik) e snapshots regulares num repositório Sonatype próprio.

## Exemplo
O guia abre com um banner: a partir da versão 1.10 o jqwik adota uma Anti-AI Usage Clause, cláusula de licença que restringe uso por IA — um caso raro de projeto de teste com política explícita na primeira linha da doc.

## Limites e trade-offs
Quem fixa versões antigas do Jupiter precisa checar a plataforma mínima da release do jqwik consumida; a exigência muda entre versões do guia.

## Como verificar
Declare jqwik e jupiter como engines no mesmo build e confirme que ambos os motores aparecem no discovery do Gradle test task.

## Conexões
- [[jqwik-gradle-setup]] — Veja também: jqwik: ligando o motor no Gradle.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
