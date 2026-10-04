---
id: software.devops.tranche05.000405
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/grafana/tempo/main/README.md", "https://grafana.com/docs/tempo/latest/getting-started/", "https://github.com/grafana/tempo"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Apache Parquet como formato colunar padrão de armazenamento a partir do Grafana Tempo 2.0

## Em uma frase
A seção de leitura complementar do README oficial destaca o marco arquitetural do **Grafana Tempo 2.0**: a adoção do **Apache Parquet como formato padrão de armazenamento** (`Apache Parquet as the default storage format`), que viabilizou o desempenho de busca estruturada do TraceQL sobre armazenamento de objetos. Ao organizar os atributos e spans em colunas tipadas com dicionários e estatísticas de bloco dentro de arquivos Parquet no S3/GCS/Azure, os queriers do Tempo conseguem ler apenas as colunas referenciadas na consulta TraceQL e descartar blocos inteiros que não contêm os valores buscados.

## Por que importa
Em formatos baseados em linhas ou blobs opacos, buscar um atributo específico exige ler e desserializar 100% dos bytes de todos os traces do período. O layout colunar Apache Parquet reduz drasticamente os bytes lidos do object storage e acelera em ordens de grandeza as consultas TraceQL.

## Como funciona
Mantenha seus clusters Tempo atualizados na geração 2.x+ utilizando o formato de bloco Parquet padrão e ajuste os parâmetros de compactação (`compactor`) para manter blocos Parquet bem dimensionados no bucket de objetos.

## Exemplo
Durante uma busca TraceQL por `span.http.status_code = 503` em terabytes de traces no S3, os queriers do Tempo inspecionam apenas os metadados e a coluna de status HTTP dos arquivos Apache Parquet, retornando os resultados em segundos.

## Limites e trade-offs
Não desabilite o componente `compactor` do Tempo em produção: sem compactação regular dos blocos Parquet recém-descarregados pelos ingesters, a fragmentação de pequenos objetos no bucket degrada a performance de leitura e aumenta custos de chamadas de API no S3/GCS.

## Como verificar
Inspecione a configuração de armazenamento do Tempo e as métricas do compactador e dos queriers confirmando o uso dos blocos no formato Apache Parquet padrão.

## Conexões
- [[tempo-traceql-metrics-ad-hoc-aggregation]] — Veja também: Geração ad-hoc de métricas a partir de traces com TraceQL metrics no Tempo.
- [[tempo-opentelemetry-native-receiver-wire-and-storage-format]] — Veja também: Arquitetura nativa em OpenTelemetry e ingestão multi-protocolo (OTLP, Jaeger, Zipkin e Kafka).

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
