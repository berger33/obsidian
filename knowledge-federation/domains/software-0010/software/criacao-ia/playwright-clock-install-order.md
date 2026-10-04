---
id: software.criacao_ia.tranche03.000271
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
fontes: ["https://playwright.dev/docs/clock", "https://playwright.dev/docs/api/class-clock"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright Clock: instalar relógio antes de APIs temporais

## Em uma frase
Se um teste chamar `page.clock.install()`, essa instalação precisa ocorrer antes de qualquer outra chamada relacionada ao relógio controlado.

## Por que importa
A instalação substitui APIs nativas como Date, timers e animation frames. Criar timer e instalar o relógio depois deixa um handle associado a uma implementação que foi sobrescrita e pode causar comportamento indefinido.

## Como funciona
Prefira `setFixedTime` quando só precisar controlar `Date.now()` e `new Date()` mantendo timers em fluxo natural. Use `install` com `pauseAt`, `fastForward`, `runFor` ou `resume` quando precisar dirigir relógio e timers juntos; invoque-o antes de código da aplicação ou chamadas de teste que configurem timers. Reserve `setSystemTime` para casos avançados.

## Exemplo
Para testar expiração de sessão, instale um horário inicial antes de navegar e avance cinco minutos com `fastForward`. Para uma interface que só exibe a data, `setFixedTime` pode ser suficiente e evita congelar timers que atualizam o DOM.

## Limites e trade-offs
O relógio virtual substitui várias APIs do browser, mas não controla todos os relógios externos, como tempo do servidor, sistema operacional ou processos fora da página. Misturar relógio fixo com scheduler real requer confirmar quais APIs são controladas.

## Como verificar
Execute o mesmo caso com temporizadores inicializados antes e depois da instalação, revise ordem de setup e avance o relógio em pequenos intervalos. Confirme que timeout de aplicação, requestAnimationFrame e Date retornam o comportamento esperado.

## Conexões
- [[playwright-websocketroute-mock-ou-proxy]] — Playwright WebSocketRoute: escolher mock completo ou interceptação.

## Fontes
- [Playwright — Clock](https://playwright.dev/docs/clock) — define diferença entre setFixedTime/install e avisa sobre ordem indefinida de instalação Consulta: 2026-10-04.
- [Playwright — Clock API](https://playwright.dev/docs/api/class-clock) — lista APIs temporais controladas e métodos disponíveis no relógio Consulta: 2026-10-04.
