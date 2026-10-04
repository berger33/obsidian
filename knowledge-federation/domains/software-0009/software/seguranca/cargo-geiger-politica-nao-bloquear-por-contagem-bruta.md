---
id: software.seguranca.tranche17.001640
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

# Evitar gate binário por contagem bruta de `unsafe` sem contexto de risco

## Em uma frase
Um limite numérico universal para operações `unsafe` ignora tamanho do projeto, padrões de encapsulamento e criticidade das invariantes revisadas.

## Por que importa
Gates cegos podem incentivar reescritas cosméticas ou suprimir relatório, em vez de ajudar a equipe a examinar mudanças que afetam memória e FFI.

## Como funciona
Prefira diff consciente, revisão de novos blocos e justificativas locais; use métricas agregadas como sinal para tendência e priorização, não aprovação automática.

## Exemplo
Uma policy pode exigir revisão de um aumento no módulo central de parsing e permitir crescimento em bindings gerados com justificativa e owner específico.

## Limites e trade-offs
Uma métrica contextual ainda depende de configuração correta e pode não capturar mudanças sem alteração de contagem, como mudança de invariantes.

## Como verificar
Teste a policy com mudanças de exemplo e confira que novos usos recebem revisão útil sem que uma queda numérica seja tratada como certificação.

## Conexões
- [[cargo-geiger-complementar-cargo-audit-clippy-miri]] — Combinar `cargo-geiger` com auditoria de advisories e testes de comportamento inseguro.

## Fontes
- [`cargo-geiger` — README publicado no Docs.rs](https://docs.rs/crate/cargo-geiger/latest/source/README.md) — uso do plugin Cargo, estatísticas de `unsafe`, instalação, intenção de auditoria e limitações reconhecidas pelo projeto; consultado em 2026-10-04.
- [The Rustonomicon — Meet Safe and Unsafe](https://doc.rust-lang.org/nomicon/meet-safe-and-unsafe.html) — distinção entre Safe Rust e Unsafe Rust, responsabilidades de invariantes e possíveis usos de operações unsafe; consultado em 2026-10-04.
