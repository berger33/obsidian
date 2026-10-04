---
id: software.devops.tranche02.000127
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
fontes: ["https://raw.githubusercontent.com/cilium/cilium/main/README.rst", "https://docs.cilium.io/en/stable/overview/component-overview/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Observabilidade integrada com Hubble, métricas Prometheus e motivos de descarte

## Em uma frase
A subseção `Observability and Troubleshooting` do `README.rst` apresenta os três pilares de visibilidade construídos desde a base no Cilium: **Hubble** (plataforma de observabilidade integrada que oferece mapas de serviços em tempo real, visibilidade de fluxos com metadados de identidade e labels, filtragem ciente de DNS e insights por protocolo), **Metrics and alerting** (integração com Prometheus, Grafana e outros sistemas) e **Drop reasons and audit trails** (insights acionáveis sobre por que o tráfego foi descartado, incluindo violações de política ou porta e falhas de lookup DNS).

## Por que importa
Diagnosticar falhas de conectividade em Kubernetes com `tcpdump` bruto é lento porque IPs mudam constantemente; o Hubble traduz os fluxos diretamente em identidades, pods, serviços, consultas DNS e razão exata de drop.

## Como funciona
Habilite o Hubble e a exportação de métricas Prometheus no Cilium para inspecionar fluxos negados por `NetworkPolicy` ou erros de DNS em tempo real.

## Exemplo
Ao investigar um timeout entre dois microsserviços, o engenheiro consulta o Hubble e identifica imediatamente um descarte por violação de política L7 no caminho HTTP.

## Limites e trade-offs
Retenção histórica longa de métricas do Prometheus geradas pelo Cilium/Hubble pode ser combinada com Thanos (itens 151–160) e logs de auditoria com Loki (itens 161–170).

## Como verificar
Conferi a subseção Observability and Troubleshooting em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-service-mesh-encryption-and-gateway-api]] — Veja também: Service Mesh sem sidecars tradicionais: criptografia IPsec/WireGuard/ztunnel e Gateway API.
- [[cilium-stable-releases-and-three-minor-support-policy]] — Veja também: Política de manutenção das três últimas versões menores estáveis do Cilium.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
