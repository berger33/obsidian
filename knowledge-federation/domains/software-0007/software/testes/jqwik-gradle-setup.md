---
id: software.testes.tranche22.001601
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
fontes: ["https://jqwik.net/docs/current/user-guide.html", "https://s01.oss.sonatype.org/content/repositories/snapshots"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# jqwik: ligando o motor no Gradle

## Em uma frase
A configuração Gradle documentada usa useJUnitPlatform { includeEngines 'jqwik' } — com a variante comentada de incluir mais motores juntos — e filtra classes por **/*Properties.class, **/*Test.class e **/*Tests.class no bloco test.

## Por que importa
Sem includeEngines, o Gradle roda todo engine presente; nomear o jqwik de propósito torna o build um registro de quais motores a suíte realmente cobre.

## Como funciona
O guia também adiciona -parameters no compileTestJava para habilitar nomes de argumentos em relatórios e no debug, e usa ext.junitJupiterVersion = '5.14.4' ao lado de ext.jqwikVersion = '1.10.1'.

## Exemplo
Repositórios: mavenCentral() mais, para snapshots, um bloco maven { url 'https://central.sonatype.com/repository/maven-snapshots/' } copiado do próprio guia.

## Limites e trade-offs
Desde o Gradle 4.6 o suporte à plataforma é nativo; builds mais antigos não pegam useJUnitPlatform e o falho fica silencioso se o plugin não reclamar.

## Como verificar
Comente o -parameters, provoque uma falha de propriedade e veja o relatório perder os nomes dos parâmetros gerados.

## Conexões
- [[jqwik-what-it-is]] — Veja também: jqwik: um engine de properties na plataforma JUnit.
- [[jqwik-property-forall]] — Veja também: jqwik: @Property, @ForAll e os mil tries.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — repositório de snapshots](https://s01.oss.sonatype.org/content/repositories/snapshots) — repositório de snapshot citado pelo guia; consultado em 2026-10-03.
