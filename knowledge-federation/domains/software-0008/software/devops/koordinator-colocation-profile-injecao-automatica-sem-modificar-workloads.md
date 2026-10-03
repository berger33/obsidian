---
id: software.devops.tranche16.001563
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
fontes: ["https://koordinator.sh/docs/architecture/overview/", "https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md", "https://github.com/koordinator-sh/koordinator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Koordinator: adoção transparente de co-localização via `ClusterColocationProfile` sem alterar manifestos

## Em uma frase
O controlador `ColocationProfile` (no `koord-manager`), configurado pelo CRD `ClusterColocationProfile`, intercepta Pods na criação via mutating webhook e injeta automaticamente `koordinator.sh/qosClass`, `schedulerName: koord-scheduler`, `priorityClassName` e reescrita de recursos estendidos (`batch-cpu`/`batch-memory`).

## Por que importa
Em organizações com dezenas de operadores de big data (Spark Operator, Argo Workflows, Kubeflow) já implantados, exigir que todas as equipes reescrevam seus geradores de Pod para trocar `cpu` por `kubernetes.io/batch-cpu` e adicionar labels do Koordinator atrasaria a adoção da co-localização.

## Como funciona
O administrador cria um `ClusterColocationProfile` com seletores `namespaceSelector` e `selector` (por labels do Pod). Quando um operador submete um Pod batch comum naquele namespace pedindo `cpu: 2`, o webhook do `koord-manager` converte automaticamente o pedido para `kubernetes.io/batch-cpu: 2000`, define `koordinator.sh/qosClass: BE` e direciona o Pod para o `koord-scheduler`.

## Exemplo
```yaml
apiVersion: config.koordinator.sh/v1alpha1
kind: ClusterColocationProfile
metadata:
  name: spark-batch-colocation
spec:
  namespaceSelector:
    matchLabels:
      koordinator.sh/enable-colocation: "true"
  selector:
    matchLabels:
      spark-role: executor
  qosClass: BE
  priorityClassName: koord-batch
  schedulerName: koord-scheduler
  koordinatorPriority: 1000
```

## Limites e trade-offs
Antes de ativar um `ClusterColocationProfile` em um namespace, certifique-se de que a `PriorityClass` referenciada (como `koord-batch`) já existe no cluster.

## Como verificar
Rotule um namespace com `koordinator.sh/enable-colocation=true`, crie um Pod com label `spark-role=executor` e verifique com `kubectl get pod -o yaml` que `qosClass: BE` e `kubernetes.io/batch-cpu` foram injetados automaticamente.

## Conexões
- [[koordinator-modelo-qos-lse-lsr-ls-be-system-prioridades]] — Veja também: Koordinator: classes de QoS diferenciadas (`LSE`, `LSR`, `LS`, `BE` e `SYSTEM`) para cargas híbridas.
- [[koordinator-koord-scheduler-load-aware-scheduling-prevencao-hotspots]] — Veja também: Koordinator: agendamento sensível à carga real (`Load-Aware Scheduling`) no `koord-scheduler`.

## Fontes
- [Koordinator GitHub — README.md (QoS-Based Scheduling System for Hybrid Orchestration Workloads on Kubernetes)](https://koordinator.sh/docs/architecture/overview/) — README oficial do koordinator-sh/koordinator apresentando os objetivos de utilização de recursos, redução de interferência e políticas de agendamento; consultado em 2026-10-03.
- [Koordinator Official Documentation — Architecture Overview (Koord-Scheduler, Koord-Descheduler, Koord-Manager, Koordlet & Koord-RuntimeProxy)](https://raw.githubusercontent.com/koordinator-sh/koordinator/main/README.md) — Visão geral oficial da arquitetura do Koordinator detalhando os componentes do control plane e do nó (Koordlet e Koord-RuntimeProxy); consultado em 2026-10-03.
- [Koordinator — Official GitHub Repository](https://github.com/koordinator-sh/koordinator) — Repositório oficial Apache-2.0 do Koordinator; consultado em 2026-10-03.
