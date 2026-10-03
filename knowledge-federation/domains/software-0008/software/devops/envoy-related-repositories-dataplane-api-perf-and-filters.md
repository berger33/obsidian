---
id: software.devops.tranche03.000273
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
fontes: ["https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md", "https://github.com/envoyproxy/envoy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Repositórios relacionados: data-plane-api, envoy-perf e envoy-filter-example

## Em uma frase
A seção `Related` do README destaca três repositórios complementares na organização `envoyproxy`: **data-plane-api** (`envoyproxy/data-plane-api`, espelho somente leitura do diretório `api/` com as definições standalone da API do plano de dados), **envoy-perf** (`envoyproxy/envoy-perf`, framework de testes de performance) e **envoy-filter-example** (`envoyproxy/envoy-filter-example`, exemplo prático de como adicionar novos filtros e vinculá-los ao repositório principal).

## Por que importa
Equipes que constroem control planes xDS em Go, Rust ou Java consomem os contratos Protobuf de `api/` (`data-plane-api`), enquanto engenheiros que precisam criar um filtro C++ customizado sem alterar o upstream usam o modelo `envoy-filter-example` para linkar contra o repositório principal.

## Como funciona
Consulte `envoyproxy/envoy-filter-example` como template oficial ao escrever um novo filtro C++ para o Envoy e utilize `envoyproxy/envoy-perf` para medir o impacto de performance das suas configurações.

## Exemplo
Uma equipe de infraestrutura desenvolve um filtro customizado de protocolo interno partindo da estrutura de build demonstrada em `envoyproxy/envoy-filter-example`.

## Limites e trade-offs
Como `envoyproxy/data-plane-api` é apenas um espelho somente leitura (`read-only mirror`) do diretório `api/`, qualquer contribuição ou alteração nas definições Protobuf deve ser feita diretamente no repositório principal `envoyproxy/envoy`.

## Como verificar
Conferi a seção Related no README oficial de envoyproxy/envoy.

## Conexões
- [[envoy-core-architecture-threading-hot-restart-stats-xds]] — Veja também: Pilares arquiteturais documentados no README: threading model, hot restart, stats e universal data plane API.
- [[envoy-mailing-lists-and-slack-best-effort-policy]] — Veja também: Cinco listas de comunicação oficial e política de resposta no Slack versus envoy-users.

## Fontes
- [Envoy Proxy — GitHub README](https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md) — Visão geral do Envoy (edge/middle/service proxy na CNCF, artigos de arquitetura sobre threading, hot restart, stats e xDS, repositórios relacionados, listas de e-mail, reuniões, auditorias Cure53/Ada Logics, OSS-Fuzz e política ppc64le).; consultado em 2026-10-03.
- [Envoy Proxy — Repositório Oficial no GitHub](https://github.com/envoyproxy/envoy) — Repositório oficial do Envoy Proxy com código-fonte C++, api/, docs/security/, DEVELOPER.md, SECURITY.md e RELEASES.md.; consultado em 2026-10-03.
