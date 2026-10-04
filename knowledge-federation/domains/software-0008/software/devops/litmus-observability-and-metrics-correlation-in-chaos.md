---
id: software.devops.tranche06.000508
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

# Correlação de observabilidade e métricas Prometheus durante experimentos do LitmusChaos

## Em uma frase
Como destaca o README oficial (tanto na descrição do `ChaosResult` / `Chaos-exporter` quanto nos artigos referenciados sobre *Observability Considerations in Chaos: The Metrics Story*), a prática eficaz de Engenharia de Caos depende intrinsecamente da observabilidade: além de expor o status e o veredito dos experimentos como séries temporais via **`Chaos-exporter`** para o Prometheus, o LitmusChaos permite sobrepor os intervalos exatos de injeção de falha (anotações e métricas de caos) diretamente nos dashboards do Grafana ao lado das métricas de aplicação e infraestrutura.

## Por que importa
Quando um gráfico de latência no Grafana apresenta um pico às 14h15, cruzar visualmente e programaticamente a métrica do `Chaos-exporter` com as métricas RED da aplicação comprova imediatamente se o pico foi causado pelo experimento de caos ativo, quanto tempo o sistema levou para detectar a falha e se houve recuperação completa após o término.

## Como funciona
Configure o Prometheus (ou VictoriaMetrics) para fazer scrape do `Chaos-exporter` e utilize `promProbe` nos seus `ChaosEngines` para validar consultas PromQL diretamente como critério de aprovação do experimento.

## Exemplo
Durante um experimento de saturação de CPU em um nó Kubernetes, uma `promProbe` configurada no `ChaosEngine` executa uma query PromQL verificando se a taxa de erros 5xx do Ingress permaneceu abaixo de `0.1%` e se o HPA escalou novas réplicas em outros nós.

## Limites e trade-offs
Garanta que o intervalo de scraping do Prometheus seja suficientemente granular (ex.: 10s a 15s) em relação à duração total do experimento (`TOTAL_CHAOS_DURATION`) para que a `promProbe` capture os efeitos reais da falha durante a janela de injeção.

## Como verificar
Consulte no Prometheus as métricas expostas pelo `Chaos-exporter` (`litmuschaos_*`) durante e após um experimento e verifique a atualização dos contadores de experimentos aprovados e reprovados.

## Conexões
- [[litmus-developer-cicd-and-sre-chaos-use-cases]] — Veja também: Os três casos de uso do LitmusChaos: Desenvolvimento, estágios de pipelines CI/CD e SRE em produção.
- [[litmus-security-controls-rbac-and-blast-radius-containment]] — Veja também: Controles de segurança, RBAC por namespace e contenção de raio de explosão (blast radius) no LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
