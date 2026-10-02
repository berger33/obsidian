---
id: software.testes.tranche12.000571
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://testng.org/parameters.html", "https://testng.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: organizar parâmetros XML por escopo

## Em uma frase
`@Parameters` injeta valores declarados no `testng.xml` em métodos de teste ou de configuração que declaram os nomes correspondentes.

## Por que importa
Parâmetros de suite e de test ajudam a variar ambiente ou configuração sem embutir valores em código, mas valores ausentes precisam ter política explícita.

## Como funciona
Mantenha identificadores e defaults claros no XML, associe o nome com a anotação correspondente e use `@Optional` quando a execução realmente puder ocorrer sem aquele valor.

## Exemplo
Uma suíte pode definir uma URL base comum e fornecer uma URL substituta no bloco de teste que aponta para uma instância de staging.

## Limites e trade-offs
Valores de ambiente não devem transportar segredos em XML versionado, e uma substituição pode fazer testes comparáveis usarem endpoints diferentes sem que o relatório destaque a causa.

## Como verificar
Rode o mesmo método com dois blocos `<test>`, inspecione o valor efetivamente recebido e confirme como a execução responde quando o parâmetro opcional não é fornecido.

## Conexões
- [[testng-dataprovider-casos]] — Veja também: TestNG: alinhar DataProvider e assinatura do teste.
- [[testng-dependencies-hard-soft]] — Veja também: TestNG: dependências hard e soft entre testes.

## Fontes
- [TestNG — Parameters](https://testng.org/parameters.html) — parâmetros XML, opções, hierarquia de escopo e data providers; consultado em 2026-10-02.
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
