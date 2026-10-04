---
id: software.seguranca.tranche17.001608
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

# `cargo auditable`: metadados embutidos e limites da auditoria de binários Rust

## Em uma frase
Quando o programa é compilado com `cargo auditable`, `cargo audit bin` pode obter do executável as informações necessárias para uma auditoria mais completa.

## Por que importa
O inventário no artefato aproxima a verificação daquilo que realmente foi publicado, reduzindo dependência de um lockfile externo possivelmente diferente.

## Como funciona
Integre a instrumentação na cadeia de build, preserve proveniência do executável e associe o relatório ao digest; valide se a compilação de produção recebeu o recurso.

## Exemplo
Uma esteira pode gerar `app`, calcular seu digest, executar `cargo audit bin app` e arquivar os resultados junto ao manifesto da release.

```text
cargo audit bin ./dist/app
```

## Limites e trade-offs
A presença de metadados não corrige código vulnerável nem garante que todos os componentes fora do ecossistema Rust estejam representados no inventário.

## Como verificar
Confira a documentação de build do artefato, compare a árvore embutida com o lockfile de release e repita a auditoria sobre o mesmo digest distribuído.

## Conexões
- [[cargo-audit-bin-inventario-dependencias-binario-rust]] — `cargo audit bin`: leitura de dependências em binários Rust distribuídos.
- [[cargo-audit-fix-dry-run-remediacao-experimental]] — `cargo audit fix --dry-run`: avaliar remediação antes de alterar dependências.

## Fontes
- [RustSec `cargo-audit` — README oficial](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md) — relação entre `cargo audit bin`, metadados e precisão do inventário; consultado em 2026-10-04.
- [`cargo-auditable` — projeto oficial](https://github.com/rust-secure-code/cargo-auditable) — integração de build que incorpora informações de dependências em binários Rust; consultado em 2026-10-04.
