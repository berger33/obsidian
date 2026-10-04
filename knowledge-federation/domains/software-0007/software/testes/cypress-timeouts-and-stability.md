---
id: software.testes.tranche18.001164
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
fontes: ["https://docs.cypress.io/api/table-of-contents", "https://docs.cypress.io/guides/references/best-practices"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Cypress: ajustar tempos e reduzir instabilidade

## Em uma frase
Limites de tempo podem ser definidos por comando, por asserção ou para toda a configuração, e a espera por condição é preferível a pausas fixas.

## Por que importa
Ambientes de integração contínua são mais lentos, e limites adequados por operação evitam falhas que não indicam defeito real.

## Como funciona
Defina limites na configuração para o caso comum, ajuste pontualmente onde a operação é naturalmente lenta e registre a justificativa.

## Exemplo
Uma consulta a relatório pesado pode precisar de limite maior do que a verificação de um rótulo na tela.

## Limites e trade-offs
Elevar todos os limites uniformemente atrasa o diagnóstico de falhas genuínas e esconde lentidão crescente da aplicação.

## Como verificar
Meça a duração típica de um caso e confirme que o limite está acima do observado com margem justificada.

## Conexões
- [[cypress-custom-commands]] — Veja também: Cypress: extrair comandos próprios.
- [[cypress-debugging-and-artifacts]] — Veja também: Cypress: investigar falhas com artefatos.

## Fontes
- [Cypress — API](https://docs.cypress.io/api/table-of-contents) — comandos, asserções, comandos próprios e opções de execução; consultado em 2026-10-03.
- [Cypress — Best practices](https://docs.cypress.io/guides/references/best-practices) — seletores estáveis, independência entre testes e dados de apoio; consultado em 2026-10-03.
