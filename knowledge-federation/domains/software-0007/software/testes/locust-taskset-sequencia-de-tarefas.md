---
id: software.testes.tranche11.000516
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
fontes: ["https://docs.locust.io/en/stable/tasksets.html", "https://docs.locust.io/en/stable/writing-a-locustfile.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: escolher TaskSet para comportamento hierárquico ou sequência

## Em uma frase
TaskSet organiza conjunto de tarefas e pode delegar para subtasksets; SequentialTaskSet expressa sequência declarada quando a jornada requer ordem.

## Por que importa
Um conjunto plano de tasks pode gerar transições impossíveis, enquanto ordem rígida aplicada ao usuário inteiro reduz variabilidade sem justificativa.

## Como funciona
Use TaskSet para subfluxo coerente e SequentialTaskSet somente quando próxima etapa depende da ordem explícita.

## Exemplo
Usuário autentica, navega seção e encerra subfluxo antes de voltar à jornada principal.

## Limites e trade-offs
TaskSet não implementa máquina de estados de negócio automaticamente; transições e interrupção ainda precisam ser definidas.

## Como verificar
Observe logs de sequência e confirme que o modelo não emite checkout sem carrinho criado quando essa dependência é obrigatória.

## Conexões
- [[locust-catch-response-validacao-manual]] — Veja também: Locust: marcar resposta manualmente com catch_response.
- [[locust-loadtestshape-tick]] — Veja também: Locust: codificar estágio de carga via LoadTestShape.

## Fontes
- [Locust — TaskSet](https://docs.locust.io/en/stable/tasksets.html) — tarefas aninhadas, pesos e sequências de comportamento; consultado em 2026-10-02.
- [Locust 2.46 — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — User/HttpUser, tarefas, pesos, wait_time, lifecycle, cliente e agrupamento de estatísticas; consultado em 2026-10-02.
