---
id: software.testes.tranche11.000543
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
fontes: ["https://appium.io/docs/en/latest/guides/context/", "https://appium.io/docs/en/latest/ecosystem/drivers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: consultar contexts antes de alternar entre native e webview

## Em uma frase
Contexts representam modos de automação que o driver implementa; API permite listar, ler contexto atual e trocar para outro nome disponível.

## Por que importa
Appium usa sessões WebDriver e drivers específicos para automação native, hybrid ou web em diferentes plataformas; capabilities e contextos definem comandos aceitos durante a execução. Comandos e locators podem se comportar diferente em app híbrido conforme contexto ativo e referência do elemento.

## Como funciona
Instale e versione driver explicitamente, fixe capabilities no início da sessão, selecione contexto suportado pelo driver e encerre a sessão mesmo quando assertion ou comando falhar. Consulte contexts no runtime, identifique WebView correto e altere contexto somente quando driver reportar sua disponibilidade.

## Exemplo
Fluxo interage com botão nativo, troca para webview de checkout, valida DOM e restaura contexto nativo.

## Limites e trade-offs
Appium abstrai o protocolo, mas semântica de gesto, locator, porta e lifecycle continua dependente de plataforma/driver. Uma execução em emulador não comprova compatibilidade em todos os devices reais. Lista, nome e suporte de cada contexto dependem do driver/plataforma; não fixe WEBVIEW_1 sem verificação.

## Como verificar
Registre contexts disponíveis por build e valide interação correspondente a cada contexto sem reutilizar elemento antigo.

## Conexões
- [[appium-automationname-seleciona-driver]] — Veja também: Appium: usar automationName para selecionar implementação do driver.
- [[appium-session-finally-delete]] — Veja também: Appium: encerrar session em finally após cada fluxo.

## Fontes
- [Appium — Managing Contexts](https://appium.io/docs/en/latest/guides/context/) — contextos native/web, enumeração e troca conforme suporte do driver; consultado em 2026-10-02.
- [Appium — Drivers](https://appium.io/docs/en/latest/ecosystem/drivers/) — drivers separados, plataformas e modos suportados; consultado em 2026-10-02.
