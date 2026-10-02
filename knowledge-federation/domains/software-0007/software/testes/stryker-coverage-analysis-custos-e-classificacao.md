---
id: software.testes.tranche10.000443
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
fontes: ["https://stryker-mutator.io/docs/stryker-js/configuration/", "https://stryker-mutator.io/docs/stryker-js/guides/create-a-plugin/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: usar coverage analysis para reduzir execuções

## Em uma frase
Coverage analysis pode selecionar quais testes executar para cada mutant e distinguir categorias conforme dados do runner.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Executar a suíte completa por mutant pode tornar mutação inviável em projetos maiores.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Escolha modo all ou perTest conforme o suporte do runner e verifique cobertura reportada no dry run.

## Exemplo
Após mapear testes por linha, Stryker executa somente os testes que cobrem aquele mutant durante a análise.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. A otimização depende do runner fornecer cobertura; configuração incompatível pode alterar classificação e desempenho.

## Como verificar
Compare score e categorias com coverageAnalysis off em um subconjunto pequeno para confirmar que o resultado permanece coerente.

## Conexões
- [[stryker-threshold-break-falha-pipeline]] — Veja também: StrykerJS: usar break threshold para bloquear score baixo.
- [[stryker-incremental-resultados-cache-validade]] — Veja também: StrykerJS: verificar validade de resultados incrementais.

## Fontes
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
- [StrykerJS — Creating a plugin](https://stryker-mutator.io/docs/stryker-js/guides/create-a-plugin/) — instrumentação, dry run, cobertura por teste e execução de mutants; consultado em 2026-10-02.
