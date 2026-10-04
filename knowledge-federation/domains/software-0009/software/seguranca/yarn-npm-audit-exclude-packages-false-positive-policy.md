---
id: software.seguranca.tranche17.001667
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
fontes: ["https://yarnpkg.com/cli/npm/audit#options", "https://yarnpkg.com/configuration/yarnrc#npmAuditExcludePackages"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--exclude` no Yarn: reduzir ruído com escopo de pacote documentado

## Em uma frase
A opção `--exclude` pode retirar pacotes selecionados do relatório e também pode ser configurada como `npmAuditExcludePackages`.

## Por que importa
Exclusões ajudam em falsos positivos ou ambientes específicos, mas sem justificativa podem ocultar dependências que voltam a ser alcançáveis.

## Como funciona
Prefira padrões estreitos, registre a razão, mantenha owner e revise a lista quando dependências, workspaces ou ambientes mudarem.

## Exemplo
Ao excluir pacote de uma vista específica, anexe evidência de que ele não participa daquele ambiente e mantenha uma auditoria integral em outro job.

```text
yarn npm audit --exclude pacote-interno
```

## Limites e trade-offs
Excluir um pacote apenas altera a auditoria; não remove a dependência do lockfile nem impede que o código seja incluído em outra configuração.

## Como verificar
Compare resultados com e sem `--exclude`, valide o padrão de pacote e confirme que o inventário completo ainda está visível.

## Conexões
- [[yarn-npm-audit-json-ndjson-registry-payload]] — Saída JSON/NDJSON no `yarn npm audit`: automação sem perder o relatório bruto.
- [[yarn-npm-audit-ignore-advisory-id-governanca]] — `--ignore` no Yarn: suprimir advisory específico com revisão recorrente.

## Fontes
- [Yarn — opção `--exclude`](https://yarnpkg.com/cli/npm/audit#options) — exclusão de padrões de pacote de um audit; consultado em 2026-10-04.
- [Yarn — `npmAuditExcludePackages`](https://yarnpkg.com/configuration/yarnrc#npmAuditExcludePackages) — configuração persistente de pacotes excluídos; consultado em 2026-10-04.
