---
id: software.testes.tranche24.001837
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

# Contribuir tem duas portas: docs.cucumber.io e CONTRIBUTING.md

## Em uma frase
A seção "Contributing" separa os fluxos de contribuição: para a documentação, o repositório é o cucumber/docs.cucumber.io; para o código do framework, o CONTRIBUTING.md do próprio repositório é o guia, com nota explícita de que é o caminho para quem não é docs.

## Por que importa
A separação revela que o produto tem duas superfícies mantidas em repositórios distintos — a especificação escrita do comportamento da ferramenta (o Cucumber usa features para descrever seus próprios testes) e as páginas de documentação — e cada uma aceita contribuição pela própria porta, sem burocracia de cruzamento.

## Como funciona
Para corrigir um parágrafo ambíguo da doc, o PR vai para o repo de docs; para ajustar comportamento do engine, siga o CONTRIBUTING.md do código (ambiente, testes, estilo) antes de abrir a PR.

## Exemplo
Um fix pequeno de redação numa página do site oficial é um PR no docs.cucumber.io — a trilha separada é declarada no README justamente para evitar PR de texto no repositório do motor.

## Limites e trade-offs
O README aponta as duas portas mas não reproduz os critérios internos de aceite; ambos os fluxos têm suas próprias regras nos documentos linkados.

## Como verificar
A seção "Contributing" do README oficial define a divisão dos dois destinos.

## Conexões
- [[cucumber-jvm-volunteer-reality]] — Veja também: A frase mais importante para quem vai abrir uma issue.
- [[cucumber-jvm-ci-quality]] — Veja também: CI de teste e de release, com scorecard público.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
