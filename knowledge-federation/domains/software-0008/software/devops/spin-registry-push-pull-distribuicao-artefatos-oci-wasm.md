---
id: software.devops.tranche18.001788
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
fontes: ["https://raw.githubusercontent.com/spinframework/spin/main/README.md", "https://www.spinkube.dev/docs/overview/", "https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Spin OCI Distribution: empacotamento e distribuição de aplicações Wasm em Registries OCI (`spin registry push` / `pull`)

## Em uma frase
O comando **`spin registry push`** empacota o manifesto `spin.toml`, todos os binários `.wasm` compilados dos componentes e os ativos estáticos da aplicação como um artefato OCI padrão e o publica em qualquer container registry compatível (GHCR, Docker Hub, ACR, ECR, Harbor, Zot).

## Por que importa
Se aplicações WebAssembly exigissem um servidor de pacotes proprietário diferente dos registries OCI que a empresa já usa para imagens Docker e Helm charts, toda a cadeia de suprimentos (autenticação, replicação, assinatura Cosign) precisaria ser duplicada.

## Como funciona
Após autenticar com `spin registry login`, `spin registry push ghcr.io/org/minha-app:v1.0.0` envia as camadas Wasm para o registry. Essa mesma referência OCI pode ser executada diretamente em qualquer máquina com `spin up --from-registry ghcr.io/org/minha-app:v1.0.0` ou referenciada em `spec.image` de uma `SpinApp` no Kubernetes com SpinKube.

## Exemplo
```bash
spin build
spin registry login ghcr.io -u "$GITHUB_USER" --password-stdin <<< "$GITHUB_TOKEN"
spin registry push ghcr.io/org/hello-rust:v0.1.0
spin up --from-registry ghcr.io/org/hello-rust:v0.1.0
```

## Limites e trade-offs
Diferentemente de uma imagem Docker tradicional presa a `linux/amd64` ou `linux/arm64`, o artefato OCI gerado por `spin registry push` contém bytecode `.wasm` portátil que roda sem recompilação tanto em nós x86_64 quanto em nós ARM64.

## Como verificar
Publique uma aplicação de teste em um registry OCI local e execute-a diretamente a partir da URL do registry com `spin up --from-registry`.

## Conexões
- [[spinkube-runtime-class-manager-kwasm-instalacao-shims-nos-kubernetes]] — Veja também: SpinKube Runtime Class Manager (`Shim` CRD): instalação declarativa de shims Wasm (`containerd-shim-spin`) nos worker nodes.
- [[spinkube-autoscaling-hpa-keda-scale-to-zero-workloads-wasm]] — Veja também: SpinKube: auto-escalonamento horizontal (HPA) e *scale-to-zero* orientado a eventos com KEDA para `SpinApp`.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
