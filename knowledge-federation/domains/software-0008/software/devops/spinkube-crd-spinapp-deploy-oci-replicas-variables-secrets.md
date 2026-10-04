---
id: software.devops.tranche18.001785
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md", "https://www.spinkube.dev/docs/overview/", "https://raw.githubusercontent.com/spinframework/spin/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SpinKube CRD `SpinApp`: implantação declarativa de artefatos OCI WebAssembly com réplicas, variáveis e recursos no Kubernetes

## Em uma frase
O Custom Resource **`SpinApp`** (`core.spinkube.dev/v1alpha1`) é a abstração principal do SpinKube onde o desenvolvedor declara a imagem OCI da aplicação Spin (`spec.image`), o número de réplicas (`spec.replicas`), o executor (`spec.executor`) e o vínculo de variáveis e configurações de runtime a `Secrets` e `ConfigMaps` do Kubernetes.

## Por que importa
Escrever manualmente um `Deployment` com `runtimeClassName`, portas de container, probes e montagens de configuração do Spin para cada microsserviço Wasm é propenso a erros; o `SpinApp` reduz a implantação a poucas linhas declarativas.

## Como funciona
Ao aplicar um `SpinApp`, o Spin Operator valida o recurso via webhook (suportado pelo `cert-manager`), resolve o executor referenciado e reconcilia o `Deployment` e o `Service` Kubernetes, injetando variáveis de aplicação e o `runtime-config.toml` a partir de Secrets do cluster.

## Exemplo
```yaml
apiVersion: core.spinkube.dev/v1alpha1
kind: SpinApp
metadata:
  name: simple-spinapp
spec:
  image: "ghcr.io/spinkube/containerd-shim-spin/examples/spin-rust-hello:v0.15.1"
  executor: containerd-shim-spin
  replicas: 2
```

## Limites e trade-offs
Para que os webhooks de validação e mutação do `spin-operator` funcionem em um cluster remoto, o `cert-manager` deve estar instalado e operacional antes do deploy do operador.

## Como verificar
Aplique o manifesto `SpinApp`, execute `kubectl get spinapps,deploy,pods,svc` e teste o serviço com `kubectl port-forward svc/simple-spinapp 8083:80` seguido de `curl http://localhost:8083/hello`.

## Conexões
- [[spinkube-arquitetura-wasm-kubernetes-spin-operator-runwasi-shim]] — Veja também: SpinKube: arquitetura CNCF Sandbox para operar aplicações WebAssembly no Kubernetes (`Spin Operator`, `runwasi` e `RuntimeClass`).
- [[spinkube-crd-spinappexecutor-containerd-shim-spin-deployment-model]] — Veja também: SpinKube CRD `SpinAppExecutor`: configuração do modelo de execução (`containerd-shim-spin`) e `RuntimeClass`.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
