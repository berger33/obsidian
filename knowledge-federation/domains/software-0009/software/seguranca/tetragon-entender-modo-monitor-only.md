---
id: software.seguranca.tranche18.001755
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

# Cilium Tetragon: Entender modo monitor_only

## Em uma frase
**Cilium Tetragon — Entender modo monitor_only:** Uma policy monitor_only não contém ações de enforcement e não pode ser promovida a enforcement em runtime.

## Por que importa
O recorte de **entender modo monitor_only** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **entender modo monitor_only**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Publique policy de observabilidade com modo monitor_only quando a regra não deve bloquear. Teste em staging autorizado.

## Limites e trade-offs
Confundir monitor_only com monitor pode levar à expectativa errada sobre futura promoção. Exceções exigem responsável e prazo.

## Como verificar
Inspecione o modo reportado pelo agente antes de atribuir comportamento à policy. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-separar-dominios-de-carregamento]] — Complementa o tópico com cilium tetragon: separar domínios de carregamento.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
