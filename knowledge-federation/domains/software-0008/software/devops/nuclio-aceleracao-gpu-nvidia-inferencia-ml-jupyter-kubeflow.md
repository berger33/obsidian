---
id: software.devops.tranche19.001828
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio para IA/ML e GPUs: alocação de GPUs NVIDIA (`nvidia.com/gpu`), integração com Jupyter (`nuclio-jupyter`) e MLRun

## Em uma frase
O Nuclio oferece suporte nativo a execução sobre **GPUs** (`resources.limits."nvidia.com/gpu"`) e integra-se diretamente com **Jupyter Notebooks** (`nuclio-jupyter`), **Kubeflow Pipelines** e **MLRun** para converter células de notebook de cientistas de dados em microsserviços de inferência em tempo real.

## Por que importa
Um cientista de dados treina um modelo PyTorch/ONNX em um Jupyter Notebook, mas colocá-lo em produção com auto-scaling, batching de inferência em GPU e consumo de fila Kafka geralmente exige semanas de reescrita pela engenharia de software.

## Como funciona
Com a biblioteca `nuclio-jupyter`, o cientista adiciona comentários mágicos (`# nuclio: start-code`, `# nuclio: end-code`) no próprio notebook e exporta/implanta a função diretamente no cluster Kubernetes com suporte a GPUs, variáveis de ambiente e montagem de volumes de modelos.

## Exemplo
```yaml
spec:
  runtime: python:3.11
  resources:
    limits:
      nvidia.com/gpu: 1
      memory: 8Gi
    requests:
      nvidia.com/gpu: 1
      memory: 4Gi
```

## Limites e trade-offs
Quando uma função solicita recursos `nvidia.com/gpu`, configure o número de workers por Pod e o modo de alocação cuidadosamente para não estourar a memória VRAM da GPU com múltiplos processos concorrentes carregando o mesmo modelo.

## Como verificar
Implante uma função solicitando recursos e verifique no `Deployment` gerado pelo operador do Nuclio a propagação exata de `resources.limits` e `requests`.

## Conexões
- [[nuclio-data-bindings-conexoes-persistentes-context-zero-copy]] — Veja também: Nuclio Data Bindings: conexões persistentes pré-inicializadas em `context.data_binding` com prefetching e caching.
- [[nuclio-dlx-auto-scaling-scale-to-zero-min-max-replicas]] — Veja também: Nuclio Auto-Scaling e DLX (*Dead Letter / Scale-to-Zero*): escalonamento dinâmico de `0` a `N` réplicas.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
