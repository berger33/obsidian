---
id: software.devops.tranche02.000124
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

# Cluster Mesh: descoberta global de serviços e identidade unificada entre clusters

## Em uma frase
A subseção `Cluster Mesh` do `README.rst` descreve como o Cilium Cluster Mesh conecta múltiplos clusters Kubernetes em ambientes híbridos ou multi-cloud, fornecendo dois recursos centrais: **Global service discovery** (cargas de trabalho descobrem e conectam-se a serviços de outros clusters como se fossem locais, permitindo failover automático e compartilhamento de serviços como logging, autenticação ou bancos de dados) e **Unified identity model** (políticas de segurança aplicadas por identidade, e não por endereço IP, através de todos os clusters).

## Por que importa
Conectar clusters sem depender de proxies manuais ou regras de firewall por IP simplifica arquiteturas ativo-ativo e recuperação de desastres entre regiões.

## Como funciona
Configure o Cilium Cluster Mesh entre clusters que precisem de descoberta global de serviços e aplique políticas baseadas em identidade válidas em toda a malha multi-cluster.

## Exemplo
Uma aplicação crítica faz failover transparente para backends em um segundo cluster quando as réplicas locais ficam indisponíveis.

## Limites e trade-offs
O Cluster Mesh requer planejamento de conectividade de rede entre os nós dos clusters participantes e sincronização segura de identidades e certificados.

## Como verificar
Conferi a subseção Cluster Mesh em `README.rst` de `cilium/cilium`.

## Conexões
- [[cilium-ebpf-load-balancing-kube-proxy-replacement]] — Veja também: Balanceamento de carga eBPF L4, substituição do kube-proxy, XDP, DSR e Maglev.
- [[cilium-identity-based-l3-l7-and-dns-network-policy]] — Veja também: Políticas de rede L3–L7 e DNS baseadas em identidade de segurança.

## Fontes
- [Cilium — GitHub README.rst](https://raw.githubusercontent.com/cilium/cilium/main/README.rst) — Visão geral do Cilium (dataplane eBPF, CNI overlay/native/BGP, substituição do kube-proxy, Cluster Mesh, Network Policy L3-L7/DNS, Service Mesh, Hubble, releases estáveis, SBOM SPDX e licenças).; consultado em 2026-10-03.
- [Cilium Documentation — Architecture and Component Overview](https://docs.cilium.io/en/stable/overview/component-overview/) — Documentação oficial de arquitetura, requisitos de sistema e operação do Cilium referenciada no README.; consultado em 2026-10-03.
