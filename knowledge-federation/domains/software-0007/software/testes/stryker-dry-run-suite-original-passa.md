---
id: software.testes.tranche10.000440
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
fontes: ["https://stryker-mutator.io/docs/stryker-js/introduction/", "https://stryker-mutator.io/docs/stryker-js/guides/create-a-plugin/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: exigir dry run verde antes de mutar

## Em uma frase
Stryker executa um dry run sem mutações antes de iniciar a avaliação de mutants.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Se a suíte original já falha ou não inicia, o resultado de mutação não separa defeito preexistente de efeito do mutant.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Corrija falhas de baseline e valide comando, ambiente e runner antes de interpretar score.

## Exemplo
A CI guarda output do dry run e só inicia mutação quando a execução sem alterações termina com sucesso.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Baseline verde não comprova que os testes cobrem todos os comportamentos importantes.

## Como verificar
Quebre deliberadamente um teste original e confirme que a etapa de mutação para ou reporta o dry run como falha.

## Conexões
- [[stryker-killed-survived-no-coverage]] — Veja também: StrykerJS: distinguir killed, survived e no coverage.

## Fontes
- [StrykerJS — Introduction](https://stryker-mutator.io/docs/stryker-js/introduction/) — mutação de código, execução da suíte e interpretação de resultados; consultado em 2026-10-02.
- [StrykerJS — Creating a plugin](https://stryker-mutator.io/docs/stryker-js/guides/create-a-plugin/) — instrumentação, dry run, cobertura por teste e execução de mutants; consultado em 2026-10-02.
