---
id: software.testes.tranche09.000291
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
fontes: ["https://developer.apple.com/documentation/xctest/xctestexpectation", "https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest: controlar fulfillment e over-fulfillment de expectations

## Em uma frase
XCTestExpectation modela um resultado assíncrono, com espera por fulfillment e timeout, e pode configurar quantidade esperada de fulfillments.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Callback duplicado ou observer registrado duas vezes pode passar despercebido se o teste só verifica o primeiro evento.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Defina descrição e contagem esperada; ative assertion de fulfillment excedente quando a regra exige uma única chamada.

## Exemplo
O delegate deve notificar uma vez; teste registra expectation, provoca uma atualização e falha se chegar notificação extra.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Uma contagem rígida é errada quando o contrato admite eventos múltiplos; defina a expectativa pela semântica do componente.

## Como verificar
Cubra sucesso, ausência de evento e fulfillment duplicado com timeout curto e diagnóstico identificável.

## Conexões
- [[xctest-async-await-test-method]] — Veja também: XCTest: usar async/await em testes assíncronos Swift.
- [[xctest-waiter-group-timeout]] — Veja também: XCTest: aguardar grupo de expectativas com resultado explícito.

## Fontes
- [Apple — XCTestExpectation](https://developer.apple.com/documentation/xctest/xctestexpectation) — fulfillment, timeout e configuração de expectations; consultado em 2026-10-02.
- [Apple — Asynchronous tests and expectations](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) — async/await e expectativas para callbacks e delegates; consultado em 2026-10-02.
