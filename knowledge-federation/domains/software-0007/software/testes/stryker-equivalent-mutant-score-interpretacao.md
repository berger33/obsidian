---
id: software.testes.tranche10.000449
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
fontes: ["https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/", "https://stryker-mutator.io/docs/stryker-js/disable-mutants/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: interpretar sobreviventes sem perseguir score perfeito

## Em uma frase
Mutation score resume resultados de mutants no escopo selecionado, mas não classifica automaticamente equivalência semântica.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Forçar teste para matar todo sobrevivente pode levar a assertions sobre detalhe irrelevante ou comportamento impossível de distinguir.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Investigue o efeito observável do mutant, fortaleça teste quando necessário e documente exclusão justificada quando a mutação for equivalente.

## Exemplo
Um mutant que troca operador em ramo inalcançável é analisado com requisito e domínio de entrada antes de se criar assertion artificial.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Equivalência é difícil de provar automaticamente e a pontuação não substitui revisão do modelo de comportamento.

## Como verificar
Revise sobreviventes com código, requisitos e conjunto de entradas válidas; registre decisão para não reabrir o mesmo falso objetivo.

## Conexões
- [[stryker-timeout-investigar-runner-e-mutante]] — Veja também: StrykerJS: investigar timeout antes de alterar o limite.

## Fontes
- [Stryker — Mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/) — estados killed, survived, No coverage, Ignored e inclusão no mutation score; consultado em 2026-10-02.
- [StrykerJS — Disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/) — exclusão de mutators, comentários e plugins de ignore; consultado em 2026-10-02.
