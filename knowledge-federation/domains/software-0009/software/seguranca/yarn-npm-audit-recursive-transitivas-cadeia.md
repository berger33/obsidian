---
id: software.seguranca.tranche17.001663
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
fontes: ["https://yarnpkg.com/cli/npm/audit#options", "https://yarnpkg.com/cli/why"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `yarn npm audit --recursive`: incluir dependências transitivas no relatório

## Em uma frase
A opção `--recursive` amplia a busca a dependências diretas e transitivas do grafo instalado, em vez da visão direta padrão.

## Por que importa
Um pacote vulnerável pode ser introduzido por vários níveis de dependências e não aparecer no `package.json` do aplicativo.

## Como funciona
Use a saída completa para identificar a cadeia e complemente-a com `yarn why` para localizar o pacote pai responsável pela versão selecionada.

## Exemplo
Em uma revisão de release, execute `yarn npm audit --recursive --json` e associe cada advisory ao caminho transitivo e ao workspace de origem.

```text
yarn npm audit --recursive --json
```

## Limites e trade-offs
O relatório informa advisories conhecidos, mas não prova que aplicação executa a função atingida; paths podem mudar após resolução.

## Como verificar
Compare a lista de advisories com a árvore de `yarn why`, confira versão e lockfile e rode novamente após atualizar a dependência pai.

## Conexões
- [[yarn-npm-audit-all-workspaces-monorepo]] — `yarn npm audit --all`: ampliar a auditoria aos workspaces do monorepo.
- [[yarn-npm-audit-environment-production-devdeps]] — `--environment production`: focar dependências de runtime sem apagar contexto de build.

## Fontes
- [Yarn — opção `--recursive`](https://yarnpkg.com/cli/npm/audit#options) — inclusão de dependências transitivas no audit; consultado em 2026-10-04.
- [Yarn — `yarn why`](https://yarnpkg.com/cli/why) — inspeção de quem depende de um pacote no grafo instalado; consultado em 2026-10-04.
