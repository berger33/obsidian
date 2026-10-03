---
id: software.devops.tranche03.000283
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

# Plugins de autoridade e transferência de zonas: file, auto, secondary (AXFR), dnssec, transfer e loadbalance

## Em uma frase
Na lista de capacidades atuais do README oficial, o CoreDNS documenta seus plugins para servir zonas DNS: **file** e **auto** (servir dados de zona a partir de arquivos em disco ou carregá-los automaticamente, suportando DNS e DNSSEC com NSEC only), **secondary** (recuperar dados de zona de servidores primários atuando como secundário via AXFR only), **dnssec** (assinar dados de zona on-the-fly), **loadbalance** (balanceamento de carga das respostas, embaralhando registros A/AAAA) e **transfer** (permitir transferências de zona atuando como servidor primário em conjunto com `file`).

## Por que importa
Esses plugins mostram que o CoreDNS não é apenas um proxy recursivo simples: ele pode atuar como servidor autoritativo primário ou secundário com transferência AXFR, assinatura DNSSEC em tempo real e round-robin de respostas.

## Como funciona
Combine `file` (ou `auto`) com `transfer` e `dnssec` quando operar o CoreDNS como servidor autoritativo primário para zonas internas, ou utilize `secondary` para sincronizar zonas via AXFR de um servidor primário existente.

## Exemplo
Uma zona interna de laboratório é carregada automaticamente do disco pelo plugin `auto`, assinada em tempo real pelo plugin `dnssec` e transferida para servidores secundários via `transfer`.

## Limites e trade-offs
Observe as restrições documentadas pelo próprio README: o suporte estático de zona menciona `NSEC only` para DNSSEC e o plugin `secondary` opera com `AXFR only` (sem IXFR incremental nessa descrição).

## Como verificar
Conferi os seis primeiros itens da lista Currently CoreDNS is able to no README oficial de coredns/coredns.

## Conexões
- [[coredns-transport-protocols-dot-doh-doh3-doq-grpc]] — Veja também: Protocolos de transporte DNS suportados: UDP/TCP, DoT (RFC 7858), DoH (RFC 8484), DoH3, DoQ (RFC 9250) e gRPC.
- [[coredns-kubernetes-etcd-route53-and-forward-backends]] — Veja também: Plugins de backend e integração cloud-native: kubernetes, etcd (substituindo SkyDNS), route53, forward e cache.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
