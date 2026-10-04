---
id: software.devops.tranche18.001790
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

# Spin: sistema de Plugins (`spin plugins`), Templates (`spin templates`) e criação de Custom Triggers

## Em uma frase
A CLI do Spin é extensível por meio de **Templates** (`spin templates install`) e **Plugins** (`spin plugins install`, como o plugin `kube` para gerar manifestos SpinKube, `js2wasm` ou `py2wasm`), além de permitir criar **Custom Triggers** em Rust usando o Spin SDK.

## Por que importa
Equipes de plataforma precisam padronizar templates de projetos internos (já configurados com observabilidade e lint) e adicionar comandos como `spin kube scaffold` diretamente na CLI dos desenvolvedores.

## Como funciona
Com `spin plugins update && spin plugins install kube`, o desenvolvedor ganha o subcomando `spin kube scaffold --from ghcr.io/org/app:v1.0.0`, que gera o manifesto `SpinApp` pronto para aplicar no cluster Kubernetes.

## Exemplo
```bash
spin plugins update
spin plugins install kube --yes
spin kube scaffold --from ghcr.io/spinkube/containerd-shim-spin/examples/spin-rust-hello:v0.15.1
```

## Limites e trade-offs
De acordo com a tabela oficial de suporte de linguagens do Spin, a autoria de novos *Custom Triggers* (além dos gatilhos nativos `http` e `redis`) é suportada usando o SDK de **Rust**.

## Como verificar
Execute `spin plugins list` e `spin kube scaffold --from <image>` para validar a geração automática do manifesto `SpinApp`.

## Conexões
- [[spinkube-autoscaling-hpa-keda-scale-to-zero-workloads-wasm]] — Veja também: SpinKube: auto-escalonamento horizontal (HPA) e *scale-to-zero* orientado a eventos com KEDA para `SpinApp`.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
