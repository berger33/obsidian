---
id: software.testes.tranche17.001070
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: preparar e encerrar o usuário

## Em uma frase
Ganchos de início e término permitem autenticar o usuário virtual antes das tarefas e liberar recursos quando ele deixa a execução.

## Por que importa
Sessões autenticadas e conexões persistentes precisam ser estabelecidas por usuário, e não uma única vez para todo o teste.

## Como funciona
Implemente o gancho de início para login e o de término para limpeza, mantendo tokens no próprio usuário.

## Exemplo
Um cenário autenticado pode guardar o token obtido no início e usá-lo como cabeçalho em todas as tarefas seguintes.

## Limites e trade-offs
Falhas no gancho de início geram usuários inutilizáveis que ainda contam nas estatísticas, e o término pode não ser chamado em parada abrupta.

## Como verificar
Interrompa o teste durante a execução e confirme que o encerramento é registrado e que nenhuma sessão de teste permanece aberta.

## Conexões
- [[locust-custom-load-shape]] — Veja também: Locust: desenhar a carga com forma personalizada.
- [[locust-response-validation]] — Veja também: Locust: marcar falhas com validação explícita.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
