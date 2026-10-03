---
id: software.devops.tranche18.001794
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

# wasmCloud `wash-runtime`: arquitetura dos 3 mecanismos de capacidades (`wasmtime-wasi`, `Ingress` e `Host Plugins`)

## Em uma frase
O **`wash-runtime`** (`crates/wash-runtime`) é o runtime Rust embarcável que envolve o motor **Wasmtime** e expõe capacidades controladas aos componentes WebAssembly por meio de três mecanismos arquiteturais distintos: capacidades embutidas (`wasmtime-wasi`), `Ingress` e `Host Plugins` (`with_plugin()`).

## Por que importa
Separar as capacidades básicas de sistema (relógio, gerador aleatório) das capacidades de entrada HTTP e dos serviços de armazenamento/mensageria permite embutir o `wash-runtime` tanto em servidores de cluster Kubernetes quanto em dispositivos de borda restritos apenas com os plugins necessários.

## Como funciona
De acordo com a documentação oficial do repositório wasmCloud, o `wash-runtime` fornece: 1) **Built-in via `wasmtime-wasi`**: `wasi:filesystem`, `wasi:clocks`, `wasi:random`, `wasi:io`, `wasi:sockets` e `wasi:cli`; 2) **Ingress (`Ingress`)**: `wasi:http` (cliente e servidor HTTP); e 3) **Host plugins (`with_plugin()`)**: implementações em memória ou apoiadas em NATS para `wasi:keyvalue`, `wasi:blobstore`, `wasi:config`, `wasi:logging` e `wasmcloud:messaging`.

## Exemplo
```bash
# Testando um componente que consome wasi:http e wasi:keyvalue no wash-runtime:
cd templates/http-kv-handler && wash build && wash dev
```

## Limites e trade-offs
Engenheiros que constroem hosts customizados para cenários embarcados ou industriais podem estender o `wash-runtime` em tempo de compilação registrando seus próprios plugins Rust via `.with_plugin(...)`.

## Como verificar
Gere um projeto com o template `http-kv-handler`, execute `wash dev` e valide a persistência de estado através da interface `wasi:keyvalue`.

## Conexões
- [[wasmcloud-wash-cli-scaffolding-build-hot-reload-wash-dev]] — Veja também: wasmCloud Wasm Shell (`wash`): ciclo de desenvolvimento com `wash new`, `wash build` e loop hot-reload `wash dev`.
- [[wasmcloud-kubernetes-runtime-operator-crds-host-workload-deployment]] — Veja também: wasmCloud Kubernetes `runtime-operator`: reconciliação dos CRDs `Host`, `Workload`, `WorkloadDeployment`, `WorkloadReplicaSet` e `Artifact`.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
