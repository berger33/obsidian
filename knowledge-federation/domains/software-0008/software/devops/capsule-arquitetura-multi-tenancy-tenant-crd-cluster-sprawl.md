---
id: software.devops.tranche15.001481
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

# Clastix Capsule: operador CNCF Sandbox de multi-tenancy em Kubernetes baseado na abstração `Tenant`

## Em uma frase
O Capsule (projeto CNCF Sandbox criado pela Clastix, licença Apache-2.0) implementa multi-tenancy seguro e baseado em políticas em um único cluster Kubernetes agrupando múltiplos namespaces sob a abstração declarativa `Tenant`.

## Por que importa
A estrutura plana de namespaces nativos do Kubernetes dificulta o compartilhamento de cotas e políticas entre múltiplos namespaces de uma mesma equipe, levando organizações a criar um cluster inteiro por equipe (*cluster sprawl*). O Capsule resolve isso permitindo que vários departamentos compartilhem o mesmo cluster com autonomia e isolamento.

## Como funciona
O Capsule Controller gerencia o Custom Resource `Tenant`: dentro de cada tenant, os usuários proprietários (`owners`) têm autonomia para criar seus próprios namespaces sob demanda (`kubectl create ns`), enquanto o motor de políticas do Capsule propaga automaticamente RBAC, NetworkPolicies, ResourceQuotas e LimitRanges para todos os namespaces daquele tenant.

## Exemplo
```bash
kubectl get tenants
kubectl describe tenant oil-tenant
```

## Limites e trade-offs
O Capsule segue uma abordagem minimalista 100% nativa do Kubernetes: não exige binários cliente customizados nem plugins proprietários para criar namespaces dentro da cota do tenant.

## Como verificar
Execute `kubectl get tenants` e verifique a contagem de namespaces alocados (`namespaceCount`) versus a cota máxima (`namespaceQuota`) de cada tenant.

## Conexões
- [[capsule-self-service-namespaces-heranca-rbac-quotas-limitranges]] — Veja também: Capsule: autoatendimento de namespaces e herança automática de RBAC, ResourceQuotas e LimitRanges.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
