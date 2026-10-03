---
id: software.testes.tranche22.001584
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
fontes: ["https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html", "https://docs.reqnroll.net/latest/automation/cucumber-expressions.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: expressões Cucumber embutidas

## Em uma frase
Os pacotes CucumberExpressions.SpecFlow.* externos não são mais necessários: o Reqnroll traz suporte a Cucumber Expressions embutido, o binding pattern no formato {param} escrito direto no atributo do passo.

## Por que importa
Regex de binding é o ponto onde times novos em BDD mais travam; expressões Cucumber dão um mini-idioma legível ({word}, {int}) que a maioria dos novos cenários aceita sem tocar em regex.

## Como funciona
Declare o passo com [Given("I have {int} cuke(s) in my belly")] e o runtime extrai os argumentos tipados automaticamente, sem grupo de captura manual.

## Exemplo
O guia recomenda remover os pacotes CucumberExpressions.SpecFlow.* exatamente porque o suporte nativo os substitui na migração.

## Limites e trade-offs
Passo ambíguo entre regex antiga e expression nova exige rodar a suíte inteira para descobrir conflitos de binding; a detecção só aparece em tempo de execução.

## Como verificar
Converta um passo regex simples para Cucumber Expression e confirme que o teste continua verde sem editar o feature.

## Conexões
- [[reqnroll-datatable-assist]] — Veja também: Reqnroll: DataTable, assistentes e o container DI.
- [[reqnroll-plugins-actions]] — Veja também: Reqnroll: plugins portados e Actions de automação.

## Fontes
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
- [Reqnroll — Cucumber Expressions](https://docs.reqnroll.net/latest/automation/cucumber-expressions.html) — suporte embutido citado pela guia de migração; consultado em 2026-10-03.
