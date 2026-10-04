---
id: software.devops.tranche16.001585
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://volcano.sh/docs/home/architecture/", "https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md", "https://github.com/volcano-sh/volcano"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Volcano: governança multi-tenant de recursos com CRD `Queue`, plugin `proportion` e `reclaimable`

## Em uma frase
O CRD `Queue` (`scheduling.volcano.sh/v1beta1`) e o plugin `proportion` permitem dividir a capacidade do cluster entre diferentes equipes ou projetos usando pesos relativos (`weight`), limites de capacidade (`capability`), garantias (`deserved`) e empréstimo elástico de ociosidade (`reclaimable: true`).

## Por que importa
Travar cotas rígidas via `ResourceQuota` nativo deixa GPUs ociosas na Fila A mesmo quando a Fila B tem 50 treinamentos aguardando na fila. O modelo de filas proporcionais do Volcano permite que a Fila B use 100% do cluster quando a Fila A está ociosa e devolva a fatia imediatamente quando a Fila A submeter novos jobs.

## Como funciona
Cada `Queue` declara seu `weight` (por exemplo `weight: 2` para pesquisa e `weight: 1` para analytics) e `reclaimable: true`. O plugin `proportion` calcula a fatia justa (`deserved`) de cada fila a cada ciclo; se uma fila estiver abaixo de seu `deserved` com jobs pendentes, a ação `reclaim` evicta tarefas marcadas como reclamáveis das filas que estão usando recursos emprestados acima do seu `deserved`.

## Exemplo
```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: llm-research
spec:
  weight: 3
  reclaimable: true
  capability:
    cpu: "128"
    memory: "512Gi"
    nvidia.com/gpu: "16"
```

## Limites e trade-offs
Se uma fila hospedar jobs críticos que não suportam checkpointing e não podem sofrer preempção inter-fila sob nenhuma hipótese, configure `reclaimable: false` naquela `Queue` (ou proteja o job específico), sabendo que isso restringe o empréstimo elástico.

## Como verificar
Execute `kubectl get queue` para verificar o estado (`Open`), o peso (`WEIGHT`) e os contadores de `PodGroups` (`PENDING`, `RUNNING`, `UNKNOWN`) em cada fila.

## Conexões
- [[volcano-scheduler-pipeline-sessao-actions-enqueue-allocate-preempt-backfill]] — Veja também: Volcano Scheduler: arquitetura de pipeline de sessão (`enqueue`, `allocate`, `preempt`, `reclaim`, `backfill`).
- [[volcano-scheduler-drf-dominant-resource-fairness-multi-recurso]] — Veja também: Volcano: algoritmo `drf` (*Dominant Resource Fairness*) e filas hierárquicas para justiça multi-recurso.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://volcano.sh/docs/home/architecture/) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
