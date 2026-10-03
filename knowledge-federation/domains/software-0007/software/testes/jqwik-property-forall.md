---
id: software.testes.tranche22.001602
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

# jqwik: @Property, @ForAll e os mil tries

## Em uma frase
Uma propriedade é um método anotado com @Property — público, protegido ou package-scoped — cujos parâmetros são todos anotados com @ForAll; o jqwik preenche os valores em runtime, por padrão 1000 tries (conjuntos distintos de parâmetros) por propriedade.

## Por que importa
Teste baseado em exemplo checa o caso que você lembrou; a property checa o espaço inteiro que o gerador cobre, e o padrão de mil execuções torna a aleatoriedade estatisticamente incômoda o bastante para pegar bugs.

## Como funciona
A primeira execução que falha interrompe a geração e é reportada como falha — normalmente seguida de uma tentativa de shrinking do conjunto de valores falsificado.

## Exemplo
@Property boolean absoluteValueOfAllNumbersIsPositive(@ForAll int anInteger) { return Math.abs(anInteger) >= 0; } é o exemplo inaugural do guia.

## Limites e trade-offs
Sem -parameters e com nomes de variáveis genéricos, o relatório de tries fica ilegível; a qualidade do output depende da disciplina de nomenclatura dos parâmetros.

## Como verificar
Reduza tries para 50 num cenário lento com @Property(tries = 50) e confirme no cabeçalho do report quantos checks ocorreram de fato.

## Conexões
- [[jqwik-gradle-setup]] — Veja também: jqwik: ligando o motor no Gradle.
- [[jqwik-failure-report]] — Veja também: jqwik: anatomia do relatório de falsificação.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — repositório de snapshots](https://s01.oss.sonatype.org/content/repositories/snapshots) — repositório de snapshot citado pelo guia; consultado em 2026-10-03.
