---
id: software.testes.tranche10.000446
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
fontes: ["https://stryker-mutator.io/docs/stryker-js/disable-mutants/", "https://stryker-mutator.io/docs/stryker-js/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: ignorar somente mutant não testável com justificativa

## Em uma frase
Stryker permite excluir mutators, usar comentários disable ou plugins ignore para padrões específicos.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Exclusão ampla pode elevar score sem que testes melhores tenham sido escritos.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Prefira justificativa local e específica e mantenha mutant ignorado visível no relatório para revisão posterior.

## Exemplo
Uma linha marca EqualityOperator como desabilitado porque a comparação é invariável por contrato e referencia a justificativa no código.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Mutants ignorados não entram no score, mas ainda representam decisões de escopo que precisam de manutenção.

## Como verificar
Revise lista de mutantes ignorados no diff e confirme que comentário ou plugin aponta uma razão verificável.

## Conexões
- [[stryker-mutate-apenas-codigo-de-producao]] — Veja também: StrykerJS: delimitar mutate a código de produção.
- [[stryker-static-mutants-pertest-requirement]] — Veja também: StrykerJS: respeitar a exigência de perTest para ignorar static mutants.

## Fontes
- [StrykerJS — Disable mutants](https://stryker-mutator.io/docs/stryker-js/disable-mutants/) — exclusão de mutators, comentários e plugins de ignore; consultado em 2026-10-02.
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
