---
id: software.testes.tranche22.001582
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
fontes: ["https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html", "https://github.com/reqnroll/Reqnroll/blob/main/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: o que muda de nome vindo do SpecFlow

## Em uma frase
A migração do SpecFlow é majoritariamente renomeação: pacotes SpecFlow.* viram Reqnroll.*, o namespace TechTalk.SpecFlow vira Reqnroll, e classes com SpecFlow no nome (por exemplo ISpecFlowOutputHelper) são renomeadas em consequência.

## Por que importa
Times com milhares de bindings não podem reescrever API de teste inteira para adotar um fork mantido; a migration guide existe para reduzir isso a search-and-replace mais o compatibility package.

## Como funciona
Substitua as referências NuGet removendo tudo que começa com SpecFlow (inclusive CucumberExpressions.SpecFlow.*, agora embutido) e adicionando o Reqnroll.<executor> correspondente ao seu framework.

## Exemplo
Para migrar sem tocar nos using, basta adicionar o pacote opcional Reqnroll.SpecFlowCompatibility, que devolve os nomes TechTalk.SpecFlow por cima das classes Reqnroll.

## Limites e trade-offs
A guia avisa que Reqnroll nasce do codebase do SpecFlow v4; quem vem do v3 precisa ler também a seção de breaking changes do v3 para cá, e não só a tabela de renomeações.

## Como verificar
Faça um build só com troca de pacotes + compatibility package e conte quantos erros de compilação restam antes de qualquer edição manual.

## Conexões
- [[reqnroll-platforms-runners]] — Veja também: Reqnroll: sistemas, .NETs e quatro executores.
- [[reqnroll-datatable-assist]] — Veja também: Reqnroll: DataTable, assistentes e o container DI.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
