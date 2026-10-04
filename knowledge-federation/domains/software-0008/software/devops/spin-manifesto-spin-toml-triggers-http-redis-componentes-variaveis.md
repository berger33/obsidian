---
id: software.devops.tranche18.001782
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

# Spin `spin.toml`: configuração declarativa de triggers (`http`, `redis`), rotas, variáveis e permissões de rede

## Em uma frase
O arquivo de manifesto **`spin.toml`** (formato `spin_manifest_version = 2`) define a topologia completa de uma aplicação Spin: metadados da aplicação, variáveis de configuração, gatilhos (*triggers* `http` ou `redis`), rotas mapeadas para cada componente `.wasm` e a lista explícita de capacidades permitidas (`allowed_outbound_hosts`, `key_value_stores`, `sqlite_databases`).

## Por que importa
Por segurança *deny-by-default*, um componente WebAssembly no Spin não tem acesso a nenhum arquivo arbitrário do host, não pode abrir conexões de rede para nenhum domínio externo e não acessa bancos de dados a menos que o `spin.toml` conceda explicitamente essa permissão para aquele componente.

## Como funciona
No `spin.toml`, cada componente aponta para seu binário `.wasm` (`source = "target/wasm32-wasip2/release/hello.wasm"`), seu comando de build e a lista `allowed_outbound_hosts = ["https://api.corp.internal:443"]`. Qualquer tentativa do código Wasm de chamar uma URL fora dessa lista é bloqueada imediatamente pelo runtime do Spin.

## Exemplo
```toml
spin_manifest_version = 2

[application]
name = "hello-rust"
version = "0.1.0"

[component.hello-rust]
source = "target/wasm32-wasip2/release/hello_rust.wasm"
allowed_outbound_hosts = ["https://api.example.com:443"]
key_value_stores = ["default"]

[component.hello-rust.build]
command = "cargo build --target wasm32-wasip2 --release"
```

## Limites e trade-offs
Para permitir chamadas de saída para qualquer porta de um host ou protocolo específico (como Redis ou PostgreSQL), declare o esquema, host e porta explícitos em `allowed_outbound_hosts` (ex.: `"redis://redis.internal:6379"` ou `"postgres://db.internal:5432"`).

## Como verificar
Remova um host de `allowed_outbound_hosts` no `spin.toml`, execute `spin up` e confirme que chamadas HTTP de saída do componente para aquele host são negadas pelo sandbox.

## Conexões
- [[spin-arquitetura-webassembly-microservices-wasi-component-model-wasmtime]] — Veja também: Spin: arquitetura do framework CNCF para microsserviços serverless em WebAssembly com Component Model e Wasmtime.
- [[spin-sdks-poliglotas-rust-typescript-python-tinygo-apis-embutidas]] — Veja também: Spin SDKs Poliglotas e APIs de Plataforma: suporte a Rust, TypeScript/JS, Python e TinyGo com KV, SQLite, SQL e Serverless AI.

## Fontes
- [Spin Framework GitHub — README.md (WebAssembly Microservices with Component Model & Wasmtime, Polyglot SDKs & Triggers)](https://raw.githubusercontent.com/spinframework/spin/main/README.md) — README oficial do spinframework/spin detalhando alvo wasm32-wasip2, comandos spin new/build/up e tabela de suporte dos SDKs Rust/TS/Python/Go/C#; consultado em 2026-10-03.
- [SpinKube Official Documentation — Project Overview (Spin Operator, containerd-shim-spin / runwasi & Runtime Class Manager)](https://www.spinkube.dev/docs/overview/) — Visão geral oficial do projeto CNCF Sandbox SpinKube integrando cargas Wasm ao Kubernetes com SpinApp e RuntimeClass; consultado em 2026-10-03.
- [Spin Operator GitHub — README.md (SpinApp & SpinAppExecutor CRDs, k3d Wasm Cluster & Cert-Manager Webhook Setup)](https://raw.githubusercontent.com/spinkube/spin-operator/main/README.md) — README oficial do spinkube/spin-operator demonstrando instalação dos CRDs SpinApp e SpinAppExecutor e execução com containerd-shim-spin; consultado em 2026-10-03.
