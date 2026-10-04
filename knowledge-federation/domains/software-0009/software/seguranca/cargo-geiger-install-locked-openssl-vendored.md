---
id: software.seguranca.tranche17.001636
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
fontes: ["https://github.com/geiger-rs/cargo-geiger", "https://doc.rust-lang.org/cargo/commands/cargo-install.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Instalar `cargo-geiger` com Cargo lockado e escolher a biblioteca OpenSSL

## Em uma frase
O README do `cargo-geiger` oferece uma instalação com `cargo install --locked` e uma alternativa com OpenSSL compilado estaticamente usando a feature `vendored-openssl`.

## Por que importa
Fixar as dependências de instalação reduz variação no ambiente da ferramenta; a opção vendored ajuda em runners sem uma instalação de OpenSSL compatível, com custo de build próprio.

## Como funciona
Escolha entre usar uma biblioteca OpenSSL de sistema ou compilar a versão vendored, registre a versão do cargo-geiger e valide a instalação no mesmo tipo de runner da CI.

## Exemplo
Em um runner padronizado, instale o plugin com `cargo install --locked cargo-geiger`; se não houver OpenSSL de sistema compatível, use `cargo install --locked cargo-geiger --features vendored-openssl`.

```text
cargo install --locked cargo-geiger --features vendored-openssl
```

## Limites e trade-offs
A feature vendored aumenta o trabalho de compilação e não torna o relatório mais correto; versões de Rust, plataforma e requisitos criptográficos continuam sendo decisões separadas.

## Como verificar
Confira a versão instalada com `cargo geiger --version`, valide a disponibilidade do executável no PATH e repita a instalação num runner limpo para detectar dependências implícitas.

## Conexões
- [[cargo-geiger-baseline-historico-delta-unsafe]] — Usar baseline de `cargo-geiger` para acompanhar mudanças sem premiar dívida antiga.
- [[cargo-geiger-comparacao-crates-normalizada-toolchain]] — Comparar relatórios `cargo-geiger` com toolchain, features e grafo fixos.

## Fontes
- [`cargo-geiger` — repositório oficial](https://github.com/geiger-rs/cargo-geiger) — README oficial com a instalação `--locked` e a feature `vendored-openssl`; consultado em 2026-10-04.
- [Cargo Reference — `cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html) — sintaxe e semântica de `--locked` e `--features` durante instalação de um pacote Cargo; consultado em 2026-10-04.
