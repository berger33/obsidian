---
id: software.testes.tranche10.000393
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
fontes: ["https://vitest.dev/api/vi.html", "https://vitest.dev/guide/mocking"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: restaurar timers falsos após cada teste

## Em uma frase
vi.useFakeTimers substitui timers do ambiente selecionado até que o teste volte ao relógio real.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Um clock deixado ativo pode afetar timeout do runner, debounce ou callbacks de outros testes no mesmo worker.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Ative timers falsos apenas no escopo necessário, avance os timers relevantes e sempre chame vi.useRealTimers no cleanup.

## Exemplo
O hook afterEach restaura relógio real mesmo quando uma assertion de retry falha.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Timers falsos não virtualizam automaticamente rede, scheduler externo ou todas as APIs de cada ambiente de navegador.

## Como verificar
Execute um caso seguinte com relógio real e confirme que a duração e os timeouts do runner permanecem normais.

## Conexões
- [[vitest-setupfiles-mocks-modulos-cache]] — Veja também: Vitest: planejar mocks registrados em setupFiles.
- [[vitest-setsystemtime-nao-disparar-timers]] — Veja também: Vitest: separar setSystemTime do avanço de timers.

## Fontes
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
- [Vitest — Mocking](https://vitest.dev/guide/mocking) — uso de mocks, spies e isolamento de chamadas; consultado em 2026-10-02.
