---
id: software.devops.tranche18.001799
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
fontes: ["https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md", "https://wasmcloud.com/docs/concepts/components/", "https://github.com/wasmCloud/wasmCloud"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# wasmCloud: arquiteturas de referência (`blobby`, `grpc-hello-world`, `otel-config`, `qrcode`) e observabilidade OpenTelemetry

## Em uma frase
O monorepo do wasmCloud mantém em `examples/` projetos de referência completos construídos e publicados continuamente em `ghcr.io/wasmcloud/components/*` — cobrindo armazenamento de blobs (`blobby`), servidores gRPC (`grpc-hello-world`), telemetria **OpenTelemetry** (`otel-config`), geração de imagens (`qrcode`) e armazenamento persistente.

## Por que importa
Adotar WebAssembly em produção exige comprovar que cargas `.wasm` suportam não apenas um "Hello World" HTTP simples, mas também gRPC, rastreamento distribuído OpenTelemetry (`traces`, `metrics`, `logs`), TCP e armazenamento persistente.

## Como funciona
O `wash-runtime` e os exemplos como `otel-config` demonstram como exportar telemetria estruturada OpenTelemetry a partir do host e dos componentes via `wasi:logging` e `wasi:config`, integrando-se diretamente a coletores OTel, Jaeger e Prometheus do cluster Kubernetes.

## Exemplo
```bash
git clone --depth 1 https://github.com/wasmCloud/wasmCloud.git
ls -la wasmCloud/examples/
```

## Limites e trade-offs
Todos os componentes de exemplo em `examples/` são compilados e enviados pelo pipeline de CI oficial para `ghcr.io/wasmcloud/components/*`, servindo como imagens prontas para validar novos clusters wasmCloud.

## Como verificar
Implante um `WorkloadDeployment` apontando para um componente de `ghcr.io/wasmcloud/components/` para validar o agendamento e a telemetria do cluster.

## Conexões
- [[wasmcloud-desenvolvimento-poliglota-rust-tinygo-typescript-python-wasi]] — Veja também: wasmCloud Poliglota: compilação e interoperabilidade de componentes em Rust, Go, TypeScript e Python.
- [[wasmcloud-execucao-hibrida-edge-custom-hosts-densidade-seguranca]] — Veja também: wasmCloud na Borda e Hosts Customizados: execução de alta densidade fora de containers com `wash-runtime`.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
