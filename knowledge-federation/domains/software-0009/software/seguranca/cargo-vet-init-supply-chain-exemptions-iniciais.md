---
id: software.seguranca.tranche17.001622
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
fontes: ["https://mozilla.github.io/cargo-vet/setup.html", "https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-init"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo vet init`: inicializar supply chain sem confundir exemptions com auditorias

## Em uma frase
O comando `cargo vet init` cria metadados de política e pode colocar dependências existentes em uma lista inicial de exemptions para facilitar adoção gradual.

## Por que importa
Um bootstrap que passa imediatamente não significa que todas as crates antigas foram auditadas; documentar o backlog impede que exceções sejam tratadas como certificados.

## Como funciona
Versione `config.toml` e `audits.toml` em `supply-chain/`, reduza exemptions com auditorias reais ao longo do tempo e revise alterações da lista.

## Exemplo
Depois de `cargo vet init`, use o relatório para escolher uma dependência prioritária e substitua a exemption correspondente por uma auditoria explícita.

```text
cargo vet init
```

## Limites e trade-offs
O estado inicial pode ser permissivo em relação ao passado e precisa de governança para não se tornar uma aprovação permanente sem revisão.

## Como verificar
Procure dependências sem registro de auditoria, conte exemptions por versão e confirme que pull requests novos acionam `cargo vet check`.

## Conexões
- [[cargo-vet-modelo-auditoria-terceiros-criterios-rust]] — `cargo-vet`: registrar auditorias de código Rust de terceiros junto ao projeto.
- [[cargo-vet-check-novas-dependencias-gate-ci]] — `cargo vet check`: detectar código de terceiro novo no grafo de build.

## Fontes
- [Cargo Vet — Setup](https://mozilla.github.io/cargo-vet/setup.html) — efeito de `cargo vet init` sobre `supply-chain/`, `config.toml` e exemptions; consultado em 2026-10-04.
- [Cargo Vet — Commands: init](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-init) — comando de inicialização e opções suportadas; consultado em 2026-10-04.
