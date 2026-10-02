---
id: software.testes.tranche10.000442
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
fontes: ["https://stryker-mutator.io/docs/stryker-js/configuration/", "https://stryker-mutator.io/docs/stryker-js/introduction/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: usar break threshold para bloquear score baixo

## Em uma frase
Thresholds high e low classificam a pontuação, enquanto break pode fazer a execução terminar com erro abaixo do limite.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Sem break threshold, um score baixo pode aparecer apenas como relatório informativo e não bloquear CI.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Escolha limites graduais por criticidade e configure break somente quando a política de build for explícita.

## Exemplo
O projeto publica scores em níveis high/low e reprova o job se o mutation score cair abaixo do break acordado.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Score depende do escopo de mutação, runner e mutants excluídos; não compare projetos como se fossem equivalentes.

## Como verificar
Force um conjunto pequeno de testes a deixar mutant sobreviver e confirme a saída e o status da pipeline.

## Conexões
- [[stryker-killed-survived-no-coverage]] — Veja também: StrykerJS: distinguir killed, survived e no coverage.
- [[stryker-coverage-analysis-custos-e-classificacao]] — Veja também: StrykerJS: usar coverage analysis para reduzir execuções.

## Fontes
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
- [StrykerJS — Introduction](https://stryker-mutator.io/docs/stryker-js/introduction/) — mutação de código, execução da suíte e interpretação de resultados; consultado em 2026-10-02.
