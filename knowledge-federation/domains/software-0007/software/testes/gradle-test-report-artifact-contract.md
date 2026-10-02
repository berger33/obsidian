---
id: software.testes.tranche14.000778
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

# Gradle: preservar relatórios de cada task Test

## Em uma frase
Cada task de teste produz resultados que o Gradle pode converter em relatórios, e suites separadas permitem inspecionar resultados por finalidade.

## Por que importa
Relatórios persistidos mantêm evidência mesmo quando a console resume centenas de casos em poucas linhas.

## Como funciona
Publique os XML e HTML gerados para cada task, com nome ou caminho que diferencie unitários de integração.

## Exemplo
Um pipeline pode carregar `build/test-results/test` e a saída correspondente de `integrationTest` como artefatos separados em caso de falha.

## Limites e trade-offs
Saída de console e um agregador de relatórios não substituem a conservação dos arquivos por task e execução.

## Como verificar
Force uma falha em cada suite, localize os artefatos e confirme que o coletor de CI os associa à execução certa.

## Conexões
- [[gradle-fail-on-empty-test-discovery]] — Veja também: Gradle: tratar ausência de testes descobertos como falha.
- [[gradle-ignore-failures-policy]] — Veja também: Gradle: não confundir ignoreFailures com teste aprovado.

## Fontes
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
