---
id: software.criacao_ia.tranche03.000279
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script", "https://playwright.dev/docs/api/class-page#page-add-init-script"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright addInitScript: preparar ambiente antes do código da página

## Em uma frase
`addInitScript` executa depois da criação do document e antes dos scripts da aplicação em navegação ou novo frame.

## Por que importa
Recursos como relógio de seed aleatório precisam existir antes de a aplicação inicializar seu estado. Injetar mock depois de `goto` pode perder valores já calculados ou introduzir uma corrida dependente de velocidade do browser.

## Como funciona
Registre `browserContext.addInitScript()` para cobrir páginas e frames do contexto, ou `page.addInitScript()` para a página específica. Passe dados serializáveis por argumento em vez de montar código com concatenação insegura. A ordem relativa entre vários init scripts instalados em page e context não é definida, então combine o setup que precisa de ordem numa função controlada.

## Exemplo
Um teste semeia `Math.random` com valor calculado a partir do ID do caso no init script, antes da primeira navegação. A aplicação então gera entidades determinísticas e o teste consegue reproduzir a mesma fixture em retry.

## Limites e trade-offs
Scripts também rodam em novos documents e child frames no escopo aplicável, o que pode interferir com páginas de terceiros. Não injete credenciais ou código que dependa de ordem não documentada; mudanças globais podem alterar comportamento sob teste.

## Como verificar
Registre timestamp e marcador de inicialização antes de `goto`, verifique execução em navegação subsequente e iframe novo, e teste ausência de dependência entre múltiplos scripts init.

## Conexões
- [[playwright-timeouts-escopos-separados]] — Playwright Test: diagnosticar timeouts por escopo.
- [[playwright-page-errors-observabilidade-cliente]] — Playwright: coletar erros de runtime sem confundir com falha de teste.

## Fontes
- [Playwright — BrowserContext addInitScript](https://playwright.dev/docs/api/class-browsercontext#browser-context-add-init-script) — documenta escopo para páginas/frames, momento de execução e ordem não definida Consulta: 2026-10-04.
- [Playwright — Page addInitScript](https://playwright.dev/docs/api/class-page#page-add-init-script) — mostra preloading antes de scripts da página e passagem de argumentos Consulta: 2026-10-04.
