---
id: software.seguranca.tranche17.001613
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

# Exceções em `[advisories]`: ID, motivo, escopo e expiração

## Em uma frase
A configuração de advisories permite ignorar um identificador específico, registrar uma razão e restringir o efeito da exceção a crates selecionadas.

## Por que importa
Supressões sem prazo acumulam dívida invisível; `expiry` e `ignore-expiry` ajudam a transformar uma decisão temporária em item de revisão periódica.

## Como funciona
Prefira corrigir a dependência; se houver exceção, registre ID, crate afetada, justificativa verificável e expiração, e revise o diff quando o advisory mudar.

## Exemplo
Um pull request que adiciona uma exceção deve incluir evidência da análise de reachability e uma data de retorno, não apenas o status de CI desejado.

```text
cargo deny check advisories
```

## Limites e trade-offs
Uma razão em TOML não comprova que o código vulnerável seja inalcançável; a configuração pode ficar desatualizada quando o grafo ou features mudam.

## Como verificar
Execute o check com uma versão afetada e depois com a corrigida, confirme o escopo da exceção e teste que uma nova dependência não herda a permissão.

## Conexões
- [[cargo-deny-advisory-db-rustsec-atualizacao-offline]] — `cargo-deny check advisories`: fonte RustSec, cache local e atualidade dos dados.
- [[cargo-deny-yanked-unmaintained-unsound-advisories]] — Separar vulnerabilidade, crate `yanked`, descontinuidade e advisory de soundness.

## Fontes
- [`cargo-deny` — configuração de advisories](https://embarkstudios.github.io/cargo-deny/checks/advisories/cfg.html) — IDs ignorados, razões, expiração e escopo por crate/versão; consultado em 2026-10-04.
- [`cargo-deny` — Advisories](https://embarkstudios.github.io/cargo-deny/checks/advisories/) — comportamento do check de advisories no grafo Cargo; consultado em 2026-10-04.
