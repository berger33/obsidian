---
id: software.seguranca.tranche17.001662
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
fontes: ["https://yarnpkg.com/cli/npm/audit#options", "https://yarnpkg.com/features/workspaces"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `yarn npm audit --all`: ampliar a auditoria aos workspaces do monorepo

## Em uma frase
A opção `--all` solicita a auditoria das dependências de todos os workspaces em vez de somente o workspace ativo.

## Por que importa
Bibliotecas internas, aplicativos e ferramentas de build podem compartilhar dependências vulneráveis mesmo que apenas um workspace seja executado localmente.

## Como funciona
Inclua `--all` em uma execução de CI do monorepo e preserve qual projeto introduz cada achado para direcionar a correção ao owner certo.

## Exemplo
Um job noturno pode executar a auditoria global e gerar relatório separado por workspace, facilitando encontrar dependências mantidas por equipes distintas.

```text
yarn npm audit --all
```

## Limites e trade-offs
`--all` não implica necessariamente varrer dependências transitivas; para isso a documentação aponta a opção `--recursive`.

## Como verificar
Rode auditoria em um monorepo de teste com advisories distintos por workspace e confirme que todos aparecem com o escopo selecionado.

## Conexões
- [[yarn-npm-audit-escopo-direto-workspace-default]] — `yarn npm audit`: escopo padrão limitado ao workspace ativo.
- [[yarn-npm-audit-recursive-transitivas-cadeia]] — `yarn npm audit --recursive`: incluir dependências transitivas no relatório.

## Fontes
- [Yarn — opção `--all`](https://yarnpkg.com/cli/npm/audit#options) — alcance da auditoria a todos os workspaces; consultado em 2026-10-04.
- [Yarn — Workspaces](https://yarnpkg.com/features/workspaces) — estrutura de workspaces e execução no monorepo; consultado em 2026-10-04.
