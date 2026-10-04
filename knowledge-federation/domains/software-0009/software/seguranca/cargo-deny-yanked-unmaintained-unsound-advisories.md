---
id: software.seguranca.tranche17.001614
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html", "https://embarkstudios.github.io/cargo-deny/checks/advisories/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Separar vulnerabilidade, crate `yanked`, descontinuidade e advisory de soundness

## Em uma frase
O check de advisories distingue avisos de segurança de crates yanked, não mantidas ou marcadas como unsound, permitindo política diferenciada por categoria.

## Por que importa
Esses sinais representam riscos distintos: uma versão removida, ausência de manutenção e problema de soundness exigem triagem e remediação diferentes.

## Como funciona
Defina comportamento explícito para cada grupo em `[advisories]`, revise defaults da versão instalada e evite reduzir tudo a um único nível genérico de severidade.

## Exemplo
Uma equipe pode bloquear advisories de vulnerabilidade, alertar sobre crate yanked e priorizar crates não mantidas que sejam dependências diretas.

```text
cargo deny check advisories
```

## Limites e trade-offs
As opções e defaults evoluem por versão do `cargo-deny`; uma categoria pode ser marcada sem demonstrar que o produto exercita o caminho relacionado.

## Como verificar
Consulte a referência correspondente à versão fixada, inspecione o ID do advisory e teste a policy com fixtures seguras ou lockfiles de exemplo.

## Conexões
- [[cargo-deny-ignores-advisory-expiry-reason-escopo]] — Exceções em `[advisories]`: ID, motivo, escopo e expiração.
- [[cargo-deny-licencas-spdx-allowlist-exceptions]] — Política de licenças em `cargo-deny`: expressões SPDX e exceções explícitas.

## Fontes
- [`cargo-deny` — configuração de advisories](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html) — policies distintas para vulnerabilidades, yanked, unmaintained e unsound; consultado em 2026-10-04.
- [`cargo-deny` — Advisories](https://embarkstudios.github.io/cargo-deny/checks/advisories/) — categorias de findings emitidas pelo check de advisories; consultado em 2026-10-04.
