---
id: software.devops.tranche15.001490
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

# Capsule: operação em produção, alta disponibilidade do controlador de admissão e diagnóstico de webhooks

## Em uma frase
Em ambientes de produção, o `capsule-controller-manager` e o `capsule-proxy` devem operar com múltiplas réplicas, certificados TLS válidos nos webhooks e monitoramento de latência de admissão no Kubernetes API Server.

## Por que importa
Como o Capsule registra Validating e Mutating Webhooks sobre recursos centrais (`namespaces`, `pods`, `services`, `ingresses`, `persistentvolumeclaims`), a indisponibilidade total de todas as réplicas do webhook pode bloquear a criação de recursos nos tenants.

## Como funciona
A implantação recomendada via Helm chart oficial (`projectcapsule/capsule`) configura eleição de líder entre réplicas do controlador, gerenciamento automático dos certificados CA dos webhooks e métricas Prometheus para acompanhar rejeições de política e saúde da reconciliação.

## Exemplo
```bash
kubectl get pods -n capsule-system
kubectl logs -n capsule-system deployment/capsule-controller-manager --tail=30
```

## Limites e trade-offs
Evite aplicar políticas restritivas do Capsule sobre o próprio namespace `capsule-system` ou `kube-system`, mantendo os namespaces de sistema na lista de exceção da configuração (`CapsuleConfiguration`).

## Como verificar
Inspecione o recurso global `kubectl get capsuleconfiguration default -o yaml` para auditar os grupos de usuários gerenciados e as expressões regulares de namespaces protegidos.

## Conexões
- [[capsule-sbom-cyclonedx-clomonitor-openssf-seguranca-releases]] — Veja também: Capsule: artefatos OCI com SBOM CycloneDX JSON, conformidade OpenSSF Best Practices e CLOMonitor.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
