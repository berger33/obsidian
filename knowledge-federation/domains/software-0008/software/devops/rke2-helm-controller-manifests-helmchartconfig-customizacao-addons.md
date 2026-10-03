---
id: software.devops.tranche17.001676
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://docs.rke2.io/architecture", "https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: gerenciamento declarativo de add-ons via `helm-controller` e customização com `HelmChartConfig`

## Em uma frase
O RKE2 embute o `helm-controller` (da suíte K3s) que observa o diretório `/var/lib/rancher/rke2/server/manifests` e reconcilia automaticamente objetos `HelmChart` e `HelmChartConfig` (`helm.cattle.io/v1`) para instalar e customizar add-ons de cluster (CoreDNS, CNI, Ingress, Metrics Server ou charts do usuário).

## Por que importa
Se o operador editar diretamente os arquivos gerados pelo RKE2 dentro de `/var/lib/rancher/rke2/server/manifests/rke2-coredns.yaml`, o processo `rke2 server` sobrescreverá essas edições no próximo reinício ao reextrair a imagem `rke2-runtime`.

## Como funciona
Para customizar qualquer componente empacotado pelo RKE2 (como `rke2-coredns`, `rke2-cilium` ou `rke2-traefik`), o administrador cria um arquivo separado contendo um recurso `HelmChartConfig` com o mesmo nome e namespace (`kube-system`) e coloca seus overrides Helm em `spec.valuesContent`. O `helm-controller` mescla esses valores de forma persistente através de upgrades.

## Exemplo
```yaml
# /var/lib/rancher/rke2/server/manifests/rke2-coredns-config.yaml
apiVersion: helm.cattle.io/v1
kind: HelmChartConfig
metadata:
  name: rke2-coredns
  namespace: kube-system
spec:
  valuesContent: |-
    autoscaler:
      enabled: true
      coresPerReplica: 128
```

## Limites e trade-offs
Para desabilitar completamente um add-on embutido que não será usado (por exemplo, usar um Ingress próprio em vez do embutido), utilize a chave `disable: [rke2-ingress-nginx]` ou `disable: [rke2-traefik]` no `/etc/rancher/rke2/config.yaml`.

## Como verificar
Aplique o arquivo `rke2-coredns-config.yaml` em `/var/lib/rancher/rke2/server/manifests/` e acompanhe o Job `helm-install-rke2-coredns` em `kube-system`.

## Conexões
- [[rke2-cni-plugins-canal-cilium-calico-flannel-multus]] — Veja também: RKE2: seleção de plugins CNI (`canal`, `cilium`, `calico`, `flannel`) e composição multi-NIC com `multus`.
- [[rke2-migracao-ingress-nginx-eol-para-traefik-v1-36]] — Veja também: RKE2: transição de Ingress NGINX (EOL em março de 2026) para Traefik como Ingress Controller padrão no RKE2 v1.36+.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
