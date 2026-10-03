---
id: software.devops.tranche19.001822
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

# Nuclio Function Processor: arquitetura interna de Event Listeners e motores de Runtime (`Native`, `SHMEM` e `Shell`)

## Em uma frase
O **Function Processor** é o coração de cada Pod de função no Nuclio: ele desacopla a lógica da função das fontes de eventos e executa o handler do usuário por meio de três implementações de motor de runtime: **Native** (Go/C inline), **SHMEM** (memória compartilhada zero-copy para Python, Java, Node.js, .NET) e **Shell** (executáveis CLI).

## Por que importa
Comunicar o processo supervisor em Go com um worker Python ou Java usando chamadas HTTP/REST locais introduz cópias de memória e serialização JSON caras; já usar canais de memória compartilhada (*SHMEM*) entrega velocidade próxima ao código nativo.

## Como funciona
O Function Processor é composto por quatro blocos: 1) **Event-source listeners** (ouvindo sockets/filas com garantia *at-least-once* ou *exactly-once* e checkpoints de stream); 2) **Runtime engine** (`Native`, `SHMEM` ou `Shell` com múltiplos workers paralelos); 3) **Data bindings** (conexões persistentes pré-inicializadas no objeto `context`); e 4) **Control framework** (coleta de logs estruturados, estatísticas e health checks em `/__internal/health`).

## Exemplo
```python
def handler(context, event):
    context.logger.info_with("Evento recebido", body_len=len(event.body))
    return context.Response(
        body="Processado pelo runtime SHMEM Python",
        headers={},
        content_type="text/plain",
        status_code=200,
    )
```

## Limites e trade-offs
Conforme documentado na arquitetura do Nuclio, o runtime **Shell** (que executa binários via linha de comando mapeando `stdout`/`stderr`) suporta apenas *data bindings* baseados em arquivos.

## Como verificar
Verifique o endpoint de saúde interno de um Function Processor consultando `/__internal/health` no Pod da função.

## Conexões
- [[nuclio-arquitetura-serverless-real-time-data-gpu-processor]] — Veja também: Nuclio: arquitetura serverless de tempo real de alta performance para eventos, dados e GPUs no Kubernetes.
- [[nuclio-blocking-vs-non-blocking-allocator-workers-sync-async]] — Veja também: Nuclio: alocação de EventProcessors em dois níveis (`Blocking Allocator` vs `Non-blocking Allocator`) para modos Sync e Async.

## Fontes
- [Nuclio GitHub — README.md (High-Performance Serverless for Real-Time Events, Data Processing, GPUs, Kaniko & Kubernetes)](https://raw.githubusercontent.com/nuclio/nuclio/development/docs/concepts/architecture.md) — README oficial do nuclio/nuclio apresentando integração com Jupyter/Kubeflow/MLRun, suporte a GPUs, builder Kaniko e fluxo de deploy; consultado em 2026-10-03.
- [Nuclio Official Documentation — Architecture (Function Processors, Event-Source Listeners, Native/SHMEM/Shell Runtimes, Allocators & Auth-Proxy)](https://raw.githubusercontent.com/nuclio/nuclio/development/README.md) — Documentação oficial de arquitetura do Nuclio detalhando o Function Processor, Blocking vs Non-blocking Allocator, Data Bindings e sidecar auth-proxy; consultado em 2026-10-03.
- [Nuclio — Official GitHub Repository](https://github.com/nuclio/nuclio) — Repositório oficial Apache-2.0 do projeto Nuclio; consultado em 2026-10-03.
