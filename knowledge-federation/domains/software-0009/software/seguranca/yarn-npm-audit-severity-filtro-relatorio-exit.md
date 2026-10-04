---
id: software.seguranca.tranche17.001665
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
fontes: ["https://yarnpkg.com/cli/npm/audit#details", "https://yarnpkg.com/cli/npm/audit#options"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--severity` no Yarn: filtrar severidades exibidas e interpretar exit status

## Em uma frase
O Yarn permite selecionar severidade mínima para a tabela de auditoria, mas mantém código de saída não zero quando encontra relatório para o escopo selecionado.

## Por que importa
Um filtro de apresentação não deve ser interpretado como remoção de achados menores da árvore ou como autorização para ignorá-los sem política.

## Como funciona
Execute uma vista humana com o threshold escolhido e, em uma chamada separada, preserve `--json` para obter o fluxo NDJSON bruto; documente que qualquer report no escopo selecionado mantém exit code não zero.

## Exemplo
Um job pode imprimir `high` e acima para leitura rápida e executar uma segunda chamada `--json` para anexar o fluxo completo ao backlog de segurança.

```text
yarn npm audit --severity high
```

## Limites e trade-offs
O comportamento depende do escopo de workspace escolhido; filtro por severidade não altera a base de advisories nem corrige dependências.

## Como verificar
Use um fixture com achados de severidades distintas e confira tabela, JSON e exit status com as flags da versão instalada.

## Conexões
- [[yarn-npm-audit-environment-production-devdeps]] — `--environment production`: focar dependências de runtime sem apagar contexto de build.
- [[yarn-npm-audit-json-ndjson-registry-payload]] — Saída JSON/NDJSON no `yarn npm audit`: automação sem perder o relatório bruto.

## Fontes
- [Yarn — `--severity` e exit status](https://yarnpkg.com/cli/npm/audit#details) — filtro de tabela por severidade e código de saída quando há report; consultado em 2026-10-04.
- [Yarn — opções do audit](https://yarnpkg.com/cli/npm/audit#options) — valores e sintaxe da opção `--severity`; consultado em 2026-10-04.
