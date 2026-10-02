---
id: software.testes.tranche11.000545
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
fontes: ["https://appium.io/docs/en/latest/guides/migrating-2-to-3/", "https://github.com/appium/appium-uiautomator2-driver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: separar W3C Actions de comandos móveis específicos

## Em uma frase
Appium oferece comandos W3C e extensões específicas do driver; migrações podem remover endpoints touch legados e apontar alternativas.

## Por que importa
Appium usa sessões WebDriver e drivers específicos para automação native, hybrid ou web em diferentes plataformas; capabilities e contextos definem comandos aceitos durante a execução. Código que usa endpoint antigo pode quebrar ao atualizar servidor/driver, e gesto pode ter semântica diferente entre plataformas.

## Como funciona
Instale e versione driver explicitamente, fixe capabilities no início da sessão, selecione contexto suportado pelo driver e encerre a sessão mesmo quando assertion ou comando falhar. Prefira API suportada pelo client e driver escolhidos; fixe versão e mapeie gesto para W3C Actions ou extensão documentada.

## Exemplo
Swipe usa pointer actions no client quando suportado ou comando mobile do driver Android em fluxo que exige gesto nativo.

## Limites e trade-offs
Appium abstrai o protocolo, mas semântica de gesto, locator, porta e lifecycle continua dependente de plataforma/driver. Uma execução em emulador não comprova compatibilidade em todos os devices reais. Migração Appium 3 altera comandos disponíveis; compatibilidade depende da versão de servidor e do driver.

## Como verificar
Execute gesto em device de referência e confirme estado final observável, não apenas ausência de erro HTTP.

## Conexões
- [[appium-session-finally-delete]] — Veja também: Appium: encerrar session em finally após cada fluxo.
- [[appium-parallel-device-identidade-ports]] — Veja também: Appium: atribuir device e recursos isolados a cada sessão paralela.

## Fontes
- [Appium — Migrating to Appium 3](https://appium.io/docs/en/latest/guides/migrating-2-to-3/) — mudanças de endpoint, comandos removidos e alternativas W3C/driver; consultado em 2026-10-02.
- [Appium — UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) — opções e comportamento específico do driver Android UiAutomator2; consultado em 2026-10-02.
