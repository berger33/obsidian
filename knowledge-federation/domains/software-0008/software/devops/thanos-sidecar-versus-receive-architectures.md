---
id: software.devops.tranche02.000156
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/thanos-io/thanos/main/README.md", "https://thanos.io/tip/thanos/getting-started.md/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Arquiteturas de implantação no Kubernetes: modelo com Sidecar versus modelo com Receive

## Em uma frase
A seção `Architecture Overview` do README apresenta os dois modelos clássicos de implantação do Thanos para Kubernetes: **Deployment with Sidecar for Kubernetes** (no qual o Thanos roda acoplado ao servidor Prometheus existente) e **Deployment with Receive** (voltado a escalar horizontalmente — scale out — ou integrar outras fontes compatíveis com `remote write` do Prometheus).

## Por que importa
Em clusters onde o Prometheus já raspa os alvos locais e possui disco para blocos recentes, o modelo `Sidecar` é o menos intrusivo; já em ambientes multi-tenant, borda ou coletores que apenas fazem push via Prometheus Remote Write (como OpenTelemetry Collector, Alloy, Fluent Bit ou Vector), o modelo `Receive` centraliza a ingestão.

## Como funciona
Escolha a arquitetura `Sidecar` quando quiser estender servidores Prometheus completos por cluster ou a arquitetura `Receive` quando precisar receber fluxos `remote_write` em escala.

## Exemplo
Clusters de borda com poucos recursos enviam métricas via `remote_write` para um cluster central rodando Thanos `Receive`, enquanto clusters de datacenter principais usam o modelo `Sidecar`.

## Limites e trade-offs
O componente `Receive` recebe séries ativas via push e exige dimensionamento cuidadoso de memória, disco local e anel de hashing (hashring) conforme o volume de séries ativas.

## Como verificar
Conferi a seção Architecture Overview no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-grpc-store-api-unified-data-access]] — Veja também: API gRPC Store API simples para acesso unificado a dados e provedores customizados.
- [[thanos-unix-and-golang-design-philosophy]] — Veja também: Filosofia UNIX e Go no design do Thanos: um binário com subcomandos coesos.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
