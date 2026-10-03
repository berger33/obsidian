---
id: software.devops.tranche01.000082
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://www.jaegertracing.io/docs/latest/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Quick Start com a imagem `jaegertracing/jaeger:latest`: UI na porta `16686` e OTLP em `4317` (gRPC) e `4318` (HTTP)

## Em uma frase
A seção Quick Start do README oficial mostra como subir o Jaeger em segundos com Docker usando a distribuição all-in-one (que inclui UI, collector, query e armazenamento em memória): `docker run --rm --name jaeger -p 16686:16686 -p 4317:4317 -p 4318:4318 jaegertracing/jaeger:latest`, acessando a interface web em `http://localhost:16686` e enviando traces via protocolo OTLP usando gRPC na porta `4317` ou HTTP na porta `4318`.

## Por que importa
Receber traces diretamente nas portas padrão do protocolo OTLP (`4317` para gRPC e `4318` para HTTP) significa que qualquer aplicação instrumentada com os SDKs padrão do OpenTelemetry pode apontar seu exporter OTLP direto para o contêiner do Jaeger sem precisar de bibliotecas clientes legadas específicas do Jaeger.

## Como funciona
Para desenvolvimento local e testes de instrumentação, execute o comando `docker run` expondo as portas `16686`, `4317` e `4318`, configure o exporter OTLP da sua aplicação para `localhost:4317` (gRPC) ou `localhost:4318` (HTTP) e inspecione os traces em `http://localhost:16686`.

## Exemplo
Um único contêiner `jaegertracing/jaeger:latest` empacota o collector, o serviço de query, a Jaeger UI e o armazenamento in-memory para uso imediato.

## Limites e trade-offs
Como o próprio comentário do comando destaca, o modo all-in-one utiliza armazenamento em memória (in-memory storage); para implantações de produção com persistência e escalabilidade, consulte o Getting Started Guide (`jaegertracing.io/docs/latest/getting-started/`).

## Como verificar
Conferi a seção Quick Start no README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-what-it-is-and-cncf-history]] — Veja também: Jaeger: plataforma de rastreamento distribuído criada na Uber e graduada na CNCF (com Jaeger v2).
- [[jaeger-architecture-components-and-data-flow]] — Veja também: Arquitetura de componentes do Jaeger: OpenTelemetry SDK, Collector, Storage/Plugin, Query Service e UI.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Jaeger — Getting Started Guide oficial](https://www.jaegertracing.io/docs/latest/getting-started/) — Guia oficial Getting Started da documentação do Jaeger para implantação e uso da plataforma de tracing distribuído.; consultado em 2026-10-03.
