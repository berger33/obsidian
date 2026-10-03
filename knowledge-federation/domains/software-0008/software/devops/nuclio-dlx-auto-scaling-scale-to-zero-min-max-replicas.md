---
id: software.devops.tranche19.001829
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
fontes: ["https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md", "https://raw.githubusercontent.com/nuclio/nuclio/development/README.md", "https://github.com/nuclio/nuclio"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nuclio Auto-Scaling e DLX (*Dead Letter / Scale-to-Zero*): escalonamento dinâmico de `0` a `N` réplicas

## Em uma frase
No Kubernetes, o Nuclio gerencia o escalonamento horizontal automático de cada função entre `minReplicas` e `maxReplicas` (incluindo **`minReplicas: 0`**), utilizando o componente **DLX** para interceptar chamadas destinadas a funções adormecidas, acordar o Deployment e encaminhar a requisição.

## Por que importa
Funções de inferência em GPU ou pipelines de processamento batch esporádicos têm custo elevado se mantiverem `minReplicas: 1` durante madrugadas e fins de semana sem tráfego.

## Como funciona
Quando uma função com `minReplicas: 0` fica ociosa pelo período configurado de janela de inatividade, o controlador do Nuclio reduz o `Deployment` para `0` réplicas e aponta a rota para o serviço **DLX**. Na chegada de uma nova requisição HTTP, o DLX (opcionalmente validando com o `auth-proxy` em modo `auth-only`) aciona o scale-up da função, aguarda a probe `/__internal/health` ficar pronta e entrega a chamada.

## Exemplo
```yaml
spec:
  minReplicas: 0
  maxReplicas: 5
  targetCPU: 75
```

## Limites e trade-offs
Para funções que exigem latência de cauda sub-milissegundo constante sem tolerar a subida inicial do Pod a partir do DLX, configure `minReplicas: 1` (ou maior).

## Como verificar
Configure `minReplicas: 0` em uma função de teste, aguarde o scale-to-zero (`kubectl get pods -n nuclio`) e faça uma chamada HTTP para observar o DLX acordando o Pod automaticamente.

## Conexões
- [[nuclio-aceleracao-gpu-nvidia-inferencia-ml-jupyter-kubeflow]] — Veja também: Nuclio para IA/ML e GPUs: alocação de GPUs NVIDIA (`nvidia.com/gpu`), integração com Jupyter (`nuclio-jupyter`) e MLRun.
- [[nuclio-api-gateways-canary-deployments-projects-k8s-crds]] — Veja também: Nuclio `NuclioAPIGateway` e `NuclioProject`: roteamento canário com divisão percentual de tráfego e governança multi-projeto.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
