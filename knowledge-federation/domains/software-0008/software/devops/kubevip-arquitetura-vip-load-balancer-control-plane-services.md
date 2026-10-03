---
id: software.devops.tranche13.001281
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md", "https://kube-vip.io/docs/about/architecture/", "https://github.com/kube-vip/kube-vip"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kube-vip: Arquitetura de Virtual IP (VIP) e Load Balancer para Control Plane e Services Kubernetes

## Em uma frase
O **kube-vip** (`kube-vip/kube-vip`) é uma solução autocontida escrita em Go que fornece tanto um endereço IP Virtual (VIP IPv4 ou IPv6) de alta disponibilidade para o **control plane do Kubernetes** quanto balanceamento de carga para **Kubernetes Services do tipo `LoadBalancer`** em ambientes bare-metal, virtualizados e edge (x86, ARM, Raspberry Pi, ppc64le).

## Por que importa
Tradicionalmente, montar um control plane altamente disponível em bare-metal exigia combinar e manter pelo menos duas ferramentas externas separadas nos hosts (como `Keepalived` ou `UCARP` para o VIP flutuante mais `HAProxy` ou `Nginx` para o balanceamento TCP na porta 6443).

## Como funciona
O `kube-vip` consolida a gestão do VIP (via **ARP Layer 2** com eleição de líder ou **BGP Layer 3** multi-nó) e o balanceamento de carga (via **IPVS** em espaço de kernel) em um único container enxuto, podendo rodar como **Static Pod** (em clusters `kubeadm` em `/etc/kubernetes/manifests/`) ou como **DaemonSet** (em K3s, RKE2 e distribuições similares).

## Exemplo
```bash
# Verificar pods do kube-vip operando no namespace kube-system:
kubectl -n kube-system get pods -l app.kubernetes.io/name=kube-vip -o wide
```

## Limites e trade-offs
Executar simultaneamente o `kube-vip` como Static Pod e como DaemonSet no mesmo nó configurando o mesmo endereço VIP do control plane gera conflito de posse da interface e instabilidade de ARP/BGP.

## Como verificar
Escolha uma única topologia de implantação para o control plane (Static Pod para `kubeadm` ou DaemonSet para K3s) e separe claramente as flags de control plane (`cp_enable`) e de services (`svc_enable`).

## Conexões
- [[kubevip-arp-layer2-leader-election-gratuitous-arp-failover]] — Veja também: kube-vip: Modo ARP (Layer 2), Eleição de Líder e Failover Rápido com Gratuitous ARP.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
