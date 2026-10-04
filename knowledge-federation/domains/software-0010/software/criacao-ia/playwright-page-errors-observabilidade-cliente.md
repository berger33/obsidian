---
id: software.criacao_ia.tranche03.000280
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
fontes: ["https://playwright.dev/docs/api/class-page", "https://playwright.dev/docs/trace-viewer"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright: coletar erros de runtime sem confundir com falha de teste

## Em uma frase
`page.pageErrors()` consulta um conjunto limitado de erros JavaScript recentes, enquanto eventos de Page podem capturar erros conforme ocorrem.

## Por que importa
Uma assertion pode passar mesmo quando a aplicação registrou exception não tratada em outro componente. Coletar erros de cliente junto ao teste ajuda detectar falhas silenciosas e relacioná-las à navegação, frame ou ação que as provocou.

## Como funciona
Registre `page.on('pageerror')` antes da navegação para observar exceções futuras ou leia `page.pageErrors()` em Playwright atual após o cenário. A API de armazenamento retorna até 200 erros recentes; `clearPageErrors()` pode começar uma janela nova em versões compatíveis. Capture contexto suficiente sem imprimir conteúdo sensível de objetos.

## Exemplo
Um teste de renderização registra erros de page em array, navega, realiza ações e no final falha se a lista contiver exception inesperada. Para um cenário com bootstrap conhecido, limpa o conjunto após a etapa inicial e valida apenas erros emitidos pela interação investigada.

## Limites e trade-offs
Erros de console, exceções de página, falhas de request e erros de teste são sinais diferentes. Uma lista limitada pode descartar os mais antigos, e handlers registrados depois da navegação não observam exceções passadas salvo se forem mantidas pela API de consulta.

## Como verificar
Gere erro antes e depois de listener, valide limite e limpeza da lista e diferencie pageerror de console.error e requestfailed. Inclua frames e navegações múltiplas no teste de integração.

## Conexões
- [[playwright-add-init-script-determinismo]] — Playwright addInitScript: preparar ambiente antes do código da página.

## Fontes
- [Playwright — Page API](https://playwright.dev/docs/api/class-page) — documenta page events, `pageErrors()` e limpeza do buffer de erros Consulta: 2026-10-04.
- [Playwright — Trace Viewer](https://playwright.dev/docs/trace-viewer) — mostra como console e logs de execução podem ser correlacionados com ações gravadas Consulta: 2026-10-04.
