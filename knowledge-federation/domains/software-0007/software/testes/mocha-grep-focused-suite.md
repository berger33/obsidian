---
id: software.testes.tranche13.000657
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://mochajs.org/running/cli/", "https://mochajs.org/features/parallel-mode/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: filtrar casos sem deixar foco acidental

## Em uma frase
`--grep` seleciona testes pelos títulos correspondentes e pode ser usado para executar um recorte sem alterar a suíte.

## Por que importa
Filtros permitem reproduzir rapidamente uma falha e são mais seguros que deixar `it.only()` no código que será commitado.

## Como funciona
Use um nome completo ou expressão regular que identifique o comportamento, combine com o arquivo quando útil e limpe qualquer suite focada antes de executar a pipeline completa.

## Exemplo
Para investigar apenas casos de renovação, a CLI pode filtrar o título do `describe` e dos exemplos sem mudar as declarações compartilhadas.

## Limites e trade-offs
No modo paralelo, `only` é desabilitado porque arquivos são carregados sob demanda; filtros por CLI continuam sendo a alternativa documentada.

## Como verificar
Rode a mesma seleção local e na CI e confira que pelo menos um teste foi selecionado e que a execução de regressão completa continua incluindo os demais.

## Conexões
- [[mocha-timeout-test-and-hook]] — Veja também: Mocha: dimensionar timeout de teste e hook.
- [[mocha-reporter-parallel-output]] — Veja também: Mocha: combinar reporter com o modo de execução.

## Fontes
- [Mocha — Command-Line Usage](https://mochajs.org/running/cli/) — grep, retries, timeouts, parallel flags and reporter options; consultado em 2026-10-02.
- [Mocha — Parallel Mode](https://mochajs.org/features/parallel-mode/) — workers, nondeterministic file order and parallel-mode limitations; consultado em 2026-10-02.
