---
id: software.devops.tranche03.000282
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

# Protocolos de transporte DNS suportados: UDP/TCP, DoT (RFC 7858), DoH (RFC 8484), DoH3, DoQ (RFC 9250) e gRPC

## Em uma frase
O README oficial lista os seis protocolos pelos quais o CoreDNS pode escutar requisições DNS de entrada: **UDP/TCP** (o DNS clássico), **TLS - DoT** (`RFC 7858`), **DNS over HTTP/2 - DoH** (`RFC 8484`), **DNS over HTTP/3 - DoH3**, **DNS over QUIC - DoQ** (`RFC 9250`) e **gRPC** (observando que gRPC não é um padrão DNS da IETF).

## Por que importa
Ambientes zero-trust, redes de borda e clientes modernos exigem cada vez mais transporte DNS criptografado (DoT, DoH, DoH3 ou DoQ) para impedir espionagem ou manipulação de consultas DNS em trânsito, além de integrações programáticas via gRPC.

## Como funciona
Configure blocos de servidor no `Corefile` com os certificados e portas apropriados quando precisar expor resolução DNS criptografada via DoT (`RFC 7858`), DoH (`RFC 8484`), DoH3 ou DoQ (`RFC 9250`).

## Exemplo
Um gateway DNS corporativo usa o CoreDNS para receber consultas criptografadas via DoT e DoH de estações remotas e resolver nomes internos com segurança.

## Limites e trade-offs
Protocolos baseados em TLS/HTTPS/QUIC exigem gerenciamento automático e rotação de certificados válidos (por exemplo, integrando com o `cert-manager` visto nos itens 201–210 desta tranche).

## Como verificar
Conferi a lista de protocolos de escuta na abertura do README oficial de coredns/coredns.

## Conexões
- [[coredns-plugin-chained-dns-server-cncf-graduated]] — Veja também: Servidor e encaminhador DNS em Go baseado em cadeia de plugins graduado na CNCF.
- [[coredns-zone-serving-dnssec-axfr-and-loadbalance]] — Veja também: Plugins de autoridade e transferência de zonas: file, auto, secondary (AXFR), dnssec, transfer e loadbalance.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
