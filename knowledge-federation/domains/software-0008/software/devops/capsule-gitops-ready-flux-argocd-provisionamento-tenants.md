---
id: software.devops.tranche15.001487
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

# Capsule: operação declarativa GitOps-ready de Tenants e delegação segura para Argo CD e Flux CD

## Em uma frase
Sendo 100% declarativo e baseado em Custom Resources nativos, o Capsule permite gerenciar o ciclo de vida de todos os `Tenants` via GitOps (Flux CD ou Argo CD) e delegar uma ServiceAccount de reconciliação GitOps como `owner` de cada tenant.

## Por que importa
Em plataformas corporativas, tanto a criação de novos tenants (onboarding de novas tribos/squads) quanto o deploy contínuo das aplicações de cada squad dentro de seus próprios namespaces precisam ocorrer via Pull Requests auditáveis no Git.

## Como funciona
A equipe de plataforma versiona os manifestos `kind: Tenant` no repositório Git administrativo; dentro de cada `Tenant`, inclui a `ServiceAccount` da instância ou AppProject do Argo CD/Flux daquela equipe na lista `spec.owners`, permitindo que o motor GitOps da equipe crie namespaces e aplique recursos apenas dentro das fronteiras do seu tenant.

## Exemplo
```yaml
apiVersion: capsule.clastix.io/v1beta2
kind: Tenant
metadata:
  name: payments-tenant
spec:
  namespaceOptions:
    quota: 5
  owners:
    - name: system:serviceaccount:argocd:payments-deployer
      kind: ServiceAccount
```

## Limites e trade-offs
Ao remover ou reduzir a cota de um `Tenant` via GitOps, verifique antes o comportamento de retenção configurado para que namespaces produtivos não sejam órfãos ou bloqueados inadvertidamente.

## Como verificar
Aplique o manifesto `Tenant` em modo `--dry-run=server` e confirme a validação pelo webhook do Capsule antes do merge no repositório GitOps.

## Conexões
- [[capsule-proxy-proxysetting-vs-globalproxysettings-fronteira-seguranca]] — Veja também: Capsule Proxy: fronteira de segurança entre `ProxySetting` (namespaced) e `GlobalProxySettings` (cluster-wide).
- [[capsule-combinado-kamaji-hard-vs-soft-multitenancy-kubernetes]] — Veja também: Capsule e Kamaji: escolha e combinação entre Soft Multi-Tenancy (namespaces) e Hard Multi-Tenancy (control planes).

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
