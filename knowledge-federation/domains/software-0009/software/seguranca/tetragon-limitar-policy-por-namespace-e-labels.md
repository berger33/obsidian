---
id: software.seguranca.tranche18.001757
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

# Cilium Tetragon: Limitar policy por namespace e labels

## Em uma frase
**Cilium Tetragon — Limitar policy por namespace e labels:** Filtros Kubernetes podem reduzir a policy a namespaces ou pods escolhidos.

## Por que importa
O recorte de **limitar policy por namespace e labels** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **limitar policy por namespace e labels**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique uma policy a workload-canary e namespace de teste antes de incluir serviços vizinhos. Teste em staging autorizado.

## Limites e trade-offs
Labels podem ser alteradas por controladores; seletor amplo aumenta alcance sem revisão. Exceções exigem responsável e prazo.

## Como verificar
Teste pod dentro e fora do seletor e confirme eventos ou ações esperados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-monitorar-acesso-a-arquivos-sensiveis]] — Complementa o tópico com cilium tetragon: monitorar acesso a arquivos sensíveis.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
