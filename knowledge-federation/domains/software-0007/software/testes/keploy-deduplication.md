---
id: software.testes.tranche20.001393
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://keploy.io/docs/", "https://github.com/keploy/keploy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Keploy: reduzir casos sem perder cobertura

## Em uma frase
A ferramenta aplica deduplicação sobre o tráfego gravado, mantendo um conjunto menor de casos representativos.

## Por que importa
Suítes extensas de gravação crescem sem limite, e a deduplicação mantém o tempo de execução controlado sem descartar caminhos distintos.

## Como funciona
Gere os casos, aplique a deduplicação, revise os casos removidos e mantenha o conjunto versionado enxuto.

## Exemplo
Exercitar o mesmo endpoint com variações repetidas pode produzir um caso representativo em vez de dezenas equivalentes.

## Limites e trade-offs
Deduplicação agressiva pode remover variações de entrada relevantes, e o conjunto reduzido precisa ser ampliado quando um caminho novo for descoberto.

## Como verificar
Compare a cobertura antes e depois da deduplicação e confirme que os caminhos exercitados continuam representados.

## Conexões
- [[keploy-test-assertions]] — Veja também: Keploy: ler e ajustar as verificações geradas.
- [[keploy-coverage-report]] — Veja também: Keploy: medir cobertura da repetição.

## Fontes
- [Keploy — Documentação](https://keploy.io/docs/) — instalação, gravação de tráfego, repetição e integração; consultado em 2026-10-03.
- [Keploy — repositório oficial](https://github.com/keploy/keploy) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
