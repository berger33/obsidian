---
id: software.devops.tranche03.000288
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

# Comportamento padrão sem Corefile (plugins whoami e log na porta 53) e substituição com -dns.port

## Em uma frase
A subseção `Querying CoreDNS` do README documenta que, ao iniciar o CoreDNS sem nenhum arquivo de configuração, ele carrega por padrão os plugins `whoami` e `log` e passa a escutar na porta `53`, respondendo a qualquer consulta (como `dig @127.0.0.1 -p 53 www.example.com`) com o endereço de origem do cliente, porta e protocolo utilizado; e, caso a porta `53` já esteja ocupada por processos do sistema, pode-se alterar a porta no `Corefile` (por exemplo `.:1053`) ou sobrescrever a porta padrão via flag `-dns.port` (`coredns -dns.port 1053`).

## Por que importa
O plugin `whoami` embutido e a flag `-dns.port 1053` permitem testar conectividade de rede, NAT, balanceadores UDP/TCP e cabeçalhos de cliente como um usuário comum sem privilégios de root (já que portas acima de 1024 como a `1053` não exigem privilégio root no Linux).

## Como funciona
Utilize `coredns -dns.port 1053` com o plugin `whoami` em testes locais ou pipelines de CI para validar roteamento DNS e inspecionar qual endereço IP de origem e porta chegam ao servidor DNS.

## Exemplo
Um engenheiro sobe o CoreDNS na porta `1053` com `whoami` para verificar se o balanceador de carga está preservando o IP real do cliente (Direct Server Return / externalTrafficPolicy) nas pacotes UDP.

## Limites e trade-offs
Em produção, forneça sempre um `Corefile` explícito via `-conf Corefile` em vez de iniciar o processo sem configuração.

## Como verificar
Conferi a subseção Querying CoreDNS no README oficial de coredns/coredns.

## Conexões
- [[coredns-json-logging-format-and-structured-fields]] — Veja também: Logging operacional estruturado em JSON com -log-format=json e campos time, level, msg e plugin.
- [[coredns-corefile-import-globs-and-env-var-single-token]] — Veja também: Diretiva import com globs e expansão de variáveis {$VARIABLE} como token único no Corefile.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
