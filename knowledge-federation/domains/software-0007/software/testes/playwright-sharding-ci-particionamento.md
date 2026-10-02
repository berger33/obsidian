---
id: software.testes.tranche12.000553
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://playwright.dev/docs/test-sharding", "https://playwright.dev/docs/test-reporters#blob-reporter"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright Test: particionamento por shards na CI

## Em uma frase
O parâmetro `--shard=x/y` seleciona uma parte da suíte, permitindo distribuir a execução entre jobs independentes.

## Por que importa
Sharding reduz o tempo de feedback quando a suíte cresce, mas exige dividir um conjunto estável de testes e recombinar evidências produzidas em workers diferentes.

## Como funciona
Escolha um total de shards compatível com a capacidade dos agentes, use `fullyParallel` quando precisar dividir no nível de testes em vez de arquivos, e guarde os artefatos de cada job para consolidação.

## Exemplo
Uma pipeline pode iniciar quatro jobs com shards 1/4 até 4/4 e combinar seus relatórios blob após todos terminarem.

## Limites e trade-offs
Arquivos de duração desigual podem deixar shards desbalanceados quando a divisão é por arquivo. Repetir a suíte completa em cada job invalida o ganho e pode mascarar resultados duplicados.

## Como verificar
Execute uma amostra com todos os shards, confira que nenhum teste esperado ficou ausente ou repetido e só então compare duração e relatório agregado com o job sem partição.

## Conexões
- [[playwright-webserver-readiness-reuse]] — Veja também: Playwright Test: prontidão do servidor local.
- [[playwright-visual-snapshots-baseline]] — Veja também: Playwright Test: snapshots visuais e baseline.

## Fontes
- [Playwright — Sharding](https://playwright.dev/docs/test-sharding) — particionamento por shard, granularidade de testes e merge de relatórios blob; consultado em 2026-10-02.
- [Playwright — Blob reporter](https://playwright.dev/docs/test-reporters#blob-reporter) — artefatos blob para combinar resultados de execuções particionadas; consultado em 2026-10-02.
