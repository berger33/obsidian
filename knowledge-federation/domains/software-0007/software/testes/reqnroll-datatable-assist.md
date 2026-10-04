---
id: software.testes.tranche22.001583
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

# Reqnroll: DataTable, assistentes e o container DI

## Em uma frase
Além da renomeação, a API ganhou ajustes de vocabulário Gherkin: existe agora o alias DataTable para a classe Table, os assistentes de mapeamento viraram "DataTable Helpers" no namespace Reqnroll (usáveis sem using extra) e o container de injeção de dependência mudou de BoDi para Reqnroll.BoDi.

## Por que importa
Mapear tabelas Gherkin em objetos de domínio é o coração da legibilidade dos cenários; a nomenclatura alinhada ao Gherkin remove uma camada de tradução mental de quem lê o passo.

## Como funciona
Use Table ou o novo alias DataTable para dados tabulares dos cenários e chame os métodos de conversão dos DataTable Helpers diretamente nos bindings, já visíveis no namespace principal.

## Exemplo
Uma tabela Examples de clientes vira lista tipada pelo assistente sem using adicional, porque as extension methods foram movidas para o namespace Reqnroll propriamente dito.

## Limites e trade-offs
Quem customizou a resolução de dependências acessando o container diretamente precisa atualizar os usings para Reqnroll.BoDi — a guia chama atenção específica para esse ponto.

## Como verificar
Escreva um binding que materializa um objeto de domínio a partir da tabela do cenário usando os helpers e confirme a compilação sem imports de TechTalk.

## Conexões
- [[reqnroll-rename-migration]] — Veja também: Reqnroll: o que muda de nome vindo do SpecFlow.
- [[reqnroll-cucumber-expressions]] — Veja também: Reqnroll: expressões Cucumber embutidas.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
