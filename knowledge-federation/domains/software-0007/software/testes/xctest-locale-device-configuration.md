---
id: software.testes.tranche09.000298
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
fontes: ["https://developer.apple.com/documentation/xcode/organizing-tests-to-improve-feedback", "https://developer.apple.com/documentation/xcuiautomation/xcuiapplication"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest: cobrir locale e device sem depender do simulador anterior

## Em uma frase
Variações de locale, aparência e tamanho de tela devem ser fornecidas pela configuração do teste, não por estado manual do simulador.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Ambiente herdado de uma execução anterior pode fazer datas, textos e layouts variarem sem alteração de código.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Declare locale e destino no plano de teste e limite configurações a requisitos de internacionalização e suporte.

## Exemplo
A mesma tela de vencimento é executada em locale que muda formato de data e em dispositivo compacto definido no plano.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Nem toda combinação de idioma, orientação e dispositivo precisa rodar em cada commit; priorize risco.

## Como verificar
Registre configuração efetiva e execute casos de fronteira de texto, data e layout na matriz selecionada.

## Conexões
- [[xctest-order-independent-state-reset]] — Veja também: XCTest: não depender da ordem dos métodos de teste.
- [[xctest-ui-wait-for-condition-not-sleep]] — Veja também: XCTest UI tests: aguardar condição da interface, não sleep.

## Fontes
- [Apple — Organizing tests to improve feedback](https://developer.apple.com/documentation/xcode/organizing-tests-to-improve-feedback) — organização e execução configurável das test suites; consultado em 2026-10-02.
- [Apple — XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication) — proxy para iniciar, monitorar e terminar a aplicação sob teste; consultado em 2026-10-02.
