---
id: software.devops.tranche15.001483
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

# Capsule: governança de políticas com Admission Controllers para redes, StorageClasses, IngressClasses e registries

## Em uma frase
O Capsule Policy Engine utiliza Validating e Mutating Admission Webhooks do Kubernetes para impor limites de segurança por `Tenant`, restringindo quais `StorageClasses`, `IngressClasses`, registries de container, tipos de Service (`NodePort`/`LoadBalancer`) e políticas de rede cada tenant pode usar.

## Por que importa
Em um cluster compartilhado, impedir que um tenant utilize uma `StorageClass` cara de NVMe dedicada a outro departamento, exponha portas arbitrárias via `NodePort` ou baixe imagens de registros externos não confiáveis é essencial para governança e segurança.

## Como funciona
As regras declaradas na especificação do `Tenant` são validadas em tempo de admissão no API Server: se um desenvolvedor tentar criar um PVC ou Ingress com uma classe fora da lista permitida do seu tenant, a requisição é rejeitada imediatamente com mensagem explicativa.

## Exemplo
```bash
kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations | grep capsule
```

## Limites e trade-offs
Políticas de admissão do Capsule validam objetos no momento da criação ou atualização; ao restringir uma regra em um `Tenant` que já possui workloads antigos em execução, audite também os recursos preexistentes nos namespaces.

## Como verificar
Tente criar um recurso usando uma `StorageClass` não autorizada como usuário do tenant e valide que o webhook do Capsule bloqueia a operação.

## Conexões
- [[capsule-self-service-namespaces-heranca-rbac-quotas-limitranges]] — Veja também: Capsule: autoatendimento de namespaces e herança automática de RBAC, ResourceQuotas e LimitRanges.
- [[capsule-byod-bring-your-own-device-isolamento-nos-noisy-neighbor]] — Veja também: Capsule: modelo Bring Your Own Device (BYOD) e isolamento de nós contra o efeito Noisy Neighbor.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
