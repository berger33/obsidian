---
id: software.testes.tranche11.000511
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
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://docs.locust.io/en/stable/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: interpretar peso de @task como probabilidade relativa

## Em uma frase
Decorador @task com peso faz Locust escolher tarefas com frequência relativa entre as opções disponíveis do usuário.

## Por que importa
Peso 3 não significa três chamadas HTTP nem taxa exata de 3 requests por segundo; a tarefa pode executar múltiplas operações.

## Como funciona
Modele proporção de jornadas no nível de tarefa e considere duração, wait_time e número de requests dentro de cada método.

## Exemplo
Tarefa view_item peso 3 é mais provável que checkout peso 1, mas checkout pode disparar várias requests.

## Limites e trade-offs
Frequência observada varia com duração e estado das tarefas e representa distribuição aproximada, não sequência rígida.

## Como verificar
Rode amostra longa e compare proporções de tasks e requests com o workload desejado.

## Conexões
- [[locust-httpuser-nao-e-browser]] — Veja também: Locust: não confundir HttpUser com navegador real.
- [[locust-wait-time-pos-task-nao-rps]] — Veja também: Locust: interpretar wait_time após tarefa sem tratá-lo como taxa.

## Fontes
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
- [Locust — API Reference](https://docs.locust.io/en/stable/api.html) — classes User, HttpUser, TaskSet e helpers de pacing; consultado em 2026-10-02.
