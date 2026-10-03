---
id: software.testes.tranche24.001832
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md", "https://github.com/cucumber/cucumber-jvm"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Aprendizado oficial: dois starters e um repositório de exemplos

## Em uma frase
Em "Getting started", o README fornece os pontos de entrada prontos: projetos hello world para Maven (cucumber-jvm-starter-maven-java) e para Gradle (cucumber-jvm-starter-gradle-java), mais o repositório agregado cucumber-jvm-examples de projetos de exemplo — ao lado dos links de instalação e documentação no site oficial.

## Por que importa
A existência de starters por ferramenta de build elimina a fase de "montar o esqueleto" da avaliação: o time clona, roda a primeira feature, e a decisão de adoção parte de um projeto que compila, não de um README com snippet quebrado.

## Como funciona
Comece pelo starter da sua ferramenta, rode o build para ver a feature de exemplo executando, e só então substitua o scenario hello-world pela primeira especificação real do domínio; o repositório de exemplos cobre variações além do esqueleto.

## Exemplo
O fluxo sugerido pela estrutura do README: starter → instalação documentada → doc de referência; três degraus, cada um com repositório ou URL própria.

## Limites e trade-offs
Os starters são repositórios separados do core; a nota afirma a existência e o destino pelo índice oficial, sem verificar em cada um o estado de compatibilidade com a versão mais recente do framework.

## Como verificar
Os três repositórios e os dois links de doc aparecem na seção Getting started do README oficial.

## Conexões
- [[cucumber-jvm-run-with-your-tools]] — Veja também: Execução plugável: com suas ferramentas e contêineres DI.
- [[cucumber-jvm-artifacts]] — Veja também: Artefatos versionados no Maven Central.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
