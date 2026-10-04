---
id: software.testes.tranche22.001587
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

# Reqnroll: Scenario Outlines sob MsTest geram testes data-driven

## Em uma frase
Com MsTest, o Reqnroll gera testes data-driven a partir de Scenario Outlines, e isso pode conflitar com tooling que filtra por nome — VSTest pipeline task e VSTest.Console.exe entre eles; a guia documenta a incompatibilidade e o caminho para voltar ao comportamento compatível com SpecFlow.

## Por que importa
O trap é silencioso: no CI o pipeline pode deixar de executar execuções filhas dos outlines e o time achar que rodou tudo; quem vem do SpecFlow com MsTest precisa checar exatamente isso.

## Como funciona
Leia a seção "MsTest Scenario Outline Handling" da guia antes do primeiro merge e aplique a configuração de compatibilidade se seu filtro do VSTest depende de nomes de método.

## Exemplo
A recomendação do projeto é migrar direto para a versão mais atual do Reqnroll (exemplo citado: v2.0), porque a experiência de migração e esses cantos vão sendo corrigidos entre releases.

## Limites e trade-offs
Com NUnit ou xUnit o problema descrito não se aplica da mesma forma; a seção é específica ao modelo data-driven do MsTest.

## Como verificar
Force um filtro de nome no VSTest contra um outline com três Examples e conte quantos casos filhos efetivamente rodam.

## Conexões
- [[reqnroll-livingdoc]] — Veja também: Reqnroll: Living Documentation ficou de fora.
- [[reqnroll-license-sponsors]] — Veja também: Reqnroll: licença, patrocínio e linhagem.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
