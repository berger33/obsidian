---
id: software.seguranca.tranche17.001630
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
fontes: ["https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-add-exemption", "https://mozilla.github.io/cargo-vet/setup.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Exemptions no `cargo-vet`: backlog explícito, não selo de segurança

## Em uma frase
Exemptions podem permitir começar sem auditar todo o grafo legado, mas representam código ainda não coberto por uma auditoria aceita.

## Por que importa
Se a lista cresce sem responsável, a exceção temporária vira um atalho permanente e reduz a capacidade de notar novas mudanças na cadeia.

## Como funciona
Trate exemptions como backlog: atribua responsável, defina prioridade e substitua cada entrada por auditoria diferencial ou evidência compartilhada confiável.

## Exemplo
Gere um relatório periódico de exemptions, escolha uma crate por risco e remova a exceção somente após registrar o critério revisado.

```text
cargo vet check
```

## Limites e trade-offs
A remoção automática de exemptions para fazer o check passar não demonstra que houve análise; a própria documentação recomenda evitar esse atalho.

## Como verificar
Compare o tamanho da lista antes e depois, revise entradas novas e confirme que o check não passa apenas porque exceções foram ampliadas.

## Conexões
- [[cargo-vet-record-violation-integridade-audits]] — `cargo vet record-violation`: registrar que uma versão contradiz uma auditoria.

## Fontes
- [Cargo Vet — Commands: add-exemption/regenerate](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-add-exemption) — comandos para registrar/excluir exemptions; consultado em 2026-10-04.
- [Cargo Vet — Setup](https://mozilla.github.io/cargo-vet/setup.html) — significado da aprovação inicial baseada em exemptions e orientação para reduzi-las; consultado em 2026-10-04.
