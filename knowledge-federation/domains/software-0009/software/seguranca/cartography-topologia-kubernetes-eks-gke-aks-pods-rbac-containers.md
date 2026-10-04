---
id: software.seguranca.tranche11.001007
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md", "https://docs.cartography.dev/usage/tutorial.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Mapeamento de Clusters **Kubernetes (EKS, GKE, AKS)** no Cartography: Conectando `Pod`, `Container`, `ServiceAccount`, `RBAC`, `Service` e Imagens Cloud

## Em uma frase
Quando um cluster Kubernetes roda na nuvem (como **AWS EKS**, **Google GKE** ou **Azure AKS**), analisá-lo isoladamente da conta cloud esconde metade da superfície de ataque: de onde veio a imagem do container? Qual Load Balancer da AWS/GCP expõe aquele `Service`? Qual `IAM Role` a `ServiceAccount` do Pod assume via `OIDCProvider` (IRSA)?

## Por que importa
O módulo **`kubernetes`** do Cartography ingere toda a hierarquia interna do cluster — `KubernetesCluster`, `KubernetesNamespace`, `KubernetesPod`, `KubernetesContainer`, `KubernetesService`, `KubernetesServiceAccount`, `KubernetesRole`, `KubernetesClusterRole`, `KubernetesRoleBinding`, `KubernetesClusterRoleBinding` e `OIDCProvider` — e **cria arestas diretas com os nós de nuvem correspondentes (`AWSEKSCluster`, `ECRImage`, `AWSLoadBalancerV2`, `AWSRole`)**!

## Como funciona
Isso permite auditar de ponta a ponta desde a exposição externa do `Service` no Load Balancer até a `ServiceAccount` do Pod e as permissões RBAC/IAM!

## Exemplo
```cypher
// Identificar Pods Kubernetes vinculados a ServiceAccounts que possuem ClusterRoleBinding para cluster-admin
MATCH (ns:KubernetesNamespace)-[:CONTAINS]->(pod:KubernetesPod)-[:USES_SERVICE_ACCOUNT]->(sa:KubernetesServiceAccount)
MATCH (sa)<-[:SUBJECT]-(crb:KubernetesClusterRoleBinding)-[:ROLE_REF]->(cr:KubernetesClusterRole)
WHERE cr.name = "cluster-admin"
RETURN ns.name AS namespace, pod.name AS pod_name, sa.name AS service_account, crb.name AS binding;
```

## Limites e trade-offs
Use essa visão integrada do Cartography para validar a defesa contra as ferramentas de pós-exploração **Peirates** e **CDK** estudadas na Tranche 10: qualquer `KubernetesPod` que apareça na query acima com vínculo para `cluster-admin` (ou cuja `KubernetesServiceAccount` assuma uma `AWSRole` privilegiada) é um alvo prioritário para redução de privilégio!

## Como verificar
Sincronize múltiplos clusters passando seus contextos no kubeconfig para o módulo `kubernetes` do Cartography.

## Conexões
- [[cartography-gestao-vulnerabilidades-cves-epss-kev-crowdstrike-ecr]] — Veja também: Priorização de Vulnerabilidades Baseada em Contexto no Cartography: Cruzando **CrowdStrike Spotlight, AWS ECR/Inspector, EPSS e CISA KEV**.
- [[cartography-governanca-ia-agentes-bedrock-vertex-openai-anthropic-aibom]] — Veja também: Segurança e Governança de **IA em Produção (`AI Security Posture / AIBOM`)** no Cartography: **AWS Bedrock, GCP Vertex AI, OpenAI e Anthropic**.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac]] — Referência cruzada direta com peirates-coleta-tokens-secrets-secret-to-sa-kubectl-try-all-rbac.
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — Referência cruzada direta com cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
