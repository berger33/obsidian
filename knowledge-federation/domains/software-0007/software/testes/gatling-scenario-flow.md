---
id: software.testes.tranche17.001057
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
fontes: ["https://docs.gatling.io/concepts/scenario/", "https://docs.gatling.io/concepts/simulation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: descrever a jornada com ações encadeadas

## Em uma frase
O cenário encadeia requisições, pausas e extrações de valores, representando o comportamento de um usuário virtual ao longo de uma sessão.

## Por que importa
Medir apenas o primeiro pedido ignora o custo acumulado da jornada, que é onde a experiência costuma degradar sob carga.

## Como funciona
Ordene as requisições como no uso real, nomeie cada passo para facilitar a leitura do relatório e insira pausas representativas entre ações.

## Exemplo
Um cenário de compra pode consultar a vitrine, pausar para simular leitura, buscar o detalhe e enviar o pedido na mesma sequência da pessoa usuária.

## Limites e trade-offs
Cenários longos concentram muitas responsabilidades e dificultam atribuir degradação a um passo específico; os nomes das requisições ajudam a isolar o ponto.

## Como verificar
Rode a simulação e localize no relatório a latência por requisição nomeada, confirmando que cada passo aparece separadamente.

## Conexões
- [[gatling-simulation-structure]] — Veja também: Gatling: organizar a simulação como código.
- [[gatling-injection-profiles]] — Veja também: Gatling: escolher o perfil de injeção.

## Fontes
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — encadeamento de ações, pausas e nomeação de requisições na jornada; consultado em 2026-10-03.
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
