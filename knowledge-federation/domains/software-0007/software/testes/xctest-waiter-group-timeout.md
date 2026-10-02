---
id: software.testes.tranche09.000292
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations", "https://developer.apple.com/documentation/xctest/xctestexpectation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest: aguardar grupo de expectativas com resultado explícito

## Em uma frase
XCTWaiter pode esperar um conjunto de expectations e produzir um resultado para fulfillment, timeout ou interrupção.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Usar somente timeout genérico sem registrar qual evento faltou torna defeitos concorrentes difíceis de diagnosticar.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Crie uma expectation por evento relevante e interprete o resultado do waiter com mensagem que identifique a condição.

## Exemplo
Uma tela de sincronização espera resposta e indicador de término; o relatório informa qual dos dois não ocorreu.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. O timeout é limite de espera do teste, não garantia de prazo do serviço ou medida de performance.

## Como verificar
Force cada expectation a não cumprir, a cumprir após atraso e a cumprir no prazo para validar os resultados relatados.

## Conexões
- [[xctest-expectation-fulfillment-count]] — Veja também: XCTest: controlar fulfillment e over-fulfillment de expectations.
- [[xctest-ui-accessibility-identifiers]] — Veja também: XCTest UI tests: selecionar controles por identificadores estáveis.

## Fontes
- [Apple — Asynchronous tests and expectations](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) — async/await e expectativas para callbacks e delegates; consultado em 2026-10-02.
- [Apple — XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestexpectation) — fulfillment, timeout e configuração de expectations; consultado em 2026-10-02.
