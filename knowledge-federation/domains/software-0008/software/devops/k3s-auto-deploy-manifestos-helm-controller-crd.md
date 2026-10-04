---
id: software.devops.tranche09.000816
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

# K3s: auto-deploy em tempo real de manifestos em /var/lib/rancher/k3s/server/manifests e Helm-controller (CRD HelmChart)

## Em uma frase
O K3s monitora continuamente o diretório local `/var/lib/rancher/k3s/server/manifests`, aplicando automaticamente em tempo real qualquer manifesto Kubernetes (`.yaml`) colocado ali e processando charts Helm de forma declarativa através do **Helm-controller** embutido (`CRD HelmChart`).

## Por que importa
Em dispositivos de borda (Edge/IoT), appliances desconectados ou provisionamento automatizado de imagens de sistema operacional, o operador muitas vezes precisa que o cluster já suba no primeiro boot com aplicações, operadores e charts Helm instalados automaticamente sem exigir um servidor externo rodando `kubectl apply` ou `helm install`. O README oficial do K3s destaca o auto-deploy de manifestos locais e o `Helm-controller`.

## Como funciona
Qualquer arquivo `.yaml`, `.yml` ou `.json` presente em **`/var/lib/rancher/k3s/server/manifests`** em um nó `k3s server` é vigiado pelo controlador do K3s e aplicado automaticamente ao cluster (de maneira análoga a um `kubectl apply`), sendo reaplicado em tempo real sempre que o arquivo em disco muda. Combinado ao **`k3s-io/helm-controller`** embutido no K3s, o operador pode colocar nesse diretório um manifesto declarativo do Custom Resource **`HelmChart`** (ou `HelmChartConfig` para customizar componentes nativos como o Traefik): o `helm-controller` detecta o CRD e lança um Job `helm-install-<nome>` no cluster para instalar ou atualizar o chart Helm especificado.

## Exemplo
```yaml
# Exemplo de CRD HelmChart salvo em /var/lib/rancher/k3s/server/manifests/ para customizar ou instalar um chart automaticamente
apiVersion: helm.cattle.io/v1
kind: HelmChartConfig
metadata:
  name: traefik
  namespace: kube-system
spec:
  valuesContent: |-
    ports:
      web:
        exposedPort: 80
```

## Limites e trade-offs
Jamais edite manualmente via `kubectl edit` recursos que foram criados a partir de arquivos em `/var/lib/rancher/k3s/server/manifests` (nem delete diretamente os manifestos dos addons embutidos como `traefik.yaml` desse diretório, pois o K3s os recria no próximo boot/upgrade); para alterar um addon embutido sem desabilitá-lo, use um arquivo `HelmChartConfig` separado, e para desabilitá-lo use `--disable=<addon>` na configuração do servidor.

## Como verificar
Execute `sudo k3s kubectl get helmcharts,helmchartconfigs -A` para inspecionar os charts gerenciados pelo `helm-controller` embutido do K3s.

## Conexões
- [[k3s-seguranca-identidade-nos-node-password-secrets-certificados]] — Veja também: K3s: proteção de identidade de nós com Secrets node-password.k3s e flag --with-node-id.
- [[k3s-gerenciamento-certificados-tls-rotacao-operacoes]] — Veja também: K3s: gerenciamento automatizado e rotação de certificados TLS dos componentes com k3s certificate.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Referência cruzada direta com k3s-componentes-embutidos-containerd-flannel-traefik-klipper.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
