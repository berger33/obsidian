---
id: software.testes.tranche22.001585
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html", "https://docs.reqnroll.net/latest/integrations/available-plugins.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: plugins portados e Actions de automação

## Em uma frase
Os plugins de integração mantidos pelo SpecFlow foram portados (exemplo: Reqnroll.Autofac), e os pacotes SpecFlow.Actions.* — que traziam suporte pronto a tecnologias de automação — vivem como Reqnroll.SpecFlowCompatibility.Actions.*, por exemplo Actions.Selenium.

## Por que importa
Times que usavam Actions para API testing e Selenium com o SpecFlow ganham a ponte pronta; não precisam reimplementar bindings de infra para continuar rodando no fork.

## Como funciona
Adicione o pacote Reqnroll conforme seu executor, o compatibility package quando não quiser renomear namespaces, e os Actions equivalentes aos que já usava.

## Exemplo
A migration guide lista textualmente: remover SpecFlow.Actions.*, adicionar Reqnroll.SpecFlowCompatibility.Actions.Selenium — o par exato da troca.

## Limites e trade-offs
A extensão para Visual Studio foi refeita para lidar com projetos SpecFlow e Reqnroll lado a lado (inclusive .NET 8.0), mas quem usa Rider ou VS Code depende de suporte próprio de cada IDE para highlighting.

## Como verificar
Rode um projeto de exemplo com Actions.Selenium na matriz CI e confirme que os steps pré-fabricados resolvem sem editar feature files.

## Conexões
- [[reqnroll-cucumber-expressions]] — Veja também: Reqnroll: expressões Cucumber embutidas.
- [[reqnroll-livingdoc]] — Veja também: Reqnroll: Living Documentation ficou de fora.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — Available Plugins](https://docs.reqnroll.net/latest/integrations/available-plugins.html) — plugins portados citados pela guia de migração; consultado em 2026-10-03.
