---
id: software.seguranca.tranche18.001760
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

# Cilium Tetragon: Versionar policies e testar compatibilidade

## Em uma frase
**Cilium Tetragon — Versionar policies e testar compatibilidade:** Policies precisam acompanhar kernel, API CRD e comportamento do agente usados no cluster.

## Por que importa
O recorte de **versionar policies e testar compatibilidade** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **versionar policies e testar compatibilidade**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Valide uma alteração em versão de cluster representativa antes de publicar o CRD em produção. Teste em staging autorizado.

## Limites e trade-offs
Um exemplo válido em outro kernel não garante o mesmo hook ou semântica local. Exceções exigem responsável e prazo.

## Como verificar
Guarde versão do agente, kernel e teste de regressão junto da policy aprovada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[renovate-versionar-configuracao-de-renovate]] — Complementa o tópico com renovate: versionar configuração de renovate.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
