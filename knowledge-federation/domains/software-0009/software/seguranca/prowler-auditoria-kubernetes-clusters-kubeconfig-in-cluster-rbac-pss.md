---
id: software.seguranca.tranche02.000176
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://docs.prowler.com/introduction", "https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md", "https://github.com/prowler-cloud/prowler"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Prowler para Kubernetes (`prowler kubernetes`): auditoria CIS Kubernetes Benchmark, RBAC, Pod Security e NetworkPolicies

## Em uma frase
Conforme listado na tabela oficial de provedores (`docs.prowler.com/introduction`), o provedor **`prowler kubernetes`** audita clusters Kubernetes (EKS, AKS, GKE, OpenShift ou self-hosted) tanto externamente via arquivo `kubeconfig` (`--kubeconfig-file`) quanto de dentro do próprio cluster (modo *In-Cluster* via ServiceAccount de um CronJob/Pod).

## Por que importa
Erros de configuração dentro do cluster Kubernetes — como Pods rodando com `privileged: true`, `hostNetwork: true`, `ClusterRoleBindings` concedendo `cluster-admin` a contas de serviço padrão ou namespaces sem `NetworkPolicy` — comprometem o isolamento de containers mesmo quando a conta de nuvem subjacente está bem configurada.

## Como funciona
O `prowler kubernetes` inspeciona os recursos da API Server (`Pods`, `Deployments`, `DaemonSets`, `Roles`, `ClusterRoles`, `NetworkPolicies`, `Secrets`, `ConfigMaps`) e configurações do Control Plane (`apiserver`, `kubelet`, `etcd`, `controller-manager`, `scheduler`), mapeando-os contra o **CIS Kubernetes Benchmark** e boas práticas NSA/CISA.

## Exemplo
```bash
# Auditando um cluster Kubernetes específico do kubeconfig (restringindo a namespaces críticos):
prowler kubernetes \
  --kubeconfig-file ~/.kube/config \
  --context prod-eks-cluster \
  --namespace kube-system production payments
```

## Limites e trade-offs
Ao implantar o Prowler como `CronJob` periódico dentro do cluster Kubernetes, associe uma `ClusterRole` estritamente somente-leitura (`verbs: ["get", "list"]`) sem permissão de ler o valor de `Secrets` se você auditar apenas metadados.

## Como verificar
Execute `prowler kubernetes --list-checks` para visualizar todas as verificações de Kubernetes disponíveis.

## Conexões
- [[prowler-mutelist-yaml-supressao-excecoes-accounts-regions-resources-tags]] — Veja também: Prowler `Mutelist` (`-w` / `--mutelist-file`): gerenciamento declarativo de exceções por conta, região, check, recurso e tags.
- [[prowler-saas-github-m365-googleworkspace-okta-iac-containers]] — Veja também: Prowler SaaS, IaC e Containers (`github`, `m365`, `googleworkspace`, `okta`, `iac`, `image`): postura unificada além da IaaS.

## Fontes
- [Prowler GitHub — README.md (Open-Source Cloud Security Platform, CLI/Dashboard/Server Architecture, Attack Paths with Cartography/Neo4j & Security Hub)](https://docs.prowler.com/introduction) — README oficial do prowler-cloud/prowler documentando a arquitetura da plataforma, execução multi-cloud, configuração de Attack Paths com Neo4j/Amazon Neptune e formatos de saída; consultado em 2026-10-03.
- [Prowler Official Documentation — Introduction & Supported Providers (AWS/Azure/GCP/Kubernetes/SaaS/IaC Coverage, ThreatScore, Compliance & Prowler MCP)](https://raw.githubusercontent.com/prowler-cloud/prowler/master/README.md) — Documentação oficial de introdução ao Prowler detalhando a matriz de provedores suportados, Prowler ThreatScore, frameworks de conformidade, Mutelist e extensibilidade; consultado em 2026-10-03.
- [Prowler — Official GitHub Repository](https://github.com/prowler-cloud/prowler) — Repositório oficial Apache-2.0 do Prowler; consultado em 2026-10-03.
