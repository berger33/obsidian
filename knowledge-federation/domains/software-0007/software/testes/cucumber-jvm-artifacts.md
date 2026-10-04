---
id: software.testes.tranche24.001833
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

# Artefatos versionados no Maven Central

## Em uma frase
O badge principal do README aponta para o artefato canônico io.cucumber/cucumber-java no Maven Central da Sonatype — o canal oficial de consumo da biblioteca, com a versão estável consultável no próprio link do badge.

## Por que importa
Para governança de dependências em JVM, o Maven Central com groupId io.cucumber significa artefatos assinados, versionamento semântico nas séries de major e histórico auditável — a alternativa a "baixar do GitHub" que muitos times ainda aceitam como default.

## Como funciona
Declare a dependência com o groupId io.cucumber no pom/build.gradle, fixe a versão no gerenciador de dependências e acompanhe upgrades via release notes (ver a nota específica deste grupo).

## Exemplo
No Spring Boot atual, o starter de teste já administra BOMs; adicionar o artifact do Cucumber ao mesmo plano de versionamento mantém o upgrade deliberado, não transitivo.

## Limites e trade-offs
O README não lista plataformas de consumo além do Central (por exemplo, artefatos nativos ou BOM completa); a consulta canônica de versão é o link do próprio badge, que muda entre releases.

## Como verificar
O badge de Maven Central para io.cucumber/cucumber-java está na fileira de topo do README oficial.

## Conexões
- [[cucumber-jvm-hello-world-starters]] — Veja também: Aprendizado oficial: dois starters e um repositório de exemplos.
- [[cucumber-jvm-upgrading]] — Veja também: Upgrade sem susto: release-notes archive + CHANGELOG do major.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
