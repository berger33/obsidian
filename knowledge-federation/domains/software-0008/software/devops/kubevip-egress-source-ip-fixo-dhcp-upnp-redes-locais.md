---
id: software.devops.tranche13.001288
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md", "https://kube-vip.io/docs/about/architecture/", "https://github.com/kube-vip/kube-vip"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kube-vip: Egress com IP de Origem Fixo por Pod, Alocação via DHCP e Exposição UPnP

## Em uma frase
Além do tráfego de entrada, o `kube-vip` suporta **Egress** (utilizando o IP de um `Service LoadBalancer` também como endereço IP de origem de saída para o Pod), alocação dinâmica de IPs de LoadBalancer via servidor **DHCP** existente na rede (`0.0.0.0`) e exposição automática de portas em gateways via **UPnP**.

## Por que importa
Quando uma aplicação dentro do Kubernetes precisa acessar um banco de dados legado ou parceiro externo protegido por firewall de IP de origem (allowlist), o SNAT padrão pelo IP do worker node muda sempre que o Pod é reagendado em outro nó.

## Como funciona
Com o modo Egress do `kube-vip` ativado por anotações no `Service`, o `kube-vip` configura regras de roteamento/NAT no nó onde o Pod está rodando para que todo tráfego de saída daquele Pod saia com o endereço VIP estático do `Service` como IP de origem.

## Exemplo
```yaml
apiVersion: v1
kind: Service
metadata:
  name: payment-gateway-egress
  annotations:
    kube-vip.io/egress: "true"
    kube-vip.io/loadbalancerIPs: "192.168.1.240"
spec:
  type: LoadBalancer
  externalTrafficPolicy: Local
```

## Limites e trade-offs
Habilitar `kube-vip.io/egress: "true"` em um `Service` sem `externalTrafficPolicy: Local` ou com múltiplos Pods espalhados em nós diferentes gera conflito sobre qual nó deve originar e receber o retorno do tráfego daquele IP.

## Como verificar
Use `externalTrafficPolicy: Local` e garanta relação determinística entre o VIP de Egress e o Pod que origina conexões externas.

## Conexões
- [[kubevip-gateway-api-loadbalancer-sem-endpoints-annotation]] — Veja também: kube-vip: Suporte a Services LoadBalancer de Gateway API sem Endpoints (allow-reconcile-without-endpoints).
- [[kubevip-eleicao-lider-por-service-arp-distribuicao-carga]] — Veja também: kube-vip: Eleição de Líder por Service (svc_election) para Distribuir VIPs ARP entre Worker Nodes.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
