---
id: software.seguranca.tranche17.001661
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
fontes: ["https://yarnpkg.com/cli/npm/audit#details", "https://yarnpkg.com/features/workspaces"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `yarn npm audit`: escopo padrão limitado ao workspace ativo

## Em uma frase
A documentação do Yarn Berry informa que, por padrão, a auditoria verifica dependências diretas do workspace ativo, não todo monorepo transitivo.

## Por que importa
Um comando aparentemente único pode deixar outros workspaces ou dependências indiretas fora do relatório, criando cobertura diferente da equipe que lê o resultado.

## Como funciona
Declare se a policy cobre apenas o workspace atual, todos os workspaces ou a árvore transitiva, e execute as flags apropriadas no CI.

## Exemplo
Em um monorepo, faça um job por workspace sensível ou use `--all --recursive` para consolidar dependências diretas e transitivas de todos eles.

```text
yarn npm audit
```

## Limites e trade-offs
A saída reflete advisories do registry e pode incluir achados irrelevantes para o caminho de código usado pela aplicação.

## Como verificar
Compare o conjunto de workspaces e a árvore resolvida com o relatório e confira as flags que aparecem no comando do pipeline.

## Conexões
- [[yarn-npm-audit-all-workspaces-monorepo]] — `yarn npm audit --all`: ampliar a auditoria aos workspaces do monorepo.

## Fontes
- [Yarn — `yarn npm audit` details](https://yarnpkg.com/cli/npm/audit#details) — escopo default no workspace ativo e expansão por `--all`/`--recursive`; consultado em 2026-10-04.
- [Yarn — Workspaces](https://yarnpkg.com/features/workspaces) — modelo e enumeração de workspaces em monorepos; consultado em 2026-10-04.
