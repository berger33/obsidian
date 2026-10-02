---
id: software.testes.tranche11.000546
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
fontes: ["https://appium.io/docs/en/latest/guides/caps/", "https://github.com/appium/appium-uiautomator2-driver"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: atribuir device e recursos isolados a cada sessão paralela

## Em uma frase
Capabilities como udid identificam dispositivo alvo; drivers também podem requerer portas e recursos distintos para sessões simultâneas.

## Por que importa
Appium usa sessões WebDriver e drivers específicos para automação native, hybrid ou web em diferentes plataformas; capabilities e contextos definem comandos aceitos durante a execução. Duas sessões podem disputar device ou porta auxiliar e produzir flakiness que parece defeito da aplicação.

## Como funciona
Instale e versione driver explicitamente, fixe capabilities no início da sessão, selecione contexto suportado pelo driver e encerre a sessão mesmo quando assertion ou comando falhar. Atribua device id exclusivo, configure portas por driver segundo sua documentação e isole dados/contas por execução.

## Exemplo
Dois workers iniciam Android com udid e systemPort distintos, cada um usando instalação e usuário de teste próprios.

## Limites e trade-offs
Appium abstrai o protocolo, mas semântica de gesto, locator, porta e lifecycle continua dependente de plataforma/driver. Uma execução em emulador não comprova compatibilidade em todos os devices reais. Requisitos de porta variam por driver/versão e Grid não cria isolamento de dados da aplicação automaticamente.

## Como verificar
Rode duas sessões simultâneas repetidamente e verifique device, porta reservada, logs e estado de app de cada worker.

## Conexões
- [[appium-w3c-actions-vs-comandos-driver]] — Veja também: Appium: separar W3C Actions de comandos móveis específicos.
- [[appium-uiautomator2-android-boundary]] — Veja também: Appium: validar opções específicas de UiAutomator2 na versão usada.

## Fontes
- [Appium — Session Capabilities](https://appium.io/docs/en/latest/guides/caps/) — parâmetros W3C de criação de sessão, prefixos Appium e capabilities imutáveis; consultado em 2026-10-02.
- [Appium — UiAutomator2 Driver](https://github.com/appium/appium-uiautomator2-driver) — opções e comportamento específico do driver Android UiAutomator2; consultado em 2026-10-02.
