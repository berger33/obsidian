---
id: software.devops.tranche03.000284
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
fontes: ["https://raw.githubusercontent.com/coredns/coredns/master/README.md", "https://coredns.io/plugins/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Plugins de backend e integração cloud-native: kubernetes, etcd (substituindo SkyDNS), route53, forward e cache

## Em uma frase
A lista de capacidades do README destaca os plugins que conectam o CoreDNS a plataformas cloud-native: **cache** (caching de respostas DNS), **etcd** (usar o etcd como backend, substituindo o antigo SkyDNS), **kubernetes** (usar a API do Kubernetes como backend para descoberta de serviços e pods), **forward** (atuar como proxy encaminhando consultas para outros nameservers recursivos) e **route53** (integração com provedores de nuvem como AWS Route 53).

## Por que importa
Em qualquer cluster Kubernetes, a dupla `kubernetes` + `forward` + `cache` é o coração da resolução de nomes: consultas para `cluster.local` são respondidas pelo plugin `kubernetes`, consultas externas são encaminhadas pelo `forward` aos resolvedores upstream e o `cache` reduz a latência e a carga sobre ambos.

## Como funciona
Dimensione o plugin `cache` e os endpoints de `forward` no `Corefile` do cluster para absorver picos de consultas DNS das aplicações sem sobrecarregar os servidores DNS da VPC ou da rede corporativa.

## Exemplo
Quando um pod resolve `pagamentos.default.svc.cluster.local`, o plugin `kubernetes` responde diretamente; quando resolve um domínio externo, o plugin `forward` consulta o DNS recursivo configurado e o `cache` armazena o resultado pelo TTL.

## Limites e trade-offs
Em clusters com `ndots:5` padrão no `/etc/resolv.conf` dos pods, cada nome externo gera múltiplas consultas de sufixo antes de chegar ao `forward`; monitore a taxa de requisições com o plugin `prometheus`.

## Como verificar
Conferi a lista Currently CoreDNS is able to no README oficial de coredns/coredns.

## Conexões
- [[coredns-zone-serving-dnssec-axfr-and-loadbalance]] — Veja também: Plugins de autoridade e transferência de zonas: file, auto, secondary (AXFR), dnssec, transfer e loadbalance.
- [[coredns-observability-security-and-query-manipulation-plugins]] — Veja também: Plugins de observabilidade, diagnóstico e manipulação: prometheus, log, errors, pprof, rewrite, template, any e dns64.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
