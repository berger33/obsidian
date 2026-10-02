---
id: software.testes.tranche08.000211
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data", "https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ML: detectar divergência entre transformação de treino e serving

## Em uma frase
Reutilize ou compare transformações de treino e serving para detectar diferenças de feature antes da implantação.

## Por que importa
Uma mesma entrada pode receber valores diferentes em pipelines distintos, tornando a predição online incompatível com a distribuição que treinou o modelo.

## Como funciona
Crie fixtures com entradas e saídas esperadas, compare transformações em lote e online e acompanhe estatísticas de features em execução.

## Exemplo
Uma data em UTC e local atravessa ambos os caminhos; o teste confere que bucket temporal e normalização têm o mesmo resultado.

## Limites e trade-offs
Paridade em fixtures não cobre todo dado vivo; monitoramento de produção é necessário para padrões que os exemplos não representam.

## Como verificar
Execute casos de fronteira e históricos representativos no pipeline de treino e serving; alerte quando distribuições comparáveis divergem além de limiar definido.

## Conexões
- [[ml-batch-online-paridade-predicoes]] — Veja também: ML: comparar predição batch e online.
- [[ml-monitoring-drift-feature-label]] — Veja também: ML: monitorar drift sem confundir com queda de qualidade.

## Fontes
- [Google ML — Transforming data](https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data) — transformação de dados e riscos de discrepância entre treino e serving; consultado em 2026-10-02.
- [Google ML — Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) — schema, training-serving skew, leakage e métricas de produção; consultado em 2026-10-02.
