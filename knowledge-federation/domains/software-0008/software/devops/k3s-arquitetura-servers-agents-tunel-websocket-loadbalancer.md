---
id: software.devops.tranche09.000814
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

# K3s: arquitetura de nós Server e Agent, túnel WebSocket reverso do kubelet e load balancer client-side

## Em uma frase
O K3s divide os nós entre `k3s server` (control plane + datastore) e `k3s agent` (workers), eliminando a necessidade de expor portas de entrada nos workers para a API do `kubelet` ao estabelecer um túnel WebSocket iniciado pelo agente com balanceamento de carga client-side na porta `6443`.

## Por que importa
No Kubernetes tradicional, o `kube-apiserver` precisa iniciar conexões TCP diretas para a porta `10250` do `kubelet` de cada nó worker (para `kubectl logs`, `kubectl exec` e `port-forward`), o que falha quando workers de borda estão atrás de NAT/firewalls que bloqueiam conexões de entrada. Conforme documentado no README e em `docs.k3s.io/architecture`, o túnel WebSocket e o load balancer local do agente resolvem tanto a travessia de firewall quanto a alta disponibilidade.

## Como funciona
Quando um nó worker executa **`k3s agent --server https://<ip-ou-lb>:6443 --token <token>`**, o processo do agente inicia uma conexão **WebSocket** de saída para o servidor, permitindo que o control plane acesse a API do `kubelet` através desse túnel bidirecional sem abrir portas de entrada no worker. Além disso, o `k3s agent` executa internamente um **load balancer client-side** local na porta `6443`: inicialmente ele se conecta ao endereço passado em `--server`; assim que entra no cluster, o agente busca a lista dinâmica de todos os endereços de `kube-apiserver` nos endpoints do Service `kubernetes` (namespace `default`) e mantém conexões estáveis com todos os servers do cluster, tolerando a queda do servidor inicial sem perder comunicação.

## Exemplo
```bash
# Juntar um nó worker (k3s agent) ao cluster apontando para o endereço de registro e token do servidor
K3S_TOKEN=$(sudo cat /var/lib/rancher/k3s/server/node-token)
curl -sfL https://get.k3s.io | K3S_URL=https://10.0.0.10:6443 K3S_TOKEN="${K3S_TOKEN}" sh -
```

## Limites e trade-offs
Embora o load balancer client-side embutido em cada `k3s agent` descubra e distribua automaticamente o tráfego entre todos os nós `k3s server` depois que o agente já se registrou, para o momento do registro inicial (ou para clientes `kubectl` externos acessando o cluster) em produção HA ainda é recomendado usar um endereço de registro fixo (`Fixed Registration Address`, como um VIP kube-vip, DNS round-robin ou balanceador TCP externo) para não depender de um único IP estático no `--server`.

## Como verificar
Em um nó worker (`k3s agent`), verifique o status do serviço `systemctl status k3s-agent` e confirme que comandos `kubectl logs` e `kubectl exec` a partir do servidor funcionam mesmo com o firewall de entrada do worker bloqueado.

## Conexões
- [[k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais]] — Veja também: K3s: shim de datastore Kine (SQLite padrão, PostgreSQL, MySQL/MariaDB) e etcd3 embutido.
- [[k3s-seguranca-identidade-nos-node-password-secrets-certificados]] — Veja também: K3s: proteção de identidade de nós com Secrets node-password.k3s e flag --with-node-id.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
