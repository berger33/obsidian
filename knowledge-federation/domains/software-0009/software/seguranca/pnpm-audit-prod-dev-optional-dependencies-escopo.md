---
id: software.seguranca.tranche17.001652
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
fontes: ["https://pnpm.io/cli/audit#--prod--p", "https://pnpm.io/cli/audit#--no-optional"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Delimitar `pnpm audit` por produção, desenvolvimento e dependências opcionais

## Em uma frase
`--prod` e `--dev` permitem consultar subconjuntos; `--no-optional` exclui dependências opcionais da auditoria solicitada.

## Por que importa
Uma vista por runtime auxilia priorização, enquanto ferramentas de build ou dependências opcionais podem continuar relevantes para a cadeia de entrega.

## Como funciona
Gere a vista de produção e uma visão completa em jobs distintos, rotule escopo no artefato e não elimine dependências de desenvolvimento do inventário total.

## Exemplo
Uma política pode usar `pnpm audit --prod` para exposição de produção e executar o comando sem filtro para verificar ferramentas e dependências de desenvolvimento.

```text
pnpm audit --prod
```

## Limites e trade-offs
Filtrar escopo não altera o advisory e não demonstra que uma dependência omitida seja inofensiva; build scripts também podem ser executados na CI.

## Como verificar
Compare relatórios com e sem filtros, registre as classes excluídas e confira que o lockfile e SBOM incluem todo o conjunto resolvido.

## Conexões
- [[pnpm-audit-bulk-advisory-ghsa-pnpm-v11]] — `pnpm audit` v11+: Bulk Advisory e uso de IDs GHSA.
- [[pnpm-audit-json-patched-versions-null]] — `pnpm audit --json`: diferenciar advisories corrigíveis de sem versão corrigida.

## Fontes
- [pnpm — `pnpm audit`](https://pnpm.io/cli/audit#--prod--p) — flags `--prod`, `--dev` e `--no-optional` para delimitar o audit; consultado em 2026-10-04.
- [pnpm — `--no-optional`](https://pnpm.io/cli/audit#--no-optional) — opção para excluir explicitamente `optionalDependencies` da auditoria; consultado em 2026-10-04.
