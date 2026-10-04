---
id: software.devops.tranche01.000083
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
fontes: ["https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md", "https://github.com/jaegertracing/jaeger"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquitetura de componentes do Jaeger: OpenTelemetry SDK, Collector, Storage/Plugin, Query Service e UI

## Em uma frase
O diagrama Mermaid da seção Architecture no README oficial mapeia o fluxo completo de dados e controle: o **OpenTelemetry SDK** dentro da aplicação do usuário (no Application Host) envia dados por HTTP ou gRPC ao **Jaeger Collector** (que também pode responder configurações de sampling via `gRPC/sampling` ao SDK); o Collector grava diretamente no **Storage** ou via gRPC em um **Storage Plugin** que acessa o Storage; o **Jaeger Query Service** lê do Storage (diretamente ou via gRPC no Storage Plugin); e a **Jaeger UI** consulta o Query Service via HTTP.

## Por que importa
Separar o caminho de escrita (Collector -> Storage/Plugin) do caminho de leitura e visualização (UI -> HTTP -> Query Service -> Storage/Plugin) permite escalar os coletores de acordo com a taxa de ingestão de spans das aplicações sem degradar a interface de consulta usada pelos engenheiros durante um incidente.

## Como funciona
Em ambientes de produção, dimensione o Jaeger Collector para a carga de escrita vinda dos OpenTelemetry SDKs, escolha um backend de Storage suportado (nativo ou via Storage Plugin gRPC) e exponha a Jaeger UI conectada ao Jaeger Query Service.

## Exemplo
O diagrama também evidencia dois repositórios relacionados listados no README: a interface web em `github.com/jaegertracing/jaeger-ui` e o modelo de dados em `github.com/jaegertracing/jaeger-idl`.

## Limites e trade-offs
Observe no diagrama que o canal entre o Jaeger Collector e o OpenTelemetry SDK inclui também `gRPC/sampling` para estratégias de amostragem controlada remotamente.

## Como verificar
Conferi o diagrama Mermaid da seção Architecture e a seção Related Repositories no README oficial.

## Conexões
- [[jaeger-docker-all-in-one-quickstart-ports]] — Veja também: Quick Start com a imagem `jaegertracing/jaeger:latest`: UI na porta `16686` e OTLP em `4317` (gRPC) e `4318` (HTTP).
- [[jaeger-config-deprecation-grace-period-policy]] — Veja também: Garantia de compatibilidade de configuração: carência mínima de 3 meses ou duas versões menores.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Repositório oficial jaegertracing/jaeger](https://github.com/jaegertracing/jaeger) — Repositório oficial do Jaeger no GitHub com código-fonte, GOVERNANCE.md, MAINTAINERS.md, CONTRIBUTING.md e ADOPTERS.md.; consultado em 2026-10-03.
