---
id: software.devops.tranche02.000151
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

# Definição do Thanos e os três objetivos centrais sobre o Prometheus 2.0

## Em uma frase
O README oficial no repositório `thanos-io/thanos` define o Thanos como um conjunto de componentes que podem ser compostos em um sistema de métricas altamente disponível com capacidade de armazenamento ilimitada, adicionado de forma transparente sobre implantações existentes do Prometheus, sendo um projeto Incubating da CNCF com três objetivos concretos: **1. Global query view of metrics**, **2. Unlimited retention of metrics** e **3. High availability of components, including Prometheus**.

## Por que importa
Uma instância isolada do Prometheus armazena dados localmente em disco e não faz federação horizontal nem retenção de longo prazo em armazenamento de objetos por conta própria; o Thanos resolve essas três limitações sem exigir abandonar o Prometheus.

## Como funciona
Adicione os componentes do Thanos sobre seus servidores Prometheus existentes para unificar consultas entre clusters, deduplicar réplicas em alta disponibilidade e arquivar blocos históricos em Object Storage.

## Exemplo
Uma organização com dezenas de clusters Kubernetes mantém um par Prometheus HA em cada cluster e adiciona o Thanos para consulta global unificada e retenção de anos em armazenamento de objetos.

## Limites e trade-offs
O Thanos não substitui o coletor/scraper local: ele aproveita o formato de armazenamento do Prometheus 2.0 para estender sua disponibilidade e retenção.

## Como verificar
Conferi a seção Overview no README oficial de `thanos-io/thanos`.

## Conexões
- [[thanos-prometheus-2-storage-format-and-object-storage]] — Veja também: Formato de armazenamento do Prometheus 2.0 e Object Storage como única dependência opcional.

## Fontes
- [Thanos — GitHub README](https://raw.githubusercontent.com/thanos-io/thanos/main/README.md) — Visão geral do Thanos (CNCF Incubating), objetivos sobre o formato Prometheus 2.0, deduplicação HA, Store API gRPC, arquiteturas Sidecar vs Receive, filosofia UNIX/Go e releases a cada 6 semanas.; consultado em 2026-10-03.
- [Thanos Documentation — Getting Started & Design](https://thanos.io/tip/thanos/getting-started.md/) — Documentação oficial de introdução e design arquitetural do Thanos referenciada no README.; consultado em 2026-10-03.
