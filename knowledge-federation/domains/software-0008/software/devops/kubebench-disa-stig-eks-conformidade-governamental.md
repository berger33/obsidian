---
id: software.devops.tranche13.001215
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

# Aqua kube-bench: Varredura de Conformidade DISA STIG em Clusters Kubernetes e EKS (job-eks-stig.yaml)

## Em uma frase
Além dos benchmarks do Center for Internet Security (CIS), o `kube-bench` inclui suporte nativo para auditoria contra o guia **DISA STIG (Defense Information Systems Agency — Security Technical Implementation Guide)**, incluindo manifesto dedicado para Amazon EKS (`job-eks-stig.yaml`).

## Por que importa
Ambientes governamentais, financeiros ou submetidos a regimes regulatórios rigorosos exigem evidência de conformidade com os controles DISA STIG além das diretrizes padrão do CIS.

## Como funciona
Ao aplicar `job-eks-stig.yaml` (ou especificar o benchmark STIG correspondente na CLI), o `kube-bench` carrega o conjunto de regras YAML do STIG em `/opt/kube-bench/cfg/` e valida os parâmetros de criptografia, auditoria e isolamento exigidos nos worker nodes.

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/aquasecurity/kube-bench/main/job-eks-stig.yaml
kubectl wait --for=condition=complete job/kube-bench --timeout=60s
kubectl logs job/kube-bench
```

## Limites e trade-offs
Puxar a imagem `docker.io/aquasec/kube-bench:latest` diretamente do Docker Hub em clusters EKS privados sem NAT Gateway ou com políticas restritas de registro causa falha `ImagePullBackOff` na execução do `job-eks-stig.yaml`.

## Como verificar
Espelhe e assine a imagem do `kube-bench` em um repositório privado do Amazon ECR (`aws ecr create-repository --repository-name k8s/kube-bench`) e referencie a tag/digest interna no manifesto do Job.

## Conexões
- [[kubebench-clusters-gerenciados-eks-gke-aks-limites-worker-nodes]] — Veja também: Aqua kube-bench: Auditoria de Worker Nodes em Clusters Gerenciados (EKS, GKE, AKS e ACK) e Limites de Escopo.
- [[kubebench-customizacao-cfg-targets-check-skip-filtros]] — Veja também: Aqua kube-bench: Seleção de Alvos (--targets), Filtros de Controles (--check, --skip) e Customização de /opt/kube-bench/cfg.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
