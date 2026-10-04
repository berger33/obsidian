---
id: software.devops.tranche16.001574
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
fontes: ["https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md", "https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md", "https://github.com/fluid-cloudnative/fluid"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluid: co-orquestração de dados e computação via agendamento por afinidade de cache (*Data-Affinity Scheduling*)

## Em uma frase
O Fluid injeta automaticamente regras de afinidade de nó nos Pods das aplicações consumidoras para agendá-los preferencialmente ou obrigatoriamente nos nós Kubernetes onde os workers de cache do `Dataset` já estão alocados.

## Por que importa
Mesmo que um dataset esteja em cache na memória RAM de 4 nós de um cluster de 100 nós, se o `kube-scheduler` agendar o Pod de treinamento de IA no nó 85 (que não possui worker de cache local), a leitura continuará trafegando pela rede entre nós.

## Como funciona
Quando o `AlluxioRuntime` (ou outro runtime do Fluid) aloca seus workers em determinados nós, o controlador aplica labels de localidade nesses nós (como `fluid.io/s-<namespace>-<dataset>=true`). Ao mesmo tempo, o webhook mutante do Fluid (`fluid-webhook`) intercepta qualquer Pod serverless ou de treinamento que monte o PVC daquele `Dataset` e injeta `nodeAffinity` apontando para os nós que hospedam o cache, unindo computação e dados sem exigir configuração manual no Pod.

## Exemplo
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pytorch-trainer
  namespace: ai-workloads
spec:
  containers:
    - name: trainer
      image: pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime
      command: ["python", "train.py", "--data-dir", "/data/spark"]
      volumeMounts:
        - mountPath: /data
          name: dataset-vol
  volumes:
    - name: dataset-vol
      persistentVolumeClaim:
        claimName: imagenet-train
```

## Limites e trade-offs
Se todos os nós com workers de cache já estiverem com GPUs ou CPUs 100% ocupadas, a afinidade preferencial (`preferredDuringSchedulingIgnoredDuringExecution`) permite que novos Pods transbordem para nós vizinhos na mesma zona/rack acessando o cache distribuído via rede local.

## Como verificar
Inspecione o Pod criado com `kubectl get pod pytorch-trainer -n ai-workloads -o yaml` e confirme a presença das regras de `nodeAffinity` injetadas pelo webhook do Fluid.

## Conexões
- [[fluid-cache-alluxioruntime-tieredstore-mem-ssd-hdd-workers]] — Veja também: Fluid: aceleração de cache distribuído com `AlluxioRuntime` e armazenamento em camadas (`tieredstore`).
- [[fluid-cache-dataload-pre-aquecimento-declarativo-datasets]] — Veja também: Fluid: pré-carregamento declarativo de dados (`DataLoad`) antes da execução de treinamentos.

## Fontes
- [Fluid GitHub — README.md (CNCF Incubating Distributed Dataset Orchestrator, Dataset & Runtime Abstractions & Academic Papers)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/docs/en/userguide/overview.md) — README oficial do fluid-cloudnative/fluid (CNCF Incubating) detalhando abstração de Dataset, Runtimes escaláveis de cache e operações automatizadas de dados; consultado em 2026-10-03.
- [Fluid Official Documentation — Overview (Computation-Storage Separation, AlluxioRuntime, Data Affinity Scheduling & Co-Orchestration)](https://raw.githubusercontent.com/fluid-cloudnative/fluid/master/README.md) — Guia oficial Overview do Fluid explicando a co-orquestração de dataset e aplicação, agendamento por afinidade de dados e isolamento por namespace; consultado em 2026-10-03.
- [Fluid — Official GitHub Repository](https://github.com/fluid-cloudnative/fluid) — Repositório oficial Apache-2.0 do Fluid na CNCF; consultado em 2026-10-03.
