---
id: software.testes.tranche18.001162
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://docs.cypress.io/guides/references/best-practices", "https://docs.cypress.io/api/table-of-contents"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: servir dados com arquivos de apoio

## Em uma frase
Os arquivos de apoio guardam dados de teste e podem alimentar respostas simuladas ou servir de origem para o estado inicial do cenário.

## Por que importa
Dados versionados junto da suíte tornam o cenário determinístico e permitem revisar a evolução do que é esperado.

## Como funciona
Organize um arquivo por contexto, referencie pelo nome e mantenha os dados pequenos e legíveis.

## Exemplo
Um cenário de listagem pode usar arquivo com três produtos, permitindo verificar ordenação e formatação de forma explícita.

## Limites e trade-offs
Arquivos grandes dificultam a leitura e escondem dependências entre campos, e apoiar-se em dados implícitos do ambiente reduz a reprodutibilidade.

## Como verificar
Substitua um arquivo por versão com menos itens e confirme que o teste falha exatamente nas verificações que dependem deles.

## Conexões
- [[cypress-selectors-and-testids]] — Veja também: Cypress: escolher seletores estáveis.
- [[cypress-custom-commands]] — Veja também: Cypress: extrair comandos próprios.

## Fontes
- [Cypress — Best practices](https://docs.cypress.io/guides/references/best-practices) — seletores estáveis, independência entre testes e dados de apoio; consultado em 2026-10-03.
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
