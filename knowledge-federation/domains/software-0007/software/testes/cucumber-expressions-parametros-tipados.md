---
id: software.testes.tranche11.000482
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
fontes: ["https://cucumber.io/docs/cucumber/step-definitions/", "https://cucumber.io/docs/cucumber/cucumber-expressions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cucumber: converter parâmetros de expressão para tipos de domínio

## Em uma frase
Step definitions podem usar Cucumber Expressions ou regular expressions e receber valores capturados como argumentos.

## Por que importa
Parsing manual de números, datas e enums em cada método repete lógica e deixa formatos inválidos produzirem erros pouco localizados.

## Como funciona
Use parâmetros integrados ou tipos registrados para converter texto ao tipo necessário antes de executar o método.

## Exemplo
A expressão “tenho {int} itens” passa inteiro à definição; um valor textual que não corresponde não alcança essa implementação.

## Limites e trade-offs
Conversão automática depende do tipo e da expressão registrada; formatação localizada pode exigir parâmetro customizado explícito.

## Como verificar
Teste valores válidos, limites e texto inválido e confirme erro de matching ou transformação antes da regra de negócio.

## Conexões
- [[cucumber-keywords-nao-fazem-parte-do-matching]] — Veja também: Cucumber: não tratar Given When Then como namespaces de step.
- [[cucumber-step-definitions-ambiguos-unicos]] — Veja também: Cucumber: impedir step definitions ambíguos e duplicados.

## Fontes
- [Cucumber — Step Definitions](https://cucumber.io/docs/cucumber/step-definitions/) — expressões, correspondência de steps e parâmetros tipados; consultado em 2026-10-02.
- [Cucumber — Cucumber Expressions](https://cucumber.io/docs/cucumber/cucumber-expressions/) — parâmetros nomeados, tipos integrados e expressões de step; consultado em 2026-10-02.
