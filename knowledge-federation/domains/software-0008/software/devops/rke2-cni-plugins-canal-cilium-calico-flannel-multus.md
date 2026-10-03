---
id: software.devops.tranche17.001675
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

# RKE2: seleção de plugins CNI (`canal`, `cilium`, `calico`, `flannel`) e composição multi-NIC com `multus`

## Em uma frase
O RKE2 empacota e gerencia nativamente múltiplos plugins de Container Network Interface (**Canal** [Flannel + Calico], **Cilium**, **Calico** ou **Flannel**), além de suportar composição com o **Multus** para anexar múltiplas interfaces de rede aos Pods.

## Por que importa
Ambientes de telecomunicações (5G/NFV) e data centers corporativos frequentemente exigem substituir o overlay VXLAN padrão por eBPF de alta performance (Cilium) ou BGP puro (Calico) combinado com uma segunda placa de rede SR-IOV/MACVLAN via Multus.

## Como funciona
Configurado pela chave `cni` em `/etc/rancher/rke2/config.yaml` (por exemplo `cni: cilium` ou `cni: [multus, calico]`), o RKE2 implanta e atualiza a pilha de rede automaticamente como um add-on gerenciado pelo `helm-controller` a partir dos manifestos em `/var/lib/rancher/rke2/server/manifests`.

## Exemplo
```yaml
# /etc/rancher/rke2/config.yaml com Multus + Cilium:
cni:
  - multus
  - cilium
```

## Limites e trade-offs
Quando o `multus` é combinado com outro plugin CNI na lista `cni`, o `multus` deve obrigatoriamente ser listado como o **primeiro** elemento da lista (`[multus, cilium]` ou `[multus, canal]`).

## Como verificar
Verifique os Pods da CNI e os objetos `HelmChart` gerados em `kube-system` com `kubectl get helmcharts.helm.cattle.io -n kube-system`.

## Conexões
- [[rke2-sequencia-boot-server-agent-static-pods-etcd-apiserver]] — Veja também: RKE2: coreografia de inicialização de `server` e `agent` via goroutines e Static Pods.
- [[rke2-helm-controller-manifests-helmchartconfig-customizacao-addons]] — Veja também: RKE2: gerenciamento declarativo de add-ons via `helm-controller` e customização com `HelmChartConfig`.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
