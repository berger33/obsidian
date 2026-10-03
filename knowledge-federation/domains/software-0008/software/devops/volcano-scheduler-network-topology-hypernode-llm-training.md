---
id: software.devops.tranche16.001588
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

# Volcano: agendamento consciente de topologia de rede via `HyperNode` para treinamento de LLMs

## Em uma frase
O Volcano introduz a modelagem de topologia de rede baseada em `HyperNode` (*Network Topology Aware Scheduling*) para alocar todos os Pods de um treinamento distribuído de LLM dentro do mesmo domínio de switches ToR/Spine de alta velocidade (InfiniBand / RoCE RDMA).

## Por que importa
Em treinamentos de grandes modelos de linguagem com dezenas ou centenas de GPUs, o tempo gasto sincronizando gradientes (`AllReduce` / `AllGather`) domina o tempo de época; se os Pods de um job forem espalhados entre switches Spine distantes, a latência e contenção de rede reduzem drasticamente o *Model FLOPs Utilization* (MFU).

## Como funciona
Os recursos `HyperNode` modelam a árvore hierárquica de switches do data center (Tier 1 ToR, Tier 2 Leaf, Tier 3 Spine) agrupando os nós Kubernetes. Quando um `vcjob` especifica restrições de topologia de rede (`networkTopology`), o Volcano Scheduler prioriza alocar todo o `PodGroup` no `HyperNode` de menor nível (mais próximo fisicamente) que comporte os recursos solicitados.

## Exemplo
```yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: llm-pretrain-64gpu
spec:
  minAvailable: 8
  schedulerName: volcano
  networkTopology:
    mode: hard
    highestTierAllowed: 2
  tasks:
    - replicas: 8
      name: trainer
      template:
        spec:
          containers:
            - name: llm
              image: nvcr.io/nvidia/pytorch:24.07-py3
```

## Limites e trade-offs
No modo `mode: hard` com `highestTierAllowed: 2`, se nenhum `HyperNode` de Tier 1 ou Tier 2 tiver capacidade livre para alocar todos os 8 Pods juntos, o job permanecerá aguardando na fila em vez de sofrer degradação severa de banda em Tier 3.

## Como verificar
Verifique a árvore de `HyperNode` do cluster e confirme com `kubectl get pods -l volcano.sh/job-name=llm-pretrain-64gpu -o wide` que os nós selecionados pertencem à mesma sub-árvore de switches.

## Conexões
- [[volcano-scheduler-plugins-ssh-env-svc-mpi-pytorch-horovod]] — Veja também: Volcano: plugins de ciclo de vida de VCJob (`ssh`, `env` e `svc`) para MPI, PyTorch e Horovod.
- [[volcano-scheduler-integracao-ecossistema-spark-ray-kubeflow-flink]] — Veja também: Volcano: integração nativa com Spark, KubeRay, Kubeflow Trainer e Flink sobre Kubernetes.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
