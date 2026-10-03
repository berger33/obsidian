---
id: software.devops.tranche13.001285
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

# kube-vip: Balanceamento de Kubernetes Services (svc_enable) e Integração com kube-vip-cloud-provider

## Em uma frase
Quando `svc_enable: "true"` está ativo, o `kube-vip` observa objetos `Service` do tipo `LoadBalancer` que possuem a anotação `metadata.annotations["kube-vip.io/loadbalancerIPs"]` (preenchida pelo `kube-vip-cloud-provider` ou declarada estaticamente), anuncia o IP na rede via ARP/BGP e atualiza `status.loadBalancer.ingress`.

## Por que importa
Em clusters bare-metal, criar um `Service` com `type: LoadBalancer` deixa o campo `EXTERNAL-IP` eternamente em `<pending>` se não houver um controlador que aloque um IP de um pool e um daemon que anuncie esse IP na rede.

## Como funciona
O fluxo ocorre em dois passos coordenados: o **kube-vip-cloud-provider** lê o `ConfigMap` `kubevip` (em `kube-system`, contendo `cidr-global` ou faixas por namespace `cidr-<namespace>`), escolhe um IP livre e grava a anotação `kube-vip.io/loadbalancerIPs` no `Service`; em seguida, o Pod do `kube-vip` detecta a anotação, anuncia o VIP via ARP ou BGP e marca o `Service` como pronto.

## Exemplo
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubevip
  namespace: kube-system
data:
  cidr-global: 192.168.1.200/29
  range-development: 192.168.1.210-192.168.1.219
```

## Limites e trade-offs
Depender exclusivamente do campo legado `spec.loadBalancerIP` (depreciado desde o Kubernetes 1.24) sem usar a anotação moderna `kube-vip.io/loadbalancerIPs` gera avisos de depreciação e perde suporte a múltiplos IPs dual-stack.

## Como verificar
Utilize a anotação `kube-vip.io/loadbalancerIPs` (ou deixe o `kube-vip-cloud-provider` gerenciá-la automaticamente a partir do `ConfigMap` `kubevip`).

## Conexões
- [[kubevip-control-plane-ipvs-load-balancing-selinux-modprobe]] — Veja também: kube-vip: Balanceamento do Control Plane com IPVS (lb_enable) e Pré-Carregamento de Módulos com SELinux.
- [[kubevip-runtime-config-file-precedencia-validacao-estrita]] — Veja também: kube-vip: Arquivo de Configuração de Runtime (--config-file), Ordem de Precedência e Validação Estrita.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://kube-vip.io/docs/about/architecture/) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
