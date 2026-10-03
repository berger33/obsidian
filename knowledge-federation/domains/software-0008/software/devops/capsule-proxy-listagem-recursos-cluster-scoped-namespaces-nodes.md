---
id: software.devops.tranche15.001485
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

# Capsule Proxy: superando a limitação do Kubernetes API Server na listagem filtrada de recursos cluster-scoped

## Em uma frase
O `capsule-proxy` é um add-on opcional de proxy reverso para o Kubernetes API Server que permite aos usuários de um `Tenant` executar comandos como `kubectl get namespaces`, `kubectl get nodes`, `kubectl get storageclasses` e `kubectl get ingressclasses` vendo apenas os recursos que pertencem ou são permitidos ao seu próprio tenant.

## Por que importa
No RBAC nativo do Kubernetes, não existe filtro por recurso em chamadas `LIST` de escopo de cluster: ou o usuário tem permissão `list` em `namespaces` (e vê todos os namespaces de todas as equipes do cluster) ou recebe erro `Forbidden (403)` ao rodar `kubectl get ns`, quebrando dashboards e ferramentas CLI.

## Como funciona
O `capsule-proxy` intercepta requisições direcionadas ao API Server, identifica os tenants e permissões do usuário autenticado, aplica seletores de rótulos dinamicamente e retorna apenas a fatia de objetos cluster-scoped autorizada para aquele tenant.

## Exemplo
```bash
kubectl get pods -n capsule-system -l app.kubernetes.io/name=capsule-proxy
kubectl --as=alice --as-group=capsule.clastix.io get namespaces
```

## Limites e trade-offs
O `capsule-proxy` atua no caminho de leitura/listagem de recursos de escopo de cluster para melhorar a experiência nativa (`kubectl` e UIs); a segurança de escrita e isolamento continua sendo garantida pelos Admission Webhooks do Capsule e pelo RBAC do API Server.

## Como verificar
Execute `kubectl get ns` através do endpoint do `capsule-proxy` com a identidade de um tenant owner e confirme que apenas os namespaces daquele tenant são listados.

## Conexões
- [[capsule-byod-bring-your-own-device-isolamento-nos-noisy-neighbor]] — Veja também: Capsule: modelo Bring Your Own Device (BYOD) e isolamento de nós contra o efeito Noisy Neighbor.
- [[capsule-proxy-proxysetting-vs-globalproxysettings-fronteira-seguranca]] — Veja também: Capsule Proxy: fronteira de segurança entre `ProxySetting` (namespaced) e `GlobalProxySettings` (cluster-wide).

## Fontes
- [Capsule GitHub — README.md (Multi-Tenancy Operator, Tenant Abstraction, Policy Engine, Self-Service Namespaces, BYOD & CycloneDX SBOM)](https://raw.githubusercontent.com/projectcapsule/capsule-proxy/main/README.md) — README oficial do projectcapsule/capsule (CNCF Sandbox) detalhando a prevenção de cluster sprawl via CRD Tenant, herança automática de políticas/cotas e modelo BYOD; consultado em 2026-10-03.
- [Capsule Proxy GitHub — README.md (Filtered Cluster-Scoped Resource Listing, ProxySetting vs GlobalProxySettings Security Boundary)](https://raw.githubusercontent.com/projectcapsule/capsule/main/README.md) — README oficial do projectcapsule/capsule-proxy explicando a filtragem de recursos cluster-scoped para tenants e a fronteira de segurança entre ProxySetting e GlobalProxySettings; consultado em 2026-10-03.
- [Project Capsule — Official GitHub Repository](https://github.com/projectcapsule/capsule) — Repositório oficial Apache-2.0 do Capsule na CNCF; consultado em 2026-10-03.
