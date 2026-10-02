---
id: software.testes.tranche11.000514
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://docs.locust.io/en/stable/writing-a-locustfile.html#http-client"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: agrupar URLs variáveis com name estável nas estatísticas

## Em uma frase
O parâmetro name do client pode agrupar requests com paths ou query values diferentes sob um nome de estatística comum.

## Por que importa
Ids dinâmicos criam muitas linhas e fragmentam amostras de endpoint, dificultando comparação de latência e erro.

## Como funciona
Use nome estável para rotas equivalentes e preserve ids em logs de diagnóstico sem transformá-los em labels de métrica.

## Exemplo
Requests /item?id=1 a /item?id=10 usam name=/item e aparecem como grupo de endpoint único.

## Limites e trade-offs
Agrupar endpoints funcionalmente distintos sob o mesmo nome também esconde comportamento divergente.

## Como verificar
Confira que cada grupo de estatística corresponde a um contrato/rota comparável e que a cardinalidade diminuiu sem perder distinções necessárias.

## Conexões
- [[locust-on-start-stop-lifecycle]] — Veja também: Locust: preparar e liberar estado por usuário no lifecycle.
- [[locust-catch-response-validacao-manual]] — Veja também: Locust: marcar resposta manualmente com catch_response.

## Fontes
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
- [Locust — Using the HTTP client](https://docs.locust.io/en/stable/writing-a-locustfile.html#http-client) — response context, validação manual e cliente HTTP sem browser; consultado em 2026-10-02.
