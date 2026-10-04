---
id: software.testes.tranche10.000444
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://stryker-mutator.io/docs/stryker-js/incremental/", "https://stryker-mutator.io/docs/stryker-js/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: verificar validade de resultados incrementais

## Em uma frase
Incremental mode reutiliza resultados quando arquivos mutados e testes não mudaram segundo o diff que o runner suporta.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Cache desatualizado pode associar resultado passado a código ou teste, e o modo não detecta toda mudança ambiental.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Use o arquivo incremental como artefato de cache apropriado e force execução ampla quando dependências, variáveis, snapshots ou configuração fora do diff mudarem.

## Exemplo
A CI registra mutants reutilizados, mantém o dry run e agenda periodicamente uma análise limpa para comparar resultados.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Stryker não detecta alterações em todos os arquivos nem em dependências, variáveis de ambiente e snapshots; suporte também depende do runner.

## Como verificar
Compare uma execução incremental com execução limpa após mudança relevante fora do código mutado/testado e investigue divergência de resultado.

## Conexões
- [[stryker-coverage-analysis-custos-e-classificacao]] — Veja também: StrykerJS: usar coverage analysis para reduzir execuções.
- [[stryker-mutate-apenas-codigo-de-producao]] — Veja também: StrykerJS: delimitar mutate a código de produção.

## Fontes
- [StrykerJS — Incremental mode](https://stryker-mutator.io/docs/stryker-js/incremental/) — resultados anteriores e execução incremental de mutants; consultado em 2026-10-02.
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
