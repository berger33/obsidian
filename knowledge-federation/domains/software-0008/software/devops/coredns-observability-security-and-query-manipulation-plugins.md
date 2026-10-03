---
id: software.devops.tranche03.000285
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

# Plugins de observabilidade, diagnóstico e manipulação: prometheus, log, errors, pprof, rewrite, template, any e dns64

## Em uma frase
Concluindo a lista de capacidades no README oficial, o CoreDNS inclui plugins para métricas com **prometheus**, registro de consultas (**log**) e de erros (**errors**), suporte à classe CH como `version.bind` (**chaos**), suporte à opção RFC 5001 DNS Name Server Identifier — NSID (**nsid**), profiling de performance (**pprof**), reescrita de consultas `qtype`, `qclass` e `qname` (**rewrite** e **template**), bloqueio de consultas `ANY` (**any**) e tradução IPv6 DNS64 (**dns64**).

## Por que importa
Em operação real, o plugin `any` protege contra ataques de amplificação DNS bloqueando queries `ANY`, `rewrite`/`template` permitem redirecionar nomes sem tocar nas aplicações, `dns64` viabiliza redes IPv6-only acessarem destinos IPv4 e `prometheus` + `errors` + `pprof` garantem observabilidade completa do servidor DNS.

## Como funciona
Habilite sempre os plugins `errors` e `prometheus` em produção, utilize `rewrite` quando precisar mapear CNAMEs/nomes internos transparentemente e ative `any` em servidores expostos para bloquear consultas `ANY`.

## Exemplo
Uma equipe migra um serviço legado de endereço e usa o plugin `rewrite` no CoreDNS para traduzir o `qname` antigo para o novo nome de serviço sem reconfigurar os clientes.

## Limites e trade-offs
Ativar o plugin `log` (que registra cada consulta DNS individual) em clusters de altíssimo tráfego pode gerar volume massivo de logs e I/O; use-o com cautela ou filtros em produção.

## Como verificar
Conferi os itens finais da lista Currently CoreDNS is able to no README oficial de coredns/coredns.

## Conexões
- [[coredns-kubernetes-etcd-route53-and-forward-backends]] — Veja também: Plugins de backend e integração cloud-native: kubernetes, etcd (substituindo SkyDNS), route53, forward e cache.
- [[coredns-source-and-docker-compilation-coredns-plugins-env]] — Veja também: Compilação a partir do código-fonte (Go 1.26.0+), variável COREDNS_PLUGINS e build via Docker.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
