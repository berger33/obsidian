---
id: software.devops.tranche20.001999
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/redpanda-data/connect/main/README.md", "https://docs.redpanda.com/redpanda-connect/about", "https://github.com/redpanda-data/connect"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redpanda Connect `Streams Mode` e `Resources`: execução de múltiplos pipelines independentes em um único processo e API HTTP

## Em uma frase
O **Streams Mode** (`rpk connect streams ./streams/*.yaml`) permite executar **múltiplos pipelines de streaming independentes** dentro de um único processo Redpanda Connect, compartilhando conexões, caches, rate-limiters e processadores declarados em arquivos de **`resources`** (`--resources` / `-r`) e permitindo criar, atualizar ou remover streams em tempo de execução via **REST API (`/streams`)**.

## Por que importa
Quando uma equipe opera 25 pequenos pipelines de integração de baixo volume, subir 25 Deployments separados no Kubernetes (ou 25 VMs) desperdiça memória base e multiplica conexões ociosas com o mesmo cluster Redis ou Kafka.

## Como funciona
No *Streams Mode*, cada arquivo `.yaml` no diretório `./streams/` define um pipeline isolado (`input` -> `pipeline` -> `output`), enquanto `--resources ./resources/*.yaml` carrega componentes compartilhados (`input_resources`, `processor_resources`, `output_resources`, `cache_resources`). A API HTTP na porta `4195` (`GET/POST/PUT/DELETE /streams/<id>`) permite gerenciar o ciclo de vida individual de cada stream sem reiniciar os demais.

## Exemplo
```bash
# Executando múltiplos pipelines em Streams Mode compartilhando um arquivo de recursos comuns:
rpk connect streams --resources ./common/resources.yaml ./streams/*.yaml

# Consultando o status de todos os streams carregados via API HTTP local:
curl -s http://127.0.0.1:4195/streams | jq .
```

## Limites e trade-offs
No *Streams Mode*, a probe global `/ready` verifica a conectividade de todos os streams ativos, enquanto `/streams/<id>/stats` permite inspecionar as métricas isoladas de um stream específico.

## Como verificar
Execute `rpk connect streams --help` e valide seus arquivos de stream e recursos com `rpk connect lint --resources ./common/resources.yaml ./streams/*.yaml`.

## Conexões
- [[benthos-observabilidade-probes-ping-ready-prometheus-opentelemetry-tracing]] — Veja também: Redpanda Connect Observabilidade no Kubernetes: probes `/ping` e `/ready` (`:4195`), métricas Prometheus e traces OpenTelemetry.
- [[benthos-extensibilidade-plugins-go-sdk-inline-overrides-docker-scratch]] — Veja também: Redpanda Connect Extensibilidade e Deploy: plugins customizados em Go (`public/service`), overrides `-s` e imagem OCI `scratch`.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://docs.redpanda.com/redpanda-connect/about) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
