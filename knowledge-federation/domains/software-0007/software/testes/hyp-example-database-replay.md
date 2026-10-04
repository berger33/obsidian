---
id: software.testes.tranche12.000567
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
fontes: ["https://hypothesis.readthedocs.io/en/latest/reference/api.html#hypothesis.database.ExampleDatabase", "https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hypothesis: banco persistente para replay de falhas

## Em uma frase
O banco de exemplos guarda entradas que Hypothesis encontrou e pode reutilizá-las em execuções posteriores da mesma configuração.

## Por que importa
Replay acelera a confirmação de falhas já observadas e ajuda a manter a descoberta útil entre execuções, sem exigir que cada valor seja escrito manualmente no teste.

## Como funciona
Deixe a configuração de banco consistente no ambiente de desenvolvimento e CI, observe os artefatos de cache e preserve em versionamento apenas regressões que precisam ser explícitas no contrato do repositório.

## Exemplo
Uma entrada minimizada que revelou falha pode reaparecer no próximo `pytest` com Hypothesis, mesmo quando a busca aleatória não a sorteia de imediato.

## Limites e trade-offs
O banco é um cache mutável de exemplos, não uma especificação de cobertura nem garantia de que um comportamento correto foi provado. Apagá-lo pode mudar quais casos aparecem primeiro.

## Como verificar
Reproduza a falha com o banco presente e depois com uma estratégia de teste limpa para distinguir replay de exemplo persistido da cobertura normal da propriedade.

## Conexões
- [[hyp-example-regressao-explicito]] — Veja também: Hypothesis: adicionar regressões com `@example`.
- [[hyp-settings-profiles-healthchecks]] — Veja também: Hypothesis: perfis de settings e health checks.

## Fontes
- [Hypothesis — ExampleDatabase API](https://hypothesis.readthedocs.io/en/latest/reference/api.html#hypothesis.database.ExampleDatabase) — persistência, replay e política de cache do banco de exemplos; consultado em 2026-10-02.
- [Hypothesis — Replaying failures](https://hypothesis.readthedocs.io/en/latest/tutorial/replaying-failures.html) — banco de exemplos, replay, @example e @reproduce_failure; consultado em 2026-10-02.
