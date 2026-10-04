---
id: software.devops.tranche16.001589
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
fontes: ["https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md", "https://volcano.sh/docs/home/architecture/", "https://github.com/volcano-sh/volcano"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Volcano: integração nativa com Spark, KubeRay, Kubeflow Trainer e Flink sobre Kubernetes

## Em uma frase
O Volcano integra-se nativamente como motor de agendamento batch nos principais operadores do ecossistema cloud-native, incluindo Apache Spark (nativo e Spark Operator), KubeRay (`RayJob`/`RayCluster`), Kubeflow Trainer (v1 e v2), Flink Kubernetes Operator e Argo Workflows.

## Por que importa
Sem um scheduler batch unificado, um cluster que executa pipelines mistos de ETL em Spark, pré-processamento em Ray e treinamento em Kubeflow PyTorch teria três controladores disputando recursos às cegas sem fila única nem proteção contra deadlocks de `PodGroup`.

## Como funciona
No Spark nativo sobre Kubernetes, basta configurar `spark.kubernetes.scheduler.name=volcano` e o step de feature de `PodGroup` do Volcano; no KubeRay e Kubeflow Training Operator, habilita-se `enableGangScheduling: true` apontando para o grupo `scheduling.volcano.sh`. Todos os jobs passam a compartilhar as mesmas `Queues`, prioridades e políticas de `drf`/`proportion` do Volcano.

## Exemplo
```bash
spark-submit \
  --master k8s://https://kubernetes.default.svc \
  --deploy-mode cluster \
  --conf spark.kubernetes.scheduler.name=volcano \
  --conf spark.kubernetes.scheduler.volcano.podGroupTemplateFile=/opt/spark/conf/podgroup-template.yaml \
  local:///opt/spark/examples/jars/spark-examples.jar
```

## Limites e trade-offs
Ao habilitar `enableGangScheduling` em operadores externos como KubeRay ou Kubeflow, verifique se o operador está configurado para emitir `PodGroups` da API `scheduling.volcano.sh/v1beta1` (e não apenas `scheduling.x-k8s.io/v1alpha1` do scheduler-plugins), ou se o adaptador correspondente está ativo.

## Como verificar
Submeta um `PyTorchJob` ou `RayCluster` com gang scheduling habilitado e confirme que um objeto `podgroups.scheduling.volcano.sh` foi criado automaticamente no mesmo namespace.

## Conexões
- [[volcano-scheduler-network-topology-hypernode-llm-training]] — Veja também: Volcano: agendamento consciente de topologia de rede via `HyperNode` para treinamento de LLMs.
- [[volcano-scheduler-vcctl-cli-operacao-jobs-filas-suspensao]] — Veja também: Volcano: operação de jobs e filas pela linha de comando com `vcctl`.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
