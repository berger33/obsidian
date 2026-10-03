---
id: software.devops.tranche18.001783
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

# Spin SDKs Poliglotas e APIs de Plataforma: suporte a Rust, TypeScript/JS, Python e TinyGo com KV, SQLite, SQL e Serverless AI

## Em uma frase
O Spin fornece SDKs oficiais para **Rust**, **TypeScript/JavaScript**, **Python** e **Go (TinyGo)** (além de C# e integrações comunitárias para Zig e Moonbit), expondo interfaces WIT padronizadas para **HTTP**, **Redis**, **Key-Value Store**, **SQLite**, **MySQL/PostgreSQL**, **Configuration Variables** e **Serverless AI**.

## Por que importa
Compilar drivers nativos de banco de dados baseados em sockets C/POSIX tradicionais para WebAssembly puro costuma exigir reescrever pilhas de rede; o Spin resolve isso fornecendo conexões gerenciadas pelo host através de interfaces WASI/WIT de alto nível.

## Como funciona
Como todos os SDKs compilam para o **WebAssembly Component Model**, uma única aplicação Spin pode combinar um componente de API em TypeScript na rota `/api/*`, um componente de inferência em Python na rota `/predict` e um worker de alta performance em Rust na rota `/ingest`, compartilhando o mesmo Key-Value Store e banco SQLite embutidos.

## Exemplo
```rust
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;
use spin_sdk::key_value::Store;

#[http_component]
fn handle_request(_req: Request) -> anyhow::Result<impl IntoResponse> {
    let store = Store::open_default()?;
    store.set("visitas", b"1")?;
    Ok(Response::builder().status(200).body("OK from Spin Wasm!").build())
}
```

## Limites e trade-offs
Durante o desenvolvimento local com `spin up`, o Spin cria e gerencia automaticamente um Key-Value Store e um banco SQLite locais em `.spin/` sem exigir instalar servidores externos; em produção, os mesmos stores podem ser mapeados para Redis/Turso/bancos externos em `runtime-config.toml`.

## Como verificar
Execute `spin templates list` para visualizar os templates disponíveis em Rust, JS/TS, Python e Go.

## Conexões
- [[spin-manifesto-spin-toml-triggers-http-redis-componentes-variaveis]] — Veja também: Spin `spin.toml`: configuração declarativa de triggers (`http`, `redis`), rotas, variáveis e permissões de rede.
- [[spinkube-arquitetura-wasm-kubernetes-spin-operator-runwasi-shim]] — Veja também: SpinKube: arquitetura CNCF Sandbox para operar aplicações WebAssembly no Kubernetes (`Spin Operator`, `runwasi` e `RuntimeClass`).

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
