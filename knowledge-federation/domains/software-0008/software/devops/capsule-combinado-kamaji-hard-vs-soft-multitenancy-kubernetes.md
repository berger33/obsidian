---
id: software.devops.tranche15.001488
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md", "https://raw.githubusercontent.com/clastix/kamaji/master/README.md", "https://github.com/projectcapsule/capsule"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Capsule e Kamaji: escolha e combinação entre Soft Multi-Tenancy (namespaces) e Hard Multi-Tenancy (control planes)

## Em uma frase
Dentro do ecossistema Clastix/CNCF, o Capsule resolve o *multi-tenancy* no nível de namespaces compartilhando um único Control Plane, enquanto o Kamaji resolve o *multi-tenancy* no nível de Control Planes hospedados em Pods — podendo ambos operar juntos na mesma arquitetura.

## Por que importa
Nem todo caso de uso exige um API Server dedicado: equipes internas da mesma empresa que não instalam CRDs conflitantes operam com altíssima eficiência em um `Tenant` do Capsule; já clientes externos SaaS ou equipes que precisam instalar operadores cluster-wide exigem um `TenantControlPlane` do Kamaji.

## Como funciona
Em plataformas avançadas, o Capsule governa o cluster de gerenciamento (isolando cada cliente em seu próprio `Tenant` de namespaces onde rodam os objetos `TenantControlPlane` do Kamaji e os `MachineDeployments` do Cluster API) ou governa o interior de cada cluster Kamaji para subdividi-lo entre subequipes.

## Exemplo
```bash
kubectl api-resources | grep -E "capsule.clastix.io|kamaji.clastix.io"
```

## Limites e trade-offs
Se dois tenants precisarem instalar versões diferentes do mesmo CRD cluster-scoped no mesmo cluster Kubernetes, o isolamento por namespaces do Capsule não basta (pois CRDs são globais ao API Server), sendo necessário provisionar um `TenantControlPlane` separado via Kamaji ou vCluster.

## Como verificar
Avalie se as cargas de trabalho do tenant requerem CRDs globais próprios antes de decidir entre um `Tenant` Capsule puro ou um `TenantControlPlane` Kamaji.

## Conexões
- [[capsule-gitops-ready-flux-argocd-provisionamento-tenants]] — Veja também: Capsule: operação declarativa GitOps-ready de Tenants e delegação segura para Argo CD e Flux CD.
- [[capsule-sbom-cyclonedx-clomonitor-openssf-seguranca-releases]] — Veja também: Capsule: artefatos OCI com SBOM CycloneDX JSON, conformidade OpenSSF Best Practices e CLOMonitor.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/clastix/kamaji/master/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
