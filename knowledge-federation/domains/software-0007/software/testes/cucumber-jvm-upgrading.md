---
id: software.testes.tranche24.001834
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

# Upgrade sem susto: release-notes archive + CHANGELOG do major

## Em uma frase
A seção "Upgrading?" do README define a política de migração: instruções de migração entre majors e a explicação estendida das mudanças notáveis ficam no arquivo de release notes do próprio repositório (pasta release-notes), enquanto as mudanças da linha major corrente ficam no CHANGELOG.md.

## Por que importa
Framework de execução de testes com API de steps sensível a versão ganha uma rota de upgrade documentada por major — o arquivo que separa "migração" de "lista de mudanças" é o que permite planevar a travessia de v6→v7, por exemplo, sem depender de caça em issues.

## Como funciona
Antes de subir um major, leia o documento de migração da pasta release-notes da versão destino e o CHANGELOG corrente; trate as instruções do projeto como checklist de PR de upgrade, incluindo os ajustes de anotação e plugin que cada migration cobre.

## Exemplo
O padrão descrito pelo README para o upgrade de um projeto grande: diff do CHANGELOG corrente para decisão, migration guide da archive para execução do código de steps.

## Limites e trade-offs
A nota afirma a estrutura e o destino da documentação, não o conteúdo de cada guia; cada release pode adicionar detalhes de migração que só existem no próprio documento.

## Como verificar
A seção "Upgrading?" do README oficial aponta os dois arquivos canônicos.

## Conexões
- [[cucumber-jvm-artifacts]] — Veja também: Artefatos versionados no Maven Central.
- [[cucumber-jvm-support-channels]] — Veja também: Onde pedir ajuda: Discussions, Discord e Stack Overflow.

## Fontes
- [Cucumber-JVM — README oficial](https://raw.githubusercontent.com/cucumber/cucumber-jvm/main/README.md) — README oficial do Cucumber-JVM com proposta, execução com ferramentas e DI, starters Maven/Gradle, política de upgrade, suporte voluntário e badges.; consultado em 2026-10-03.
- [Repositório oficial cucumber/cucumber-jvm](https://github.com/cucumber/cucumber-jvm) — Repositório oficial do Cucumber-JVM no GitHub com módulos para a JVM, workflows de CI/release, release-notes e CHANGELOG.; consultado em 2026-10-03.
