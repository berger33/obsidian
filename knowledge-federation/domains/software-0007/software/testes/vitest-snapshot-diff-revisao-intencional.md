---
id: software.testes.tranche10.000399
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
fontes: ["https://vitest.dev/guide/snapshot", "https://vitest.dev/api/vi.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vitest: revisar o diff antes de atualizar snapshot

## Em uma frase
Snapshots registram uma saída serializada e falham quando a nova saída difere do baseline salvo.

## Por que importa
Vitest integra o runner ao ecossistema Vite; hoisting, imports ESM, Browser Mode e isolamento influenciam a substituição de dependências. Um update em massa sem revisão aceita qualquer mudança e elimina o sinal que o snapshot deveria oferecer.

## Como funciona
Escolha vi.mock ou vi.doMock conforme o momento de avaliação, restaure clocks e mocks e separe opções globais de opções de cada projeto. Inspecione o diff e atualize somente os casos cuja nova saída foi confirmada como intencional.

## Exemplo
A alteração de markup acessível é revisada e aprovada; uma mudança inesperada de valor permanece como falha a investigar.

## Limites e trade-offs
O comportamento citado segue a documentação atual do Vitest consultada; pools, Browser Mode e versões de plugins podem alterar detalhes práticos. Snapshots excessivamente grandes ou voláteis geram ruído e não substituem assertions semânticas sobre requisitos críticos.

## Como verificar
Na revisão, confira o conteúdo do snapshot alterado e acrescente assertion direta para propriedades cuja estabilidade importa.

## Conexões
- [[vitest-coverage-provider-relatorio-declarado]] — Veja também: Vitest: declarar provider e formato de relatório de coverage.

## Fontes
- [Vitest — Snapshot testing](https://vitest.dev/guide/snapshot) — asserções de snapshot e atualização de resultados; consultado em 2026-10-02.
- [Vitest — vi API](https://vitest.dev/api/vi.html) — mock functions, timers, relógio do sistema e ciclo de vida de mocks; consultado em 2026-10-02.
