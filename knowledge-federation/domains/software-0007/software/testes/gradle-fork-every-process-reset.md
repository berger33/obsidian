---
id: software.testes.tranche14.000775
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html", "https://docs.gradle.org/current/userguide/java_testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gradle: usar forkEvery para limitar estado por processo

## Em uma frase
`forkEvery` reinicia o processo de teste depois de certo número de classes ou definições executadas.

## Por que importa
O recurso pode conter vazamentos de estado estático ou recursos de framework que não podem ser limpos entre classes.

## Como funciona
Meça o problema primeiro, escolha um limite suficientemente alto e trate o reinício como contenção, não como substituto de teardown correto.

## Exemplo
Se uma biblioteca acumula registries globais, configurar um limite moderado pode ajudar a localizar o número de classes após o qual a contaminação começa.

## Limites e trade-offs
Valor baixo reinicia JVM com frequência e pode prejudicar muito a performance; processos novos também não limpam arquivos ou bancos compartilhados.

## Como verificar
Compare duração e falhas com `forkEvery=0` e com um limite investigativo, depois corrija a origem de estado persistente quando possível.

## Conexões
- [[gradle-parallel-forks-and-unique-resources]] — Veja também: Gradle: isolar recursos quando maxParallelForks aumenta.
- [[gradle-test-filter-vs-discovery]] — Veja também: Gradle: combinar filtro dirigido com descoberta visível.

## Fontes
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
