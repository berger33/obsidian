---
id: software.devops.tranche06.000504
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

# Auditoria de execução, status de rollback e métricas Prometheus com ChaosResult e Chaos-exporter

## Em uma frase
O terceiro recurso customizado fundamental descrito no README oficial é o **`ChaosResult`**, criado e atualizado para armazenar os resultados detalhados de cada execução de experimento. O `ChaosResult` registra o **sucesso de cada restrição de validação (probe)**, o **status de reversão/rollback da falha injetada** e o **veredito final (`Verdict`: `Pass`, `Fail`, `Awaited`)**. Adicionalmente, o componente **`Chaos-exporter`** lê continuamente os recursos `ChaosResult` no cluster e expõe essas informações como **métricas Prometheus**, tornando os `ChaosResults` especialmente valiosos durante execuções automatizadas.

## Por que importa
Em pipelines automatizados de CI/CD ou execuções noturnas agendadas, duas perguntas precisam de resposta programática imediata: (1) a aplicação sobreviveu ao teste (`Verdict: Pass`)? e (2) a falha injetada foi totalmente revertida ao final para não deixar o ambiente sujo? O `ChaosResult` responde ambas na API do Kubernetes e no Prometheus.

## Como funciona
Em estágios de caos automatizados no pipeline, aguarde a conclusão do experimento e consulte o campo de veredito do objeto `ChaosResult` (`kubectl get chaosresult <nome> -o jsonpath='{.status.experimentStatus.verdict}'`) e configure o Prometheus para coletar o `Chaos-exporter`.

## Exemplo
Após rodar um experimento de perda de pacotes de rede, o pipeline inspeciona o `ChaosResult`, confirma que todas as probes passaram (`Pass`), que o rollback das regras de rede concluído limpou o nó e libera a promoção da release para produção.

## Limites e trade-offs
Se um experimento for abortado à força ou o pod executor sofrer falha inesperada, verifique sempre o status de revert/rollback no `ChaosResult` para confirmar que nenhuma regra de caos residual permaneceu ativa no alvo.

## Como verificar
Inspecione `kubectl describe chaosresult <engine-name>-<experiment-name>` e consulte o endpoint `/metrics` do `Chaos-exporter` para validar as séries Prometheus exportadas.

## Conexões
- [[litmus-chaosengine-steady-state-probes-and-chaos-operator]] — Veja também: Vinculação de alvo, validação de hipótese de estado estável via probes e Chaos-Operator no ChaosEngine.
- [[litmus-chaos-workflows-chaining-serial-and-parallel-experiments]] — Veja também: Encadeamento de múltiplos experimentos em Chaos Workflows no LitmusChaos.

## Fontes
- [LitmusChaos GitHub — README.md (Chaos Control & Execution Plane, ChaosExperiment, ChaosEngine, ChaosResult & Chaos Hub)](https://raw.githubusercontent.com/litmuschaos/litmus/master/README.md) — README oficial do LitmusChaos (projeto CNCF sob Apache-2.0) detalhando separação entre Chaos Control Plane (chaos-center) e Chaos Execution Plane, CRDs ChaosExperiment (com BYOC), ChaosEngine (probes e Chaos-Operator) e ChaosResult (métricas via Chaos-exporter), portal hub.litmuschaos.io e casos de uso para Devs, CI/CD e SREs.; consultado em 2026-10-03.
- [LitmusChaos Official Documentation — What is Litmus & Getting Started](https://docs.litmuschaos.io/docs/introduction/what-is-litmus) — Documentação oficial de introdução e arquitetura de instalação do LitmusChaos.; consultado em 2026-10-03.
- [LitmusChaos — Official GitHub Repository](https://github.com/litmuschaos/litmus) — Repositório oficial Apache-2.0 do LitmusChaos na CNCF.; consultado em 2026-10-03.
