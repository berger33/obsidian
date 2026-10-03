---
id: software.devops.tranche09.000813
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

# K3s: shim de datastore Kine (SQLite padrão, PostgreSQL, MySQL/MariaDB) e etcd3 embutido

## Em uma frase
O K3s inclui o projeto **Kine** (`k3s-io/kine`) como um shim de datastore que traduz a API gRPC do `etcd` para bancos de dados relacionais, permitindo usar **SQLite3** como backend padrão de nó único ou PostgreSQL, MySQL e MariaDB em alta disponibilidade, além de suportar `etcd3` embutido ou externo.

## Por que importa
O `kube-apiserver` do Kubernetes upstream só sabe falar com a API do `etcd`, mas rodar um daemon `etcd` em um dispositivo de borda (como um Raspberry Pi ou gateway industrial com cartão SD/eMMC lento e 1 GB de RAM) consome muita memória e sofre com latência de fsync. Segundo o README e a página `Architecture` do K3s, o Kine viabiliza tanto clusters de nó único ultra-leves em SQLite quanto clusters HA apoiados em bancos relacionais gerenciados (RDS/CloudSQL).

## Como funciona
O **Kine** (`Kine is not etcd`) expõe um subconjunto da API gRPC `etcdv3` para o `kube-apiserver` e traduz operações de watch, list, create, update e compactação para tabelas SQL append-only: (1) **Single-server Setup**: usa por padrão um banco **SQLite3** embutido (`/var/lib/rancher/k3s/server/db/state.db`), zero configuração extra; (2) **High-Availability com Embedded DB (`--cluster-init`)**: usa um cluster **`etcd3` embutido** gerenciado pelo próprio K3s em **3 ou mais** nós `k3s server` (número ímpar para quórum Raft); e (3) **High-Availability com External DB (`--datastore-endpoint`)**: usa **2 ou mais** nós `k3s server` stateless apontando via Kine para um banco externo MySQL, MariaDB, PostgreSQL ou cluster `etcd` externo.

## Exemplo
```bash
# Iniciar o primeiro nó de um cluster K3s em Alta Disponibilidade (HA) com etcd3 embutido (--cluster-init)
curl -sfL https://get.k3s.io | sh -s - server --cluster-init
sudo k3s etcd-snapshot ls
```

## Limites e trade-offs
Na topologia HA com **etcd embutido** (`--cluster-init`), são necessários no mínimo **3 nós server** (e sempre um número ímpar: 3, 5) para manter o quórum Raft se um nó cair (com apenas 2 nós de etcd, a perda de 1 nó derruba o quórum do cluster inteiro); já na topologia HA com **banco externo** via Kine (PostgreSQL/MySQL), como o estado vive fora dos nós K3s, apenas **2 nós server** já bastam para alta disponibilidade do control plane.

## Como verificar
Verifique em `/var/lib/rancher/k3s/server/db/` se o nó está operando com `state.db` (SQLite via Kine) ou com o diretório `etcd/` (etcd3 embutido).

## Conexões
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Veja também: K3s: pilha de tecnologias embutidas (containerd, Flannel, CoreDNS, Traefik, Klipper-lb, Kube-router e utilitários de host).
- [[k3s-arquitetura-servers-agents-tunel-websocket-loadbalancer]] — Veja também: K3s: arquitetura de nós Server e Agent, túnel WebSocket reverso do kubelet e load balancer client-side.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[talos-bootstrap-etcd-gerenciamento-control-plane-ha]] — Referência cruzada direta com talos-bootstrap-etcd-gerenciamento-control-plane-ha.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
