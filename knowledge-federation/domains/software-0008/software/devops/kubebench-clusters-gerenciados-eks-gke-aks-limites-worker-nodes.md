---
id: software.devops.tranche13.001214
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

# Aqua kube-bench: Auditoria de Worker Nodes em Clusters Gerenciados (EKS, GKE, AKS e ACK) e Limites de Escopo

## Em uma frase
Em clusters Kubernetes gerenciados na nuvem (como Amazon EKS, Google GKE, Azure AKS e Alibaba ACK), é impossível inspecionar os nós de control plane com o `kube-bench` porque o provedor de nuvem não concede acesso de host aos masters; nesses ambientes, o `kube-bench` utiliza perfis específicos (`job-eks.yaml`, `job-aks.yaml`, `job-gke.yaml`) focados nos worker nodes.

## Por que importa
Rodar o benchmark CIS de Kubernetes vanilla contra um worker node de EKS ou AKS gera dezenas de falsos negativos porque os caminhos de configuração do `kubelet` e certificados gerenciados pela nuvem seguem layouts específicos do provedor.

## Como funciona
Para EKS, por exemplo, o repositório oficial disponibiliza `job-eks.yaml` (CIS EKS Benchmark) e `job-eks-stig.yaml` (DISA STIG para EKS), que avaliam as configurações do `kubelet`, argumentos de runtime e permissões de arquivos de acordo com as recomendações oficiais para nós de trabalho gerenciados.

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job-eks.yaml
kubectl get pods -l app=kube-bench
kubectl logs -l app=kube-bench > kube-bench-eks-report.txt
```

## Limites e trade-offs
Tentar forçar a execução de `--targets master` do `kube-bench` dentro de um cluster EKS, GKE ou AKS falha inevitavelmente por ausência dos processos `kube-apiserver` e `etcd` nos nós acessíveis ao cliente.

## Como verificar
Utilize os manifestos específicos de provedor (`job-eks.yaml`, `job-eks-stig.yaml`, `job-aks.yaml`) para auditar os worker nodes e audite o control plane gerenciado por meio das APIs e logs de auditoria da própria nuvem.

## Conexões
- [[kubebench-control-plane-master-nodes-nodeselector-tolerations]] — Veja também: Aqua kube-bench: Execução de Controles de Control Plane (Master, API Server, etcd, Scheduler) com Tolerations.
- [[kubebench-disa-stig-eks-conformidade-governamental]] — Veja também: Aqua kube-bench: Varredura de Conformidade DISA STIG em Clusters Kubernetes e EKS (job-eks-stig.yaml).

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
