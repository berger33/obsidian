---
id: software.testes.tranche11.000542
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
fontes: ["https://appium.io/docs/en/latest/guides/caps/", "https://appium.io/docs/en/latest/ecosystem/drivers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: usar automationName para selecionar implementação do driver

## Em uma frase
appium:automationName indica qual driver deve executar comandos da sessão.

## Por que importa
Testes podem selecionar driver incorreto quando capability é omitida ou copiada de outra plataforma, falhando com comandos não suportados.

## Como funciona
Escolha automationName compatível com OS e registre driver/version junto ao resultado do teste.

## Exemplo
Android usa UiAutomator2 e iOS usa XCUITest com capabilities separadas por job.

## Limites e trade-offs
Drivers suportam plataformas e modos diferentes; não extrapole capability de um driver para outro.

## Como verificar
Verifique nome do driver na sessão e execute comando pequeno de leitura antes do fluxo completo.

## Conexões
- [[appium-capabilities-prefix-vendor]] — Veja também: Appium: prefixar capabilities específicas e fixá-las ao iniciar sessão.
- [[appium-context-native-webview]] — Veja também: Appium: consultar contexts antes de alternar entre native e webview.

## Fontes
- [Appium — Session Capabilities](https://appium.io/docs/en/latest/guides/caps/) — parâmetros W3C de criação de sessão, prefixos Appium e capabilities imutáveis; consultado em 2026-10-02.
- [Appium — Drivers](https://appium.io/docs/en/latest/ecosystem/drivers/) — drivers separados, plataformas e modos suportados; consultado em 2026-10-02.
