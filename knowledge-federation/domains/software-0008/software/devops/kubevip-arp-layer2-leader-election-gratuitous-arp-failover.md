---
id: software.devops.tranche13.001282
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
fontes: ["https://kube-vip.io/docs/about/architecture/", "https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md", "https://github.com/kube-vip/kube-vip"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# kube-vip: Modo ARP (Layer 2), Eleição de Líder e Failover Rápido com Gratuitous ARP

## Em uma frase
No modo **ARP (Layer 2)** (`enableARP: true`), o `kube-vip` utiliza a eleição de líder nativa do Kubernetes (`client-go/tools/leaderelection` ou Raft para bootstrap do control plane) para eleger um único nó que vincula o endereço VIP à interface de rede declarada e anuncia a mudança na rede local via **Gratuitous ARP**.

## Por que importa
Quando o nó líder falha e o VIP migra para outro host na mesma sub-rede L2, clientes e roteadores locais continuariam enviando pacotes para o endereço MAC antigo até o cache ARP expirar (tipicamente 30 segundos) se o novo líder não transmitisse um broadcast Gratuitous ARP.

## Como funciona
Assim que o novo líder assume o lease da eleição, o `kube-vip` associa o VIP à interface de rede local e transmite pacotes Gratuitous ARP que atualizam imediatamente o mapeamento VIP-para-MAC nos switches e hosts vizinhos, completando o failover em poucos segundos.

## Exemplo
```yaml
# Variaveis de ambiente para modo ARP Layer 2 com eleicao de lider:
- name: vip_arp
  value: "true"
- name: vip_leaderelection
  value: "true"
- name: vip_leaseduration
  value: "5"
- name: vip_renewdeadline
  value: "3"
- name: vip_retryperiod
  value: "1"
```

## Limites e trade-offs
Configurar o modo ARP (Layer 2) entre nós que estão em sub-redes ou VLANs diferentes sem conectividade de broadcast Layer 2 impede que o VIP flutuante seja alcançado quando o líder muda de sub-rede.

## Como verificar
Use o modo ARP apenas quando todos os nós candidatos ao VIP compartilharem o mesmo domínio de broadcast L2; para nós em sub-redes/racks distintos, utilize o modo BGP (Layer 3).

## Conexões
- [[kubevip-arquitetura-vip-load-balancer-control-plane-services]] — Veja também: kube-vip: Arquitetura de Virtual IP (VIP) e Load Balancer para Control Plane e Services Kubernetes.
- [[kubevip-bgp-layer3-ecmp-rotas-peers-multinodo]] — Veja também: kube-vip: Modo BGP (Layer 3) para Anúncio Multi-Nó de VIPs e Balanceamento ECMP.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://kube-vip.io/docs/about/architecture/) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
