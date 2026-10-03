---
id: software.testes.tranche18.001163
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
fontes: ["https://docs.cypress.io/api/table-of-contents", "https://github.com/cypress-io/cypress"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: extrair comandos próprios

## Em uma frase
É possível registrar comandos personalizados e sobrescrever comandos existentes, reunindo sequências repetidas em uma operação nomeada.

## Por que importa
Fluxos usados por muitos testes ficam definidos em um ponto único, facilitando ajustes quando a interface muda.

## Como funciona
Registre o comando com nome descritivo, receba parâmetros explícitos e componha a partir de comandos existentes em vez de manipular o navegador diretamente.

## Exemplo
Um comando de acesso pode encapsular o preenchimento de credenciais e a verificação da tela inicial.

## Limites e trade-offs
Comandos próprios que engolem falhas escondem problemas, e a sobrescrita de comandos nativos dificulta entender o comportamento em depuração.

## Como verificar
Altere o comando próprio e confirme que todos os testes que o usam passam a refletir a mudança sem edição individual.

## Conexões
- [[cypress-fixtures]] — Veja também: Cypress: servir dados com arquivos de apoio.
- [[cypress-timeouts-and-stability]] — Veja também: Cypress: ajustar tempos e reduzir instabilidade.

## Fontes
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
- [Cypress — repositório oficial](https://github.com/cypress-io/cypress) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
