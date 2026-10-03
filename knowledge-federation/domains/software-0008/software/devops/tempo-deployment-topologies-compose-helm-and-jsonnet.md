---
id: software.devops.tranche05.000407
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

# Exemplos e modelos de implantação do Tempo com Docker Compose, Helm e Jsonnet (Tanka)

## Em uma frase
A seção *Getting started with Tempo* do README oficial disponibiliza exemplos práticos de implantação em `./example` cobrindo três ferramentas principais de infraestrutura: **Docker Compose** (`./example/docker-compose`) para laboratórios locais completos com Grafana, Prometheus, Loki e Tempo; **Helm** (`./example/helm`) para implantações em Kubernetes (em modo monolítico ou distribuído em microsserviços); e **Jsonnet / Grafana Tanka** (`./example/tk`) para gerenciamento declarativo avançado em clusters de larga escala.

## Por que importa
Equipes precisam validar a correlação completa entre métricas, logs e traces localmente na máquina de desenvolvimento antes de implantar em Kubernetes. Os exemplos oficiais em `./example/docker-compose`, `./example/helm` e `./example/tk` fornecem topologias de referência testadas pelos próprios mantenedores do Tempo.

## Como funciona
Use os exemplos de `./example/docker-compose` para testar instrumentação OpenTelemetry e consultas TraceQL localmente, e adote os Helm charts ou bibliotecas Jsonnet oficiais para implantar o Tempo em produção no Kubernetes.

## Exemplo
Para homologar uma nova versão do pipeline de observabilidade, o engenheiro sobe o ambiente local de `./example/docker-compose`, valida o fluxo de exemplars entre Prometheus, Loki e Tempo e em seguida promove a configuração correspondente no Helm chart de staging.

## Limites e trade-offs
Não utilize a configuração de disco local de nó único dos exemplos de laboratório (`docker-compose`) para cargas produtivas em Kubernetes; em produção, configure sempre um bucket de object storage durável (S3, GCS ou Azure) nos valores do Helm ou Jsonnet.

## Como verificar
Suba o ambiente de referência ou aplique o chart Helm em um namespace de teste e verifique que todos os pods do Tempo atingem o estado `Ready`.

## Conexões
- [[tempo-opentelemetry-native-receiver-wire-and-storage-format]] — Veja também: Arquitetura nativa em OpenTelemetry e ingestão multi-protocolo (OTLP, Jaeger, Zipkin e Kafka).
- [[tempo-tempo-vulture-consistency-checking-tool]] — Veja também: Monitoramento contínuo de consistência de ponta a ponta com tempo-vulture.

## Fontes
- [Grafana Tempo GitHub — README.md (Object Storage Tracing, Traces Drilldown, TraceQL & Apache Parquet)](https://raw.githubusercontent.com/grafana/tempo/main/README.md) — README oficial do Grafana Tempo detalhando operação exclusiva sobre armazenamento de objetos (S3, GCS, Azure ou disco local), integração com Grafana/Prometheus/Loki, app Traces Drilldown, linguagem TraceQL e TraceQL metrics, formato padrão Apache Parquet (Tempo 2.0), compatibilidade OpenTelemetry/Jaeger/Zipkin/Kafka e utilitários tempo-vulture e tempo-cli.; consultado em 2026-10-03.
- [Grafana Tempo Documentation — Getting Started](https://grafana.com/docs/tempo/latest/getting-started/) — Guia oficial de início rápido e operação do Grafana Tempo.; consultado em 2026-10-03.
- [Grafana Tempo — Official GitHub Repository](https://github.com/grafana/tempo) — Repositório oficial do Grafana Tempo distribuído sob AGPL-3.0-only (com exceções Apache-2.0 em LICENSING.md).; consultado em 2026-10-03.
