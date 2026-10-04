---
id: software.seguranca.tranche18.001756
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

# Cilium Tetragon: Separar domínios de carregamento

## Em uma frase
**Cilium Tetragon — Separar domínios de carregamento:** Policies adicionadas por Kubernetes, gRPC ou arquivo estático podem residir em domínios separados.

## Por que importa
O recorte de **separar domínios de carregamento** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar domínios de carregamento**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Registre origem de uma policy ao comparar configuração declarada com policies ativas. Teste em staging autorizado.

## Limites e trade-offs
Alterar uma policy em um domínio não necessariamente remove policy homônima de outro. Exceções exigem responsável e prazo.

## Como verificar
Liste domínios carregados e verifique remoção no domínio que originalmente recebeu a regra. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-limitar-policy-por-namespace-e-labels]] — Complementa o tópico com cilium tetragon: limitar policy por namespace e labels.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
