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
Código que usa endpoint antigo pode quebrar ao atualizar servidor/driver, e gesto pode ter semântica diferente entre plataformas.

## Como funciona
Prefira API suportada pelo client e driver escolhidos; fixe versão e mapeie gesto para W3C Actions ou extensão documentada.

## Exemplo
Swipe usa pointer actions no client quando suportado ou comando mobile do driver Android em fluxo que exige gesto nativo.

## Limites e trade-offs
Migração Appium 3 altera comandos disponíveis; compatibilidade depende da versão de servidor e do driver.

## Como verificar
Execute gesto em device de referência e confirme estado final observável, não apenas ausência de erro HTTP.

## Conexões
- [[appium-session-finally-delete]] — Veja também: Appium: encerrar session em finally após cada fluxo.
- [[appium-parallel-device-identidade-ports]] — Veja também: Appium: atribuir device e recursos isolados a cada sessão paralela.

## Fontes
- [Appium — Migrating to Appium 3](https://appium.io/docs/en/latest/guides/migrating-2-to-3/) — mudanças de endpoint, comandos removidos e alternativas W3C/driver; consultado em 2026-10-02.
- [Appium — UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) — opções e comportamento específico do driver Android UiAutomator2; consultado em 2026-10-02.
