---
id: software.testes.tranche11.000481
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://cucumber.io/docs/gherkin/reference/", "https://cucumber.io/docs/cucumber/step-definitions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: não tratar Given When Then como namespaces de step

## Em uma frase
A palavra Given, When ou Then dá semântica ao texto, mas não é usada por Cucumber para distinguir step definitions durante matching.

## Por que importa
Definir “Given user exists” e “Then user exists” como métodos diferentes pode criar ambiguidade quando o texto após keyword é igual.

## Como funciona
Use texto de step distinto e expressão de domínio precisa; deixe a palavra-chave comunicar papel narrativo, não despacho de código.

## Exemplo
A suíte tem um único step definition para “a conta possui saldo de 50” mesmo quando cenário o usa como contexto ou resultado.

## Limites e trade-offs
A recomendação de reutilizar expressão não exige que toda frase curta do domínio compartilhe método com efeitos diferentes.

## Como verificar
Faça discovery e confirme que os steps da feature resolvem a exatamente uma implementação intencional.

## Conexões
- [[cucumber-feature-scenario-executable-spec]] — Veja também: Cucumber: escrever Feature e Example como regra verificável.
- [[cucumber-expressions-parametros-tipados]] — Veja também: Cucumber: converter parâmetros de expressão para tipos de domínio.

## Fontes
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
- [Cucumber — Step Definitions](https://cucumber.io/docs/cucumber/step-definitions/) — expressões, correspondência de steps e parâmetros tipados; consultado em 2026-10-02.
