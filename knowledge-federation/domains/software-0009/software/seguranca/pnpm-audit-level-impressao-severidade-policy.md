---
id: software.seguranca.tranche17.001657
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
fontes: ["https://pnpm.io/cli/audit#--audit-level-severity", "https://pnpm.io/cli/audit#--json"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--audit-level` no pnpm: controlar severidade exibida sem perder dados brutos

## Em uma frase
A opção `--audit-level` imprime advisories a partir da severidade selecionada; a configuração equivalente pode ficar no bloco `audit` do workspace.

## Por que importa
Filtros de apresentação podem reduzir ruído, porém um relatório filtrado não deve substituir arquivo bruto usado para a fila de risco.

## Como funciona
Defina o nível para visualização ou policy, armazene também JSON sem filtros quando necessário e documente a diferença entre exibição e bloqueio da pipeline.

## Exemplo
Uma revisão executa saída legível com `--audit-level high` e anexa JSON completo para que achados menores não desapareçam do histórico.

```text
pnpm audit --audit-level high
```

## Limites e trade-offs
A documentação descreve quais linhas são impressas; comportamento de saída e defaults devem ser confirmados para a versão do pnpm fixada.

## Como verificar
Execute com níveis diferentes sobre o mesmo lockfile, compare relatórios e observe o status de saída em uma fixture conhecida.

## Conexões
- [[pnpm-audit-ignore-ghsa-governanca-prune]] — `audit.ignore` no pnpm: allowlist GHSA com justificativa e limpeza de entradas antigas.
- [[pnpm-audit-registry-errors-nao-mascarar-falha]] — `--ignore-registry-errors`: não confundir indisponibilidade do serviço com resultado limpo.

## Fontes
- [pnpm — `--audit-level`](https://pnpm.io/cli/audit#--audit-level-severity) — filtro de severidade que controla quais linhas são impressas; consultado em 2026-10-04.
- [pnpm — `pnpm audit --json`](https://pnpm.io/cli/audit#--json) — formato bruto estruturado para preservar achados além da vista filtrada; consultado em 2026-10-04.
