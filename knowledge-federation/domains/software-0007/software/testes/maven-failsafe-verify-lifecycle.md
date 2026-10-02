---
id: software.testes.tranche14.000761
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
fontes: ["https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Failsafe: encerrar integração pela fase verify

## Em uma frase
Failsafe separa execução de testes de integração em `integration-test` da avaliação final de resultados em `verify`.

## Por que importa
A separação permite que plugins encerrem servidores e recursos em `post-integration-test` antes que o build seja marcado como falho.

## Como funciona
Vincule os goals `integration-test` e `verify` e execute uma fase igual ou posterior a `verify`, normalmente `mvn verify`, para completar o fluxo.

## Exemplo
Um projeto inicia o servidor em `pre-integration-test`, executa Failsafe durante `integration-test`, para o servidor em `post-integration-test` e valida em `verify`.

## Limites e trade-offs
Chamar somente `mvn integration-test` pode deixar serviços ativos e não realizar a verificação final agregada dos resultados.

## Como verificar
Provoque uma falha de integração e confirme que teardown ocorreu antes de o goal `verify` encerrar o build com erro.

## Conexões
- [[maven-surefire-test-phase]] — Veja também: Maven Surefire: executar testes unitários na fase test.
- [[maven-single-test-selection]] — Veja também: Maven Surefire: selecionar classe sem confundir o escopo.

## Fontes
- [Maven Failsafe — Usage](https://maven.apache.org/surefire/maven-failsafe-plugin/usage.html) — goals integration-test e verify, teardown do ciclo e relatórios de integração; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
