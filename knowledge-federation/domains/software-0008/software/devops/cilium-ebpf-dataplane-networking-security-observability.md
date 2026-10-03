---
id: software.devops.tranche02.000121
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

# Dataplane baseado em eBPF para rede, observabilidade e segurança graduado na CNCF

## Em uma frase
O arquivo `README.rst` oficial no repositório `cilium/cilium` define o Cilium como uma solução de rede, observabilidade e segurança com um dataplane baseado em eBPF, graduada na CNCF (`CNCF Graduated Project`), que insere dinamicamente bytecode eBPF no kernel Linux em pontos como I/O de rede, sockets de aplicação e tracepoints.

## Por que importa
Ao executar a lógica de encaminhamento, segurança e visibilidade diretamente no kernel Linux via eBPF em vez de depender de longas cadeias de regras `iptables`, o cluster reduz latência de rede e ganha escalabilidade para milhares de serviços e pods.

## Como funciona
Implante o Cilium como camada de rede e segurança do cluster Kubernetes, verificando previamente os requisitos de versão do kernel Linux na documentação oficial (`docs.cilium.io`).

## Exemplo
Uma plataforma Kubernetes de alta densidade adota o Cilium para unificar CNI, políticas de segurança L3–L7 e observabilidade de fluxos sobre eBPF.

## Limites e trade-offs
Funcionalidades avançadas de eBPF exigem kernels Linux modernos e permissões adequadas nos nós; valide os pré-requisitos do sistema antes da instalação.

## Como verificar
Conferi a abertura de `README.rst` no repositório `cilium/cilium`.

## Conexões
- [[cilium-cni-overlay-native-routing-and-bgp]] — Veja também: Modos de operação CNI: overlay (VXLAN/Geneve), roteamento nativo e BGP/L2.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
