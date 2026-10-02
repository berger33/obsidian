---
id: software.testes.tranche14.000773
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

# Gradle: tornar a suite de integração alcançável por check

## Em uma frase
Uma suite de teste adicional não passa a rodar em `check` apenas por existir; seu vínculo com o lifecycle deve ser declarado.

## Por que importa
Um build que omite acidentalmente a suite pode parecer verde enquanto deixa de validar uma camada essencial.

## Como funciona
Adicione uma dependência explícita de `check` para o target ou task da suite e diferencie relações de ordenação de dependências executáveis.

## Exemplo
Configure `tasks.named("check") { dependsOn(testing.suites.named("integrationTest")) }` e execute `gradle check` para comprovar a inclusão.

## Limites e trade-offs
`shouldRunAfter` só orienta ordem se ambas as tasks já foram selecionadas; não substitui `dependsOn`.

## Como verificar
Use `gradle tasks --all` e `gradle check --dry-run` para confirmar presença e ordem da task.

## Conexões
- [[gradle-jvm-test-suite-boundary]] — Veja também: Gradle: modelar integração como suite JVM separada.
- [[gradle-parallel-forks-and-unique-resources]] — Veja também: Gradle: isolar recursos quando maxParallelForks aumenta.

## Fontes
- [Gradle — JVM Test Suite Plugin](https://docs.gradle.org/current/userguide/jvm_test_suite_plugin.html) — modelagem de suites, dependências, frameworks, tasks adicionais e integração; consultado em 2026-10-02.
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
