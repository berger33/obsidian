---
id: software.devops.tranche18.001793
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

# wasmCloud Wasm Shell (`wash`): ciclo de desenvolvimento com `wash new`, `wash build` e loop hot-reload `wash dev`

## Em uma frase
A ferramenta de linha de comando **Wasm Shell (`wash`)** (`crates/wash`) unifica o ciclo de desenvolvimento de componentes WebAssembly para Rust, Go (TinyGo), TypeScript e Python, oferecendo um loop de desenvolvimento local instantâneo com **`wash dev`**.

## Por que importa
Configurar manualmente cadeias de compilação WASI P2, adaptadores de componente e um host local com provedores HTTP e Key-Value apenas para testar uma função durante a codificação atrasa o feedback do desenvolvedor.

## Como funciona
O comando `wash new` gera o projeto a partir de `templates/` (`http-hello-world`, `http-handler`, `http-kv-handler`, `service-tcp`); `wash build` invoca o compilador da linguagem de origem para gerar o `.wasm` assinado com metadados WIT; e `wash dev` inicia o `wash-runtime` localmente na porta `8000`, satisfazendo automaticamente as interfaces importadas pelo componente e recompilando em hot-reload a cada salvamento de arquivo.

## Exemplo
```bash
wash build
wash dev --workloads ./build/http_hello_world_s.wasm
```

## Limites e trade-offs
Em outro terminal, basta executar `curl http://localhost:8000` para testar o componente servido pelo `wash dev` em tempo real.

## Como verificar
Inicie `wash dev` em um projeto de template HTTP, altere a string de resposta no código-fonte e confirme com `curl localhost:8000` a recarga automática.

## Conexões
- [[wasmcloud-component-model-wasi-p2-wit-interfaces-composicao-dinamica]] — Veja também: wasmCloud Components: programação reativa sobre WASI Preview 2 (`wasm32-wasip2`), interfaces WIT e linkagem dinâmica.
- [[wasmcloud-wash-runtime-mecanismos-capacidades-builtin-ingress-plugins]] — Veja também: wasmCloud `wash-runtime`: arquitetura dos 3 mecanismos de capacidades (`wasmtime-wasi`, `Ingress` e `Host Plugins`).

## Fontes
- [wasmCloud GitHub — README.md (CNCF Incubating WebAssembly Platform, Deny-by-Default Capabilities, wash, wash-runtime & Kubernetes runtime-operator)](https://raw.githubusercontent.com/wasmCloud/wasmCloud/main/README.md) — README oficial do wasmCloud/wasmCloud detalhando o monorepo v2, Wasm Shell (wash), wash-runtime, runtime-operator no Kubernetes e roteamento via EndpointSlices; consultado em 2026-10-03.
- [wasmCloud Official Documentation — Wasm Component Model & Components (Reactive Sandboxed Binaries, WIT Interfaces & Dynamic Linking)](https://wasmcloud.com/docs/concepts/components/) — Documentação oficial de componentes do wasmCloud explicando segurança deny-by-default, portabilidade, desacoplamento por interfaces WIT e WASI Preview 2; consultado em 2026-10-03.
- [wasmCloud — Official GitHub Repository](https://github.com/wasmCloud/wasmCloud) — Repositório oficial Apache-2.0 do wasmCloud na CNCF; consultado em 2026-10-03.
