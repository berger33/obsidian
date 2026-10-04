---
id: software.testes.tranche14.000772
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
fontes: ["https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html", "https://docs.gradle.org/current/userguide/java_testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gradle: modelar integração como suite JVM separada

## Em uma frase
O plugin JVM Test Suite permite agrupar testes por propósito, com source, dependências, framework e task próprios.

## Por que importa
Separar integração de unidade clarifica custo, requisitos ambientais e o ponto em que cada verificação entra no build.

## Como funciona
Registre `integrationTest` na extensão `testing.suites`, configure suas dependências e escolha explicitamente a ordem ou a relação com a task `check`.

## Exemplo
A suite pode depender do código de produção e usar Testcontainers sem adicionar essas dependências aos testes unitários rápidos.

## Limites e trade-offs
A API do plugin é incubating na documentação atual e pode mudar; suites adicionais não herdam automaticamente todos os vínculos do `test` padrão.

## Como verificar
Confirme a task criada, source set, classpath, dependências e quais tarefas do lifecycle realmente a executam.

## Conexões
- [[gradle-select-junit-platform-engine]] — Veja também: Gradle: ativar explicitamente a JUnit Platform.
- [[gradle-check-dependency-for-suite]] — Veja também: Gradle: tornar a suite de integração alcançável por check.

## Fontes
- [Gradle — JVM Test Suite Plugin](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html) — modelagem de suites, dependências, frameworks, tasks adicionais e integração; consultado em 2026-10-02.
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
