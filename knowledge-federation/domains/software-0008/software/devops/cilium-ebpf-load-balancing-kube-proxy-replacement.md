---
id: software.devops.tranche02.000123
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

# Balanceamento de carga eBPF L4, substituição do kube-proxy, XDP, DSR e Maglev

## Em uma frase
A subseção `Load Balancing` do `README.rst` explica que o Cilium implementa balanceamento de carga distribuído usando tabelas hash eficientes em eBPF, dividindo-o em **East-west load balancing** — que reescreve conexões de serviço no nível do socket (`connect()`), evitando o overhead de NAT pacote a pacote e substituindo totalmente o `kube-proxy` — e **North-south load balancing**, que suporta XDP para cenários de alto throughput, Direct Server Return (DSR) e hashing consistente Maglev.

## Por que importa
Em clusters com milhares de `Services`, a atualização linear de regras `iptables` pelo `kube-proxy` torna-se um gargalo severo de CPU e latência; o uso de tabelas hash eBPF no `connect()` e XDP resolve esse limite de escala.

## Como funciona
Ative o modo de substituição completa do `kube-proxy` no Cilium e avalie XDP, DSR e Maglev para tráfego norte-sul de alta vazão.

## Exemplo
Um cluster de microsserviços elimina o `kube-proxy` e passa a realizar o balanceamento leste-oeste diretamente na chamada `connect()` via eBPF.

## Limites e trade-offs
Substituir o `kube-proxy` exige que os nós atendam aos requisitos de kernel para cgroup-ebpf no nível de socket; valide com `cilium status` após a ativação.

## Como verificar
Conferi a subseção Load Balancing em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-cni-overlay-native-routing-and-bgp]] — Veja também: Modos de operação CNI: overlay (VXLAN/Geneve), roteamento nativo e BGP/L2.
- [[cilium-cluster-mesh-multicluster-service-discovery]] — Veja também: Cluster Mesh: descoberta global de serviços e identidade unificada entre clusters.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
