---
id: software.testes.tranche15.000870
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

# coverage.py: associar linhas executadas ao teste que passou por elas

## Em uma frase
Coverage.py pode registrar contexto dinâmico para identificar qual função de teste executou cada linha, indo além do total agregado de cobertura.

## Por que importa
O contexto torna possível localizar linhas cobertas por um teste específico ou filtrar relatórios por contexto; `dynamic_context = test_function` é uma configuração suportada para atribuir o contexto ao teste ativo.

## Como funciona
Essa associação explica proveniência de execução, não se o teste fez uma asserção útil.

## Exemplo
Ative `dynamic_context = test_function` na configuração do coverage.py e execute a suíte normalmente; depois use opções de relatório por contexto para comparar caminhos exercitados por casos diferentes.

## Limites e trade-offs
O formato e a integração dependem de como o runner de testes delimita as funções; uma linha coberta por um caso ainda pode ser coberta sem verificar seu efeito observável.

## Como verificar
Faça um exemplo mínimo com dois testes que percorrem ramos distintos, gere o relatório separado por contexto e confirme que cada linha aparece apenas nos contextos que a executaram.

## Conexões
- [[coverage-py-contextos-estaticos-para-fases]] — Veja também: coverage.py: marcar fases de execução com contextos estáticos.

## Fontes
- [Coverage.py 7.16.2 — Measurement contexts](https://coverage.readthedocs.io/en/latest/contexts.html) — contextos estáticos e dinâmicos, função de teste e filtros por contexto; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
