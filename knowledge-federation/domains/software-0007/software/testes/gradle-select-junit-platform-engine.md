---
id: software.testes.tranche14.000771
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

# Gradle: ativar explicitamente a JUnit Platform

## Em uma frase
Adicionar uma dependência de teste não basta para selecionar o mecanismo de execução; a task `Test` deve usar a plataforma apropriada ao framework.

## Por que importa
A configuração explícita evita misturar engines antigas e novas sem intenção e deixa claro qual modelo o Gradle usará para descobrir testes.

## Como funciona
Configure `useJUnitPlatform()` para engines da JUnit Platform e declare API, engine e launcher necessários nas configurações corretas do projeto.

## Exemplo
Um projeto Kotlin DSL pode declarar `tasks.test { useJUnitPlatform() }` e executar a suite Jupiter pela task convencional `test`.

## Limites e trade-offs
JUnit Platform é uma plataforma de execução, não um framework único; engines distintos continuam definindo descoberta e semântica próprias.

## Como verificar
Atualize a dependência do engine, execute uma classe conhecida e confira no relatório que seus testes foram descobertos.

## Conexões
- [[gradle-test-task-input-contract]] — Veja também: Gradle: configurar classes e classpath da task Test.
- [[gradle-jvm-test-suite-boundary]] — Veja também: Gradle: modelar integração como suite JVM separada.

## Fontes
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
