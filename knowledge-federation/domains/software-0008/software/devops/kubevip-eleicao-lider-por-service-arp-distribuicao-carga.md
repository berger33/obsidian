---
id: software.devops.tranche13.001289
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

# kube-vip: Eleição de Líder por Service (svc_election) para Distribuir VIPs ARP entre Worker Nodes

## Em uma frase
No modo ARP (Layer 2) para Kubernetes Services, habilitar `svc_election: "true"` (`enableServicesElection`) faz com que o `kube-vip` execute uma eleição de líder independente (`Lease`) para **cada `Service` individual**, em vez de concentrar todos os VIPs de todos os Services em um único nó líder do cluster.

## Por que importa
Com uma única eleição global de líder em modo ARP, se o cluster tiver 30 Services do tipo `LoadBalancer`, 100% dos 30 endereços VIP ficarão vinculados à interface de rede do mesmo nó líder, transformando-o em gargalo de banda.

## Como funciona
Com `svc_election: "true"`, o `Service A` elege o `worker-1` como líder de seu VIP (considerando apenas nós que possuem endpoints ativos quando `externalTrafficPolicy: Local`), enquanto o `Service B` elege o `worker-2`, distribuindo a carga de rede Layer 2 pela frota.

## Exemplo
```yaml
- name: svc_enable
  value: "true"
- name: svc_election
  value: "true"
- name: vip_arp
  value: "true"
```

## Limites e trade-offs
Habilitar `svc_election: "true"` em clusters com centenas de Services `LoadBalancer` aumenta proporcionalmente o número de objetos `Lease` renovados continuamente contra o `kube-apiserver`.

## Como verificar
Use `svc_election: "true"` para distribuir até algumas dezenas de Services em redes Layer 2, ou migre para o modo BGP quando escalar para centenas de VIPs.

## Conexões
- [[kubevip-egress-source-ip-fixo-dhcp-upnp-redes-locais]] — Veja também: kube-vip: Egress com IP de Origem Fixo por Pod, Alocação via DHCP e Exposição UPnP.
- [[kubevip-geracao-manifestos-static-pod-daemonset-rbac-upgrade]] — Veja também: kube-vip: Geração de Manifestos (kube-vip manifest pod / daemonset), RBAC e Upgrade In-Place.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
