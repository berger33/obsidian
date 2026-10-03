---
id: software.devops.tranche03.000274
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

# Cinco listas de comunicação oficial e política de resposta no Slack versus envoy-users

## Em uma frase
A seção `Contact` do README enumera cinco listas no Google Groups com finalidades distintas — `envoy-announce` (anúncios gerais de baixa frequência), `envoy-security-announce` (anúncios exclusivos de segurança de baixa frequência), `envoy-users` (discussão geral de usuários), `envoy-dev` (discussão de desenvolvedores sobre APIs e design) e `envoy-maintainers` (contato direto com todos os core maintainers) — e traz uma nota explícita sobre o Slack (`envoyproxy.slack.com`): **respostas a dúvidas de usuários no Slack são em regime de melhor esforço (`best effort`); para uma resposta "garantida", envie e-mail para `envoy-users@`**.

## Por que importa
Em incidentes ou dúvidas complexas de produção, postar apenas no Slack esperando atendimento formal pode deixar a equipe sem resposta; além disso, inscrever-se em `envoy-security-announce` é obrigatório para receber alertas de CVEs críticas em um proxy de borda.

## Como funciona
Inscreva-se obrigatoriamente em `envoy-security-announce` e `envoy-announce` ao operar Envoy em produção e envie dúvidas técnicas estruturadas para a lista `envoy-users` quando precisar de acompanhamento garantido.

## Exemplo
O time de SRE assina a lista de baixo volume `envoy-security-announce` para acionar imediatamente o pipeline de atualização do Envoy quando um aviso de segurança é emitido.

## Limites e trade-offs
Nunca envie relatos privados de vulnerabilidades ainda não corrigidas para as listas públicas `envoy-users` ou `envoy-dev`; use o canal privado de segurança documentado na seção Security.

## Como verificar
Conferi a seção Contact no README oficial de envoyproxy/envoy.

## Conexões
- [[envoy-related-repositories-dataplane-api-perf-and-filters]] — Veja também: Repositórios relacionados: data-plane-api, envoy-perf e envoy-filter-example.
- [[envoy-modern-cpp-contributing-and-docker-ci-quickstart]] — Veja também: Desenvolvimento em C++ moderno, quick start de build/teste via Docker (ci/) e toolchain de suporte.

## Fontes
- [Envoy Proxy — GitHub README](https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md) — Visão geral do Envoy (edge/middle/service proxy na CNCF, artigos de arquitetura sobre threading, hot restart, stats e xDS, repositórios relacionados, listas de e-mail, reuniões, auditorias Cure53/Ada Logics, OSS-Fuzz e política ppc64le).; consultado em 2026-10-03.
- [Envoy Proxy — Repositório Oficial no GitHub](https://github.com/envoyproxy/envoy) — Repositório oficial do Envoy Proxy com código-fonte C++, api/, docs/security/, DEVELOPER.md, SECURITY.md e RELEASES.md.; consultado em 2026-10-03.
