---
id: software.testes.tranche09.000299
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
fontes: ["https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations", "https://developer.apple.com/documentation/xcuiautomation/xcuiapplication"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest UI tests: aguardar condição da interface, não sleep

## Em uma frase
UI tests devem aguardar elemento ou expectativa correspondente ao evento assíncrono em vez de pausar por duração fixa.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Sleep curto causa flakiness em device lento e sleep longo reduz feedback sem provar que a operação terminou.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Use predicate/expectation ou APIs de espera de elemento e verifique estado final após a condição ser satisfeita.

## Exemplo
Depois de tocar em atualizar, o teste aguarda indicador desaparecer e resultado aparecer, com timeout que gera falha legível.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Timeout da espera precisa refletir o cenário; não deve servir para esconder lentidão anormal indefinidamente.

## Como verificar
Introduza resposta atrasada controlada, compare device/runtime e confirme que espera termina pelo elemento, não pela duração fixa.

## Conexões
- [[xctest-locale-device-configuration]] — Veja também: XCTest: cobrir locale e device sem depender do simulador anterior.

## Fontes
- [Apple — Asynchronous tests and expectations](https://developer.apple.com/documentation/xctest/asynchronous-tests-and-expectations) — async/await e expectativas para callbacks e delegates; consultado em 2026-10-02.
- [Apple — XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication) — proxy para iniciar, monitorar e terminar a aplicação sob teste; consultado em 2026-10-02.
