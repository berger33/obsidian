---
id: software.devops.tranche15.001484
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

# Capsule: modelo Bring Your Own Device (BYOD) e isolamento de nós contra o efeito Noisy Neighbor

## Em uma frase
O recurso *Bring Your Own Device* (BYOD) do Capsule permite associar um conjunto dedicado de nós de computação, armazenamento e rede a um `Tenant` específico por meio de `nodeSelector` forçado e taints/tolerations, eliminando o efeito *noisy neighbor*.

## Por que importa
Mesmo com `ResourceQuotas` de CPU e memória, cargas de trabalho intensivas em I/O de disco, cache L3 de CPU ou largura de banda de rede podem degradar aplicações de outro tenant se compartilharem o mesmo worker node físico.

## Como funciona
Quando um `Tenant` possui `nodeSelector` configurado no Capsule, todos os Pods criados em qualquer namespace daquele tenant recebem automaticamente a afinidade para o pool de nós dedicado àquela equipe, impedindo que escalonem nos nós de outros departamentos.

## Exemplo
```bash
kubectl get nodes --show-labels | grep pool.corp.io/tenant
kubectl get tenant oil-tenant -o jsonpath='{.spec.nodeSelector}'
```

## Limites e trade-offs
Ao usar o modo BYOD com `nodeSelector` injetado pelo Capsule, impeça que usuários do tenant editem diretamente os rótulos dos objetos `Node` no RBAC do cluster.

## Como verificar
Crie um Pod simples em um namespace do tenant e verifique com `kubectl get pod -o wide` que ele foi agendado exclusivamente nos nós do pool daquele tenant.

## Conexões
- [[capsule-governanca-admission-controllers-network-storage-ingress]] — Veja também: Capsule: governança de políticas com Admission Controllers para redes, StorageClasses, IngressClasses e registries.
- [[capsule-proxy-listagem-recursos-cluster-scoped-namespaces-nodes]] — Veja também: Capsule Proxy: superando a limitação do Kubernetes API Server na listagem filtrada de recursos cluster-scoped.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
