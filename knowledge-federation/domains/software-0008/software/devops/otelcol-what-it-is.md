---
id: software.devops.tranche01.000001
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
fontes: ["https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md", "https://github.com/open-telemetry/opentelemetry-collector"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# OpenTelemetry Collector: implementação agnóstica a fornecedor para receber, processar e exportar telemetria

## Em uma frase
O README oficial no repositório open-telemetry/opentelemetry-collector explica que o OpenTelemetry Collector fornece uma implementação agnóstica a fornecedor sobre como receber, processar e exportar dados de telemetria, eliminando a necessidade de rodar, operar e manter múltiplos agentes ou coletores distintos para suportar formatos de telemetria open-source (como Jaeger e Prometheus) rumo a múltiplos back-ends open-source ou comerciais.

## Por que importa
Em arquiteturas de microsserviços que evoluem ao longo do tempo, acoplar cada aplicação diretamente ao agente proprietário de um fornecedor obriga a reimplantar todos os serviços quando o back-end de observabilidade muda; centralizar a tradução e o roteamento no Collector isola as aplicações.

## Como funciona
Implante o OpenTelemetry Collector entre os serviços instrumentados e os back-ends de observabilidade para receber múltiplos formatos abertos e exportá-los para um ou mais destinos configurados.

## Exemplo
Um mesmo cluster pode receber métricas no formato Prometheus e traces no formato Jaeger ou OTLP em um único OpenTelemetry Collector e enviá-los simultaneamente para back-ends abertos e comerciais.

## Limites e trade-offs
A lista de componentes disponíveis depende da distribuição utilizada (como a imagem base otel/opentelemetry-collector versus a distribuição ampliada otel/opentelemetry-collector-contrib mencionadas no README).

## Como verificar
Conferi o parágrafo de abertura do README oficial em open-telemetry/opentelemetry-collector.

## Conexões
- [[otelcol-five-core-objectives]] — Veja também: Os cinco objetivos de projeto: Usable, Performant, Observable, Extensible e Unified.

## Fontes
- [OpenTelemetry Collector — README oficial](https://raw.githubusercontent.com/open-telemetry/opentelemetry-collector/main/README.md) — README oficial do OpenTelemetry Collector com proposta vendor-agnostic, cinco objetivos, versão OTLP v1.10.0, política de versões menores N e N-2 do Go, verificação cosign e governança do SIG.; consultado em 2026-10-03.
- [Repositório oficial open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) — Repositório oficial do OpenTelemetry Collector no GitHub com docs/vision.md, docs/security-best-practices.md, código-fonte e releases.; consultado em 2026-10-03.
