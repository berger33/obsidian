---
id: software.devops.tranche13.001213
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Execução de Controles de Control Plane (Master, API Server, etcd, Scheduler) com Tolerations

## Em uma frase
Para auditar a seção 1 (Control Plane Components: API Server, Controller Manager, Scheduler) e a seção 2 (etcd) do CIS Benchmark em clusters autogerenciados (`kubeadm`, bare-metal, Rancher, OpenShift), o Job do `kube-bench` precisa ser agendado diretamente nos nós de control plane usando `nodeSelector` e `tolerations`.

## Por que importa
Se você aplicar o `job.yaml` genérico em um cluster onde os nós de control plane possuem a taint `node-role.kubernetes.io/control-plane:NoSchedule`, o Pod do `kube-bench` cai em um worker node e pula todas as verificações de API Server e `etcd`.

## Como funciona
O manifesto `job-master.yaml` (ou um `DaemonSet` de auditoria) configura `nodeSelector: { "node-role.kubernetes.io/control-plane": "" }` (observando que versões antigas do Kubernetes usavam `node-role.kubernetes.io/master`) e a toleration correspondente, permitindo inspecionar `/etc/kubernetes/manifests` e `/etc/kubernetes/pki` diretamente no nó master.

## Exemplo
```yaml
spec:
  template:
    spec:
      hostPID: true
      nodeSelector:
        node-role.kubernetes.io/control-plane: ""
      tolerations:
        - key: node-role.kubernetes.io/control-plane
          operator: Exists
          effect: NoSchedule
```

## Limites e trade-offs
Usar um `Job` de réplica única em um cluster com 3 ou 5 nós de control plane audita apenas um dos nós masters, deixando possíveis desvios de permissão de arquivos nos outros nós de control plane sem verificação.

## Como verificar
Em clusters multi-master, execute o `kube-bench` em todos os nós do control plane (por exemplo, via `DaemonSet` temporário ou Jobs por nó) para validar a uniformidade dos manifestos estáticos.

## Conexões
- [[kubebench-autodetect-versao-kubernetes-mapeamento-cis-benchmark]] — Veja também: Aqua kube-bench: Autodetecção de Versão do Kubernetes e Mapeamento para Releases do CIS Benchmark.
- [[kubebench-clusters-gerenciados-eks-gke-aks-limites-worker-nodes]] — Veja também: Aqua kube-bench: Auditoria de Worker Nodes em Clusters Gerenciados (EKS, GKE, AKS e ACK) e Limites de Escopo.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
