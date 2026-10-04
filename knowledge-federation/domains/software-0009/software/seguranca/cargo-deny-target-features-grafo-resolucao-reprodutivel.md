---
id: software.seguranca.tranche17.001619
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
fontes: ["https://embarkstudios.github.io/cargo-deny/checks/cfg.html", "https://doc.rust-lang.org/cargo/reference/features.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Alvos e features na policy do `cargo-deny`: auditar o grafo que realmente será compilado

## Em uma frase
A configuração de grafo pode definir alvos e features considerados, afetando quais dependências transitivas entram nas verificações de policy.

## Por que importa
Uma auditoria feita apenas para o alvo padrão pode omitir crates ativadas em outra plataforma ou por uma feature usada em produção.

## Como funciona
Espelhe a matriz de compilação do produto na configuração do check, identifique combinações relevantes e mantenha configurações específicas documentadas quando o conjunto divergir.

## Exemplo
Se a aplicação publica Linux e macOS, execute verificações sobre os dois alvos suportados e compare o inventário resolvido antes de aprovar uma exceção.

```text
cargo deny check
```

## Limites e trade-offs
Ativar todas as features pode produzir combinações que o produto nunca usa; auditar uma matriz reduzida pode deixar caminhos de build sem cobertura.

## Como verificar
Inspecione as opções de grafo da versão fixada e confirme em CI que cada alvo de release aparece em uma execução do check.

## Conexões
- [[cargo-deny-sources-registries-git-allowlist]] — `[sources]` no `cargo-deny`: limitar registries e dependências Git.
- [[cargo-deny-github-action-ci-review-policy]] — Executar `cargo-deny` em CI: configuração como código e feedback de pull request.

## Fontes
- [`cargo-deny` — configuração global do grafo](https://embarkstudios.github.io/cargo-deny/checks/cfg.html) — targets, features e opções que determinam quais crates entram nos checks; consultado em 2026-10-04.
- [Cargo Reference — Features](https://doc.rust-lang.org/cargo/reference/features.html) — resolução de features e dependências condicionais no build Cargo; consultado em 2026-10-04.
