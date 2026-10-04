---
id: software.testes.tranche14.000777
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

# Gradle: tratar ausência de testes descobertos como falha

## Em uma frase
`failOnNoDiscoveredTests` pode impedir que uma task com fontes de teste existentes termine silenciosamente sem descobrir nenhum teste.

## Por que importa
Renomear uma classe, remover engine ou alterar pacote pode fazer um job continuar verde sem testar o código esperado.

## Como funciona
Preserve a política de falha em suites nas quais fontes de teste devem produzir casos e trate explicitamente módulos que legitimamente não contêm testes.

## Exemplo
Uma task da suite de pagamento deve falhar quando seu diretório contém código de teste mas o provider descobre zero casos após uma migração.

## Limites e trade-offs
A verificação depende da condição de fontes presentes e da configuração da task; um source set vazio legítimo merece configuração própria.

## Como verificar
Crie um cenário de descoberta zero e confira a saída do Gradle, em vez de assumir que task executada significa casos executados.

## Conexões
- [[gradle-test-filter-vs-discovery]] — Veja também: Gradle: combinar filtro dirigido com descoberta visível.
- [[gradle-test-report-artifact-contract]] — Veja também: Gradle: preservar relatórios de cada task Test.

## Fontes
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
