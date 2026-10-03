---
id: software.testes.tranche17.001068
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

# Locust: modelar o tempo entre ações

## Em uma frase
O tempo de espera pode ser sorteado em uma faixa, constante ou calculado para manter um ritmo fixo de tarefas por usuário.

## Por que importa
O intervalo entre ações define quantos pedidos por segundo cada usuário gera e aproxima a simulação do comportamento humano.

## Como funciona
Escolha a estratégia conforme a intenção, ajuste os limites com base no uso real e mantenha a mesma estratégia entre execuções comparáveis.

## Exemplo
Um teste de navegação pode sortear esperas entre um e cinco segundos, enquanto um consumidor de fila pode manter intervalo constante.

## Limites e trade-offs
Faixas muito amplas aumentam a variância do resultado, e o ritmo fixo esconde atrasos internos ao acumular trabalho para a próxima volta.

## Como verificar
Rode com duas configurações de espera e compare a taxa de requisições alcançada para verificar o efeito do intervalo.

## Conexões
- [[locust-tasks-and-weights]] — Veja também: Locust: ponderar tarefas do usuário.
- [[locust-custom-load-shape]] — Veja também: Locust: desenhar a carga com forma personalizada.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
