---
id: software.devops.tranche18.001791
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

# wasmCloud: arquitetura CNCF Incubating de execução distribuída de componentes WebAssembly *deny-by-default*

## Em uma frase
O **wasmCloud** (projeto CNCF Incubating licenciado sob Apache 2.0) é uma plataforma cloud-native para executar cargas de trabalho **WebAssembly (Wasm)** (microsserviços, funções e agentes) em qualquer nuvem, Kubernetes, data center ou borda como sandboxes de bytecode ultra-densos com segurança **deny-by-default**.

## Por que importa
Containers tradicionais operam no modelo *allow-by-default* (tendo acesso amplo a syscalls, rede, sistema de arquivos e variáveis de ambiente a menos que bloqueados externamente por Seccomp/AppArmor), enquanto componentes WebAssembly no wasmCloud não podem fazer absolutamente nada fora da CPU/memória linear a menos que uma capacidade tipada seja explicitamente concedida pelo host.

## Como funciona
A plataforma wasmCloud no monorepo atual articula três pilares principais: 1) **Wasm Shell (`wash`) CLI** (para criar, compilar, rodar em hot-reload com `wash dev` e publicar componentes); 2) **`wash-runtime`** (runtime Rust embarcável baseado no Wasmtime com modelo de capacidades via plugins); e 3) **Kubernetes Runtime Operator (`runtime-operator`)** (que reconcilia CRDs wasmCloud no Kubernetes e agenda cargas nos pods de host via NATS).

## Exemplo
```bash
# Instalando o Wasm Shell (wash) e verificando a versão:
curl -fsSL https://wasmcloud.com/sh | bash
wash -V
```

## Limites e trade-offs
Os componentes WebAssembly executados pelo wasmCloud medem de poucos kilobytes a poucos megabytes, iniciam em milissegundos e são portáveis entre qualquer sistema operacional e arquitetura de CPU compatível com WASI.

## Como verificar
Instale o `wash`, adicione o target `rustup target add wasm32-wasip2` e execute `wash -V` para validar o ambiente.

## Conexões
- [[wasmcloud-component-model-wasi-p2-wit-interfaces-composicao-dinamica]] — Veja também: wasmCloud Components: programação reativa sobre WASI Preview 2 (`wasm32-wasip2`), interfaces WIT e linkagem dinâmica.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
