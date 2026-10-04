---
id: software.devops.tranche09.000812
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/k3s-io/k3s/main/README.md", "https://docs.k3s.io/architecture", "https://github.com/k3s-io/k3s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K3s: pilha de tecnologias embutidas (containerd, Flannel, CoreDNS, Traefik, Klipper-lb, Kube-router e utilitários de host)

## Em uma frase
O binário único do K3s empacota de forma coesa `containerd` e `runc`, `Flannel` (CNI), `CoreDNS`, `Metrics Server`, `Traefik` (Ingress), `Klipper-lb` (ServiceLB), `Kube-router` (NetworkPolicy), `Helm-controller`, `Kine`, `Local-path-provisioner` e utilitários de host (`k3s-root`).

## Por que importa
No Kubernetes vanilla (`kubeadm`), após inicializar o control plane o cluster ainda não tem rede de pods (CNI), não tem Ingress controller, não tem provisionador dinâmico de `PersistentVolumeClaim`, não atende serviços `type: LoadBalancer` e depende de pacotes `iptables`/`socat` pré-instalados no sistema operacional hospedeiro. O README oficial do K3s lista as 11 tecnologias integradas que entregam tudo isso pronto de fábrica.

## Como funciona
Ao iniciar o processo `k3s server`, a distribuição disponibiliza automaticamente: (1) **Runtime**: `containerd` e `runc`; (2) **Rede e Segurança**: `Flannel` para CNI, `CoreDNS` para DNS interno, `Kube-router` (netpol controller) para aplicar objetos `NetworkPolicy` e `Klipper-lb` como provedor embutido de balanceador de carga para Services `LoadBalancer`; (3) **Ingress e Observabilidade**: `Traefik` para roteamento HTTP/HTTPS e `Metrics Server` para `kubectl top` e HPA; (4) **Persistência e Automação**: `Kine` (shim de datastore), `Local-path-provisioner` (StorageClass `local-path`) e `Helm-controller` (implantação declarativa de charts via CRD `HelmChart`); e (5) **Host utilities (`k3s-io/k3s-root`)**: binários embutidos no espaço de usuário como `iptables`/`nftables`, `ebtables`, `ethtool` e `socat`, eliminando dependências do SO host.

## Exemplo
```bash
# Inspecionar os pods de sistema implantados automaticamente pelo K3s no namespace kube-system
sudo k3s kubectl get pods -n kube-system
```

## Limites e trade-offs
O provedor `Klipper-lb` (ServiceLB embutido) funciona agendando pods DaemonSet que fazem bind nas portas solicitadas pelo Service `LoadBalancer` diretamente no IP dos nós usando `hostPort`; por isso, em um único nó K3s, dois Services `LoadBalancer` diferentes não podem solicitar a mesma porta externa (ex.: porta `80` e `443` já usadas pelo `Traefik`) a menos que haja múltiplos nós ou que o `Klipper-lb` seja substituído pelo MetalLB/ Cilium LB IPAM.

## Como verificar
Execute `sudo k3s kubectl get storageclass,ingressclass -A` para confirmar que a StorageClass `local-path` (padrão) e a IngressClass `traefik` estão ativas no cluster.

## Conexões
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Veja também: K3s: distribuição Kubernetes leve e certificada em binário único menor que 100 MB.
- [[k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais]] — Veja também: K3s: shim de datastore Kine (SQLite padrão, PostgreSQL, MySQL/MariaDB) e etcd3 embutido.
- [[k3s-auto-deploy-manifestos-helm-controller-crd]] — Referência cruzada direta com k3s-auto-deploy-manifestos-helm-controller-crd.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
