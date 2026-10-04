---
id: software.seguranca.tranche18.001752
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

# Cilium Tetragon: Filtrar eventos no kernel

## Em uma frase
**Cilium Tetragon — Filtrar eventos no kernel:** Selectors permitem filtrar eventos antes que cheguem ao espaço de usuário e podem associar ações aos matches.

## Por que importa
O recorte de **filtrar eventos no kernel** ajuda a observar operações selecionadas no kernel e aplicar controles direcionados em hosts e clusters autorizados. A equipe registra risco, evidência e responsável.

## Como funciona
Para **filtrar eventos no kernel**, TracingPolicies ligam pontos de instrumentação a seletores em kernel e ações para eventos que atendam às condições. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Restrinja uma regra experimental por processo e namespace em vez de coletar todos os eventos do cluster. Teste em staging autorizado.

## Limites e trade-offs
Filtro incompleto ainda pode gerar alto volume ou incluir workloads não pretendidos. Exceções exigem responsável e prazo.

## Como verificar
Compare eventos observados com um processo controle fora do escopo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-executar-primeiro-em-modo-monitor]] — Complementa o tópico com cilium tetragon: executar primeiro em modo monitor.

## Fontes
- [Tetragon — Tracing Policy](https://tetragon.io/docs/concepts/tracing-policy/) — referência oficial da CRD, hooks, selectors, ações e carregamento de policies; consultado em 2026-10-04.
- [Tetragon — Enforcement Mode](https://tetragon.io/docs/concepts/tracing-policy/mode/) — guia oficial dos modos monitor, enforcement e monitor_only; consultado em 2026-10-04.
