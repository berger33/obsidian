---
id: software.devops.tranche17.001686
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
fontes: ["https://raw.githubusercontent.com/k0sproject/k0s/main/README.md", "https://docs.k0sproject.io/stable/architecture/", "https://github.com/k0sproject/k0s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# k0s: opções de rede CNI (`kube-router` padrão, `calico` pré-configurado e CNI customizada)

## Em uma frase
Na configuração de rede (`spec.network.provider`), o `k0s` oferece o **Kube-Router** como plugin CNI padrão leve, o **Calico** como alternativa pré-configurada (suportando VXLAN, IPIP e NetworkPolicies avançadas) e o modo **`custom`** para permitir a instalação manual de Cilium ou outras CNIs.

## Por que importa
Dispositivos de borda e clusters enxutos beneficiam-se do baixo consumo de memória do Kube-Router (que também pode substituir o `kube-proxy` via IPVS), enquanto ambientes multi-tenant corporativos podem preferir o motor do Calico ou Cilium.

## Como funciona
No arquivo `k0s.yaml` (`k0s config create`), o administrador define `spec.network.provider: kuberouter` (ou `calico` / `custom`), além de `podCIDR` e `serviceCIDR`. O controlador de bootstrap do `k0s` reconcilia automaticamente os DaemonSets e CRDs da CNI selecionada na inicialização.

## Exemplo
```yaml
apiVersion: k0s.k0sproject.io/v1beta1
kind: ClusterConfig
metadata:
  name: k0s
spec:
  network:
    provider: calico
    calico:
      mode: vxlan
      vxlanPort: 4789
      mtu: 1450
    podCIDR: 10.244.0.0/16
    serviceCIDR: 10.96.0.0/12
```

## Limites e trade-offs
O campo `spec.network.provider` não deve ser trocado em um cluster já em execução com cargas de trabalho ativas sem planejar a recriação da malha de rede e dos Pods.

## Como verificar
Gere e valide um arquivo de configuração com `k0s config create > k0s.yaml` e `k0s config validate --config k0s.yaml`.

## Conexões
- [[k0s-k0sctl-gerenciamento-ciclo-vida-multi-node-upgrades-backups]] — Veja também: k0s `k0sctl`: provisionamento declarativo, upgrades zero-downtime, backup e restore de clusters multi-nó via SSH.
- [[k0s-autopilot-upgrades-declarativos-in-cluster-controlplanes-workers]] — Veja também: k0s `Autopilot`: atualizações declarativas in-cluster de controladores, workers e imagens airgap via CRD `Plan`.

## Fontes
- [k0s GitHub — README.md (Zero-Friction Kubernetes in a Single Binary, Konnectivity, Kube-Router, kine, k0sctl & Multi-Arch RISC-V/ARM/x86)](https://raw.githubusercontent.com/k0sproject/k0s/main/README.md) — README oficial do k0sproject/k0s (CNCF Sandbox) detalhando empacotamento em binário único, isolamento do control plane, opções de storage/CNI e suporte multi-arquitetura; consultado em 2026-10-03.
- [k0s Official Documentation — Architecture (Process Supervisor, Naked Control Plane Processes, In-Cluster Autopilot & CRI/Worker Runtime)](https://docs.k0sproject.io/stable/architecture/) — Documentação oficial de arquitetura do k0s detalhando supervisão de processos sem container engine no controller, gerenciamento de etcd/kine e containerd nos workers; consultado em 2026-10-03.
- [k0s — Official GitHub Repository](https://github.com/k0sproject/k0s) — Repositório oficial Apache-2.0 do k0s na CNCF; consultado em 2026-10-03.
