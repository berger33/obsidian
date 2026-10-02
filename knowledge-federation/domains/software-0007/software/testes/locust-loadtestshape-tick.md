---
id: software.testes.tranche11.000517
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
fontes: ["https://docs.locust.io/en/stable/_modules/locust/shape.html", "https://docs.locust.io/en/stable/api.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: codificar estágio de carga via LoadTestShape

## Em uma frase
LoadTestShape permite controlar usuários e spawn rate através de tick, que retorna a população desejada e pode terminar com None.

## Por que importa
Perfil estático não reproduz sempre pico, queda e recuperação que motivam o experimento de capacidade.

## Como funciona
Codifique estágios com duração e população declaradas e registre tempo decorrido usando API da shape.

## Exemplo
A shape mantém baseline, ramp-up, pico limitado e ramp-down antes de devolver None para parar execução.

## Limites e trade-offs
tick é chamado periodicamente pelo runner e mudanças de usuários ficam limitadas ao spawn rate; shape não garante RPS exato.

## Como verificar
Compare população solicitada e observada por estágio e valide que a shape encerra no tempo esperado.

## Conexões
- [[locust-taskset-sequencia-de-tarefas]] — Veja também: Locust: escolher TaskSet para comportamento hierárquico ou sequência.
- [[locust-distributed-master-worker]] — Veja também: Locust: dimensionar master e workers sem atribuir carga ao master.

## Fontes
- [Locust 2.46 — LoadTestShape API/source](https://docs.locust.io/en/stable/_modules/locust/shape.html) — contrato de tick, contagem total de usuários, spawn rate e encerramento com None; consultado em 2026-10-02.
- [Locust — API Reference](https://docs.locust.io/en/stable/api.html) — classes User, HttpUser, TaskSet e helpers de pacing; consultado em 2026-10-02.
