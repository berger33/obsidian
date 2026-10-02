---
id: software.testes.tranche11.000486
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

# Cucumber: usar Doc String para payload textual multilinha

## Em uma frase
Gherkin permite Doc Strings como argumento de step para passar texto longo, como JSON, GraphQL ou uma mensagem.

## Por que importa
Escapar payload dentro de uma frase reduz leitura e pode fazer formatação ou caracteres relevantes desaparecerem.

## Como funciona
Delimite o bloco com Doc String e receba-o explicitamente na definição, validando o conteúdo como parte do contrato.

## Exemplo
Um cenário passa body JSON formatado a um step de envio e verifica status e campos de resposta.

## Limites e trade-offs
Doc String fornece texto, não valida automaticamente se o payload é JSON válido nem o transforma no DTO da aplicação.

## Como verificar
Valide parsing e teste caractere especial, newline e campo obrigatório ausente.

## Conexões
- [[cucumber-data-tables-argumento-final]] — Veja também: Cucumber: modelar DataTable como argumento do step.
- [[cucumber-background-precondicao-compartilhada]] — Veja também: Cucumber: limitar Background a contexto comum necessário.

## Fontes
- [Cucumber — Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — estrutura Feature, Rule, Scenario, Background, Outline, tags, steps e argumentos multilinha; consultado em 2026-10-02.
- [Cucumber — Step Definitions](https://cucumber.io/docs/cucumber/step-definitions/) — expressões, correspondência de steps e parâmetros tipados; consultado em 2026-10-02.
