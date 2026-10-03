---
id: software.devops.tranche06.000507
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md", "https://docs.litmuschaos.io/docs/introduction/what-is-litmus", "https://github.com/litmuschaos/litmus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Os três casos de uso do LitmusChaos: Desenvolvimento, estágios de pipelines CI/CD e SRE em produção

## Em uma frase
A seção *Use cases* do README oficial estrutura a aplicação prática do LitmusChaos em três perfis complementares ao longo do ciclo de vida do software: (1) **Para Desenvolvedores (For Developers)** — rodar experimentos de caos durante o desenvolvimento da aplicação como uma extensão natural dos testes unitários e de integração; (2) **Para construtores de pipelines CI/CD (For CI/CD pipeline builders)** — executar o caos como um estágio automatizado do pipeline para encontrar bugs quando a aplicação é submetida a caminhos de falha antes de chegar à produção; e (3) **Para SREs (For SREs)** — planejar e agendar experimentos de caos contínuos na aplicação e na infraestrutura ao redor para identificar fraquezas no sistema de implantação e aumentar a resiliência real.

## Por que importa
Deixar a Engenharia de Caos apenas para raros testes manuais em produção descobre bugs tarde demais; quando desenvolvedores e pipelines de CI/CD já testam os caminhos de falha (`fail paths`: timeouts, retentativas, circuit breakers e quedas de pod) a cada release, a produção já recebe código resiliente por construção.

## Como funciona
Integre experimentos leves do LitmusChaos como estágio de qualidade em homologação nos pipelines de CI/CD (validando o veredito do `ChaosResult`) e execute workflows agendados pelos SREs nos clusters de staging e produção.

## Exemplo
No pipeline de release de um microsserviço crítico, após o deploy no cluster de staging, um job dispara um `ChaosEngine` de perda de pod e latência HTTP; o pipeline só aprova a promoção se o `ChaosResult` retornar `Verdict: Pass`.

## Limites e trade-offs
Em pipelines de CI/CD, escolha experimentos com duração enxuta (por exemplo 30 a 60 segundos de injeção sob carga) para validar rapidamente a tolerância a falhas sem adicionar dezenas de minutos ao tempo de feedback do desenvolvedor.

## Como verificar
Confira nos logs do estágio de CI/CD a leitura automatizada do `ChaosResult` e o bloqueio de builds que violam as probes de estado estável.

## Conexões
- [[litmus-chaos-hub-community-charts-and-experiment-sharing]] — Veja também: Compartilhamento e reutilização de experimentos no Chaos Hub (hub.litmuschaos.io).
- [[litmus-observability-and-metrics-correlation-in-chaos]] — Veja também: Correlação de observabilidade e métricas Prometheus durante experimentos do LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
