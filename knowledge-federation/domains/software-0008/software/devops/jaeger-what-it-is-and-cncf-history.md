---
id: software.devops.tranche01.000081
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://www.jaegertracing.io/docs/latest/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Jaeger: plataforma de rastreamento distribuído criada na Uber e graduada na CNCF (com Jaeger v2)

## Em uma frase
O README oficial no repositório jaegertracing/jaeger apresenta o Jaeger como uma plataforma de rastreamento distribuído (distributed tracing) criada pela Uber Technologies e doada à Cloud Native Computing Foundation (CNCF), onde ingressou em incubação em setembro de 2017 e graduou-se em outubro de 2019 como o 7º projeto top-level da fundação, destacando no topo o lançamento do **Jaeger v2** e a licença Apache 2.0.

## Por que importa
Em arquiteturas distribuídas onde uma única requisição de usuário atravessa dezenas de serviços, filas e bancos de dados, logs isolados por processo não mostram onde está o gargalo de latência ou qual chamada remota falhou; o rastreamento distribuído reconstrói o caminho ponta a ponta de cada transação.

## Como funciona
Consulte o guia oficial `https://www.jaegertracing.io/docs/latest/getting-started/` para experimentar o Jaeger v2 localmente ou planejar a implantação dos componentes em produção.

## Exemplo
Como documentado na seção Version Compatibility Guarantees do README, o Jaeger utiliza muitos componentes do **OpenTelemetry Collector**, alinhando sua arquitetura moderna diretamente ao ecossistema OpenTelemetry.

## Limites e trade-offs
O projeto mantém documentação publicada em `https://www.jaegertracing.io/docs/` (cujo código-fonte fica em `github.com/jaegertracing/documentation`) e lista pública de organizações adotantes em `ADOPTERS.md`.

## Como verificar
Conferi a abertura, a seção Architecture e as seções finais do README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-docker-all-in-one-quickstart-ports]] — Veja também: Quick Start com a imagem `jaegertracing/jaeger:latest`: UI na porta `16686` e OTLP em `4317` (gRPC) e `4318` (HTTP).

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Jaeger — Getting Started Guide oficial](https://www.jaegertracing.io/docs/latest/getting-started/) — Guia oficial Getting Started da documentação do Jaeger para implantação e uso da plataforma de tracing distribuído.; consultado em 2026-10-03.
