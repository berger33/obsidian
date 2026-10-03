---
id: software.devops.tranche19.001853
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

# Tailscale Kubernetes Ingress: exposição de `Services` e `Ingress` internos para a *tailnet* com certificados HTTPS automáticos

## Em uma frase
Com o Tailscale Kubernetes Operator, expor uma aplicação interna do cluster (como Grafana, Argo CD ou Prometheus) exclusivamente para dispositivos autorizados da *tailnet* basta definir `ingressClassName: tailscale` em um recurso **`Ingress`** (ou adicionar a anotação `tailscale.com/expose: "true"` em um `Service`).

## Por que importa
Configurar VPNs site-to-site ou proxies OAuth externos para cada painel interno do Kubernetes consome tempo de engenharia de plataforma.

## Como funciona
Ao detectar um `Ingress` com `spec.ingressClassName: tailscale` e `spec.tls.hosts: ["grafana-prod"]`, o operador cria um Pod de proxy Tailscale que registra o nó `grafana-prod.<tailnet-name>.ts.net` na *tailnet*, provisiona automaticamente um certificado TLS válido via Let's Encrypt e faz proxy reverso para o Service backend.

## Exemplo
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: grafana-internal
  namespace: monitoring
spec:
  ingressClassName: tailscale
  defaultBackend:
    service:
      name: grafana
      port:
        number: 80
  tls:
    - hosts:
        - grafana-prod
```

## Limites e trade-offs
Para expor um serviço TCP bruto (como PostgreSQL ou Redis) em vez de HTTP/HTTPS, utilize um `Service` do tipo `LoadBalancer` com `spec.loadBalancerClass: tailscale` ou a anotação `tailscale.com/expose: "true"`.

## Como verificar
Aplique o `Ingress` com `ingressClassName: tailscale` e verifique com `kubectl get ingress -n monitoring` o FQDN `.ts.net` atribuído na coluna `ADDRESS`.

## Conexões
- [[tailscale-kubernetes-operator-arquitetura-ingress-egress-api-server-proxy]] — Veja também: Tailscale Kubernetes Operator: conectividade nativa de Ingress, Egress, `Connector` e Proxy do Kubernetes API Server.
- [[tailscale-kubernetes-egress-acesso-pods-servicos-externos-tailnet]] — Veja também: Tailscale Kubernetes Egress: conectando Pods do cluster a bancos de dados e servidores privados na *tailnet*.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
