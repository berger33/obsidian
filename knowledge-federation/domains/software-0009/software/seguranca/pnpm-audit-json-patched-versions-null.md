---
id: software.seguranca.tranche17.001653
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
fontes: ["https://pnpm.io/cli/audit#--json", "https://pnpm.io/cli/audit#--fix"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `pnpm audit --json`: diferenciar advisories corrigíveis de sem versão corrigida

## Em uma frase
O formato JSON expõe `patched_versions`; quando seu valor é `null`, a documentação indica que não há resolução publicada para aquele advisory.

## Por que importa
A equipe não deve prometer atualização automática quando o ecossistema ainda não oferece versão corrigida, e precisa manter mitigação provisória visível.

## Como funciona
Parseie o campo sem converter null em lista vazia, crie estado de triagem separado e reavalie a dependência quando o mantenedor publicar correção.

## Exemplo
Um dashboard pode rotular casos com `patched_versions: null` como sem versão corrigida conhecida e encaminhar o risco a owner da aplicação.

```text
pnpm audit --json
```

## Limites e trade-offs
A informação reflete o feed consultado no instante da execução; uma versão corrigida pode surgir depois ou depender de atualização de intervalo.

## Como verificar
Valide o parser com JSON real do CLI, preserve a distinção entre null e array de versões e registre data da consulta.

## Conexões
- [[pnpm-audit-prod-dev-optional-dependencies-escopo]] — Delimitar `pnpm audit` por produção, desenvolvimento e dependências opcionais.
- [[pnpm-audit-fix-overrides-workspace-yaml]] — `pnpm audit --fix`: remediar com `overrides` no arquivo de workspace.

## Fontes
- [pnpm — `pnpm audit` JSON](https://pnpm.io/cli/audit#--json) — campos JSON do relatório, incluindo `patched_versions` nulo; consultado em 2026-10-04.
- [pnpm — `pnpm audit` remediação](https://pnpm.io/cli/audit#--fix) — semântica de versão corrigida e resultado do fluxo de fix; consultado em 2026-10-04.
