---
id: software.testes.tranche10.000447
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
fontes: ["https://stryker-mutator.io/docs/stryker-js/configuration/", "https://stryker-mutator.io/docs/mutation-testing-elements/static-mutants/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: respeitar a exigência de perTest para ignorar static mutants

## Em uma frase
StrykerJS exige coverageAnalysis perTest para ignoreStatic; mutants estáticos ignorados aparecem como Ignored e não contam no mutation score.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Mutants estáticos executam durante o carregamento do módulo; ignorá-los reduz custo, mas também reduz o conjunto efetivamente testado.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Se a decisão de escopo for ignorar static mutants, configure coverageAnalysis perTest, habilite ignoreStatic e confira a categoria Ignored no relatório.

## Exemplo
Com coverageAnalysis: perTest e ignoreStatic: true, um run pequeno mostra os mutants estáticos ignorados como Ignored, fora do mutation score e ainda visíveis no relatório.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Ignorar estáticos troca abrangência por custo; Ignored não é No coverage, que significa mutant sem cobertura e ainda undetected. Mutants híbridos com cobertura runtime seguem o comportamento de mutants runtime.

## Como verificar
Em um ambiente controlado, confirme o diagnóstico da versão adotada ao combinar ignoreStatic com um modo diferente de perTest; depois inspecione Ignored, No coverage e o escopo do score.

## Conexões
- [[stryker-ignore-mutant-justificado-e-visivel]] — Veja também: StrykerJS: ignorar somente mutant não testável com justificativa.
- [[stryker-timeout-investigar-runner-e-mutante]] — Veja também: StrykerJS: investigar timeout antes de alterar o limite.

## Fontes
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
- [Stryker — Static mutants](https://stryker-mutator.io/docs/mutation-testing-elements/static-mutants/) — execução/ignorância de static mutants, estado Ignored e efeito no mutation score; consultado em 2026-10-02.
