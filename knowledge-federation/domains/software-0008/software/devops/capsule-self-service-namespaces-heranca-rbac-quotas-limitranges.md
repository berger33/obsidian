---
id: software.devops.tranche15.001482
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
fontes: ["https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md", "https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md", "https://github.com/projectcapsule/capsule"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Capsule: autoatendimento de namespaces e herança automática de RBAC, ResourceQuotas e LimitRanges

## Em uma frase
Quando um proprietário de `Tenant` cria um novo namespace no cluster, os webhooks de admissão e controladores do Capsule vinculam automaticamente o namespace ao `Tenant` (via OwnerReference e labels) e injetam todas as políticas e cotas definidas no nível do tenant.

## Por que importa
Sem o Capsule, toda vez que uma equipe de desenvolvimento precisa de um novo namespace (`app-dev`, `app-staging`, `app-qa`), ela precisa abrir chamado para o administrador do cluster configurar RoleBindings, ResourceQuotas e NetworkPolicies manualmente.

## Como funciona
No manifesto do `Tenant`, o administrador define `namespaceQuota` (quantos namespaces a equipe pode criar), `owners` (usuários, grupos OIDC ou ServiceAccounts) e orçamentos agregados de CPU, memória e storage que são contabilizados através de todos os namespaces pertencentes àquele tenant.

## Exemplo
```bash
kubectl --as=alice --as-group=capsule.clastix.io create namespace oil-production
kubectl get namespace oil-production -o yaml | grep -E "capsule.clastix.io|ownerReferences" -A 4
```

## Limites e trade-offs
Para que os webhooks do Capsule interceptem corretamente as requisições dos usuários do tenant, os usuários ou ServiceAccounts proprietários devem pertencer ao grupo configurado no Capsule (por padrão `capsule.clastix.io` ou o grupo OIDC especificado).

## Como verificar
Crie um namespace autenticando-se como o `owner` do tenant e verifique que os `RoleBindings`, `LimitRanges` e `ResourceQuotas` foram provisionados instantaneamente dentro dele.

## Conexões
- [[capsule-arquitetura-multi-tenancy-tenant-crd-cluster-sprawl]] — Veja também: Clastix Capsule: operador CNCF Sandbox de multi-tenancy em Kubernetes baseado na abstração `Tenant`.
- [[capsule-governanca-admission-controllers-network-storage-ingress]] — Veja também: Capsule: governança de políticas com Admission Controllers para redes, StorageClasses, IngressClasses e registries.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
