---
id: software.devops.tranche19.001854
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

# Tailscale Kubernetes Egress: conectando Pods do cluster a bancos de dados e servidores privados na *tailnet*

## Em uma frase
O recurso de **Egress** do Tailscale Kubernetes Operator permite que aplicações rodando dentro do Kubernetes se comuniquem de forma transparente com máquinas externas, bancos de dados on-premises ou serviços de outros clusters presentes na *tailnet*, por meio de um `Service` anotado com **`tailscale.com/tailnet-fqdn`** ou **`tailscale.com/tailnet-ip`**.

## Por que importa
Quando um Pod no Kubernetes na nuvem precisa consultar um banco de dados legado on-premises, instalar o cliente VPN como sidecar em cada Pod de aplicação exige privilégios `NET_ADMIN` ou polui os manifestos das equipes de produto.

## Como funciona
Com o Tailscale Operator, o engenheiro cria um `Service` Kubernetes comum (`type: ExternalName` com a anotação `tailscale.com/tailnet-fqdn: "legacy-db.tailnet-xyz.ts.net"`). O operador provisiona um proxy de egresso no namespace `tailscale` e reescreve o Service para que qualquer Pod do cluster acesse `http://legacy-db-svc.default.svc.cluster.local` usando DNS padrão do Kubernetes.

## Exemplo
```yaml
apiVersion: v1
kind: Service
metadata:
  name: onprem-postgres
  namespace: default
  annotations:
    tailscale.com/tailnet-fqdn: "pg-onprem.tail-example.ts.net"
spec:
  externalName: placeholder
  type: ExternalName
  ports:
    - port: 5432
      protocol: TCP
```

## Limites e trade-offs
Combinar Ingress em um cluster `A` com Egress em um cluster `B` permite rotear tráfego **multi-cluster** entre regiões e provedores de nuvem distintos mantendo políticas de segurança baseadas em identidade (tags ACL) do Tailscale.

## Como verificar
Crie um Service de Egress anotado com `tailscale.com/tailnet-fqdn` e verifique com `kubectl describe svc onprem-postgres` que o operador provisionou o proxy e atualizou o alvo.

## Conexões
- [[tailscale-kubernetes-ingress-exposicao-servicos-tailnet-tls-automatico]] — Veja também: Tailscale Kubernetes Ingress: exposição de `Services` e `Ingress` internos para a *tailnet* com certificados HTTPS automáticos.
- [[tailscale-connector-crd-subnet-router-exit-node-kubernetes]] — Veja também: Tailscale `Connector` CRD: implantação declarativa de Subnet Routers e Exit Nodes em alta disponibilidade no Kubernetes.

## Fontes
- [Tailscale GitHub — README.md (Private WireGuard Networks Made Easy, tailscaled Daemon & tailscale CLI)](https://tailscale.com/docs/kubernetes-operator) — README oficial do tailscale/tailscale descrevendo o daemon tailscaled, a CLI tailscale e suporte multiplataforma; consultado em 2026-10-03.
- [Tailscale Official Documentation — Tailscale Kubernetes Operator (API Server Proxy, Ingress, Egress, Connector, Multi-Cluster & Session Recorder)](https://raw.githubusercontent.com/tailscale/tailscale/main/README.md) — Documentação oficial do Tailscale Kubernetes Operator detalhando exposição de workloads, egresso para a tailnet, Connector CRD (Subnet Router/Exit Node) e Recorder; consultado em 2026-10-03.
- [Tailscale — Official GitHub Repository](https://github.com/tailscale/tailscale) — Repositório oficial BSD-3-Clause do cliente e daemon Tailscale; consultado em 2026-10-03.
