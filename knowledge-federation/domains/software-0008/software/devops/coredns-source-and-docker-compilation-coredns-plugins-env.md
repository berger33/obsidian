---
id: software.devops.tranche03.000286
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
fontes: ["https://raw.githubusercontent.com/coredns/coredns/master/README.md", "https://github.com/coredns/coredns"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Compilação a partir do código-fonte (Go 1.26.0+), variável COREDNS_PLUGINS e build via Docker

## Em uma frase
As seções `Compilation from Source` e `Compilation with Docker` do README documentam que, para compilar o CoreDNS localmente (`git clone`, `cd coredns`, `make`), é necessário Go `1.26.0` ou superior, destacando na nota que **plugins extras podem ser habilitados no momento do build definindo a variável de ambiente `COREDNS_PLUGINS`** com uma lista separada por vírgulas no mesmo formato de `plugin.cfg`; alternativamente, se o usuário já tiver Docker instalado e preferir não configurar um ambiente Go local, pode gerar o binário rodando o container `golang` com `GOFLAGS="-buildvcs=false" make gen && GOFLAGS="-buildvcs=false" make`.

## Por que importa
Como os plugins do CoreDNS são compilados estaticamente dentro do binário Go para máxima performance, adicionar um plugin out-of-tree exige recompilar o CoreDNS editando `plugin.cfg` ou passando `COREDNS_PLUGINS` no build.

## Como funciona
Ao construir uma imagem customizada do CoreDNS com plugins externos, passe a lista desejada na variável de ambiente `COREDNS_PLUGINS` durante o `make` ou utilize o método de compilação em container Docker.

## Exemplo
Uma equipe precisa de um plugin externo listado em `coredns.io/explugins` e automatiza no CI o build do binário `coredns` definindo `COREDNS_PLUGINS`.

## Limites e trade-offs
Teste sempre a ordem dos plugins em `COREDNS_PLUGINS` / `plugin.cfg`, pois a precedência em `plugin.cfg` define a ordem em que os plugins processam cada requisição DNS.

## Como verificar
Conferi as seções Compilation from Source e Compilation with Docker no README oficial de coredns/coredns.

## Conexões
- [[coredns-observability-security-and-query-manipulation-plugins]] — Veja também: Plugins de observabilidade, diagnóstico e manipulação: prometheus, log, errors, pprof, rewrite, template, any e dns64.
- [[coredns-json-logging-format-and-structured-fields]] — Veja também: Logging operacional estruturado em JSON com -log-format=json e campos time, level, msg e plugin.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS — Repositório Oficial no GitHub](https://github.com/coredns/coredns) — Repositório oficial do CoreDNS na CNCF com código-fonte Go, plugin.cfg e documentação por plugin.; consultado em 2026-10-03.
