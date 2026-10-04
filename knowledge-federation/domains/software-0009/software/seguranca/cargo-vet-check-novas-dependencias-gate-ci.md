---
id: software.seguranca.tranche17.001623
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
fontes: ["https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-check", "https://mozilla.github.io/cargo-vet/how-it-works.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `cargo vet check`: detectar código de terceiro novo no grafo de build

## Em uma frase
O comando padrão `cargo vet` verifica o grafo atualizado e aponta quando código de terceiro não está coberto por auditorias aceitas.

## Por que importa
Uma dependência transitiva pode mudar mesmo sem edição direta do manifest; rodar o check sobre o lockfile evita aprovar silenciosamente novos bytes de terceiros.

## Como funciona
Execute a checagem em CI após atualizar o grafo, analise as sugestões e associe o resultado ao commit e à versão das ferramentas.

## Exemplo
Um pipeline pode comparar a branch do pull request, falhar quando o check exigir auditoria e anexar as sugestões para resolução pelo responsável.

```text
cargo vet check
```

## Limites e trade-offs
A checagem confirma cobertura segundo os registros e a política configurados; ela não executa uma auditoria de código em nome da equipe.

## Como verificar
Introduza uma crate de teste sem auditoria e verifique que o CI aponta o pacote e oferece caminho de correção, sem aprovar por default.

## Conexões
- [[cargo-vet-init-supply-chain-exemptions-iniciais]] — `cargo vet init`: inicializar supply chain sem confundir exemptions com auditorias.
- [[cargo-vet-criteria-safe-to-run-safe-to-deploy]] — Critérios do `cargo-vet`: definir o que uma auditoria precisa demonstrar.

## Fontes
- [Cargo Vet — Commands: check](https://mozilla.github.io/cargo-vet/commands.html#cargo-vet-check) — comportamento do comando padrão e falhas por auditoria ausente; consultado em 2026-10-04.
- [Cargo Vet — How it Works](https://mozilla.github.io/cargo-vet/how-it-works.html) — como o grafo de dependências é comparado com audits/imports/policy; consultado em 2026-10-04.
