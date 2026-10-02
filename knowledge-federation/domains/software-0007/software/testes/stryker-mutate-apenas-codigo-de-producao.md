---
id: software.testes.tranche10.000445
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

# StrykerJS: delimitar mutate a código de produção

## Em uma frase
A opção mutate seleciona arquivos e padrões sujeitos a alterações artificiais.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Mutar testes, bundles gerados ou código sem comportamento relevante desperdiça execução e distorce score.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Inclua fontes de produção e exclua specs, fixtures e artefatos com padrões legíveis e revisados.

## Exemplo
O projeto muta src/**/*.ts e exclui *.spec.ts, código gerado e adaptadores fora do escopo.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Glob incorreto pode omitir módulos importantes ou incluir arquivo que o runner não consegue transformar.

## Como verificar
Inspecione a lista de arquivos e mutants produzidos em uma execução pequena antes de rodar a suíte inteira.

## Conexões
- [[stryker-incremental-resultados-cache-validade]] — Veja também: StrykerJS: verificar validade de resultados incrementais.
- [[stryker-ignore-mutant-justificado-e-visivel]] — Veja também: StrykerJS: ignorar somente mutant não testável com justificativa.

## Fontes
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
- [StrykerJS — Introduction](https://stryker-mutator.io/docs/stryker-js/introduction/) — mutação de código, execução da suíte e interpretação de resultados; consultado em 2026-10-02.
