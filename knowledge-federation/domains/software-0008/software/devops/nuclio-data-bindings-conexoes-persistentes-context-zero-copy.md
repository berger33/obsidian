---
id: software.devops.tranche19.001827
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

# Nuclio Data Bindings: conexões persistentes pré-inicializadas em `context.data_binding` com prefetching e caching

## Em uma frase
Os **Data Bindings** do Nuclio inicializam conexões persistentes com bancos de dados, sistemas de arquivos ou serviços de armazenamento na subida do Function Processor e as entregam prontas para uso dentro do objeto **`context`** passado ao handler.

## Por que importa
Abrir e fechar uma nova conexão TCP/TLS com um banco de dados ou storage a cada invocação de função destrói o throughput e esgota as portas efêmeras e o pool de conexões do banco em poucos segundos.

## Como funciona
Declarado em `spec.dataBindings` na configuração da função (com `class`, `url` e credenciais), o runtime inicializa o cliente uma única vez por worker e gerencia *prefetching*, *caching* e *micro-batching* com operação *zero-copy* e *zero-serialization* sempre que suportado.

## Exemplo
```python
def init_context(context):
    # Opcionalmente inicialize modelos pesados ou recursos compartilhados uma única vez por worker:
    setattr(context.user_data, "model_loaded", True)

def handler(context, event):
    if getattr(context.user_data, "model_loaded", False):
        return "Inferência pronta em memória!"
```

## Limites e trade-offs
Além dos `dataBindings` declarativos, a função callback especial **`init_context(context)`** no Nuclio é executada uma única vez na inicialização de cada worker, sendo o local ideal para carregar pesos de modelos de Machine Learning na GPU/RAM ou inicializar clientes.

## Como verificar
Defina `init_context(context)` em sua função Python, faça deploy e confirme nos logs que a inicialização ocorre apenas 1 vez por worker na partida do Pod.

## Conexões
- [[nuclio-triggers-streaming-kafka-kinesis-rabbit-mqtt-cron-http]] — Veja também: Nuclio Triggers de Tempo Real: ingestão paralela de streams (`Kafka`, `Kinesis`, `RabbitMQ`, `MQTT`, `NATS`, `Cron` e `HTTP`).
- [[nuclio-aceleracao-gpu-nvidia-inferencia-ml-jupyter-kubeflow]] — Veja também: Nuclio para IA/ML e GPUs: alocação de GPUs NVIDIA (`nvidia.com/gpu`), integração com Jupyter (`nuclio-jupyter`) e MLRun.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
