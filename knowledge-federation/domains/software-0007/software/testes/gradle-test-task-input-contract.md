---
id: software.testes.tranche14.000770
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

# Gradle: configurar classes e classpath da task Test

## Em uma frase
Uma task Gradle do tipo `Test` precisa dos diretórios de classes de teste e do classpath de execução para descobrir e executar casos JVM.

## Por que importa
Quando qualquer uma dessas entradas aponta para saída incompleta ou configuração de outra suite, a task pode executar zero testes ou resolver dependências incorretas.

## Como funciona
Registre a task com o conjunto compilado e o runtime classpath do source set correspondente, de preferência usando providers e convenções do plugin JVM.

## Exemplo
Uma suite de integração usa `intTest.output.classesDirs` junto de `intTest.runtimeClasspath`, em vez de reutilizar o classpath unitário por engano.

## Limites e trade-offs
Criar uma `Test` task manualmente não configura automaticamente source set, compilação, dependências ou participação no lifecycle.

## Como verificar
Verifique entradas resolvidas no Gradle, faça `--dry-run` para avaliar dependências e confira classes descobertas no relatório.

## Conexões
- [[gradle-select-junit-platform-engine]] — Veja também: Gradle: ativar explicitamente a JUnit Platform.

## Fontes
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
