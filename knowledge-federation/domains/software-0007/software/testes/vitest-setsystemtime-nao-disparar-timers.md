---
id: software.testes.tranche10.000394
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://vitest.dev/guide/mocking/dates", "https://vitest.dev/api/vi.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: separar setSystemTime do avanço de timers

## Em uma frase
vi.setSystemTime altera a data percebida pelo código, mas não dispara por si só timers agendados.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Um teste de expiração pode avançar a data e concluir incorretamente que timeout e callback também foram executados.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Use setSystemTime para assertions que dependem do relógio e avance timers por uma API de fake timers quando precisa executar callbacks.

## Exemplo
O teste define meia-noite para calcular uma data limite, depois avança explicitamente o timer que deve disparar notificação.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. O efeito depende de timers falsos ativos e do ambiente; não confunda relógio do sistema com fluxo de agendamento.

## Como verificar
Afirme separadamente Date.now e o número de callbacks antes e depois de alterar data e avançar timers.

## Conexões
- [[vitest-fake-timers-restaurar-relogio]] — Veja também: Vitest: restaurar timers falsos após cada teste.
- [[vitest-browser-mode-spy-namespace]] — Veja também: Vitest Browser Mode: distinguir spy de substituição de export ESM.

## Fontes
- [Vitest — Mocking dates](https://vitest.dev/guide/mocking/dates) — controle de datas e distinção entre relógio e timers; consultado em 2026-10-02.
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
