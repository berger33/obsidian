---
id: software.devops.tranche18.001798
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
fontes: ["https://wasmcloud.com/docs/concepts/components/", "https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md", "https://github.com/wasmCloud/wasmCloud"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# wasmCloud Poliglota: compilação e interoperabilidade de componentes em Rust, Go, TypeScript e Python

## Em uma frase
Como os componentes wasmCloud aderem estritamente ao padrão W3C **Component Model** e **WASI 0.2**, equipes podem desenvolver componentes em **Rust**, **Go**, **TypeScript/JavaScript** ou **Python** e fazê-los invocar funções uns dos outros em tempo de execução sem serialização HTTP/JSON intermediária.

## Por que importa
Em arquiteturas tradicionais de microsserviços, reutilizar uma biblioteca criptográfica em Rust a partir de uma API escrita em TypeScript exige chamadas de rede gRPC/REST entre containers distintos ou bindings nativos N-API presos à plataforma Linux.

## Como funciona
No wasmCloud, cada linguagem compila para um arquivo `.wasm` com tipos de alto nível do Component Model (strings, listas, records, variants definidos em WIT). O `wash build` abstrai a invocação da toolchain específica de cada linguagem (`cargo`, `tinygo`, `jco`, `componentize-py`), produzindo artefatos interoperáveis.

## Exemplo
```bash
# Exemplos oficiais pré-compilados pelo CI do wasmCloud no GHCR:
# ghcr.io/wasmcloud/components/http-hello-world-rust:latest
wash oci pull ghcr.io/wasmcloud/components/http-hello-world-rust:latest
```

## Limites e trade-offs
Os recursos e SDKs específicos de linguagem para **TypeScript** (`github.com/wasmCloud/typescript`) e **Go** (`github.com/wasmCloud/go`) são mantidos em repositórios dedicados dentro da organização oficial `wasmCloud`.

## Como verificar
Execute `wash build` em um projeto de componente e verifique a geração do binário `.wasm` compatível com WASI Preview 2.

## Conexões
- [[wasmcloud-nats-control-plane-messaging-kv-blobstore-plugins]] — Veja também: wasmCloud e NATS: barramento de controle Protobuf e backend para `wasi:keyvalue`, `wasi:blobstore` e `wasmcloud:messaging`.
- [[wasmcloud-exemplos-referencia-blobby-grpc-otel-persistent-storage]] — Veja também: wasmCloud: arquiteturas de referência (`blobby`, `grpc-hello-world`, `otel-config`, `qrcode`) e observabilidade OpenTelemetry.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://wasmcloud.com/docs/concepts/components/) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
