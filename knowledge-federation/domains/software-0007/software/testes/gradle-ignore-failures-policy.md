---
id: software.testes.tranche14.000779
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

# Gradle: não confundir ignoreFailures com teste aprovado

## Em uma frase
`ignoreFailures` permite que o build prossiga após falha da task Test, mas não altera o resultado individual dos testes.

## Por que importa
Usar a opção indiscriminadamente remove um bloqueio de integração importante e pode converter falhas visíveis em artefatos ignorados.

## Como funciona
Ative-a apenas quando uma etapa de diagnóstico precisa coletar tarefas posteriores, e preserve um passo explícito que torne a falha final impossível de perder.

## Exemplo
Uma tarefa experimental pode reunir relatórios de vários módulos e deixar a decisão final para um verificador de resultados no fim do job.

## Limites e trade-offs
`ignoreFailures` não pula a execução, não corrige falhas e não deve servir para mascarar regressões em uma branch protegida.

## Como verificar
Introduza uma falha controlada e confirme estado da task, código de saída final e política de CI.

## Conexões
- [[gradle-test-report-artifact-contract]] — Veja também: Gradle: preservar relatórios de cada task Test.

## Fontes
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
