---
id: software.seguranca.tranche17.001656
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
fontes: ["https://pnpm.io/cli/audit#auditignore", "https://pnpm.io/cli/audit#auditignoreprune"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `audit.ignore` no pnpm: allowlist GHSA com justificativa e limpeza de entradas antigas

## Em uma frase
A configuração `audit.ignore` aceita IDs GHSA e `audit.ignorePrune` pode remover entradas que não aparecem mais no relatório quando a correção roda.

## Por que importa
Exceções sem rastreamento perdem relevância quando dependências mudam; podar ou revisar entradas antigas reduz ruído e permissões persistentes.

## Como funciona
Exija owner, motivo e prazo em cada exceção, use `ignorePrune` conscientemente e confira o resumo que distingue advisories ignorados de uma auditoria limpa.

## Exemplo
No CI, valide a lista `audit.ignore` contra o registro de risco interno e abra revisão quando um ID sair do relatório ou mudar de faixa.

```text
pnpm audit --json
```

## Limites e trade-offs
Uma exceção suprime o reporte do advisory configurado; não neutraliza a falha técnica nem substitui mitigação ou versão corrigida.

## Como verificar
Compare saída normal e saída com ignores, confirme que todos os IDs são GHSA válidos e revise entradas removidas pelo prune.

## Conexões
- [[pnpm-audit-fix-update-lockfile-interativo]] — `pnpm audit --fix=update` e modo interativo: escolher a forma da remediação.
- [[pnpm-audit-level-impressao-severidade-policy]] — `--audit-level` no pnpm: controlar severidade exibida sem perder dados brutos.

## Fontes
- [pnpm — `audit.ignore`](https://pnpm.io/cli/audit#auditignore) — IDs GHSA permitidos e comportamento da allowlist; consultado em 2026-10-04.
- [pnpm — `audit.ignorePrune`](https://pnpm.io/cli/audit#auditignoreprune) — remoção de ignores que não aparecem mais no relatório; consultado em 2026-10-04.
