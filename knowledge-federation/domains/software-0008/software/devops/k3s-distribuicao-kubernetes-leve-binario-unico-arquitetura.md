---
id: software.devops.tranche09.000811
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

# K3s: distribuição Kubernetes leve e certificada em binário único menor que 100 MB

## Em uma frase
O K3s (`k3s-io/k3s`, projeto CNCF) é uma distribuição Kubernetes pronta para produção e 100% conformante (`CNCF certified conformant`) empacotada em um único binário menor que 100 MB com metade do consumo de memória do Kubernetes tradicional.

## Por que importa
Instalar e operar um cluster Kubernetes upstream tradicional em ambientes de borda (`Edge`), dispositivos IoT, pipelines de CI, estações de desenvolvimento ou processadores ARM com poucos gigabytes de RAM é inviável quando cada componente de controle roda em processos pesados separados e exige um cluster `etcd` dedicado. Segundo o README oficial do K3s, o nome `K3s` (5 letras, metade das 10 letras de `Kubernetes` / `k8s`) reflete a meta de consumir metade da memória mantendo conformidade total.

## Como funciona
Conforme explica o README oficial (`What is this?` e `How is this lightweight?`), o K3s não é um fork divergente, mas uma **distribuição** que mantém menos de 1.000 linhas de patches sobre o Kubernetes upstream e reduz drasticamente o footprint de duas maneiras principais: (1) **Memória menor**: executa vários componentes do control plane e do nó dentro de um único processo combinados por um launcher simples, eliminando a duplicação de memória por processo; e (2) **Binário menor (< 100 MB)**: remove do código do Kubernetes apenas os antigos *in-tree storage drivers* e *in-tree cloud providers* (substituídos pelos padrões modernos out-of-tree CSI e CCM), enquanto embute todas as ferramentas necessárias para um cluster funcional.

## Exemplo
```bash
# Instalar e iniciar um nó K3s server e verificar o status do cluster usando o kubectl embutido no binário único
curl -sfL https://get.k3s.io | sh -
sudo k3s kubectl get nodes -o wide
```

## Limites e trade-offs
Como o K3s já vem com escolhas opinativas pré-integradas para funcionar imediatamente após a instalação (Flannel como CNI, Traefik como Ingress controller, Klipper-lb como Service LoadBalancer e Local-path-provisioner para armazenamento), se a sua arquitetura exigir Cilium como CNI ou NGINX/Envoy Gateway como Ingress, você deve desabilitar os componentes embutidos correspondentes na inicialização (`--flannel-backend=none --disable=traefik --disable=servicelb`) para evitar conflitos de portas e regras de rede.

## Como verificar
Execute `k3s --version` e `sudo k3s check-config` no host Linux para validar que o kernel e as montagens de cgroups atendem aos pré-requisitos do K3s.

## Conexões
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Veja também: K3s: pilha de tecnologias embutidas (containerd, Flannel, CoreDNS, Traefik, Klipper-lb, Kube-router e utilitários de host).
- [[k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais]] — Referência cruzada direta com k3s-armazenamento-estado-kine-sqlite-etcd-bancos-relacionais.
- [[k3s-arquitetura-servers-agents-tunel-websocket-loadbalancer]] — Referência cruzada direta com k3s-arquitetura-servers-agents-tunel-websocket-loadbalancer.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
