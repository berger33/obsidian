---
id: software.seguranca.tranche17.001611
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://embarkstudios.github.io/cargo-deny/", "https://embarkstudios.github.io/cargo-deny/checks/index.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-deny`: checks declarativos sobre o grafo de dependências Cargo

## Em uma frase
`cargo-deny` aplica políticas configuráveis ao grafo de dependências Rust e agrupa verificações de advisories, licenças, bans e origens.

## Por que importa
Uma revisão única do lockfile pode deixar passar licenças incompatíveis, fontes inesperadas ou versões duplicadas; regras explícitas tornam esses requisitos revisáveis no repositório.

## Como funciona
Inicialize a configuração, escolha o conjunto de checks adequado e rode o comando na mesma resolução usada pelo build; trate o resultado como lint de política do grafo.

## Exemplo
Uma equipe pode manter `deny.toml` com políticas aprovadas e executar `cargo deny check` em cada pull request que altera manifests ou `Cargo.lock`.

```text
cargo deny check
```

## Limites e trade-offs
O comando não examina semântica de código, não decide se uma licença é juridicamente aceitável e depende de base de advisories atualizada.

## Como verificar
Revise cada seção de configuração, confirme que CI executa os checks escolhidos e introduza uma dependência controlada para validar que a regra falha como esperado.

## Conexões
- [[cargo-deny-advisory-db-rustsec-atualizacao-offline]] — `cargo-deny check advisories`: fonte RustSec, cache local e atualidade dos dados.

## Fontes
- [`cargo-deny` — Quickstart e classes de checks](https://embarkstudios.github.io/cargo-deny/) — comando `cargo deny check` e escopo geral das políticas de grafo; consultado em 2026-10-04.
- [`cargo-deny` — Checks](https://embarkstudios.github.io/cargo-deny/checks/index.html) — índice oficial das verificações de advisories, licenças, bans e fontes; consultado em 2026-10-04.
