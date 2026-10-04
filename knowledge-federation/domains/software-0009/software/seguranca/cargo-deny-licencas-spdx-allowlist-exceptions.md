---
id: software.seguranca.tranche17.001615
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/licenses/cfg.html", "https://spdx.org/licenses/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Política de licenças em `cargo-deny`: expressões SPDX e exceções explícitas

## Em uma frase
O check de licenças compara expressões identificadas para crates com uma allowlist baseada em identificadores SPDX e exceções por pacote.

## Por que importa
Uma dependência pode ser tecnicamente segura e ainda violar requisitos de distribuição; a regra torna a revisão de licenciamento parte verificável do grafo.

## Como funciona
Escolha uma lista permitida com a área responsável, use exceções por crate para desvios aprovados e trate expressões compostas e cláusulas `WITH` com precisão.

## Exemplo
Em `deny.toml`, permita apenas identificadores aprovados e abra uma exceção nomeada para uma crate cuja expressão tenha sido avaliada pelo jurídico.

```text
cargo deny check licenses
```

## Limites e trade-offs
A ferramenta identifica e compara metadados de licença, não oferece aconselhamento jurídico e pode exigir clarificação quando o texto da licença é ambíguo.

## Como verificar
Compare a licença declarada e os arquivos LICENSE da dependência com a decisão registrada; verifique que uma crate não permitida realmente faz o check falhar.

## Conexões
- [[cargo-deny-yanked-unmaintained-unsound-advisories]] — Separar vulnerabilidade, crate `yanked`, descontinuidade e advisory de soundness.
- [[cargo-deny-license-clarifications-hash-confidence]] — Clarificações de licença no `cargo-deny`: expressão, arquivo e hash.

## Fontes
- [`cargo-deny` — configuração de licenças](https://embarkstudios.github.io/cargo-deny/checks/licenses/cfg.html) — identificadores SPDX, allowlist e exceções por crate; consultado em 2026-10-04.
- [SPDX — License List](https://spdx.org/licenses/) — identificadores padronizados usados para expressões de licenças; consultado em 2026-10-04.
