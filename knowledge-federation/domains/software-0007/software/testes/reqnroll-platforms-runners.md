---
id: software.testes.tranche22.001581
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
fontes: ["https://github.com/reqnroll/Reqnroll/blob/main/README.md", "https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: sistemas, .NETs e quatro executores

## Em uma frase
O Reqnroll roda nos três sistemas operacionais principais (Windows, Linux, macOS) e nas implementações correntes do .NET — do .NET Framework 4.6.2+ até o .NET 10.0 — usando MsTest, NUnit, xUnit ou TUnit como motor de execução.

## Por que importa
Suportar o executor que o time já usa evita migrar suítes inteiras ao adotar BDD; o pacote NuGet do Reqnroll muda de nome conforme o framework, nada mais.

## Como funciona
Escolha o pacote conforme o test framework: Reqnroll.NUnit, Reqnroll.MsTest, Reqnroll.xUnit ou Reqnroll.TUnit; o trabalho diário aceita Visual Studio 2022, VS Code, Rider — ou nenhum IDE, pois o projeto também funciona sem extensão.

## Exemplo
Um projeto net8.0 com Microsoft.NET.Test.Sdk 17.8.0 e MSTest.TestAdapter 3.2.0 convive com PackageReference de Reqnroll.MsTest 2.0.0, como mostra o csproj publicado na guia de migração.

## Limites e trade-offs
O suporte a TUnit é o mais novo dos quatro; listas de compatibilidade de versões antigas do Reqnroll podem não citá-lo, então confira a tabela da sua versão antes de adotar.

## Como verificar
Rode dotnet test em um projeto de exemplo com cada um dos quatro pacotes de executor e observe os cenários aparecerem como testes nativos.

## Conexões
- [[reqnroll-what-it-is]] — Veja também: Reqnroll: BDD Gherkin nativo para .NET.
- [[reqnroll-rename-migration]] — Veja também: Reqnroll: o que muda de nome vindo do SpecFlow.

## Fontes
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
