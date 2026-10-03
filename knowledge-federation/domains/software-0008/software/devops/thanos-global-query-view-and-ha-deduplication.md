---
id: software.devops.tranche02.000153
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

# Visão global de consulta, deduplicação de pares Prometheus HA e federação multi-cluster

## Em uma frase
A seção `Features` do README destaca quatro capacidades de consulta distribuída do Thanos: visão global de consulta através de todos os servidores Prometheus conectados (`Global querying view`), deduplicação e fusão em tempo real de métricas coletadas por pares Prometheus em alta disponibilidade (`Deduplication and merging of metrics collected from Prometheus HA pairs`), federação entre clusters (`Cross-cluster federation`) e roteamento de consultas tolerante a falhas (`Fault-tolerant query routing`).

## Por que importa
Quando duas réplicas idênticas do Prometheus raspam os mesmos alvos para garantir alta disponibilidade, consultar ambas sem deduplicação dobra ou embaralha séries; o Thanos funde as séries em tempo de consulta de forma transparente para o Grafana.

## Como funciona
Aponte a fonte de dados Prometheus do Grafana para o endpoint do `thanos query` com deduplicação ativada, identificando cada réplica do par HA por um rótulo externo de réplica.

## Exemplo
Se a réplica `prometheus-a` falhar durante uma janela de manutenção, o `thanos query` preenche automaticamente a série com os dados da réplica `prometheus-b` sem lacunas nos gráficos.

## Limites e trade-offs
Para que a deduplicação funcione corretamente, cada servidor Prometheus deve ter `external_labels` únicos identificando o cluster e o identificador da réplica HA.

## Como verificar
Conferi os itens Global querying view, Deduplication and merging, Cross-cluster federation e Fault-tolerant query routing na seção Features do README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-prometheus-2-storage-format-and-object-storage]] — Veja também: Formato de armazenamento do Prometheus 2.0 e Object Storage como única dependência opcional.
- [[thanos-downsampling-historical-data-query-speedup]] — Veja também: Downsampling de dados históricos para aceleração massiva de consultas.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
