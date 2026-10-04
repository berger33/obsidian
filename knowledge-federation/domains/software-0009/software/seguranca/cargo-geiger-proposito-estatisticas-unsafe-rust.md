---
id: software.seguranca.tranche17.001631
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
fontes: ["https://docs.rs/crate/cargo-geiger/latest/source/README.md", "https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo-geiger`: medir presença de `unsafe` sem converter contagem em nota de segurança

## Em uma frase
`cargo-geiger` lista estatísticas relacionadas ao uso de Rust `unsafe` em um crate e nas dependências selecionadas pelo projeto Cargo.

## Por que importa
Uma medida simples ajuda equipes a localizar áreas que merecem leitura de invariantes, mas não classifica automaticamente uma crate como segura ou insegura.

## Como funciona
Execute a ferramenta na pasta com `Cargo.toml`, registre versão e configuração e use as contagens como entrada para uma auditoria qualitativa.

## Exemplo
Em uma revisão de arquitetura, compare os resultados do binário principal e de uma biblioteca central, anotando quais componentes concentram abstrações `unsafe`.

```text
cargo geiger
```

## Limites e trade-offs
A documentação do projeto diz explicitamente que o relatório não deve aconselhar diretamente se o código é inseguro; uso de `unsafe` pode ser necessário e encapsulado.

## Como verificar
Leia a finalidade declarada no README, abra as áreas apontadas no código e documente invariantes, limites de buffer e contratos de ponteiros relevantes.

## Conexões
- [[cargo-geiger-execucao-workspace-grafo-dependencias]] — Executar `cargo geiger` na raiz do workspace e delimitar o grafo analisado.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
