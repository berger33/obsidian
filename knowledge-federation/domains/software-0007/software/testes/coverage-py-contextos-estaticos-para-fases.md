---
id: software.testes.tranche15.000871
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/contexts.html", "https://coverage.readthedocs.io/en/latest/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: marcar fases de execução com contextos estáticos

## Em uma frase
Contextos estáticos permitem rotular uma medição inteira com uma fase, ambiente ou finalidade, enquanto contextos dinâmicos podem identificar testes individuais.

## Por que importa
Um rótulo como `integration` ou `linux-py314` ajuda a comparar dados de execuções separadas sem confundir o contexto global com a função de teste atual.

## Como funciona
Os relatórios podem selecionar contextos por expressão regular e mostrar quais partes do código foram exercitadas em cada cenário.

## Exemplo
Use `coverage run --context=integration -m pytest` para nomear uma execução de integração e mantenha o rótulo dinâmico de testes se precisar de granularidade por caso.

## Limites e trade-offs
Contexto é metadado de proveniência e não corrige mistura de revisões, versões ou bancos de dados; rotule cada fonte de dados de modo consistente antes de combinar resultados.

## Como verificar
Rode a mesma suíte com dois contextos estáticos e filtre o relatório por cada valor, verificando que a seleção não altera a medição gravada.

## Conexões
- [[coverage-py-contexto-dinamico-por-teste]] — Veja também: coverage.py: associar linhas executadas ao teste que passou por elas.
- [[coverage-py-combinar-dados-de-multiplos-processos]] — Veja também: coverage.py: combinar arquivos paralelos antes de interpretar a cobertura.

## Fontes
- [Coverage.py 7.16.2 — Measurement contexts](https://coverage.readthedocs.io/en/latest/contexts.html) — contextos estáticos e dinâmicos, função de teste e filtros por contexto; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
