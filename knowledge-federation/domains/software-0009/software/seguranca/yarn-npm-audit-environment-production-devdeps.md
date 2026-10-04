---
id: software.seguranca.tranche17.001664
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
fontes: ["https://yarnpkg.com/cli/npm/audit#examples", "https://yarnpkg.com/cli/npm/audit#options"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--environment production`: focar dependências de runtime sem apagar contexto de build

## Em uma frase
A opção `--environment production` limita a auditoria às dependências de produção e exclui `devDependencies` da vista solicitada.

## Por que importa
Separar runtime ajuda priorizar risco em artefatos distribuídos, porém ferramentas usadas na CI podem executar código e continuar relevantes para segurança.

## Como funciona
Rotule o resultado como visão de produção e mantenha outra execução abrangendo todas as dependências para prevenir que riscos de build desapareçam.

## Exemplo
Gere uma auditoria `production` para release e um relatório completo na integração contínua, com owners distintos para runtime e cadeia de build.

```text
yarn npm audit --environment production
```

## Limites e trade-offs
A opção altera o escopo, não a severidade nem a existência do advisory; dependências excluídas não ficam corrigidas por serem dev-only.

## Como verificar
Compare ambos os relatórios e confira que o lockfile completo segue sendo analisado em algum estágio do pipeline.

## Conexões
- [[yarn-npm-audit-recursive-transitivas-cadeia]] — `yarn npm audit --recursive`: incluir dependências transitivas no relatório.
- [[yarn-npm-audit-severity-filtro-relatorio-exit]] — `--severity` no Yarn: filtrar severidades exibidas e interpretar exit status.

## Fontes
- [Yarn — opção `--environment`](https://yarnpkg.com/cli/npm/audit#examples) — seleção do ambiente production e exclusão de devDependencies; consultado em 2026-10-04.
- [Yarn — `yarn npm audit` options](https://yarnpkg.com/cli/npm/audit#options) — opções documentadas para delimitar o escopo do audit; consultado em 2026-10-04.
