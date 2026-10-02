---
id: software.testes.tranche12.000569
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/api.html", "https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: escolher deadline sem esconder testes lentos

## Em uma frase
O `deadline` limita quanto cada exemplo gerado pode gastar em execução, separando lentidão localizada de um teste que simplesmente consome o orçamento total da suíte.

## Por que importa
Um limite calibrado expõe regressões de desempenho por entrada, enquanto um valor inadequado pode tornar o teste instável em runners mais lentos ou mascarar latência relevante.

## Como funciona
Meça a função representativa, use uma configuração de deadline coerente com a plataforma e aplique alterações apenas ao teste que tem uma razão documentada para exceder o padrão.

## Exemplo
Um parser que leva mais tempo apenas para entradas gigantes pode ganhar uma estratégia dedicada e um orçamento explícito, sem aumentar o prazo de todos os testes do projeto.

## Limites e trade-offs
Remover todos os deadlines não impõe limite ao processo externo e tampouco resolve uma operação bloqueada; limites de CI continuam necessários para impedir jobs presos.

## Como verificar
Compare tempos de exemplos em mais de um runner, ajuste a estratégia que gera o caso caro e confirme que falhas por deadline continuam identificáveis.

## Conexões
- [[hyp-settings-profiles-healthchecks]] — Veja também: Hypothesis: perfis de settings e health checks.

## Fontes
- [Hypothesis — API Reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html) — @given, exemplos, inferência, settings, HealthCheck e configuração pública; consultado em 2026-10-02.
- [Hypothesis — Replaying failures](https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html) — banco de exemplos, replay, @example e @reproduce_failure; consultado em 2026-10-02.
