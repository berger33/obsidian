---
id: software.testes.tranche24.001831
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
fontes: ["https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md", "https://cucumber.io/docs/installation/java/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Execução plugável: com suas ferramentas e contêineres DI

## Em uma frase
O README descreve a integração com o stack como aberta: "You can run it with the tool of your choice - including with popular dependency injection containers", com links para o guia de API de execução e para a seção de instalação com DI no site oficial.

## Por que importa
Para empresas com Spring/Guice/CDI, essa é a diferença entre testes de integração que instalam contexto de aplicação de qualquer jeito e steps que recebem os beans gerenciados pelo contêiner — o suporte a DI de primeira classe é o que torna o Cucumber viável em stacks corporativos de JVM.

## Como funciona
Adicione o plugin da sua ferramenta de build (JUnit Platform, plugin Maven/Gradle) e o módulo de integração do seu contêiner de DI, conforme as páginas linkadas do site oficial; o Cucumber não exige ser o runner mestre do projeto.

## Exemplo
Um projeto Spring Boot típico roda features com o contexto de teste gerenciado pelo contêiner, reaproveitando beans, mocks de profile e propriedades — sem o segundo container bootstrap manual que a ausência de DI forçaria.

## Limites e trade-offs
O README garante o suporte com a frase e o link; a lista exata de contêineres suportados e os nomes de artefatos de integração vivem nas páginas de instalação da doc, não no trecho lido.

## Como verificar
As frases de execução e o link de DI constam da seção introdutória do README oficial.

## Conexões
- [[cucumber-jvm-what-it-is]] — Veja também: Cucumber JVM: testes automatizados em linguagem natural na JVM.
- [[cucumber-jvm-hello-world-starters]] — Veja também: Aprendizado oficial: dois starters e um repositório de exemplos.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Cucumber — Installation for Java (documentação oficial)](https://cucumber.io/docs/installation/java/) — Documentação oficial do Cucumber para instalação e injeção de dependência em Java na JVM.; consultado em 2026-10-03.
