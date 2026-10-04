---
id: software.devops.tranche13.001290
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

# kube-vip: Geração de Manifestos (kube-vip manifest pod / daemonset), RBAC e Upgrade In-Place

## Em uma frase
O binário do `kube-vip` inclui um gerador embutido de manifestos (`kube-vip manifest pod` para Static Pods no `kubeadm` e `kube-vip manifest daemonset` para K3s/clusters existentes) que produz o YAML completo com `hostNetwork: true` e as capabilities Linux requeridas (`NET_ADMIN`, `NET_RAW`).

## Por que importa
Escrever manualmente o manifesto de Static Pod para `/etc/kubernetes/manifests/kube-vip.yaml` durante o bootstrap do primeiro nó `kubeadm init` é propenso a erros no caminho do `/etc/kubernetes/super-admin.conf` (ou `admin.conf`).

## Como funciona
No primeiro nó de control plane (`kubeadm` v1.29+), aponta-se o volume `kubeconfig` do Static Pod inicialmente para `/etc/kubernetes/super-admin.conf` durante o `kubeadm init` (trocando para `/etc/kubernetes/admin.conf` após a criação do RBAC), enquanto para `DaemonSet` aplica-se primeiro `https://kube-vip.io/manifests/rbac.yaml`.

## Exemplo
```bash
kubectl apply -f https://kube-vip.io/manifests/rbac.yaml
docker run --network host --rm ghcr.io/kube-vip/kube-vip:v0.8.0 \
  manifest daemonset \
  --interface eth0 \
  --address 192.168.1.100 \
  --controlplane \
  --services \
  --arp \
  --leaderElection
```

## Limites e trade-offs
Remover os manifests de Static Pod de todos os nós do control plane ao mesmo tempo durante um upgrade in-place do `kube-vip` derruba o endereço VIP `6443` e interrompe todas as conexões de `kubectl` e dos `kubelets`.

## Como verificar
Atualize a imagem do `kube-vip` um nó de control plane por vez, aguardando a transição limpa do lease de líder para outro nó antes de atualizar o próximo.

## Conexões
- [[kubevip-eleicao-lider-por-service-arp-distribuicao-carga]] — Veja também: kube-vip: Eleição de Líder por Service (svc_election) para Distribuir VIPs ARP entre Worker Nodes.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
