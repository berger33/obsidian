---
id: software.seguranca.tranche18.001751
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

# Cilium Tetragon: Escolher hook point da policy

## Em uma frase
**Cilium Tetragon — Escolher hook point da policy:** TracingPolicy pode observar hooks como kprobes, tracepoints e uprobes, cada um ligado a pontos diferentes de execução.

## Por que importa
O recorte de **escolher hook point da policy** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher hook point da policy**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em nó descartável, selecione um hook para observar uma chamada documentada pelo kernel. Teste em staging autorizado.

## Limites e trade-offs
Hook ou assinatura incorreta pode perder eventos ou interferir em processos. Exceções exigem responsável e prazo.

## Como verificar
Valide versão do kernel, função-alvo e presença do evento em saída de teste. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-filtrar-eventos-no-kernel]] — Complementa o tópico com cilium tetragon: filtrar eventos no kernel.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
