---
id: software.testes.tranche11.000528
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
fontes: ["https://jmeter.apache.org/usermanual/component_reference.html", "https://jmeter.apache.org/usermanual/test_plan.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JMeter: definir se Transaction Controller agrega sub-samples

## Em uma frase
Transaction Controller agrupa samplers em transação e pode produzir sample agregado conforme modo configurado.

## Por que importa
Somar request individuais e transação agregada como se fossem operações independentes pode duplicar contagem e distorcer latência.

## Como funciona
Escolha modo parent/aggregate coerente com métrica e configure assertions no nível cuja duração deseja medir.

## Exemplo
Fluxo de autenticação agrupa GET challenge e POST login como uma jornada; relatório distingue parent transaction de requests filhos.

## Limites e trade-offs
Modo parent pode aplicar assertions aos sub-samples e ao aggregate dependendo da configuração.

## Como verificar
Inspecione JTL para confirmar quantidade, labels e duração de amostras antes de calcular percentis.

## Conexões
- [[jmeter-listeners-impacto-gerador]] — Veja também: JMeter: limitar listeners pesados durante execução de carga.
- [[jmeter-testplan-versioned-results]] — Veja também: JMeter: versionar plano e propriedades junto com resultado.

## Fontes
- [Apache JMeter — Component Reference](https://jmeter.apache.org/usermanual/component_reference.html) — CSV Data Set, assertions, timers, extractors e controllers; consultado em 2026-10-02.
- [Apache JMeter — Elements of a Test Plan](https://jmeter.apache.org/usermanual/test_plan.html) — Thread Groups, timers, assertions, execução e regras de escopo; consultado em 2026-10-02.
