---
id: software.testes.tranche22.001580
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

# Reqnroll: BDD Gherkin nativo para .NET

## Em uma frase
O Reqnroll é uma ferramenta open-source de automação de testes .NET para praticar BDD: um porte para .NET do Cucumber, baseado no framework e no codebase do SpecFlow, que transforma especificações em *feature files* Gherkin em testes automatizados.

## Por que importa
Times que escrevem Given-When-Then em feature files precisam de um executor .NET mantido ativamente; o Reqnroll nasceu exatamente porque o SpecFlow saiu de manutenção aberta.

## Como funciona
Escreva cenários Gherkin como especificações executáveis e ligue os passos a código de teste que roda sobre um framework de execução convencional.

## Exemplo
Um cenário "Given um carrinho vazio When adiciono um item Then o total é 1" é compilado em teste .NET executável pela suíte, sem tradutor artesanal.

## Limites e trade-offs
Por herdar o codebase do SpecFlow, a compatibilidade é alta, mas nomes e namespaces mudaram — a documentação frisa que "o que funcionava no SpecFlow funciona no Reqnroll, só com nomes diferentes".

## Como verificar
Gere um projeto de exemplo pela rota rápida apontada no README e confirme que o gerador produz os partial classes de teste a partir do .feature.

## Conexões
- [[reqnroll-platforms-runners]] — Veja também: Reqnroll: sistemas, .NETs e quatro executores.

## Fontes
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
