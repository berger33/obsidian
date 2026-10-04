---
id: software.devops.tranche03.000218
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md", "https://kubernetes-sigs.github.io/external-dns/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Precedência da lista externalIPs em clusters bare-metal atrás de NAT ou com MetalLB

## Em uma frase
O segundo parágrafo da seção Note do README explica que, se a lista externalIPs estiver definida para um Service do tipo LoadBalancer, essa lista será utilizada em vez do IP atribuído ao balanceador de carga para criar o registro DNS, destacando que isso é útil ao executar clusters Kubernetes bare-metal atrás de NAT ou em configurações similares onde o IP do balanceador difere do IP público (por exemplo, com MetalLB).

## Por que importa
Em datacenters on-premises ou homelabs com MetalLB, o Service LoadBalancer recebe um IP privado da LAN local, mas os clientes externos na internet precisam resolver o IP público do roteador/firewall NAT da borda.

## Como funciona
Preencha o campo externalIPs no Service LoadBalancer quando operar em bare-metal com MetalLB atrás de NAT e precisar que o ExternalDNS publique o endereço público externo na zona DNS.

## Exemplo
Um cluster bare-metal usando MetalLB atribui um IP privado ao Service, mas define externalIPs com o IP público do firewall para que o ExternalDNS registre o endereço acessível externamente.

## Limites e trade-offs
Certifique-se de que o roteador NAT encaminhe corretamente as portas do IP listado em externalIPs para o IP local alocado pelo MetalLB antes de publicar o registro DNS.

## Como verificar
Conferi o segundo parágrafo da seção Note no README oficial de kubernetes-sigs/external-dns.

## Conexões
- [[externaldns-txt-prefix-cname-conflict-prevention]] — Veja também: Uso obrigatório de --txt-prefix com registros CNAME e risco de perda de propriedade.
- [[externaldns-webhook-provider-architecture-pr3063]] — Veja também: Arquitetura de provedores via Webhook (PR 3063) e fim de novos provedores in-tree.

## Fontes
- [ExternalDNS — GitHub README](https://raw.githubusercontent.com/kubernetes-sigs/external-dns/master/README.md) — Visão geral do ExternalDNS (sincronização de Services e Ingresses com provedores DNS, --domain-filter, --txt-owner-id, --txt-prefix, --dry-run, --policy=sync vs upsert-only, externalIPs e provedores webhook).; consultado em 2026-10-03.
- [ExternalDNS Documentation — Official Guides & FAQ](https://kubernetes-sigs.github.io/external-dns/) — Documentação oficial do ExternalDNS cobrindo tutoriais por provedor, TTL avançado e FAQ.; consultado em 2026-10-03.
