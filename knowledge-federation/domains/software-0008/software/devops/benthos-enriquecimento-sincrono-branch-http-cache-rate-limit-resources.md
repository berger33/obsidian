---
id: software.devops.tranche20.001996
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
fontes: ["https://docs.redpanda.com/redpanda-connect/about", "https://raw.githubusercontent.com/redpanda-data/connect/main/README.md", "https://github.com/redpanda-data/connect"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Redpanda Connect `branch`, `cache` e `rate_limit`: enriquecimento de eventos com APIs externas e caches compartilhados (`redis`/`s3`)

## Em uma frase
O processador **`branch`** do Redpanda Connect permite extrair um subconjunto de campos de uma mensagem (`request_map`), executar uma cadeia de processadores externos (como uma chamada **`http`**, query **`sql_select`**, invocação **`aws_lambda`** ou inferência **`aws_bedrock_chat`**) protegida por **`cache`** e **`rate_limit`**, e mesclar apenas o resultado de volta no documento original (`result_map`).

## Por que importa
Se você executasse um processador `http` diretamente sem `branch`, o corpo inteiro da mensagem atual seria enviado no `POST` e a resposta da API sobrescreveria a mensagem original inteira, perdendo os demais campos do evento.

## Como funciona
Combinando `branch` com recursos nomeados declarados em `cache_resources` (ex.: `redis`, `memory`, `aws_s3`, `aws_dynamodb`) e `rate_limit_resources`, o pipeline consulta primeiro o cache Redis; apenas em caso de *cache miss* chama a API HTTP respeitando o limite de taxa e grava no cache para os próximos eventos.

## Exemplo
```yaml
pipeline:
  processors:
    - branch:
        request_map: 'root = ""'
        processors:
          - http:
              url: 'http://GeoIP-service.internal/lookup/${! json("client_ip") }'
              verb: GET
              rate_limit: geoip_limiter
        result_map: 'root.geo = this'

rate_limit_resources:
  - label: geoip_limiter
    local:
      count: 500
      interval: 1s
```

## Limites e trade-offs
Utilize sempre `branch` (com `request_map` enxuto e `result_map` específico) quando precisar enriquecer eventos com chamadas HTTP, SQL ou modelos de IA sem perder o payload original da mensagem.

## Como verificar
Teste o enriquecimento `branch` simulando respostas com `rpk connect test`.

## Conexões
- [[benthos-batching-windowing-agrupamento-alto-throughput-s3-clickhouse]] — Veja também: Redpanda Connect Batching e Micro-Batching: configuração de `batching` (`count`, `byte_size`, `period`) e `archive` para S3 e ClickHouse.
- [[benthos-testes-unitarios-pipelines-rpk-connect-test-assertions]] — Veja também: Redpanda Connect Unit Testing (`rpk connect test`): testes unitários determinísticos de pipelines e mapeamentos YAML em CI/CD.

## Fontes
- [Redpanda Connect GitHub — README.md (Declarative Stream Processor, At-Least-Once Transaction Model, CDC to Iceberg, /ping & /ready Probes)](https://docs.redpanda.com/redpanda-connect/about) — README oficial do redpanda-data/connect detalhando instalação, execução via Docker/CLI, exemplo de Postgres CDC para Iceberg, probes HTTP e SDK de extensibilidade em Go; consultado em 2026-10-03.
- [Redpanda Connect Official Documentation — About Redpanda Connect (Bloblang Mapping, Stateless In-Process Transactions, Batching, Branching & Observability)](https://raw.githubusercontent.com/redpanda-data/connect/main/README.md) — Documentação oficial de arquitetura do Redpanda Connect / Benthos cobrindo garantias de entrega, Bloblang, conectores e operação cloud-native; consultado em 2026-10-03.
- [Redpanda Connect (Benthos) — Official GitHub Repository](https://github.com/redpanda-data/connect) — Repositório oficial do Redpanda Connect / Benthos; consultado em 2026-10-03.
