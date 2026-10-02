---
id: software.testes.tranche11.000513
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

# Locust: preparar e liberar estado por usuário no lifecycle

## Em uma frase
on_start e on_stop são callbacks por instância de User que permitem iniciar e encerrar contexto do usuário simulado.

## Por que importa
Locust descreve usuários simulados com tarefas Python e controla concorrência, waits e geração distribuída; a taxa observada depende do tempo das tarefas e da capacidade do gerador. Repetir login dentro de cada tarefa altera o workload e pode inflar tráfego de autenticação de forma não pretendida.

## Como funciona
Modele jornadas com tarefas observáveis, escolha pacing e pesos a partir do workload esperado, normalize nomes de requests e valide que o gerador suporta o volume planejado. Use on_start para sessão ou autenticação quando isso modelar a jornada, e on_stop para liberar contexto local sem efeito caro inesperado.

## Exemplo
Cada usuário autentica uma vez em on_start e executa tarefas de leitura; encerramento limpa recurso local do cliente.

## Limites e trade-offs
HttpUser não é navegador real; resultado do teste combina comportamento da aplicação, cliente e gerador. Wait time não cria usuários para atingir throughput e tarefas podem conter várias requests. Callback pode ser chamado em lifecycle de carga interrompida e não substitui cleanup de recursos externos à sessão.

## Como verificar
Contabilize chamadas de autenticação e verifique comportamento durante graceful stop e falha no início.

## Conexões
- [[locust-wait-time-pos-task-nao-rps]] — Veja também: Locust: interpretar wait_time após tarefa sem tratá-lo como taxa.
- [[locust-request-name-cardinalidade]] — Veja também: Locust: agrupar URLs variáveis com name estável nas estatísticas.

## Fontes
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
- [Locust — API Reference](https://docs.locust.io/en/stable/api.html) — classes User, HttpUser, TaskSet e helpers de pacing; consultado em 2026-10-02.
