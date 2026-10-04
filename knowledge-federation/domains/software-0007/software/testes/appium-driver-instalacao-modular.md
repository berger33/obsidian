---
id: software.testes.tranche11.000540
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
fontes: ["https://appium.io/docs/en/latest/guides/migrating-1-to-2/", "https://appium.io/docs/en/latest/ecosystem/drivers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: instalar driver compatível além do servidor

## Em uma frase
Appium separa o servidor central de drivers que implementam automação por plataforma e precisam ser instalados para criar sessões.

## Por que importa
Instalação apenas do servidor pode subir endpoint mas falhar ao iniciar sessão porque driver Android ou iOS não está presente.

## Como funciona
Fixe versão do servidor e do driver no ambiente de CI e verifique disponibilidade antes de iniciar device session.

## Exemplo
Pipeline instala Appium e UiAutomator2 para suite Android e instala XCUITest somente no runner macOS.

## Limites e trade-offs
Plugins e drivers têm compatibilidade e dependências próprias; atualizar servidor não atualiza automaticamente cada extensão.

## Como verificar
Rode listagem de drivers instalados e crie sessão mínima em cada plataforma planejada.

## Conexões
- [[appium-capabilities-prefix-vendor]] — Veja também: Appium: prefixar capabilities específicas e fixá-las ao iniciar sessão.

## Fontes
- [Appium — Migrating to Appium 2](https://appium.io/docs/en/latest/guides/migrating-1-to-2/) — arquitetura modular, instalação de drivers e vendor prefixes; consultado em 2026-10-02.
- [Appium — Drivers](https://appium.io/docs/en/latest/ecosystem/drivers/) — drivers separados, plataformas e modos suportados; consultado em 2026-10-02.
