---
id: software.testes.tranche10.000392
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
fontes: ["https://vitest.dev/guide/mocking/modules", "https://vitest.dev/guide/projects"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: planejar mocks registrados em setupFiles

## Em uma frase
Arquivos setupFiles são executados antes dos arquivos de teste e podem carregar módulos antes de um mock local.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Se um setup importar a dependência real, o módulo sob teste pode receber referência cacheada antes da configuração do mock.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Mantenha setup compartilhado focado em matchers e hooks globais, ou limpe/recarregue módulos quando o desenho de teste exigir substituição.

## Exemplo
Um setup registra matchers, mas não importa o cliente HTTP que cada teste pretende mockar individualmente.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. resetModules afeta o cache de módulos, não apaga variáveis já capturadas por referências existentes.

## Como verificar
Revise imports indiretos do setup e faça um caso de controle que verifica a implementação efetivamente injetada.

## Conexões
- [[vitest-domock-mock-runtime-import]] — Veja também: Vitest: usar vi.doMock para substituição não hoisted.
- [[vitest-fake-timers-restaurar-relogio]] — Veja também: Vitest: restaurar timers falsos após cada teste.

## Fontes
- [Vitest — Module mocking](https://vitest.dev/guide/mocking/modules) — mocking de módulos, hoisting e limitações do Browser Mode; consultado em 2026-10-02.
- [Vitest — Test projects](https://vitest.dev/guide/projects) — configuração, herança e opções globais de projetos; consultado em 2026-10-02.
