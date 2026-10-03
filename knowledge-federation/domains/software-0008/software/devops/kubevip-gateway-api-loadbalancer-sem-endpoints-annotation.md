---
id: software.devops.tranche13.001287
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

# kube-vip: Suporte a Services LoadBalancer de Gateway API sem Endpoints (allow-reconcile-without-endpoints)

## Em uma frase
Para controladores de **Gateway API** que criam objetos `Service` do tipo `LoadBalancer` intencionalmente sem backends `Endpoints` ou `EndpointSlices` (roteando o tráfego por outros mecanismos), o `kube-vip` disponibiliza a anotação opt-in `kube-vip.io/allow-reconcile-without-endpoints: "true"`.

## Por que importa
Por padrão, o `kube-vip` aguarda que um `Service` possua pelo menos um endpoint ativo antes de anunciar o endereço VIP na rede; em implementações de Gateway API sem endpoints anexados ao Service, o VIP nunca seria anunciado sem essa anotação.

## Como funciona
Quando o `Service` declara `metadata.annotations["kube-vip.io/allow-reconcile-without-endpoints"]: "true"` combinado com `spec.type: LoadBalancer` e `spec.externalTrafficPolicy: Cluster`, o `kube-vip` reconcilia e anuncia o VIP imediatamente mesmo na ausência de `Endpoints`/`EndpointSlices`.

## Exemplo
```yaml
apiVersion: v1
kind: Service
metadata:
  name: gateway-proxy-lb
  namespace: gateway-system
  annotations:
    kube-vip.io/allow-reconcile-without-endpoints: "true"
spec:
  type: LoadBalancer
  externalTrafficPolicy: Cluster
  ports:
    - name: https
      port: 443
      targetPort: 8443
```

## Limites e trade-offs
Combinar `kube-vip.io/allow-reconcile-without-endpoints: "true"` com `externalTrafficPolicy: Local` não tem efeito, pois o comportamento sem endpoints é suportado exclusivamente quando `externalTrafficPolicy` é `Cluster`.

## Como verificar
Certifique-se de que `spec.externalTrafficPolicy: Cluster` esteja definido nos Services de Gateway API que utilizam `kube-vip.io/allow-reconcile-without-endpoints: "true"`.

## Conexões
- [[kubevip-runtime-config-file-precedencia-validacao-estrita]] — Veja também: kube-vip: Arquivo de Configuração de Runtime (--config-file), Ordem de Precedência e Validação Estrita.
- [[kubevip-egress-source-ip-fixo-dhcp-upnp-redes-locais]] — Veja também: kube-vip: Egress com IP de Origem Fixo por Pod, Alocação via DHCP e Exposição UPnP.

## Fontes
- [kube-vip GitHub — README.md (Runtime Config File Precedence, Gateway API without Endpoints & SELinux IPVS Kernel Modules)](https://raw.githubusercontent.com/kube-vip/kube-vip/main/README.md) — README oficial do kube-vip/kube-vip documentando a ordem de precedência de --config-file, anotação kube-vip.io/allow-reconcile-without-endpoints e pré-carregamento de ip_vs/ip_vs_rr com SELinux; consultado em 2026-10-03.
- [kube-vip Official Documentation — Architecture (Cluster VIP, ARP Leader Election, BGP Peering, IPVS Load Balancing & Service Watcher)](https://kube-vip.io/docs/about/architecture/) — Documentação oficial de arquitetura do kube-vip explicando eleição de líder, Gratuitous ARP, BGP multi-nó, balanceamento IPVS do control plane e integração com kube-vip-cloud-provider; consultado em 2026-10-03.
- [kube-vip — Official GitHub Repository](https://github.com/kube-vip/kube-vip) — Repositório oficial Apache-2.0 do kube-vip; consultado em 2026-10-03.
