---
id: software.seguranca.tranche18.001753
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

# Cilium Tetragon: Executar primeiro em modo monitor

## Em uma frase
**Cilium Tetragon — Executar primeiro em modo monitor:** Modo monitor registra o comportamento da policy sem realizar ações de enforcement configuradas.

## Por que importa
O recorte de **executar primeiro em modo monitor** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **executar primeiro em modo monitor**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Carregue uma policy de laboratório em monitor e estime eventos antes de qualquer bloqueio. Teste em staging autorizado.

## Limites e trade-offs
Monitor não demonstra que uma ação em enforcement funcionará sem impacto operacional. Exceções exigem responsável e prazo.

## Como verificar
Reproduza casos positivos e negativos e revise contagem antes de ativar enforcement. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-usar-enforcement-somente-com-evidencia]] — Complementa o tópico com cilium tetragon: usar enforcement somente com evidência.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
