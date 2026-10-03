---
id: software.devops.tranche06.000503
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

# Vinculação de alvo, validação de hipótese de estado estável via probes e Chaos-Operator no ChaosEngine

## Em uma frase
O segundo recurso customizado central documentado no README oficial é o **`ChaosEngine`**: o objeto que **vincula uma carga de trabalho/serviço de aplicação Kubernetes, nó ou componente de infraestrutura a uma falha descrita pelo `ChaosExperiment`**. Além de permitir ajustar propriedades da execução (duração da falha, intervalo, variáveis sobrescritas), o `ChaosEngine` é onde o engenheiro especifica as restrições de validação da **hipótese de estado estável (steady state hypothesis) usando `probes`**. O `ChaosEngine` é observado continuamente pelo **`Chaos-Operator`** (`litmuschaos/chaos-operator`), que o reconcilia disparando a execução do experimento através de pods *runners*.

## Por que importa
Na Engenharia de Caos moderna, injetar uma falha sem medir automaticamente se a aplicação manteve seu comportamento esperado antes, durante e após a falha é apenas causar destruição manual. As **probes** declaradas no `ChaosEngine` (como probes HTTP, de comando, Kubernetes ou Prometheus) automatizam a verificação da hipótese de estado estável.

## Como funciona
Em todo `ChaosEngine`, defina pelo menos uma `probe` de validação de estado estável (verificando disponibilidade HTTP da API, latência ou métricas de negócio) para que o experimento seja marcado automaticamente como aprovado ou reprovado sem depender de inspeção visual humana.

## Exemplo
Para testar a resiliência do serviço de carrinho à queda abrupta de um pod (`pod-delete`), o SRE declara um `ChaosEngine` apontando para o Deployment `cart-service` e adiciona uma `httpProbe` contínua que exige código HTTP `200` no endpoint `/healthz` durante toda a injeção da falha.

## Limites e trade-offs
Certifique-se de que o seletor de aplicação (`appinfo`: `appns`, `applabel` e `appkind`) no `ChaosEngine` corresponda exatamente aos labels do Deployment/StatefulSet alvo, evitando que o experimento falhe na fase de descoberta de pods.

## Como verificar
Aplique o manifesto `ChaosEngine` e acompanhe com `kubectl get chaosengine` e `kubectl get pods` a criação do pod runner pelo `Chaos-Operator`.

## Conexões
- [[litmus-chaosexperiment-custom-resource-and-byoc]] — Veja também: O recurso customizado ChaosExperiment e o modelo Bring-Your-Own-Chaos (BYOC) no LitmusChaos.
- [[litmus-chaosresult-verdict-rollback-and-prometheus-exporter]] — Veja também: Auditoria de execução, status de rollback e métricas Prometheus com ChaosResult e Chaos-exporter.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
