---
id: software.seguranca.tranche17.001629
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
fontes: ["https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-record-violation", "https://mozilla.github.io/cargo-vet/audit-entries.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo vet record-violation`: registrar que uma versão contradiz uma auditoria

## Em uma frase
O comando `record-violation` declara versões de crate que violam critérios alegados por auditorias ou exemptions existentes.

## Por que importa
Quando uma falha é descoberta depois, a base local pode precisar impedir que um registro antigo continue legitimando conteúdo incompatível.

## Como funciona
Documente evidência, versão e critério contradito, avalie os registros que dependem dessa confiança e incorpore o evento em uma mudança revisada.

## Exemplo
Se uma investigação demonstra que uma versão específica viola o critério de uma auditoria, registre a violação e revise consumidores que ainda usam aquela versão.

```text
cargo vet record-violation
```

## Limites e trade-offs
Registrar uma violação não corrige a crate nem atualiza automaticamente todos os sistemas consumidores de auditorias compartilhadas.

## Como verificar
Rode o check com a violação registrada, confirme que certificados conflitantes deixam de satisfazer a policy e mantenha referência à investigação original.

## Conexões
- [[cargo-vet-certify-record-audit-trilha-versao]] — `cargo vet certify`: registrar uma auditoria ligada à versão revisada.
- [[cargo-vet-exemptions-backlog-diferencial-seguranca]] — Exemptions no `cargo-vet`: backlog explícito, não selo de segurança.

## Fontes
- [Cargo Vet — Commands: record-violation](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-record-violation) — declaração de versões que violam critérios; consultado em 2026-10-04.
- [Cargo Vet — Audit Entries](https://mozilla.github.io/cargo-vet/audit-entries.html) — semântica de `violation` e conflito com exemptions; consultado em 2026-10-04.
