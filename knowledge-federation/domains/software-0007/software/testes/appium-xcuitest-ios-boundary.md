---
id: software.testes.tranche11.000548
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://github.com/appium/appium-xcuitest-driver", "https://appium.io/docs/en/latest/ecosystem/drivers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: verificar pré-requisitos de XCUITest para sessão Apple

## Em uma frase
XCUITest é driver oficial para apps iOS e seus requisitos dependem do host, toolchain Apple e configuração da sessão.

## Por que importa
Suite que passa em Android ou simulator não demonstra que build, signing ou permissões iOS estão prontos.

## Como funciona
Mantenha setup de macOS/Xcode e capabilities XCUITest explícitos no job e valide sessão em cada classe de device suportada.

## Exemplo
Pipeline macOS inicia app .app assinado por simulator, enquanto device real usa configuração de instalação e provisioning correspondente.

## Limites e trade-offs
Capability de app, bundle id e browser variam pelo fluxo; driver não substitui configuração de signing nem valida todos devices.

## Como verificar
Execute smoke em simulator e device real quando ambos são suportados e guarde diagnóstico sanitizado do driver.

## Conexões
- [[appium-uiautomator2-android-boundary]] — Veja também: Appium: validar opções específicas de UiAutomator2 na versão usada.
- [[appium-locators-acessibilidade-contrato]] — Veja também: Appium: preferir locators semânticos estáveis quando disponíveis.

## Fontes
- [Appium — XCUITest Driver](https://github.com/appium/appium-xcuitest-driver) — opções e comportamento específico do driver Apple XCUITest; consultado em 2026-10-02.
- [Appium — Drivers](https://appium.io/docs/en/latest/ecosystem/drivers/) — drivers separados, plataformas e modos suportados; consultado em 2026-10-02.
