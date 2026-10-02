---
id: software.testes.tranche11.000518
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
fontes: ["https://docs.locust.io/en/stable/running-distributed.html", "https://docs.locust.io/en/stable/writing-a-locustfile.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: dimensionar master e workers sem atribuir carga ao master

## Em uma frase
Em execução distribuída, master coordena interface e spawn/stop; workers executam Users e enviam estatísticas ao master.

## Por que importa
Locust descreve usuários simulados com tarefas Python e controla concorrência, waits e geração distribuída; a taxa observada depende do tempo das tarefas e da capacidade do gerador. Medir CPU do master como se gerasse requests ou esquecer worker ausente distorce capacidade atribuída ao sistema alvo.

## Como funciona
Modele jornadas com tarefas observáveis, escolha pacing e pesos a partir do workload esperado, normalize nomes de requests e valide que o gerador suporta o volume planejado. Inicie master e workers com versões, locustfiles e conectividade compatíveis; para headless aguarde quantidade esperada de workers.

## Exemplo
Dois workers distribuem usuários enquanto master agrega resultados e aguarda todos conectados antes de iniciar teste headless.

## Limites e trade-offs
HttpUser não é navegador real; resultado do teste combina comportamento da aplicação, cliente e gerador. Wait time não cria usuários para atingir throughput e tarefas podem conter várias requests. Mais workers não garantem escala linear; cada worker, rede e request rate continuam limitantes.

## Como verificar
Observe workers conectados, CPU/memória por nó, taxa gerada e warnings de saturação antes de concluir capacidade do alvo.

## Conexões
- [[locust-loadtestshape-tick]] — Veja também: Locust: codificar estágio de carga via LoadTestShape.
- [[locust-fast-httpuser-gerador-versus-alvo]] — Veja também: Locust: separar limite do gerador do limite do serviço.

## Fontes
- [Locust — Distributed load generation](https://docs.locust.io/en/stable/running-distributed.html) — processos master/worker, distribuição de carga, mensagens e limitações; consultado em 2026-10-02.
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
