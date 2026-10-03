---
id: software.devops.tranche03.000281
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

# Servidor e encaminhador DNS em Go baseado em cadeia de plugins graduado na CNCF

## Em uma frase
O README oficial no repositório coredns/coredns define o CoreDNS como um servidor/encaminhador DNS (DNS server/forwarder), escrito em Go, que encadeia plugins (`chains plugins`), onde cada plugin executa uma função DNS específica, sendo um projeto graduado da Cloud Native Computing Foundation (CNCF) cuja palavra-chave arquitetural é **flexibilidade**: você faz o que precisa com os dados DNS combinando plugins in-tree (`coredns.io/plugins`) ou escrevendo plugins externos (`coredns.io/explugins`).

## Por que importa
Como o CoreDNS é o servidor DNS padrão de clusters Kubernetes (requisito explícito inclusive para ferramentas como Argo CD vistas na Tranche 1), entender sua arquitetura de cadeia de plugins permite diagnosticar resolução de nomes de Services, ajustar cache, exportar métricas e encaminhar zonas corporativas sem trocar o servidor DNS do cluster.

## Como funciona
Configure o CoreDNS ativando no `Corefile` apenas os plugins necessários para cada zona DNS e consulte `coredns.io/plugins` para a documentação individual de cada plugin.

## Exemplo
No Kubernetes, uma consulta DNS recebida pelo CoreDNS percorre a cadeia de plugins configurada (como `errors`, `health`, `kubernetes`, `prometheus`, `forward` e `cache`).

## Limites e trade-offs
A ordem de execução dos plugins na cadeia é determinística; habilitar plugins desnecessários ou mal configurados no caminho crítico afeta a latência de todas as consultas DNS do cluster.

## Como verificar
Conferi os três primeiros parágrafos do README oficial de coredns/coredns.

## Conexões
- [[coredns-transport-protocols-dot-doh-doh3-doq-grpc]] — Veja também: Protocolos de transporte DNS suportados: UDP/TCP, DoT (RFC 7858), DoH (RFC 8484), DoH3, DoQ (RFC 9250) e gRPC.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
