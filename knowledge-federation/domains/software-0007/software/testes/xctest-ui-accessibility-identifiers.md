---
id: software.testes.tranche09.000293
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
fontes: ["https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:identifier:)", "https://developer.apple.com/documentation/xcuiautomation/xcuiapplication"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest UI tests: selecionar controles por identificadores estáveis

## Em uma frase
Testes de UI automatizados interagem com elementos expostos pela aplicação; accessibility identifiers permitem selecionar controles sem depender de posição visual.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Seletores por índice, texto mutável ou hierarquia interna quebram com mudanças de layout que não alteram o comportamento.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Atribua identifiers para controles importantes e ainda valide rótulo e estado acessíveis que o usuário percebe.

## Exemplo
Um teste toca o botão `checkout.submit`, verifica seu estado habilitado e confirma a confirmação visível após submissão.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Identifiers facilitam automação mas não demonstram sozinhos que o componente é acessível ou compreensível.

## Como verificar
Execute a mesma ação após mudança de layout e combine seletor estável com assertion de texto e estado.

## Conexões
- [[xctest-waiter-group-timeout]] — Veja também: XCTest: aguardar grupo de expectativas com resultado explícito.
- [[xctest-app-launch-arguments-environment]] — Veja também: XCTest UI tests: configurar o app por launch arguments.

## Fontes
- [Apple — XCUIElementQuery](https://developer.apple.com/documentation/xcuiautomation/xcuielementquery/element(matching:identifier:)) — consulta de elementos da interface por tipo e identificador; consultado em 2026-10-02.
- [Apple — XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication) — proxy para iniciar, monitorar e terminar a aplicação sob teste; consultado em 2026-10-02.
