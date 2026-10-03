---
id: software.devops.tranche18.001792
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

# wasmCloud Components: programação reativa sobre WASI Preview 2 (`wasm32-wasip2`), interfaces WIT e linkagem dinâmica

## Em uma frase
No wasmCloud, as cargas de trabalho são **WebAssembly Components** (`.wasm`) compilados segundo o padrão aberto **Component Model** do W3C e **WASI Preview 2 (`wasi 0.2`)**, contendo lógica de negócio stateless que interage com o mundo externo exclusivamente por contratos de interface **WIT** (*WebAssembly Interface Type*).

## Por que importa
Acoplar o código da aplicação diretamente ao driver de um cliente específico (ex.: biblioteca cliente do Redis ou do AWS S3 dentro do binário) obriga a recompilar e reimplantar o código toda vez que a infraestrutura muda de Redis para Valkey, Consul ou NATS KV.

## Como funciona
Um componente wasmCloud não fala com "Redis" ou "PostgreSQL": ele importa uma interface abstrata como `wasi:keyvalue` ou `wasi:http`. Isso permite: 1) trocar o provedor/plugin em tempo de execução sem recompilar o `.wasm`; 2) compor componentes escritos em linguagens diferentes (ex.: Rust chamando uma biblioteca compilada de Go ou TypeScript); e 3) vincular múltiplos componentes dinamicamente no mesmo workload em tempo de execução.

## Exemplo
```bash
wash new https://github.com/wasmCloud/wasmCloud.git \
  --subfolder templates/http-hello-world \
  --name hello
cd hello
wash build
```

## Limites e trade-offs
Quando múltiplos componentes no mesmo workload exportam a mesma interface WIT, o componente importador pode especificar qual provedor deseja utilizando o rótulo `(implements <component-name>)`.

## Como verificar
Compile um componente com `wash build` e inspecione as interfaces WIT importadas e exportadas pelo binário `.wasm` gerado.

## Conexões
- [[wasmcloud-arquitetura-cncf-incubating-deny-by-default-components]] — Veja também: wasmCloud: arquitetura CNCF Incubating de execução distribuída de componentes WebAssembly *deny-by-default*.
- [[wasmcloud-wash-cli-scaffolding-build-hot-reload-wash-dev]] — Veja também: wasmCloud Wasm Shell (`wash`): ciclo de desenvolvimento com `wash new`, `wash build` e loop hot-reload `wash dev`.

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://wasmcloud.com/docs/concepts/components/) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
