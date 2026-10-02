---
id: software.testes.tranche11.000549
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
fontes: ["https://github.com/appium/appium-uiautomator2-driver", "https://github.com/appium/appium-xcuitest-driver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: preferir locators semânticos estáveis quando disponíveis

## Em uma frase
Drivers expõem estratégias de locator dependentes da plataforma, incluindo identificadores de acessibilidade ou recursos nativos.

## Por que importa
Appium usa sessões WebDriver e drivers específicos para automação native, hybrid ou web em diferentes plataformas; capabilities e contextos definem comandos aceitos durante a execução. XPath baseado em hierarquia incidental muda com layout e aumenta fragilidade ao redesenhar tela sem mudar comportamento.

## Como funciona
Instale e versione driver explicitamente, fixe capabilities no início da sessão, selecione contexto suportado pelo driver e encerre a sessão mesmo quando assertion ou comando falhar. Priorize identificador semântico mantido pelo app e reserve selectors estruturais para caso sem alternativa adequada.

## Exemplo
Botão “Salvar” recebe accessibility id estável e teste o localiza por id em vez de caminho absoluto do XML.

## Limites e trade-offs
Appium abstrai o protocolo, mas semântica de gesto, locator, porta e lifecycle continua dependente de plataforma/driver. Uma execução em emulador não comprova compatibilidade em todos os devices reais. Availability e semântica do locator variam entre Android, iOS, native e web contexts.

## Como verificar
Rode teste com pequenas mudanças de layout e valide que locator ainda identifica um único controle com papel/ação correta.

## Conexões
- [[appium-xcuitest-ios-boundary]] — Veja também: Appium: verificar pré-requisitos de XCUITest para sessão Apple.

## Fontes
- [Appium — UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) — opções e comportamento específico do driver Android UiAutomator2; consultado em 2026-10-02.
- [Appium — XCUITest Driver](https://github.com/appium/appium-xcuitest-driver) — opções e comportamento específico do driver Apple XCUITest; consultado em 2026-10-02.
