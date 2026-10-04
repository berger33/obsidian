---
id: software.testes.tranche14.000765
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
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/examples/fork-options-and-parallel-execution.html", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: escolher forkCount pelo isolamento exigido

## Em uma frase
`forkCount` limita quantas JVMs de teste são abertas em paralelo; valor zero executa no processo Maven, enquanto valor positivo usa processos separados.

## Por que importa
Forks isolam memória e estado estático do processo de build, mas consomem memória e iniciam JVMs adicionais.

## Como funciona
Meça tempo, memória e contaminação de estado antes de aumentar `forkCount`; documente também a relação com executores paralelos do reactor.

## Exemplo
Um build pode começar com um fork de teste e ajustar a concorrência depois de identificar contenção ou vazamento entre classes.

## Limites e trade-offs
Processos separados não corrigem dependências externas compartilhadas, como portas ou banco de dados, e multiplicam seu consumo quando módulos também rodam em paralelo.

## Como verificar
Compare duração, uso máximo de memória e artefatos temporários em uma execução serial e outra com forks, além de testar repetição.

## Conexões
- [[maven-test-class-naming-patterns]] — Veja também: Maven Surefire: tornar convenções de nome parte da descoberta.
- [[maven-parallel-tests-thread-safety]] — Veja também: Maven Surefire: habilitar paralelismo só com estado seguro.

## Fontes
- [Maven Surefire — Forks and parallel execution](https://maven.apache.org/surefire/maven-surefire-plugin/examples/fork-options-and-parallel-execution.html) — processos JVM, concorrência por framework e limites de execução paralela; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
