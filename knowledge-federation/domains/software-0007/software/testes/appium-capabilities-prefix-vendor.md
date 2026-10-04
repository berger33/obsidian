---
id: software.testes.tranche11.000541
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
fontes: ["https://appium.io/docs/en/latest/guides/caps/", "https://appium.io/docs/en/latest/guides/migrating-1-to-2/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Appium: prefixar capabilities específicas e fixá-las ao iniciar sessão

## Em uma frase
Capabilities são parâmetros key-value de criação de sessão e não podem ser alteradas durante seu lifecycle; capabilities não padrão usam prefixo vendor como appium:.

## Por que importa
Enviar campo específico sem namespace ou tentar mudar device depois pode causar recusa de sessão ou configuração silenciosamente ignorada.

## Como funciona
Declare platformName padronizado e capabilities Appium com prefixo, incluindo automationName e device quando necessário.

## Exemplo
Sessão Android informa platformName e appium:automationName=UiAutomator2 no payload inicial.

## Limites e trade-offs
Cada driver pode exigir um conjunto próprio de capabilities e validar combinações incompatíveis.

## Como verificar
Capture payload seguro de criação e compare capabilities aceitas, session id e device selecionado.

## Conexões
- [[appium-driver-instalacao-modular]] — Veja também: Appium: instalar driver compatível além do servidor.
- [[appium-automationname-seleciona-driver]] — Veja também: Appium: usar automationName para selecionar implementação do driver.

## Fontes
- [Appium — Session Capabilities](https://appium.io/docs/en/latest/guides/caps/) — parâmetros W3C de criação de sessão, prefixos Appium e capabilities imutáveis; consultado em 2026-10-02.
- [Appium — Migrating to Appium 2](https://appium.io/docs/en/latest/guides/migrating-1-to-2/) — arquitetura modular, instalação de drivers e vendor prefixes; consultado em 2026-10-02.
