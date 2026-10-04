---
id: software.seguranca.tranche17.001637
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

# Comparar relatórios `cargo-geiger` com toolchain, features e grafo fixos

## Em uma frase
Uma diferença nas contagens só é interpretável se os dois relatórios usarem versões comparáveis da ferramenta, configuração Cargo e conjunto de dependências.

## Por que importa
Mudanças em targets, features ou lockfile podem deslocar as estatísticas sem qualquer refatoração do código examinado.

## Como funciona
Registre a versão do `cargo-geiger`, Rust toolchain, commit, manifest, target e opções de build junto ao relatório, para que a comparação seja reprodutível.

## Exemplo
Ao avaliar uma atualização, gere o relatório anterior e posterior com o mesmo container de CI e diffs do `Cargo.lock` explicitamente associados.

## Limites e trade-offs
Mesmo resultados perfeitamente reproduzíveis continuam sendo contagens e não indicam por si só se uma mudança reduziu risco real.

## Como verificar
Reexecute ambos os commits em ambiente equivalente, compare o grafo e faça triagem das regiões cujo uso de `unsafe` mudou.

## Conexões
- [[cargo-geiger-install-locked-openssl-vendored]] — Instalar `cargo-geiger` com Cargo lockado e escolher a biblioteca OpenSSL.
- [[cargo-geiger-relatorio-dados-entrada-auditoria-humana]] — Arquivar saída do `cargo-geiger` como evidência de revisão, não como certificado.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
