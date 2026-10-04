---
id: software.seguranca.tranche17.001655
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
fontes: ["https://pnpm.io/cli/audit#--fix", "https://pnpm.io/cli/audit#--interactive--i"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `pnpm audit --fix=update` e modo interativo: escolher a forma da remediação

## Em uma frase
A partir de pnpm 11, `--fix=update` atualiza o lockfile em vez de gravar overrides; `--interactive` permite escolher advisories associados ao fix.

## Por que importa
A equipe pode preferir atualizar a resolução explícita em vez de manter regras de override, mas cada mudança tem impacto distinto no grafo.

## Como funciona
Selecione a modalidade deliberadamente, revise diffs do lockfile e preserve o registro de quais vulnerabilidades foram escolhidas ou adiadas.

## Exemplo
Em branch de manutenção, use modo interativo para selecionar correções aceitas e gere diff legível de `pnpm-lock.yaml` antes de submeter revisão.

```text
pnpm audit --fix=update --interactive
```

## Limites e trade-offs
A opção interativa só é válida com `--fix`; atualização do lockfile pode exigir que o pacote pai amplie sua faixa e não resolver todo advisory.

## Como verificar
Confira a versão de pnpm que introduziu as opções, examine versões selecionadas e rode auditoria e testes após a modificação.

## Conexões
- [[pnpm-audit-fix-overrides-workspace-yaml]] — `pnpm audit --fix`: remediar com `overrides` no arquivo de workspace.
- [[pnpm-audit-ignore-ghsa-governanca-prune]] — `audit.ignore` no pnpm: allowlist GHSA com justificativa e limpeza de entradas antigas.

## Fontes
- [pnpm — `pnpm audit --fix=update`](https://pnpm.io/cli/audit#--fix) — modo de atualização do lockfile e interatividade a partir de v11; consultado em 2026-10-04.
- [pnpm — `pnpm audit --interactive`](https://pnpm.io/cli/audit#--interactive--i) — seleção interativa de advisories durante remediação; consultado em 2026-10-04.
