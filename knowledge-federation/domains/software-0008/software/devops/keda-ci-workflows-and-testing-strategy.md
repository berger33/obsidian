---
id: software.devops.tranche03.000259
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
fontes: ["https://raw.githubusercontent.com/kedacore/keda/main/README.md", "https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Workflows de build principal e testes end-to-end noturnos (TESTING.md)

## Em uma frase
Os badges de topo e a seção `Contributing` do README oficial destacam os dois fluxos principais de integração contínua do repositório `kedacore/keda` — `main-build.yml` (build principal a cada alteração) e `nightly-e2e.yml` (bateria noturna de testes end-to-end) — além de apontar para o documento dedicado de estratégia de testes em `./TESTING.md`.

## Por que importa
Como o KEDA possui dezenas de scalers que se conectam a filas, bancos de dados e serviços de nuvem reais, combinar o build rápido de PR (`main-build.yml`) com uma suíte noturna ponta a ponta (`nightly-e2e.yml`) e a estratégia documentada em `TESTING.md` garante que integrações com brokers externos não sofram regressões silenciosas.

## Como funciona
Ao contribuir com um novo scaler ou alterar um scaler existente no KEDA, siga a estratégia definida em `TESTING.md` para incluir testes unitários e end-to-end.

## Exemplo
Um contribuidor adiciona um teste e2e seguindo `TESTING.md` para validar o escalonamento de zero para N réplicas e de volta para zero contra o serviço alvo.

## Limites e trade-offs
Ao executar testes e2e contra serviços gerenciados de nuvem, utilize ambientes isolados de teste com limpeza automática de recursos.

## Como verificar
Conferi os badges de topo e a subseção Testing strategy no README oficial de kedacore/keda.

## Conexões
- [[keda-architecture-entrypoints-operator-and-metrics-adapter]] — Veja também: Pontos de entrada em Go: cmd/operator/main.go e cmd/adapter/main.go.
- [[keda-governance-support-policy-and-roadmap]] — Veja também: Governança em kedacore/governance, política de suporte em keda.sh/support e ROADMAP.md.

## Fontes
- [KEDA — GitHub README](https://raw.githubusercontent.com/kedacore/keda/main/README.md) — Visão geral do KEDA (Kubernetes-based Event Driven Autoscaling graduado na CNCF, scale to/from zero, integração com HPA na nuvem e borda, QuickStarts com ScaledObject/ScaledJob, deploy Helm/Operator Hub/YAML e governança).; consultado em 2026-10-03.
- [KEDA — Build & Deploy Guide (BUILD.md)](https://raw.githubusercontent.com/kedacore/keda/main/BUILD.md) — Guia oficial de build e deploy do KEDA detalhando Operator SDK, Dev Containers, GOPROXY/GOSUMDB, execução local fora do cluster com /certs, imagens customizadas e pontos de entrada cmd/operator/main.go e cmd/adapter/main.go.; consultado em 2026-10-03.
