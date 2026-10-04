---
id: software.devops.tranche02.000152
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

# Formato de armazenamento do Prometheus 2.0 e Object Storage como única dependência opcional

## Em uma frase
A seção `Overview` e a seção `Features` do README explicam que o Thanos aproveita o formato de armazenamento do Prometheus 2.0 (`Prometheus 2.0 storage format`) para armazenar dados históricos de métricas com eficiência de custo em qualquer armazenamento de objetos (`any object storage`), mantendo baixas latências de consulta e tendo o Object Storage como sua única — e opcional — dependência externa.

## Por que importa
Não exigir bancos de dados NoSQL complexos ou clusters de indexação dedicados reduz drasticamente o custo operacional de reter terabytes de séries temporais históricas: basta um bucket de objetos padrão na nuvem ou on-premises.

## Como funciona
Configure um bucket de Object Storage compatível para receber os blocos TSDB do Prometheus 2.0 quando precisar de retenção histórica além do disco local dos pods do Prometheus.

## Exemplo
Caso uma equipe queira inicialmente apenas visão global de consulta e deduplicação HA sem retenção longa, ela pode operar o Thanos mesmo sem Object Storage, pois a dependência é opcional.

## Limites e trade-offs
Dimensione políticas de ciclo de vida e permissões de leitura/escrita do bucket de objetos e nunca faça dois clusters escreverem os mesmos blocos sem rótulos externos (`external_labels`) exclusivos por instância Prometheus.

## Como verificar
Conferi as seções Overview e Features no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-ha-prometheus-global-query-unlimited-storage]] — Veja também: Definição do Thanos e os três objetivos centrais sobre o Prometheus 2.0.
- [[thanos-global-query-view-and-ha-deduplication]] — Veja também: Visão global de consulta, deduplicação de pares Prometheus HA e federação multi-cluster.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
