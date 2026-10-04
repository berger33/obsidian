---
id: software.devops.tranche06.000505
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

# Encadeamento de múltiplos experimentos em Chaos Workflows no LitmusChaos

## Em uma frase
Conforme explica o README oficial, os recursos `ChaosExperiment` e `ChaosEngine` são embutidos dentro de um objeto de **Workflow** (construído sobre Argo Workflows na arquitetura do Litmus 2.0+) capaz de **encadear um ou mais experimentos de caos na ordem desejada** (sequencial ou paralela), combinando etapas de geração de carga, injeção de múltiplas falhas simultâneas ou encadeadas e verificação final de recuperação.

## Por que importa
Incidentes reais em sistemas distribuídos raramente decorrem de uma única falha isolada em ambiente ocioso: eles acontecem quando uma degradação de rede coincide com um pico de tráfego e o reinício de um pod. Os Chaos Workflows permitem simular cenários compostos realistas e reproduzíveis.

## Como funciona
Construa Chaos Workflows no `chaos-center` (ou declarativamente via GitOps) combinando uma etapa geradora de tráfego sintético em paralelo com experimentos graduais de caos de pod, rede e recursos de nó.

## Exemplo
Durante um GameDay trimestral, a equipe executa um Chaos Workflow que primeiro injeta latência de 200ms na chamada ao catálogo e, dois minutos depois, mata uma réplica do serviço de recomendação, validando por probes se o circuito de fallback manteve o checkout saudável.

## Limites e trade-offs
Comece sempre validando experimentos individuais simples antes de encadear múltiplos experimentos destrutivos em paralelo em um mesmo Workflow, para saber exatamente qual falha causou eventual quebra de SLO.

## Como verificar
Visualize o grafo de execução do Workflow no `chaos-center` e confirme que cada nó do workflow transitou para concluído com veredito `Pass`.

## Conexões
- [[litmus-chaosresult-verdict-rollback-and-prometheus-exporter]] — Veja também: Auditoria de execução, status de rollback e métricas Prometheus com ChaosResult e Chaos-exporter.
- [[litmus-chaos-hub-community-charts-and-experiment-sharing]] — Veja também: Compartilhamento e reutilização de experimentos no Chaos Hub (hub.litmuschaos.io).

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
