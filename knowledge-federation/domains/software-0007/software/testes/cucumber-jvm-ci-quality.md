---
id: software.testes.tranche24.001838
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

# CI de teste e de release, com scorecard público

## Em uma frase
A fileira de badges do README expõe a máquina de qualidade: workflow test-java.yaml (build/teste contínuo do framework), workflow release-mvn.yaml (pipeline de publicação Maven), o selo OpenSSF Scorecard com link para o relatório do projeto, além do Maven Central e dos dois badges de financiamento — e o próprio repositório do scorecard é consultável.

## Por que importa
Para quem audita dependências, essa fileira é due diligence barata: o projeto que roda release por pipeline CI tem menos "mão no volante" do que release manual; e o scorecard público mede as práticas de segurança do repo sem depender de marketing do mantenedor.

## Como funciona
Adicione o link do Scorecard (scorecard.dev) ao inventário de terceiros; e em caso de suspeita de supply chain na lib, a comparação entre o tag no repo e o artefato no Central tem trilha pública nos workflows de release documentados no README.

## Exemplo
Um security review pode responder "como essa lib é publicada?" apontando para o workflow de release e o badge de teste que o README linka — dois links verificáveis na página inicial do projeto.

## Limites e trade-offs
A nota afirma a existência e o destino dos checks públicos; o estado atual (verde/vermelho, score N) muda por consulta e não deve ser fixado em texto editorial.

## Como verificar
Os badges na cabeça do README oficial — test-java, release-mvn e OpenSSF Scorecard — são a fonte da nota.

## Conexões
- [[cucumber-jvm-contributing-docs-code]] — Veja também: Contribuir tem duas portas: docs.cucumber.io e CONTRIBUTING.md.
- [[cucumber-jvm-funding]] — Veja também: Financiamento por OpenCollective.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
