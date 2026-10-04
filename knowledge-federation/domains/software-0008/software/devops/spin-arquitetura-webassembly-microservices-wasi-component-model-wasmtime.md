---
id: software.devops.tranche18.001781
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

# Spin: arquitetura do framework CNCF para microsserviços serverless em WebAssembly com Component Model e Wasmtime

## Em uma frase
O **Spin** (`spinframework/spin`, projeto CNCF Sandbox licenciado sob Apache 2.0) é um framework open-source para construir, distribuir e executar microsserviços cloud-native rápidos, seguros e componíveis com **WebAssembly (Wasm)** sobre o **WebAssembly Component Model** (`wasm32-wasip2`) e o runtime **Wasmtime**.

## Por que importa
Containers Linux tradicionais carregam sistemas de arquivos inteiros de dezenas ou centenas de megabytes e levam centenas de milissegundos a segundos para iniciar em *cold start*, enquanto componentes WebAssembly compilados para o Spin pesam poucos megabytes e iniciam em sub-milissegundo com isolamento sandboxed por requisição.

## Como funciona
A CLI `spin` provê o ciclo completo: `spin new -t <template>` cria o projeto a partir de templates oficiais, `spin build` compila os componentes para o alvo `wasm32-wasip2`, `spin up` executa a aplicação localmente (servindo HTTP na porta `3000` por padrão) e `spin registry push` empacota e publica a aplicação Wasm diretamente em qualquer registry OCI.

## Exemplo
```bash
rustup target add wasm32-wasip2
spin new --accept-defaults -t http-rust hello-rust
cd hello-rust
spin build
spin up
```

## Limites e trade-offs
Diferentemente de containers que permanecem em memória consumindo recursos mesmo quando ociosos, o Spin instancia um ambiente Wasm limpo para cada evento/requisição HTTP ou Redis e o descarta imediatamente ao término da resposta.

## Como verificar
Execute `spin up` em um terminal e `curl -i http://127.0.0.1:3000` em outro para comprovar a resposta instantânea do componente Wasm.

## Conexões
- [[spin-manifesto-spin-toml-triggers-http-redis-componentes-variaveis]] — Veja também: Spin `spin.toml`: configuração declarativa de triggers (`http`, `redis`), rotas, variáveis e permissões de rede.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
