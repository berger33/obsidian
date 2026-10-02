---
id: software.testes.tranche10.000448
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

# StrykerJS: investigar timeout antes de alterar o limite

## Em uma frase
A configuração oferece limites temporais para processos de teste e execução de mutants.

## Por que importa
Mutation testing avalia se testes detectam mudanças simuladas no código, complementando cobertura sem provar a correção integral do produto. Um timeout pode sinalizar suíte lenta, deadlock, ambiente congestionado ou comportamento provocado pela mutação.

## Como funciona
Parta de uma execução normal bem-sucedida, delimite arquivos mutáveis e interprete resultados por categoria, coverage analysis e thresholds. Examine logs do mutant e duração do dry run antes de elevar timeout global.

## Exemplo
A equipe reproduz um timeout numa execução isolada e verifica se o mesmo teste demora sem a mutação ativa.

## Limites e trade-offs
Mutants equivalentes, configurações de runner, exclusões e custos de execução afetam score e diagnóstico; não maximize score à custa de assertions sem valor. Aumentar limite pode alongar a CI e ainda ocultar bloqueio real; timers variam com hardware e runner.

## Como verificar
Compare tempo por teste em baseline e mutant e documente mudança de limite com motivo medido.

## Conexões
- [[stryker-static-mutants-pertest-requirement]] — Veja também: StrykerJS: respeitar a exigência de perTest para ignorar static mutants.
- [[stryker-equivalent-mutant-score-interpretacao]] — Veja também: StrykerJS: interpretar sobreviventes sem perseguir score perfeito.

## Fontes
- [StrykerJS — Configuration](https://stryker-mutator.io/docs/stryker-js/configuration/) — mutate, coverage analysis, timeouts, ignore patterns e thresholds; consultado em 2026-10-02.
- [StrykerJS — Introduction](https://stryker-mutator.io/docs/stryker-js/introduction/) — mutação de código, execução da suíte e interpretação de resultados; consultado em 2026-10-02.
