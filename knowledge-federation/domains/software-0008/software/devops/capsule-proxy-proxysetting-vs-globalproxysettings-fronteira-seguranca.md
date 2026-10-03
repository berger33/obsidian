---
id: software.devops.tranche15.001486
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
fontes: ["https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md", "https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md", "https://github.com/projectcapsule/capsule"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Capsule Proxy: fronteira de segurança entre `ProxySetting` (namespaced) e `GlobalProxySettings` (cluster-wide)

## Em uma frase
No `capsule-proxy`, recursos `ProxySetting` (escopo de namespace) delegam permissões apenas dentro do tenant associado, enquanto concessões de acesso a recursos de escopo de cluster exigem obrigatoriamente o recurso administrativo `GlobalProxySettings` com `ProxyClusterScoped` habilitado.

## Por que importa
Permitir que um objeto `ProxySetting` namespaced criado por um usuário comum concedesse visibilidade sobre recursos globais do cluster violaria a fronteira de segurança entre tenants.

## Como funciona
Por medida de segurança explícita, o campo depreciado `spec.subjects[].clusterResources` em objetos `ProxySetting` namespaced é ignorado pelo runtime do `capsule-proxy` e deve ser omitido ou vazio. Administradores devem migrar quaisquer concessões de recursos de cluster para `GlobalProxySettings` e manter a criação/edição de `GlobalProxySettings` estritamente restrita a administradores do cluster.

## Exemplo
```bash
kubectl get globalproxysettings
kubectl get proxysettings -A
```

## Limites e trade-offs
Ao atualizar o `capsule-proxy` para versões que aplicam essa restrição, a documentação enfatiza que é obrigatório fazer o rollout da nova imagem do proxy em todas as réplicas além de atualizar o CRD `ProxySetting`, removendo em seguida as concessões namespaced obsoletas.

## Como verificar
Verifique que nenhuma réplica antiga do `capsule-proxy` permanece em execução (`kubectl get pods -n capsule-system -o custom-columns=NAME:.metadata.name,IMAGE:.spec.containers[0].image`) e audite os objetos `ProxySetting` existentes.

## Conexões
- [[capsule-proxy-listagem-recursos-cluster-scoped-namespaces-nodes]] — Veja também: Capsule Proxy: superando a limitação do Kubernetes API Server na listagem filtrada de recursos cluster-scoped.
- [[capsule-gitops-ready-flux-argocd-provisionamento-tenants]] — Veja também: Capsule: operação declarativa GitOps-ready de Tenants e delegação segura para Argo CD e Flux CD.

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
