---
id: software.testes.tranche11.000512
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

# Locust: interpretar wait_time após tarefa sem tratá-lo como taxa

## Em uma frase
wait_time é aplicado após a execução de uma tarefa; ausência de wait_time inicia a próxima task assim que a atual termina.

## Por que importa
Pausa de tarefa não equivale a pausa entre cada request e não cria usuários para compensar operações lentas.

## Como funciona
Calcule throughput a partir de duração da jornada, requests por task e usuários simultâneos; escolha between/constant com hipótese clara.

## Exemplo
Uma task faz dois GETs e espera 1 segundo ao final, portanto uma iteração ainda contém duas chamadas.

## Limites e trade-offs
Tempo de resposta e ramp-up podem fazer throughput real ficar abaixo do teto especificado pelo pacing.

## Como verificar
Compare RPS medido com número de usuários, duração de task, requests por task e wait configurado.

## Conexões
- [[locust-task-weights-probabilidade]] — Veja também: Locust: interpretar peso de @task como probabilidade relativa.
- [[locust-on-start-stop-lifecycle]] — Veja também: Locust: preparar e liberar estado por usuário no lifecycle.

## Fontes
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
- [Locust — API Reference](https://docs.locust.io/en/stable/api.html) — classes User, HttpUser, TaskSet e helpers de pacing; consultado em 2026-10-02.
