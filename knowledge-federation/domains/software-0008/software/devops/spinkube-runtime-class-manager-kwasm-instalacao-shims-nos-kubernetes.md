---
id: software.devops.tranche18.001787
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

# SpinKube Runtime Class Manager (`Shim` CRD): instalação declarativa de shims Wasm (`containerd-shim-spin`) nos worker nodes

## Em uma frase
O **Runtime Class Manager** (`spinframework/runtime-class-manager`, evolução do KWasm) automatiza a instalação, atualização e configuração de shims WebAssembly do `containerd` (como `containerd-shim-spin`) nos nós de um cluster Kubernetes por meio do Custom Resource `Shim`.

## Por que importa
Conectar-se via SSH em cada worker node para copiar o binário `containerd-shim-spin-v2` em `/usr/local/bin/`, editar `/etc/containerd/config.toml` adicionando `[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.spin]` e reiniciar o `containerd` manualmente inviabiliza o auto-scaling de nós.

## Como funciona
O Runtime Class Manager observa os nós e os objetos `Shim`: quando um nó corresponde ao `nodeSelector`, um Job/DaemonSet instalador provisiona o binário do shim no host, registra o handler no `containerd`, aplica o label de prontidão no nó e cria a `RuntimeClass` correspondente.

## Exemplo
```bash
kubectl get runtimeclasses
kubectl get nodes --show-labels | grep spinkube
```

## Limites e trade-offs
Ao usar `runtimeClassName` com `scheduling.nodeSelector` na `RuntimeClass`, o Kubernetes Scheduler agenda automaticamente os Pods de `SpinApp` apenas nos worker nodes onde o shim Wasm já foi instalado.

## Como verificar
Verifique os labels dos nós e a definição da `RuntimeClass` com `kubectl get runtimeclass wasmtime-spin-v2 -o yaml`.

## Conexões
- [[spinkube-crd-spinappexecutor-containerd-shim-spin-deployment-model]] — Veja também: SpinKube CRD `SpinAppExecutor`: configuração do modelo de execução (`containerd-shim-spin`) e `RuntimeClass`.
- [[spin-registry-push-pull-distribuicao-artefatos-oci-wasm]] — Veja também: Spin OCI Distribution: empacotamento e distribuição de aplicações Wasm em Registries OCI (`spin registry push` / `pull`).

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://www.spinkube.dev/docs/overview/) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
