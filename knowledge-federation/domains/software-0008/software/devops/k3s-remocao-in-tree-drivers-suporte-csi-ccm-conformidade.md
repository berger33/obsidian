---
id: software.devops.tranche09.000820
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

# K3s: remoção de drivers in-tree legados, adoção de CSI e CCM out-of-tree e conformidade CNCF

## Em uma frase
Para reduzir o tamanho do binário mantendo 100% de conformidade CNCF, as versões atuais do K3s removem do Kubernetes upstream apenas duas categorias de código legado: os **in-tree storage drivers** e os **in-tree cloud providers**, substituídos por **CSI** e **CCM** out-of-tree.

## Por que importa
Conforme esclarece a seção `What have you removed from upstream Kubernetes?` do README oficial do K3s, este é um ponto comum de confusão: versões muito antigas do K3s removiam mais recursos, levando alguns engenheiros a achar equivocadamente que o K3s atual não possui todas as APIs do Kubernetes padrão. Na realidade, o K3s atual remove apenas o que o próprio Kubernetes upstream já descontinuou em favor de interfaces plugáveis.

## Como funciona
O binário do K3s exclui em tempo de compilação: (1) **In-tree storage drivers** (antigos plugins de volume compilados dentro do binário do kubelet/controller-manager para SANs e nuvens específicas); e (2) **In-tree cloud providers** (código específico de provedores de nuvem legado acoplado ao core). Ambas as funcionalidades possuem equivalentes modernos **out-of-tree** totalmente suportados no K3s e adotados pelo próprio Kubernetes upstream: a **Container Storage Interface (CSI)** para volumes (como Longhorn, Ceph CSI, AWS EBS CSI) e o **Cloud Controller Manager (CCM)** para integração com provedores de nuvem (enquanto o K3s fornece seu próprio CCM embutido para nós locais, substituível via `--disable-cloud-controller`).

## Exemplo
```bash
# Iniciar o K3s desabilitando o cloud controller embutido (--disable-cloud-controller) para instalar um CCM externo (ex.: AWS/Hetzner/OpenStack)
curl -sfL https://get.k3s.io | sh -s - server --disable-cloud-controller --kubelet-arg="cloud-provider=external"
```

## Limites e trade-offs
Ao implantar um Cloud Controller Manager (CCM) externo de um provedor de nuvem (como AWS, GCP, Azure ou Hetzner Cloud) em um cluster K3s, você **deve** passar `--disable-cloud-controller` e `--kubelet-arg="cloud-provider=external"`, caso contrário o cloud controller embutido do K3s entrará em conflito com o CCM externo na inicialização dos endereços e taints `node.cloudprovider.kubernetes.io/uninitialized` dos nós.

## Como verificar
Execute `sudo k3s kubectl api-resources` e `sudo k3s kubectl get csidrivers` para verificar a conformidade completa das APIs do Kubernetes e o suporte a drivers CSI no cluster K3s.

## Conexões
- [[k3s-instalacao-air-gap-imagens-tarball-registries-privados]] — Veja também: K3s: implantação offline (Air-Gap) com tarball de imagens em /var/lib/rancher/k3s/agent/images e registries.yaml.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Referência cruzada direta com k3s-componentes-embutidos-containerd-flannel-traefik-klipper.
- [[clusterapi-provedores-infraestrutura-bootstrap-control-plane]] — Referência cruzada direta com clusterapi-provedores-infraestrutura-bootstrap-control-plane.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
