---
id: software.devops.tranche06.000506
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

# Compartilhamento e reutilização de experimentos no Chaos Hub (hub.litmuschaos.io)

## Em uma frase
O README oficial destaca que os templates `ChaosExperiment` são hospedados publicamente no **Chaos Hub** (**`hub.litmuschaos.io`**), cujo repositório comunitário reside em `github.com/litmuschaos/community-charts`. O Chaos Hub funciona como um catálogo central onde desenvolvedores de aplicações, mantenedores de projetos cloud-native e fornecedores compartilham seus experimentos de caos prontos (cobrindo falhas gerais de Kubernetes, pods, nós, rede, disco, CPU/memória, nuvens AWS/GCP/Azure e aplicações específicas como Kafka, CoreDNS e Cassandra) para que os usuários possam importá-los e aumentar a resiliência de suas cargas em produção.

## Por que importa
Escrever experimentos de caos seguros do zero exige cuidar de detalhes delicados de isolamento de container runtime, limpeza garantida após sinais de interrupção e permissões mínimas. Consumir charts auditados do `hub.litmuschaos.io` acelera a adoção de Engenharia de Caos nas equipes.

## Como funciona
Conecte o Chaos Hub público (`hub.litmuschaos.io`) ou um **Chaos Hub privado corporativo** (repositório Git interno com os experimentos e workflows homologados pela empresa) diretamente ao seu `chaos-center`.

## Exemplo
Uma organização financeira sincroniza um repositório Git privado como Chaos Hub corporativo no `chaos-center`, disponibilizando para todas as squads de produto dezenas de templates de caos pré-aprovados pela equipe de SRE e segurança.

## Limites e trade-offs
Ao contribuir novos experimentos ou melhorias para o catálogo público, siga as diretrizes oficiais em `github.com/litmuschaos/community-charts/blob/master/CONTRIBUTING.md`.

## Como verificar
Verifique no `chaos-center` a sincronização bem-sucedida do Chaos Hub e a listagem das categorias e experimentos disponíveis para agendamento.

## Conexões
- [[litmus-chaos-workflows-chaining-serial-and-parallel-experiments]] — Veja também: Encadeamento de múltiplos experimentos em Chaos Workflows no LitmusChaos.
- [[litmus-developer-cicd-and-sre-chaos-use-cases]] — Veja também: Os três casos de uso do LitmusChaos: Desenvolvimento, estágios de pipelines CI/CD e SRE em produção.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
