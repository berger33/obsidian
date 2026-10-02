---
id: software.testes.tranche14.000766
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

# Maven Surefire: habilitar paralelismo só com estado seguro

## Em uma frase
Surefire não executa testes em paralelo por padrão; paralelismo precisa ser configurado segundo provider e estrutura de testes.

## Por que importa
Threads concorrentes podem revelar corridas e reduzir duração, porém compartilham processo e recursos, ao contrário de parte do isolamento fornecido por forks.

## Como funciona
Escolha granularidade como classes ou métodos, limite threads e torne dados, fixtures, portas e nomes de arquivos independentes antes de ativar concorrência.

## Exemplo
Ative execução paralela em um módulo sem efeitos globais e use nomes de recursos derivados de um identificador de teste para evitar colisões.

## Limites e trade-offs
Configurações de thread count dependem do provider; aumentar threads sem limites pode saturar CPU, banco ou memória.

## Como verificar
Rode várias vezes com ordem e concorrência alteradas e examine falhas não determinísticas, consumo de recursos e isolamento do ambiente.

## Conexões
- [[maven-fork-count-process-isolation]] — Veja também: Maven Surefire: escolher forkCount pelo isolamento exigido.
- [[maven-skip-execution-vs-test-compilation]] — Veja também: Maven: distinguir pular testes de pular sua compilação.

## Fontes
- [Maven Surefire — Forks and parallel execution](https://maven.apache.org/surefire/maven-surefire-plugin/examples/fork-options-and-parallel-execution.html) — processos JVM, concorrência por framework e limites de execução paralela; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
