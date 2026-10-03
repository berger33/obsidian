---
id: software.devops.tranche18.001784
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
fontes: ["https://www.spinkube.dev/docs/overview/", "https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md", "https://raw.githubusercontent.com/spinframework/spin/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SpinKube: arquitetura CNCF Sandbox para operar aplicações WebAssembly no Kubernetes (`Spin Operator`, `runwasi` e `RuntimeClass`)

## Em uma frase
O **SpinKube** (projeto CNCF Sandbox) integra o ecossistema Spin ao Kubernetes combinando três subprojetos: o **Spin Operator** (`spin-operator`, construído com Kubebuilder), o shim containerd **`containerd-shim-spin`** (baseado em `containerd/runwasi`) e o **Runtime Class Manager** (`runtime-class-manager`).

## Por que importa
Embora o Kubernetes tenha sido originalmente desenhado para agendar imagens de containers Linux via `runc`, estender o `containerd` com um shim `runwasi` permite que o `kubelet` execute artefatos WebAssembly OCI nativamente como Pods com DNS, probes, HPA, Services e métricas Prometheus padrão.

## Como funciona
No SpinKube, o nó Kubernetes possui o binário `containerd-shim-spin` registrado no `containerd` e exposto por uma `RuntimeClass` (`wasmtime-spin-v2`). Quando o desenvolvedor aplica um Custom Resource **`SpinApp`**, o Spin Operator cria automaticamente o `Deployment` (com `runtimeClassName: wasmtime-spin-v2`) e o `Service` correspondente.

## Exemplo
```bash
k3d cluster create wasm-cluster \
  --image ghcr.io/spinframework/containerd-shim-spin/k3d:v0.23.0 \
  -p "8081:80@loadbalancer" \
  --agents 2
kubectl get nodes -o wide
```

## Limites e trade-offs
Os artefatos Wasm empacotados para o SpinKube são significativamente menores que imagens de container e não consomem quase nada de CPU/memória quando ociosos.

## Como verificar
Suba o cluster `k3d` com a imagem `containerd-shim-spin` e verifique a presença da `RuntimeClass` e dos CRDs `spinapps.core.spinkube.dev` e `spinappexecutors.core.spinkube.dev`.

## Conexões
- [[spin-sdks-poliglotas-rust-typescript-python-tinygo-apis-embutidas]] — Veja também: Spin SDKs Poliglotas e APIs de Plataforma: suporte a Rust, TypeScript/JS, Python e TinyGo com KV, SQLite, SQL e Serverless AI.
- [[spinkube-crd-spinapp-deploy-oci-replicas-variables-secrets]] — Veja também: SpinKube CRD `SpinApp`: implantação declarativa de artefatos OCI WebAssembly com réplicas, variáveis e recursos no Kubernetes.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://www.spinkube.dev/docs/overview/) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
