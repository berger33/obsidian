---
id: software.testes.tranche23.001687
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/approvals/ApprovalTests.Java/blob/master/README.md", "https://approvaltests.com/", "https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Compatibilidade Java: JUnit 3/4/5, TestNG e JDK 8+

## Em uma frase
As três primeiras linhas técnicas do README oficial fixam a base: biblioteca de asserção/verificação open source, compatível com JUnit 3, 4 e 5 e com TestNG, funcionando em JDK 1.8+ com a lista testada 1.8, 17, 21, 24, 25 e 26 — e a nota de licença registra Apache 2.0.

## Por que importa
Essa matriz transversa é o que permite adotar approval testing incrementalmente em bases Java heterogêneas: o módulo legado no JUnit 3 e o novo no JUnit 5 compartilham a mesma dependência de verificação.

## Como funciona
A distribuição vai ao Maven Central (grupo com.approvaltests, artefato approvaltests, escopo test — o exemplo oficial na versão 31.0.0) e pode ser obtida como jar direto do repo do Maven Central; starter projects oficiais cobrem Java com Maven ou Gradle, Kotlin, Groovy e Scala.

## Exemplo
Declare a dependência no pom do seu projeto legado — ou como testImplementation no Gradle — na versão corrente e rode uma verificação de aprovação ao lado dos testes existentes; os starters servem de esqueleto comparativo.

## Limites e trade-offs
A versão citada no README (31.0.0) é o snapshot do exemplo da página, não garantia de latest; os starters declaram CI própria com GitHub Actions — a matriz 1.8 até 26 é o que o projeto testa, não o máximo imaginável.

## Como verificar
Abra o topo e as seções How to get it e LICENSE do README oficial e confirme as frases de compatibilidade, a matriz de JDK, o snippet Maven e a licença Apache 2.0.

## Conexões
- [[approvaltests-reporters]] — Veja também: Reporters: a diferença é apresentada pela ferramenta certa.
- [[approvaltests-legacy-code]] — Veja também: Approval testing como ponte para legado e dogfood.

## Fontes
- [ApprovalTests.Java — README oficial](https://github.com/approvals/ApprovalTests.Java/blob/master/README.md) — proposta, compatibilidades, exemplo verifyAll, artefatos aprovados e licença; consultado em 2026-10-03.
- [ApprovalTests — site oficial](https://approvaltests.com/) — porta de entrada referenciada pelo README; consultado em 2026-10-03.
- [ApprovalTests — tutorial Getting Started](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/tutorials/GettingStarted.md) — verify, verifyAll, JSON, AWT, combinações, aprovação e reporters; consultado em 2026-10-03.
