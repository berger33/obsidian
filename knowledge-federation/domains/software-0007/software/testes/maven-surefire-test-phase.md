---
id: software.testes.tranche14.000760
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
fontes: ["https://maven.apache.org/surefire/maven-surefire-plugin/", "https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maven Surefire: executar testes unitários na fase test

## Em uma frase
Surefire executa testes unitários na fase `test` do ciclo Maven e produz relatórios texto e XML no diretório padrão do projeto.

## Por que importa
Alinhar o plugin ao lifecycle faz com que `mvn test`, `mvn package` e fases posteriores executem a verificação esperada sem invocar goals fora de ordem.

## Como funciona
Configure dependências de teste e um framework compatível, depois invoque uma fase lifecycle como `mvn test`; o goal `surefire:test` também pode ser chamado explicitamente.

## Exemplo
Um pipeline rápido pode executar `mvn test` antes de empacotar e guardar os arquivos `target/surefire-reports/TEST-*.xml` para diagnóstico.

## Limites e trade-offs
Invocar apenas um goal pode ignorar fases de preparação esperadas pelo projeto; verifique plugins e pré-requisitos do lifecycle local.

## Como verificar
Confirme no log qual goal foi executado, se as classes foram descobertas e se o relatório XML corresponde aos testes esperados.

## Conexões
- [[maven-failsafe-verify-lifecycle]] — Veja também: Maven Failsafe: encerrar integração pela fase verify.

## Fontes
- [Maven Surefire — Introduction](https://maven.apache.org/surefire/maven-surefire-plugin/) — fase test, execução de testes unitários e diretório padrão de relatórios; consultado em 2026-10-02.
- [Maven Surefire — test goal](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html) — parâmetros do goal test, forkCount, seleção, execução paralela e sistema de propriedades; consultado em 2026-10-02.
