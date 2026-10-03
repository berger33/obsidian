---
id: software.devops.tranche02.000126
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

# Service Mesh sem sidecars tradicionais: criptografia IPsec/WireGuard/ztunnel e Gateway API

## Em uma frase
A subseção `Service Mesh` do `README.rst` destaca que o Cilium Service Mesh oferece controle fino de tráfego, criptografia, observabilidade e controle de acesso sem o custo e a complexidade de designs tradicionais baseados em proxies por pod, incluindo **Transparent encryption** (com IPsec, WireGuard ou ztunnel), **L7-aware policy enforcement** e **Deep integration with the Kubernetes Gateway API** (atuando como dataplane compatível com Gateway API para gerenciar ingress, divisão de tráfego e roteamento via CRDs nativas).

## Por que importa
Reduzir a proliferação de proxies sidecar em cada pod economiza memória e CPU no cluster enquanto mantém criptografia transparente de tráfego e suporte ao padrão Kubernetes Gateway API.

## Como funciona
Habilite criptografia transparente (WireGuard, IPsec ou ztunnel) no Cilium e utilize recursos da Kubernetes Gateway API para gerenciar ingress e traffic splitting declarativamente.

## Exemplo
Uma equipe substitui um controlador de Ingress legado pelo dataplane Gateway API embutido no Cilium e ativa criptografia WireGuard entre os nós.

## Limites e trade-offs
Avalie quando sua arquitetura exige apenas o modelo nativo do Cilium ou quando precisa de um service mesh dedicado de sidecars ultraleves como o Linkerd (visto nos itens 131–140 desta tranche).

## Como verificar
Conferi a subseção Service Mesh em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-identity-based-l3-l7-and-dns-network-policy]] — Veja também: Políticas de rede L3–L7 e DNS baseadas em identidade de segurança.
- [[cilium-hubble-observability-and-drop-reasons]] — Veja também: Observabilidade integrada com Hubble, métricas Prometheus e motivos de descarte.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
