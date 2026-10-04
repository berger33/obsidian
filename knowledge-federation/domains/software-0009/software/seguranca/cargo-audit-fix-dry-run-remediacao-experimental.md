---
id: software.seguranca.tranche17.001609
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
fontes: ["https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md#cargo-audit-fix-subcommand", "https://crates.io/crates/cargo-audit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo audit fix --dry-run`: avaliar remediação antes de alterar dependências

## Em uma frase
A funcionalidade experimental `cargo audit fix` precisa ser habilitada na instalação pela feature `fix`; ela pode alterar requisitos em `Cargo.toml`, e `--dry-run` mostra uma prévia.

## Por que importa
Atualizações automáticas podem alterar resolução, compatibilidade e comportamento; revisar a proposta antes de tocar manifestos evita transformar um advisory em regressão não analisada.

## Como funciona
Para experimentar, instale `cargo-audit` com `--features=fix`, rode a prévia em branch descartável, compare a mudança com compatibilidade e testes e aplique qualquer atualização como alteração revisada de dependências.

## Exemplo
Gere uma prévia de correção, salve a saída no ticket e só depois decida se a versão sugerida é compatível com o contrato do serviço.

```text
cargo install cargo-audit --locked --features=fix
cargo audit fix --dry-run
```

## Limites e trade-offs
A ferramenta é descrita como experimental e pode não encontrar atualização compatível; um `dry-run` não prova que a correção compila ou resolve o risco.

## Como verificar
Revise o diff de `Cargo.toml` e `Cargo.lock`, execute testes e rode novamente `cargo audit` após aplicar uma atualização aprovada.

## Conexões
- [[cargo-auditable-metadados-embed-binario-limites]] — `cargo auditable`: metadados embutidos e limites da auditoria de binários Rust.
- [[cargo-audit-ci-audit-check-agendamento-falha]] — `cargo-audit` em CI: política de falha, atualização da base e trilha do relatório.

## Fontes
- [RustSec `cargo-audit` — subcomando experimental `fix`](https://github.com/RustSec/rustsec/blob/main/cargo-audit/README.md#cargo-audit-fix-subcommand) — feature de instalação, mutações de manifest e prévia `--dry-run`; consultado em 2026-10-04.
- [Cargo Registry — `cargo-audit`](https://crates.io/crates/cargo-audit) — pacote e opções de instalação do CLI RustSec usado para habilitar a feature experimental; consultado em 2026-10-04.
