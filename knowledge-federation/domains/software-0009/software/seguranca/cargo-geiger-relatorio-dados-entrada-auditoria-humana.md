---
id: software.seguranca.tranche17.001638
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

# Arquivar saída do `cargo-geiger` como evidência de revisão, não como certificado

## Em uma frase
O resultado pode compor um pacote de evidências junto do commit, dependências e observações da equipe que examinou as áreas de maior interesse.

## Por que importa
Guardar contexto permite que revisores posteriores saibam que versão foi medida e quais pontos foram realmente avaliados, sem interpretar a métrica como garantia.

## Como funciona
Anexe saída legível, commit auditado, toolchain e links para decisões; se usar formato de máquina suportado pela versão, valide o esquema antes de automação.

## Exemplo
Uma release pode arquivar o resumo das estatísticas e a lista de módulos revisados na mesma trilha do SBOM e das evidências de build.

## Limites e trade-offs
O próprio relatório não substitui revisão humana de código, assinatura do artefato nem verificação de vulnerabilidades conhecidas nas dependências.

## Como verificar
Confirme que o relatório é do commit final, que o comando e versão estão registrados e que achados relevantes apontam para revisão concreta.

## Conexões
- [[cargo-geiger-comparacao-crates-normalizada-toolchain]] — Comparar relatórios `cargo-geiger` com toolchain, features e grafo fixos.
- [[cargo-geiger-complementar-cargo-audit-clippy-miri]] — Combinar `cargo-geiger` com auditoria de advisories e testes de comportamento inseguro.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
