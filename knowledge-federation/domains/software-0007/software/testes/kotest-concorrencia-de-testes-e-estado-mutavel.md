---
id: software.testes.tranche15.000901
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/concurrency6.html", "https://kotest.io/docs/framework/isolation-mode.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: habilitar concorrência só depois de definir segurança de estado

## Em uma frase
Kotest permite configurar concorrência de specs e de testes raiz separadamente; por padrão, testes dentro de uma spec executam sequencialmente no dispatcher descrito.

## Por que importa
O default conservador evita impor a todos os casos a obrigação de proteger campos compartilhados e callbacks de setup.

## Como funciona
`Concurrent` e `LimitedConcurrency` podem aumentar throughput, mas elevam a chance de corrida em fixtures, fake servers e recursos de banco.

## Exemplo
Mantenha a execução sequencial enquanto testes usam campos mutáveis compartilhados; onde os casos forem independentes, configure `override val testExecutionMode = TestExecutionMode.LimitedConcurrency(4)` na Spec e dê a cada teste seu próprio recurso.

## Limites e trade-offs
Concurrency mode se refere a casos no engine e tem disponibilidade específica por plataforma; chamadas suspensas ou bloqueantes podem ter efeitos distintos no dispatcher.

## Como verificar
Ative concorrência primeiro numa classe isolada, repita o run com ordem embaralhada e monitore acessos à fixture compartilhada antes de expandir globalmente.

## Conexões
- [[kotest-isolation-instance-per-root]] — Veja também: Kotest 6.2: preferir InstancePerRoot para isolamento de estado por raiz.
- [[kotest-data-testing-com-casos-derivados]] — Veja também: Kotest 6.2: escolher withXXX de acordo com estilo e tipo de nó.

## Fontes
- [Kotest 6.2 — Concurrency](https://kotest.io/docs/framework/concurrency6.html) — concorrência de specs/testes, dispatcher e escopo por plataforma; consultado em 2026-10-02.
- [Kotest 6.2 — Isolation Modes](https://kotest.io/docs/framework/isolation-mode.html) — instâncias de Spec, SingleInstance, InstancePerRoot e modos depreciados; consultado em 2026-10-02.
