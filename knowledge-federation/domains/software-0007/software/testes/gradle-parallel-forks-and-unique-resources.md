---
id: software.testes.tranche14.000774
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

# Gradle: isolar recursos quando maxParallelForks aumenta

## Em uma frase
`maxParallelForks` define o máximo de processos de teste concorrentes e seu valor padrão é um.

## Por que importa
Mais processos podem reduzir duração, mas testes que disputam nomes, arquivos ou serviços externos passam a interferir entre si.

## Como funciona
Aumente concorrência apenas após particionar recursos mutáveis e use o identificador de worker Gradle para nomes temporários únicos.

## Exemplo
Um teste que grava snapshots pode incluir `org.gradle.test.worker` no diretório temporário para que workers paralelos não sobrescrevam o mesmo arquivo.

## Limites e trade-offs
Worker id único não isola automaticamente banco, porta, usuário externo ou fixture compartilhada; a aplicação precisa usar identificadores compatíveis.

## Como verificar
Compare execução serial e paralela repetida, verificando colisões de dados e falhas que desaparecem quando a concorrência volta a um.

## Conexões
- [[gradle-check-dependency-for-suite]] — Veja também: Gradle: tornar a suite de integração alcançável por check.
- [[gradle-fork-every-process-reset]] — Veja também: Gradle: usar forkEvery para limitar estado por processo.

## Fontes
- [Gradle — Testing in Java and JVM projects](https://docs.gradle.org/current/userguide/java_testing.html) — descoberta, execução, filtragem, integração e relatórios de testes JVM; consultado em 2026-10-02.
- [Gradle — Test task API](https://docs.gradle.org/current/dsl/org.gradle.api.tasks.testing.Test.html) — propriedades e métodos da task Test, processos, filtros e falhas; consultado em 2026-10-02.
