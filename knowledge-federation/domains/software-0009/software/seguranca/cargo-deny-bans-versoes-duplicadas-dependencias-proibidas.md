---
id: software.seguranca.tranche17.001617
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html", "https://doc.rust-lang.org/cargo/commands/cargo-tree.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `[bans]` no `cargo-deny`: dependências proibidas e versões múltiplas

## Em uma frase
O check de bans pode bloquear crates selecionadas e sinalizar múltiplas versões da mesma dependência presentes no grafo resolvido.

## Por que importa
Versões duplicadas aumentam superfície e custo de atualização; uma crate banida pode representar uma implementação incompatível com a política técnica do projeto.

## Como funciona
Configure padrões específicos, explique substituições preferidas e ajuste exceções apenas para conflitos transitivos compreendidos, evitando banir pelo nome sem mapear consumidores.

## Exemplo
Um repositório pode rejeitar uma biblioteca depreciada e alertar quando uma dependência transitiva introduz uma segunda versão, abrindo tarefa para convergência.

```text
cargo deny check bans
```

## Limites e trade-offs
Duplicidade não significa automaticamente vulnerabilidade; resolver versões pode exigir coordenação upstream e uma regra agressiva pode bloquear builds válidos.

## Como verificar
Inspecione a cadeia afetada com a árvore Cargo, aplique a regra em CI e confirme que exceções listam exatamente pacote e versão pretendidos.

## Conexões
- [[cargo-deny-license-clarifications-hash-confidence]] — Clarificações de licença no `cargo-deny`: expressão, arquivo e hash.
- [[cargo-deny-sources-registries-git-allowlist]] — `[sources]` no `cargo-deny`: limitar registries e dependências Git.

## Fontes
- [`cargo-deny` — configuração de bans](https://embarkstudios.github.io/cargo-deny/checks/bans/cfg.html) — crates banidas, versões múltiplas, padrões e exceções; consultado em 2026-10-04.
- [Cargo Reference — `cargo tree`](https://doc.rust-lang.org/cargo/commands/cargo-tree.html) — inspeção dos caminhos diretos e transitivos do grafo de dependências; consultado em 2026-10-04.
