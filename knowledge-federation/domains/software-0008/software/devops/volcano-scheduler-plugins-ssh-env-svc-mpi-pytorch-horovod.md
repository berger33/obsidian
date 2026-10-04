---
id: software.devops.tranche16.001587
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

# Volcano: plugins de ciclo de vida de VCJob (`ssh`, `env` e `svc`) para MPI, PyTorch e Horovod

## Em uma frase
O `VolcanoJob` (`vcjob`) inclui plugins nativos de controlador (`ssh`, `env` e `svc`) que configuram automaticamente chaves SSH passwordless entre Pods, variáveis de ambiente de índice de task e registros DNS Headless Service sem exigir scripts manuais de bootstrap.

## Por que importa
Para executar um job distribuído MPI ou Horovod sobre Kubernetes puro, o engenheiro normalmente precisa criar manualmente um `Secret` com par de chaves RSA, um `Service` headless, um `ConfigMap` com a lista de hosts (`hostfile`) e scripts de espera por DNS.

## Como funciona
Ao declarar `spec.plugins: {ssh: [], env: [], svc: []}` em um `vcjob`, o ControllerManager do Volcano gera e monta automaticamente as chaves SSH e o `/etc/ssh/ssh_config` em todos os Pods do job, cria o Headless Service e um `ConfigMap` com as listas de hosts por tarefa (ex.: `VK_TASK_INDEX`, `MPI_HOST`), permitindo que o `mpirun` ou `torchrun` comunique-se imediatamente entre `master` e `workers`.

## Exemplo
```yaml
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: mpi-ring-allreduce
spec:
  minAvailable: 3
  schedulerName: volcano
  plugins:
    ssh: []
    env: []
    svc: []
  tasks:
    - replicas: 1
      name: mpimaster
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: mpi
              image: volcanosh/example-mpi:0.0.3
    - replicas: 2
      name: mpiworker
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: mpi
              image: volcanosh/example-mpi:0.0.3
```

## Limites e trade-offs
Para que o plugin `ssh` permita comunicação direta do `mpimaster` para os `mpiworkers`, a imagem dos containers workers precisa ter o servidor `sshd` instalado e escutando na porta configurada.

## Como verificar
Após criar o `vcjob` com `plugins: {ssh: [], env: [], svc: []}`, verifique com `kubectl get secret,svc,cm -l volcano.sh/job-name=mpi-ring-allreduce` os recursos auxiliares provisionados automaticamente.

## Conexões
- [[volcano-scheduler-drf-dominant-resource-fairness-multi-recurso]] — Veja também: Volcano: algoritmo `drf` (*Dominant Resource Fairness*) e filas hierárquicas para justiça multi-recurso.
- [[volcano-scheduler-network-topology-hypernode-llm-training]] — Veja também: Volcano: agendamento consciente de topologia de rede via `HyperNode` para treinamento de LLMs.

## Fontes
- [Volcano GitHub — README.md (Kubernetes-Native Batch Scheduling System for AI/ML, Big Data & HPC, Ecosystem Integrations & CNCF Incubating Status)](https://raw.githubusercontent.com/volcano-sh/volcano/master/README.md) — README oficial do volcano-sh/volcano (CNCF Incubating) apresentando o agendador batch e suas integrações nativas com PyTorch, Ray, Spark, Kubeflow, Flink e MPI; consultado em 2026-10-03.
- [Volcano Official Documentation — Architecture (Volcano Scheduler, ControllerManager, Admission & vcctl CLI)](https://volcano.sh/docs/home/architecture/) — Documentação oficial de arquitetura do Volcano descrevendo o Scheduler baseado em ações/plugins, Queue/PodGroup/VCJob ControllerManager, Admission e vcctl; consultado em 2026-10-03.
- [Volcano — Official GitHub Repository](https://github.com/volcano-sh/volcano) — Repositório oficial Apache-2.0 do Volcano na CNCF; consultado em 2026-10-03.
