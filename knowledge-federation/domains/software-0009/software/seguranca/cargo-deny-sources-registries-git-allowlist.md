---
id: software.seguranca.tranche17.001618
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/sources/cfg.html", "https://doc.rust-lang.org/cargo/reference/registries.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `[sources]` no `cargo-deny`: limitar registries e dependências Git

## Em uma frase
O check de fontes permite definir se registries e repositórios Git desconhecidos são aceitos, restringindo origens do grafo Cargo a locais aprovados.

## Por que importa
Uma crate com nome legítimo ainda pode vir de um registry ou URL inesperado; origem explícita ajuda a reduzir confusão e dependências não revisadas.

## Como funciona
Mantenha uma lista deliberada de fontes permitidas, registre por que cada registry é necessário e trate dependências Git por revisão imutável quando a política exigir.

## Exemplo
No pull request, introduza uma origem fictícia em um manifest de teste e confirme que a checagem bloqueia o download fora do registry permitido.

```text
cargo deny check sources
```

## Limites e trade-offs
A allowlist não autentica por si só o conteúdo de uma origem autorizada nem elimina comprometimento de credenciais ou conta do mantenedor.

## Como verificar
Revise os campos de `[sources]`, compare cada origem da resolução com a lista aprovada e rode o check após mudanças de registry.

## Conexões
- [[cargo-deny-bans-versoes-duplicadas-dependencias-proibidas]] — `[bans]` no `cargo-deny`: dependências proibidas e versões múltiplas.
- [[cargo-deny-target-features-grafo-resolucao-reprodutivel]] — Alvos e features na policy do `cargo-deny`: auditar o grafo que realmente será compilado.

## Fontes
- [`cargo-deny` — configuração de fontes](https://embarkstudios.github.io/cargo-deny/checks/sources/cfg.html) — registries, Git, fontes permitidas e política para origens desconhecidas; consultado em 2026-10-04.
- [Cargo Reference — Registries](https://doc.rust-lang.org/cargo/reference/registries.html) — origens de registries e configuração de fontes no ecossistema Cargo; consultado em 2026-10-04.
