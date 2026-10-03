---
id: software.devops.tranche13.001220
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Execução Contínua do CIS Benchmark via Trivy e Trivy Operator no Cluster

## Em uma frase
Conforme documentado no README oficial do `kube-bench`, a Aqua Security também disponibiliza a verificação do CIS Kubernetes Benchmark integrada ao **Trivy CLI** e ao **Trivy Operator**, permitindo reconciliar relatórios contínuos de conformidade (`ClusterComplianceReport`) como CRDs nativas do Kubernetes.

## Por que importa
Executar o `kube-bench` apenas como um Job manual esporádico deixa janelas de semanas em que alterações de configuração em nós ou políticas de RBAC/NetworkPolicy violam os controles CIS sem gerar alerta.

## Como funciona
Quando o Trivy Operator está instalado no cluster (combinado com o `node-collector` para inspecionar configurações de nós), ele agenda verificações periódicas baseadas nas especificações do CIS Kubernetes Benchmark e publica o status consolidado em CRDs consultáveis via `kubectl get clustercompliancereports` e métricas Prometheus.

## Exemplo
```bash
# Inspecionar relatorios de conformidade CIS gerados continuamente no cluster:
kubectl get clustercompliancereports
kubectl get clustercompliancereports cis -o wide
```

## Limites e trade-offs
Executar simultaneamente CronJobs avulsos de `kube-bench` a cada hora e o `node-collector` do Trivy Operator no mesmo cluster duplica a criação de Pods privilegiados com `hostPID: true` em todos os nós.

## Como verificar
Padronize uma única modalidade de execução contínua (Job agendado do `kube-bench` ou `ClusterComplianceReport` do Trivy Operator) e restrinja o namespace de execução via Pod Security Standards.

## Conexões
- [[kubebench-controles-apiserver-etcd-encryption-audit-log-rbac]] — Veja também: Aqua kube-bench: Auditoria do API Server e etcd (Criptografia de Secrets, Audit Logs, TLS e Permissões PKI).

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
