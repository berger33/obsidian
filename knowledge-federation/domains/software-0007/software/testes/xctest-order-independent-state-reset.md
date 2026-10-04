---
id: software.testes.tranche09.000297
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

# XCTest: não depender da ordem dos métodos de teste

## Em uma frase
Cada teste precisa preparar o estado que consome em vez de herdar implicitamente dados deixados por outro método da suite.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Ordem de execução diferente, retry ou teste isolado pode revelar dependência oculta que execução local sequencial mascara.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Crie fixture por caso, resete armazenamento ou reinstancie a app quando necessário e limpe observadores na finalização.

## Exemplo
Dois testes executados em ordem alternada partem do mesmo estado de conta e produzem o mesmo resultado esperado.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Apagar e reinstalar app pode tornar a suíte lenta e não limpa dados que vivem no backend externo.

## Como verificar
Execute métodos isoladamente, em ordem invertida e com repetição; compare efeitos residuais no app e no servidor.

## Conexões
- [[xctest-signpost-performance-metric]] — Veja também: XCTest: medir intervalo instrumentado com signpost metric.
- [[xctest-locale-device-configuration]] — Veja também: XCTest: cobrir locale e device sem depender do simulador anterior.

## Fontes
- [Apple — Organizing tests to improve feedback](https://developer.apple.com/documentation/xcode/organizing-tests-to-improve-feedback) — organização e execução configurável das test suites; consultado em 2026-10-02.
- [Apple — XCUIApplication](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication) — proxy para iniciar, monitorar e terminar a aplicação sob teste; consultado em 2026-10-02.
