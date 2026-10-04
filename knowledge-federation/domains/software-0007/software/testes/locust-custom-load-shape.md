---
id: software.testes.tranche17.001069
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
fontes: ["https://docs.locust.io/en/stable/custom-load-shape.html", "https://docs.locust.io/en/stable/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: desenhar a carga com forma personalizada

## Em uma frase
Uma classe de forma de carga decide, a cada intervalo, quantos usuários manter e a que velocidade criá-los, permitindo sequências de patamares.

## Por que importa
Perfis com aquecimento, patamares e queda não cabem em uma rampa simples e exigem controle explícito do número de usuários ao longo do tempo.

## Como funciona
Estenda a classe de forma, descreva os estágios com duração e contagem e devolva nada quando o teste deve terminar.

## Exemplo
Uma forma em degraus pode manter cem usuários por um minuto, subir para quinhentos e encerrar após o último patamar.

## Limites e trade-offs
A forma substitui as opções de linha de comando e, se a lógica de tempo estiver errada, o teste termina cedo ou nunca encerra.

## Como verificar
Execute a forma com estágios curtos e confirme no histórico que o número de usuários segue exatamente os degraus declarados.

## Conexões
- [[locust-wait-time]] — Veja também: Locust: modelar o tempo entre ações.
- [[locust-user-lifecycle]] — Veja também: Locust: preparar e encerrar o usuário.

## Fontes
- [Locust — Custom load shape](https://docs.locust.io/en/stable/custom-load-shape.html) — formas de carga personalizadas e controle por estágios; consultado em 2026-10-03.
- [Locust — Quickstart](https://docs.locust.io/en/stable/quickstart.html) — primeira execução, parâmetros de linha de comando e resumo de estatísticas; consultado em 2026-10-03.
