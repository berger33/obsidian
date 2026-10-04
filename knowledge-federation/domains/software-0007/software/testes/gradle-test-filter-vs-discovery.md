---
id: software.testes.tranche14.000776
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
fontes: ["https://docs.gradle.org/current/userguide/java_testing.html", "https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gradle: combinar filtro dirigido com descoberta visível

## Em uma frase
O filtro da task permite reduzir quais testes são executados, enquanto a descoberta identifica classes e métodos reconhecidos pelo framework.

## Por que importa
Um filtro útil para diagnóstico pode ocultar mudança na descoberta ou selecionar uma amostra menor que a cobertura esperada do módulo.

## Como funciona
Configure filtros de inclusão e exclusão de modo explícito, e revise o conjunto de testes descobertos quando alterar framework ou convenção de nomes.

## Exemplo
Um comando direcionado pode executar apenas `com.example.PaymentTest`, seguido por uma execução sem filtro antes do merge.

## Limites e trade-offs
Padrões de task e seletores de framework não são equivalentes em todo provider, especialmente em suites não baseadas em classes.

## Como verificar
Compare lista e contagem de testes com e sem filtro e valide que nenhum padrão excluiu uma package importante.

## Conexões
- [[gradle-fork-every-process-reset]] — Veja também: Gradle: usar forkEvery para limitar estado por processo.
- [[gradle-fail-on-empty-test-discovery]] — Veja também: Gradle: tratar ausência de testes descobertos como falha.

## Fontes
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
