---
id: software.testes.tranche16.001016
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://googlechrome.github.io/lighthouse-ci/docs/configuration.html", "https://github.com/GoogleChrome/lighthouse-ci"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Lighthouse CI: escolher conjuntos de asserções

## Em uma frase
A verificação aceita um conjunto pré-definido de regras e permite desligar ou ajustar itens específicos, com nível de erro ou aviso.

## Por que importa
Um conjunto pronto cobre muitas verificações de uma vez, mas itens irrelevantes para o projeto precisam ser desligados de forma consciente.

## Como funciona
Estenda um conjunto recomendado, desligue auditorias que não se aplicam ao contexto e mantenha o restante como erro para produzir sinal claro.

## Exemplo
Um painel autenticado pode desligar verificações de rastreamento enquanto mantém erros para acessibilidade e desempenho.

## Limites e trade-offs
Desligar itens demais esvazia a verificação, e manter tudo como erro gera bloqueio por questões fora do controle do time.

## Como verificar
Liste as asserções avaliadas na última execução e confirme que as desligadas têm justificativa registrada na configuração.

## Conexões
- [[lighthouseci-number-of-runs]] — Veja também: Lighthouse CI: reduzir variação com repetições.
- [[lighthouseci-numeric-assertions]] — Veja também: Lighthouse CI: definir limites numéricos e agregação.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
