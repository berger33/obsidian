---
id: software.testes.tranche14.000767
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
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/examples/skipping-tests.html", "https://maven.apache.org/surefire/maven-surefire-plugin/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven: distinguir pular testes de pular sua compilação

## Em uma frase
`-DskipTests` pula a execução dos testes, enquanto `-Dmaven.test.skip=true` também pode pular a compilação do código de teste.

## Por que importa
O primeiro preserva verificação de compilação durante uma etapa que adia execução; o segundo evita trabalho de compilação e remove essa evidência.

## Como funciona
Use o controle menos amplo necessário e reserve `maven.test.skip` para casos em que compilar testes também deva ser omitido.

## Exemplo
`mvn package -DskipTests` ainda compila as classes de teste; compare com `mvn package -Dmaven.test.skip=true` em um projeto de exemplo.

## Limites e trade-offs
Ambos reduzem validação e não devem virar padrão silencioso em CI nem ser confundidos com build totalmente validado.

## Como verificar
Inspecione o log de compilação, o status do goal e os argumentos efetivos que o pipeline passa a Maven.

## Conexões
- [[maven-parallel-tests-thread-safety]] — Veja também: Maven Surefire: habilitar paralelismo só com estado seguro.
- [[maven-rerun-flaky-evidence]] — Veja também: Maven Surefire: registrar reruns como evidência de flakiness.

## Fontes
- [Maven Surefire — Skipping tests](https://maven.apache.org/surefire/maven-surefire-plugin/examples/skipping-tests.html) — diferença entre pular execução dos testes e pular compilação do test source; consultado em 2026-10-02.
- [Maven Surefire — Introduction](https://maven.apache.org/surefire/maven-surefire-plugin/) — fase test, execução de testes unitários e diretório padrão de relatórios; consultado em 2026-10-02.
