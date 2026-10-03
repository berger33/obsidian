---
id: software.devops.tranche02.000155
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

# API gRPC Store API simples para acesso unificado a dados e provedores customizados

## Em uma frase
A seção `Features` e a seção `Thanos Philosophy` do README destacam a existência de uma simples API gRPC chamada `"Store API"` para acesso unificado a todos os dados de métricas (`Simple gRPC "Store API" for unified data access across all metric data`), oferecendo pontos fáceis de integração para provedores customizados de métricas e permitindo que o `thanos query` faça proxy de chamadas recebidas para endpoints Store API conhecidos, fundindo o resultado.

## Por que importa
Ao padronizar uma única interface gRPC (`Store API`) para dados em memória recente (Sidecar/Receive), dados históricos em Object Storage (Store Gateway) e outras fontes, o camada de consulta não precisa saber onde cada janela de tempo está armazenada.

## Como funciona
Conecte todos os seus produtores e gateways de métricas como endpoints da `Store API` ao `thanos query` via gRPC (com mTLS ou dentro da malha segura do cluster).

## Exemplo
Uma consulta PromQL de 30 dias no `thanos query` combina automaticamente as últimas horas vindas do Sidecar do Prometheus com os 29 dias anteriores lidos do Object Storage via `Store API`.

## Limites e trade-offs
Proteja e monitore a latência das conexões gRPC entre o `thanos query` e os endpoints da `Store API`, configurando timeouts e limites de concorrência adequados.

## Como verificar
Conferi as seções Features e Thanos Philosophy no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-downsampling-historical-data-query-speedup]] — Veja também: Downsampling de dados históricos para aceleração massiva de consultas.
- [[thanos-sidecar-versus-receive-architectures]] — Veja também: Arquiteturas de implantação no Kubernetes: modelo com Sidecar versus modelo com Receive.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
