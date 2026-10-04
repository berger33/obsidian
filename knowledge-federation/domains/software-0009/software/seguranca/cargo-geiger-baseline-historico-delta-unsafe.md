---
id: software.seguranca.tranche17.001635
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

# Usar baseline de `cargo-geiger` para acompanhar mudanças sem premiar dívida antiga

## Em uma frase
A comparação de resultados ao longo do tempo pode revelar aumento de `unsafe`, desde que o baseline seja tratado como referência e não como aprovação.

## Por que importa
Projetos maduros podem ter muitos usos legados; bloquear qualquer contagem absoluta pode ocultar novas áreas em vez de orientar sua revisão incremental.

## Como funciona
Armazene relatórios por commit, compare mesma versão da ferramenta e mesmo grafo e investigue cada aumento associado a nova dependência ou módulo.

## Exemplo
Uma pipeline pode anexar estatísticas da branch ao pull request e exigir justificativa quando a mudança introduzir novos pontos `unsafe`.

## Limites e trade-offs
Mudança de compilador, feature ou resolução pode alterar o resultado sem mudança direta de código; o delta não mede severidade nem qualidade de encapsulamento.

## Como verificar
Reexecute o baseline com toolchain e lockfile comparáveis e explique diferenças de grafo antes de atribuir aumento ao código alterado.

## Conexões
- [[cargo-geiger-uso-unsafe-necessario-encapsulamento]] — Interpretar `unsafe` no contexto: FFI, abstrações de baixo nível e encapsulamento seguro.
- [[cargo-geiger-install-locked-openssl-vendored]] — Instalar `cargo-geiger` com Cargo lockado e escolher a biblioteca OpenSSL.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
