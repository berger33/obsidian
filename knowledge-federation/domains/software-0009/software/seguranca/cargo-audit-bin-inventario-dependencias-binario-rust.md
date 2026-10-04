---
id: software.seguranca.tranche17.001607
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md", "https://github.com/rust-secure-code/cargo-auditable"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo audit bin`: leitura de dependências em binários Rust distribuídos

## Em uma frase
O subcomando `cargo audit bin` aceita caminhos de executáveis para procurar metadados de dependências Rust e relacioná-los à base de advisories.

## Por que importa
A verificação pós-build ajuda quando o lockfile não acompanha o artefato entregue, por exemplo em inventários de releases ou investigações de imagens já publicadas.

## Como funciona
Passe os binários selecionados ao subcomando e trate cada achado como um inventário aproximado cuja qualidade depende de como o executável foi produzido.

## Exemplo
Em um job de release, percorra os executáveis empacotados e grave a saída de `cargo audit bin` junto ao digest de cada artefato analisado.

```text
cargo audit bin ./target/release/app
```

## Limites e trade-offs
Para binários sem metadados de `cargo auditable`, a ferramenta recupera apenas parte do grafo por mensagens de panic, pode perder dependências e não encontra código C embarcado.

## Como verificar
Compare um binário produzido com `cargo auditable` a um build convencional e registre separadamente cobertura de inventário e advisories encontrados.

## Conexões
- [[cargo-audit-config-audittoml-controle-versao-excecoes]] — `audit.toml` versionado: governança das exceções locais do `cargo-audit`.
- [[cargo-auditable-metadados-embed-binario-limites]] — `cargo auditable`: metadados embutidos e limites da auditoria de binários Rust.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — subcomando `cargo audit bin` e limites ao inspecionar binários convencionais; consultado em 2026-10-04.
- [`cargo-auditable` — projeto oficial](https://github.com/rust-secure-code/cargo-auditable) — metadados de dependências embutidos em executáveis Rust para auditoria pós-build; consultado em 2026-10-04.
