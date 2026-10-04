---
id: software.devops.tranche18.001797
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

# wasmCloud e NATS: barramento de controle Protobuf e backend para `wasi:keyvalue`, `wasi:blobstore` e `wasmcloud:messaging`

## Em uma frase
O **NATS** (com JetStream) desempenha um papel duplo na arquitetura do wasmCloud: atua como o plano de controle de baixa latência (transportando comandos Protobuf entre o `runtime-operator` e os Pods `Host`) e fornece o backend distribuído pronto para uso dos plugins de host `wasi:keyvalue`, `wasi:blobstore`, `wasi:config` e `wasmcloud:messaging`.

## Por que importa
Provisionar bancos de dados separados para estado chave-valor, armazenamento de objetos pequenos e mensageria pub/sub em cada cluster de borda ou desenvolvimento aumentaria drasticamente o footprint operacional.

## Como funciona
O Helm chart `oci://ghcr.io/wasmcloud/charts/runtime-operator` pode instalar um servidor NATS embutido automaticamente na mesma release. Assim, componentes WebAssembly que importam as interfaces WIT `wasi:keyvalue`, `wasi:blobstore` ou `wasmcloud:messaging` (definidas em `wit/`) ganham persistência e mensageria distribuída imediatamente através dos plugins NATS do `wash-runtime`.

## Exemplo
```bash
kubectl get pods -n wasmcloud -l app.kubernetes.io/name=nats
```

## Limites e trade-offs
Para testes unitários rápidos ou execução local isolada no `wash dev`, o `wash-runtime` também inclui variantes *in-memory* (controladas por feature flags) dos plugins `wasi:keyvalue` e `wasi:blobstore` que não exigem cluster NATS externo.

## Como verificar
Inspecione os arquivos `.wit` no diretório `wit/` do wasmCloud para verificar os contratos das interfaces de mensageria e segredos.

## Conexões
- [[wasmcloud-roteamento-http-endpointslices-kubernetes-services-deprecacao-gateway]] — Veja também: wasmCloud no Kubernetes: roteamento HTTP nativo via `EndpointSlices` em Services padrão e depreciação do `runtime-gateway`.
- [[wasmcloud-desenvolvimento-poliglota-rust-tinygo-typescript-python-wasi]] — Veja também: wasmCloud Poliglota: compilação e interoperabilidade de componentes em Rust, Go, TypeScript e Python.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
