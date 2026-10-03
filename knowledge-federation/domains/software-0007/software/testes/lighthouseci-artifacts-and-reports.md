---
id: software.testes.tranche16.001021
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

# Lighthouse CI: consumir resultados e relatórios locais

## Em uma frase
A coleta grava relatórios e um manifesto no diretório de resultados, e há comando para abrir as páginas geradas localmente.

## Por que importa
Guardar o relatório da execução permite investigar falha sem repetir a medição e comparar a evolução da página entre revisões.

## Como funciona
Preserve o diretório de resultados como artefato, abra os relatórios localmente durante o ajuste e referencie-os na revisão que introduziu a mudança.

## Exemplo
Ao investigar queda de pontuação, o relatório detalhado da execução original mostra qual auditoria mudou e em que elemento.

## Limites e trade-offs
Relatórios acumulados ocupam espaço e podem desatualizar; a política de retenção deve priorizar execuções falhas e marcos de revisão.

## Como verificar
Baixe o artefato de uma execução e localize no relatório a auditoria responsável pela diferença observada.

## Conexões
- [[lighthouseci-config-file]] — Veja também: Lighthouse CI: versionar a configuração.
- [[lighthouseci-limits-in-ci]] — Veja também: Lighthouse CI: interpretar limites em ambiente compartilhado.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
