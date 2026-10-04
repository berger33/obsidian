---
id: software.seguranca.tranche17.001666
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
fontes: ["https://yarnpkg.com/cli/npm/audit#options", "https://yarnpkg.com/cli/npm/audit#details"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Saída JSON/NDJSON no `yarn npm audit`: automação sem perder o relatório bruto

## Em uma frase
Com `--json`, Yarn produz um fluxo NDJSON e passa a saída do registry de forma estruturada, permitindo parsing e armazenamento por execução.

## Por que importa
Automação baseada em texto de terminal costuma quebrar com mudança de versão; dados estruturados facilitam correlação com dependências e tickets.

## Como funciona
Armazene cada linha com commit, lockfile e versão do Yarn, valide parser e preserve stdout e exit status independentemente.

## Exemplo
Um job pode encaminhar o fluxo NDJSON a um coletor de findings sem transformar ausência de registros num sucesso quando a consulta falha.

```text
yarn npm audit --json
```

## Limites e trade-offs
A documentação informa que a resposta é recebida do registry; esquema e conteúdo podem variar, e JSON não determina se o alerta afeta o código.

## Como verificar
Teste parsing com relatório positivo, relatório vazio e erro de registry, mantendo evidência de qual caso ocorreu.

## Conexões
- [[yarn-npm-audit-severity-filtro-relatorio-exit]] — `--severity` no Yarn: filtrar severidades exibidas e interpretar exit status.
- [[yarn-npm-audit-exclude-packages-false-positive-policy]] — `--exclude` no Yarn: reduzir ruído com escopo de pacote documentado.

## Fontes
- [Yarn — `--json` NDJSON](https://yarnpkg.com/cli/npm/audit#options) — formato NDJSON documentado para automação; consultado em 2026-10-04.
- [Yarn — detalhes do registry](https://yarnpkg.com/cli/npm/audit#details) — resposta emitida pelo registry e comportamento de exit status; consultado em 2026-10-04.
