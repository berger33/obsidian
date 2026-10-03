---
id: software.devops.tranche19.001852
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

# Tailscale Kubernetes Operator: conectividade nativa de Ingress, Egress, `Connector` e Proxy do Kubernetes API Server

## Em uma frase
O **Tailscale Kubernetes Operator** fornece uma maneira nativa do Kubernetes para conectar dispositivos da *tailnet* a workloads do cluster (**Ingress**), conectar Pods do cluster a serviços externos na *tailnet* (**Egress**), expor o **Kubernetes API Server** de forma privada e hospedar `Connectors` e gravadores de sessão.

## Por que importa
Expor o endpoint do `kube-apiserver` ou serviços internos de administração para a internet pública exige manter load balancers caros, regras de allowlist de IP quebradiças e certificados TLS complexos.

## Como funciona
Instalado via Helm no namespace `tailscale`, o operador gerencia automaticamente Pods de proxy stateful (`StatefulSets`) para cada `Service`/`Ingress` anotado ou `Connector` CRD criado, autenticando cada proxy como um nó dedicado com identidade e tags próprias na *tailnet*.

## Exemplo
```bash
helm upgrade --install tailscale-operator tailscale/tailscale-operator \
  --namespace=tailscale \
  --create-namespace \
  --set-string oauth.clientId="<OAUTH_CLIENT_ID>" \
  --set-string oauth.clientSecret="<OAUTH_CLIENT_SECRET>"
```

## Limites e trade-offs
Com o proxy do Kubernetes API Server habilitado no operador (`apiServerProxyConfig.mode: "true"`), engenheiros e runners de CI executam `kubectl` de qualquer lugar na *tailnet* autenticados por sua identidade Tailscale (*impersonation*) sem abrir o endpoint público do cluster.

## Como verificar
Execute `kubectl get pods -n tailscale` após instalar o operador para verificar o Pod do `operator` em execução.

## Conexões
- [[tailscale-arquitetura-mesh-vpn-wireguard-tailscaled-derp-nat-traversal]] — Veja também: Tailscale: arquitetura de rede mesh sobre WireGuard com daemon `tailscaled`, NAT Traversal e relays `DERP`.
- [[tailscale-kubernetes-ingress-exposicao-servicos-tailnet-tls-automatico]] — Veja também: Tailscale Kubernetes Ingress: exposição de `Services` e `Ingress` internos para a *tailnet* com certificados HTTPS automáticos.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
