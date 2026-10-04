---
id: software.testes.tranche10.000441
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
fontes: ["https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/", "https://stryker-mutator.io/docs/stryker-js/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# StrykerJS: distinguir killed, survived e no coverage

## Em uma frase
Killed indica que um teste falhou com o mutant ativo; survived e No coverage são undetected, enquanto Ignored é excluído intencionalmente da avaliação.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Confundir ausência de cobertura com exclusão intencional esconde se falta um caminho de teste ou se o mutant foi retirado do escopo.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Leia o estado e as métricas separadamente: No coverage significa que o mutant não foi coberto e conta como undetected; Ignored não foi testado por exclusão e não conta contra o mutation score.

## Exemplo
O relatório mostra um operador Survived, um campo No coverage e um mutant Ignored: os dois primeiros são undetected, mas o último está fora do score por decisão explícita.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. No coverage depende da análise de cobertura configurada; Ignored pode refletir ação do usuário ou outra razão e reduz o escopo comparável do score.

## Como verificar
Compare as contagens de estados, cobertura e ignored no relatório e confira a configuração e o escopo de mutants antes de interpretar o score.

## Conexões
- [[stryker-dry-run-suite-original-passa]] — Veja também: StrykerJS: exigir dry run verde antes de mutar.
- [[stryker-threshold-break-falha-pipeline]] — Veja também: StrykerJS: usar break threshold para bloquear score baixo.

## Fontes
- [Stryker — Mutant states and metrics](https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/) — estados killed, survived, No coverage, Ignored e inclusão no mutation score; consultado em 2026-10-02.
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
