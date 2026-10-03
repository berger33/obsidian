---
id: software.devops.tranche19.001855
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://tailscale.com/docs/kubernetes-operator", "https://raw.githubusercontent.com/tailscale/tailscale/main/README.md", "https://github.com/tailscale/tailscale"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Tailscale `Connector` CRD: implantação declarativa de Subnet Routers e Exit Nodes em alta disponibilidade no Kubernetes

## Em uma frase
O Custom Resource **`Connector`** (`tailscale.com/v1alpha1`) do Tailscale Kubernetes Operator permite implantar **Subnet Routers** (expondo CIDRs inteiros de Pods/Services ou VPC para a *tailnet*) e **Exit Nodes** rodando como Pods gerenciados dentro do cluster Kubernetes.

## Por que importa
Se você possui centenas de serviços ou endpoints RDS em uma VPC privada sem poder instalar o agente Tailscale em cada um, um *Subnet Router* anuncia os prefixos CIDR (`10.244.0.0/16`, `10.100.0.0/16`) para a *tailnet* com failover automático.

## Como funciona
Ao aplicar um recurso `Connector` especificando `spec.subnetRouter.advertiseRoutes` e `spec.replicas: 2`, o operador implanta múltiplas réplicas para alta disponibilidade (*High Availability Subnet Router*) e aplica as tags ACL configuradas em `spec.tags`.

## Exemplo
```yaml
apiVersion: tailscale.com/v1alpha1
kind: Connector
metadata:
  name: vpc-subnet-router
spec:
  replicas: 2
  tags:
    - tag:k8s-subnet-router
  subnetRouter:
    advertiseRoutes:
      - 10.96.0.0/12
      - 10.244.0.0/16
```

## Limites e trade-offs
Para que as rotas anunciadas por um `Connector` entrem em vigor imediatamente sem aprovação manual no painel, adicione uma regra `autoApprovers` para a tag `tag:k8s-subnet-router` no arquivo de política (ACL/Grants) da *tailnet*.

## Como verificar
Execute `kubectl get connectors` para verificar a prontidão das réplicas e as rotas anunciadas pelo `Connector`.

## Conexões
- [[tailscale-kubernetes-egress-acesso-pods-servicos-externos-tailnet]] — Veja também: Tailscale Kubernetes Egress: conectando Pods do cluster a bancos de dados e servidores privados na *tailnet*.
- [[tailscale-acls-grants-tags-autoapprovers-politica-zero-trust]] — Veja também: Tailscale Políticas Zero-Trust (ACLs e `Grants`): controle de acesso baseado em identidade, `tagOwners` e `autoApprovers`.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
