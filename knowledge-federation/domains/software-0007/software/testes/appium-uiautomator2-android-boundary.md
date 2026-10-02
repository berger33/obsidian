---
id: software.testes.tranche11.000547
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
fontes: ["https://github.com/appium/appium-uiautomator2-driver", "https://appium.io/docs/en/latest/ecosystem/drivers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: validar opções específicas de UiAutomator2 na versão usada

## Em uma frase
UiAutomator2 é driver oficial para Android e documenta capabilities, comandos e requisitos que não são universais a todo Appium.

## Por que importa
Appium usa sessões WebDriver e drivers específicos para automação native, hybrid ou web em diferentes plataformas; capabilities e contextos definem comandos aceitos durante a execução. Tratar extensão de Android como comando multiplataforma dificulta migração para XCUITest ou outro dispositivo.

## Como funciona
Instale e versione driver explicitamente, fixe capabilities no início da sessão, selecione contexto suportado pelo driver e encerre a sessão mesmo quando assertion ou comando falhar. Isole helpers específicos de UiAutomator2 e consulte documentação do driver fixado para configuração e locators disponíveis.

## Exemplo
Um helper Android configura appPackage e appActivity; versão iOS usa capability e lifecycle próprios.

## Limites e trade-offs
Appium abstrai o protocolo, mas semântica de gesto, locator, porta e lifecycle continua dependente de plataforma/driver. Uma execução em emulador não comprova compatibilidade em todos os devices reais. Nomes de capability e comportamento podem mudar entre releases do driver; teste atualização como mudança de dependência.

## Como verificar
Valide configuração em emulator/device e confirme versão real do driver no log de sessão.

## Conexões
- [[appium-parallel-device-identidade-ports]] — Veja também: Appium: atribuir device e recursos isolados a cada sessão paralela.
- [[appium-xcuitest-ios-boundary]] — Veja também: Appium: verificar pré-requisitos de XCUITest para sessão Apple.

## Fontes
- [Appium — UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) — opções e comportamento específico do driver Android UiAutomator2; consultado em 2026-10-02.
- [Appium — Drivers](https://appium.io/docs/en/latest/ecosystem/drivers/) — drivers separados, plataformas e modos suportados; consultado em 2026-10-02.
