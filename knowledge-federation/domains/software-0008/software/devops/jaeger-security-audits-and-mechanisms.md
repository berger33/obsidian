---
id: software.devops.tranche01.000089
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

# Auditorias de segurança independentes (`jaegertracing/security-audits`) e resumo de mecanismos de segurança

## Em uma frase
A seção Security do README oficial informa que auditorias de segurança do Jaeger conduzidas por terceiros estão publicadas no repositório dedicado `https://github.com/jaegertracing/security-audits` e aponta a Issue `#1718` (`github.com/jaegertracing/jaeger/issues/1718`) para o resumo dos mecanismos de segurança disponíveis no Jaeger, além dos badges de OpenSSF Scorecard, OpenSSF Best Practices (projeto 1273), CLOMonitor e FOSSA no topo do README.

## Por que importa
Traces distribuídos frequentemente carregam metadados de endpoints internos, topologia de serviços e cabeçalhos; ter acesso aos relatórios de auditorias externas em `jaegertracing/security-audits` e ao mapa de mecanismos de autenticação/TLS na Issue `#1718` acelera a homologação de segurança da plataforma de observabilidade.

## Como funciona
Consulte `https://github.com/jaegertracing/security-audits` durante revisões de conformidade e utilize o resumo da Issue `#1718` e a documentação oficial para habilitar TLS e autenticação entre SDKs, Collector, Query e Storage.

## Exemplo
A combinação de auditorias de terceiros publicadas com verificação contínua pelo OpenSSF Scorecard demonstra a governança de segurança exigida de um projeto graduado da CNCF.

## Limites e trade-offs
A imagem `jaegertracing/jaeger:latest` executada no comando de Quick Start local sobe sem TLS/autenticação para facilitar testes rápidos em `localhost`; nunca exponha a porta `16686` ou as portas OTLP na internet pública sem configurar os mecanismos de segurança.

## Como verificar
Conferi a seção Security e os badges de conformidade no README oficial de `jaegertracing/jaeger`.

## Conexões
- [[jaeger-cassandra-and-clickhouse-lts-support-matrix]] — Veja também: Suporte oficial a Apache Cassandra e ClickHouse no Jaeger: versões maiores mantidas e foco em releases LTS.
- [[jaeger-governance-maintainers-and-community-channels]] — Veja também: Governança aberta (`GOVERNANCE.md`, `MAINTAINERS.md`), reuniões de status e canais `#jaeger` e `jaeger-tracing`.

## Fontes
- [Jaeger — README oficial](https://raw.githubusercontent.com/jaegertracing/jaeger/main/README.md) — README oficial do Jaeger com Jaeger v2, Quick Start Docker all-in-one (portas 16686, 4317 e 4318), diagrama de arquitetura, garantia de depreciação (3 meses ou 2 versões menores), política Go (N) e matriz de suporte a Elasticsearch/OpenSearch/Cassandra/ClickHouse.; consultado em 2026-10-03.
- [Jaeger — Getting Started Guide oficial](https://www.jaegertracing.io/docs/latest/getting-started/) — Guia oficial Getting Started da documentação do Jaeger para implantação e uso da plataforma de tracing distribuído.; consultado em 2026-10-03.
