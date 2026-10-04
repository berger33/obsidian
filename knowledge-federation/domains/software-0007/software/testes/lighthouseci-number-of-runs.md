---
id: software.testes.tranche16.001015
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

# Lighthouse CI: reduzir variação com repetições

## Em uma frase
A configuração permite repetir a auditoria várias vezes por página e consolidar o resultado, geralmente pelo valor mediano.

## Por que importa
Métricas de laboratório variam entre execuções, e uma única medição produz diferença que não corresponde a mudança real.

## Como funciona
Faça algumas repetições por página, mantenha o valor consolidado como referência e compare sempre medições produzidas no mesmo ambiente.

## Exemplo
Três execuções por página costumam reduzir oscilações de rede e de aquecimento sem alongar demais o tempo total.

## Limites e trade-offs
Repetir não elimina variação estrutural do executor, e em máquinas com poucos recursos a mediana ainda carrega o custo do ambiente.

## Como verificar
Compare os valores individuais das repetições com o consolidado e observe a dispersão antes de confiar em diferenças pequenas.

## Conexões
- [[lighthouseci-collect-targets]] — Veja também: Lighthouse CI: definir páginas e servidor de coleta.
- [[lighthouseci-assertions-presets]] — Veja também: Lighthouse CI: escolher conjuntos de asserções.

## Fontes
- [Lighthouse CI — Configuration](https://googlechrome.github.io/lighthouse-ci/docs/configuration.html) — seções collect, assert e upload, presets, asserções e orçamentos; consultado em 2026-10-03.
- [Lighthouse CI — repositório oficial](https://github.com/GoogleChrome/lighthouse-ci) — comandos, integração contínua e documentação do projeto; consultado em 2026-10-03.
