---
id: software.devops.tranche05.000408
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

# Monitoramento contínuo de consistência de ponta a ponta com tempo-vulture

## Em uma frase
Na seção *Other components*, o README oficial apresenta o **`tempo-vulture`** (`github.com/grafana/tempo/tree/main/cmd/tempo-vulture`) como a ferramenta de verificação de consistência do Tempo ("Tempo's bird themed consistency checking tool"). O `tempo-vulture` opera como um canário sintético contínuo que grava traces conhecidos no Tempo e em seguida os consulta de volta de diversas maneiras, validando tanto o caminho de escrita (ingestão e flush para object storage) quanto os múltiplos caminhos de leitura e busca (por ID e via TraceQL) e exportando métricas Prometheus sobre eventuais falhas ou inconsistências.

## Por que importa
Em um sistema distribuído de armazenamento eventual que faz buffer em memória/WAL e compacta blocos em object storage, o pipeline de ingestão pode parecer saudável enquanto uma falha silenciosa corrompe a indexação ou a leitura de novos blocos no bucket. O `tempo-vulture` detecta imediatamente qualquer degradação de leitura-após-escrita.

## Como funciona
Implante o `tempo-vulture` junto a clusters Grafana Tempo críticos de produção e configure alertas no Prometheus sobre as métricas de erro de escrita e leitura emitidas pelo canário.

## Exemplo
Em um cluster Tempo multi-zona, o `tempo-vulture` injeta traces sintéticos continuamente e executa consultas de verificação; quando uma permissão IAM incorreta impede os queriers de ler novos objetos no S3, o alerta do `tempo-vulture` aciona a equipe em poucos minutos.

## Limites e trade-offs
Separe o tenant ou os atributos dos traces sintéticos gerados pelo `tempo-vulture` para que eles não poluam as estatísticas de negócio e painéis RED das aplicações reais dos usuários.

## Como verificar
Verifique as métricas Prometheus expostas pelo `tempo-vulture` confirmando taxa zero de falhas nas verificações de escrita e leitura de traces.

## Conexões
- [[tempo-deployment-topologies-compose-helm-and-jsonnet]] — Veja também: Exemplos e modelos de implantação do Tempo com Docker Compose, Helm e Jsonnet (Tanka).
- [[tempo-tempo-cli-operations-and-block-inspection]] — Veja também: Operações administrativas e inspeção de blocos de armazenamento com tempo-cli.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
