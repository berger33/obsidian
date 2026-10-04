---
id: software.seguranca.tranche18.001754
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://tetragon.io/docs/concepts/tracing-policy/", "https://tetragon.io/docs/concepts/tracing-policy/mode/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Cilium Tetragon: Usar enforcement somente com evidência

## Em uma frase
**Cilium Tetragon — Usar enforcement somente com evidência:** Enforcement respeita ações configuradas e pode encerrar ou negar operações de processos.

## Por que importa
O recorte de **usar enforcement somente com evidência** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar enforcement somente com evidência**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em staging, aplique uma policy limitada a um namespace e mantenha rollback acessível. Teste em staging autorizado.

## Limites e trade-offs
Falha de match ou exceção inadequada pode interromper workloads críticos. Exceções exigem responsável e prazo.

## Como verificar
Teste aplicação, health checks e rollback com canary antes de expandir escopo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-entender-modo-monitor-only]] — Complementa o tópico com cilium tetragon: entender modo monitor_only.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
