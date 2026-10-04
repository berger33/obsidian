---
id: software.devops.tranche13.001284
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

# kube-vip: Balanceamento do Control Plane com IPVS (lb_enable) e Pré-Carregamento de Módulos com SELinux

## Em uma frase
A partir do `kube-vip v0.4.0+`, habilitar `lb_enable: "true"` (`lb_port: "6443"`) configura um balanceador de carga Layer 4 (TCP round-robin) usando **IPVS (IP Virtual Server)** diretamente no espaço de kernel do Linux para distribuir as requisições da API do Kubernetes entre todas as réplicas do control plane.

## Por que importa
Como o servidor virtual do IPVS opera dentro do kernel Linux antes que os pacotes cheguem a um socket TCP de user-space, ele pode escutar na porta `6443` do VIP no mesmo host onde o `kube-apiserver` já escuta na porta `6443` sem causar conflito de porta (`Address already in use`).

## Como funciona
Em nós com **SELinux** em modo `Enforcing` (como RHEL, Rocky Linux, Fedora CoreOS ou OpenShift), o container do `kube-vip` pode ser bloqueado de solicitar carregamento dinâmico de módulos de kernel (`module_request` negado para `container_t`), entrando em `CrashLoopBackOff` com a mensagem `ensure IPVS kernel modules are loaded`. A solução recomendada pela documentação oficial é pré-carregar `ip_vs` e `ip_vs_rr` no host via `/etc/modules-load.d/kube-vip-ipvs.conf`.

## Exemplo
```bash
sudo modprobe ip_vs
sudo modprobe ip_vs_rr
cat << 'EOF' | sudo tee /etc/modules-load.d/kube-vip-ipvs.conf
ip_vs
ip_vs_rr
EOF
```

## Limites e trade-offs
Habilitar o booleano global do SELinux `domain_kernel_load_modules` para todos os containers em vez de pré-carregar apenas `ip_vs` e `ip_vs_rr` no host enfraquece o isolamento de segurança de todos os containers do nó.

## Como verificar
Pré-carregue os módulos `ip_vs` e `ip_vs_rr` em `/etc/modules-load.d/kube-vip-ipvs.conf` em todos os nós que executam o `kube-vip` com IPVS.

## Conexões
- [[kubevip-bgp-layer3-ecmp-rotas-peers-multinodo]] — Veja também: kube-vip: Modo BGP (Layer 3) para Anúncio Multi-Nó de VIPs e Balanceamento ECMP.
- [[kubevip-service-loadbalancer-cloud-provider-ipam-annotations]] — Veja também: kube-vip: Balanceamento de Kubernetes Services (svc_enable) e Integração com kube-vip-cloud-provider.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
