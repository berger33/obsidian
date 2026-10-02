---
id: software.testes.tranche11.000521
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://jmeter.apache.org/usermanual/test_plan.html", "https://jmeter.apache.org/usermanual/component_reference.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: lembrar que timers atrasam samplers dentro de seu escopo

## Em uma frase
Timer é processado antes de cada sampler dentro do escopo hierárquico, e múltiplos timers podem acumular atraso.

## Por que importa
Timer colocado no nível errado pode reduzir ou aumentar a taxa de todas as requests do plano em vez de só uma.

## Como funciona
Posicione timer como filho do sampler para atraso local ou no controller/grupo quando a pausa deve valer para seus descendentes.

## Exemplo
Um timer de think time do checkout não retarda chamada de busca; timer do grupo afeta todos os samplers filhos.

## Limites e trade-offs
Timer sem sampler em seu escopo não é processado; ordem dos elementos no tree view não altera a regra de escopo hierárquico.

## Como verificar
Inspecione árvore final e compare timestamps de requests antes/depois de mover o timer.

## Conexões
- [[jmeter-threadgroup-threads-independentes]] — Veja também: JMeter: interpretar threads do Thread Group como fluxos independentes.
- [[jmeter-assertion-aplica-por-escopo]] — Veja também: JMeter: limitar Assertion ao sampler que representa o contrato.

## Fontes
- [Apache JMeter — Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html) — Thread Groups, timers, assertions, execução e regras de escopo; consultado em 2026-10-02.
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
