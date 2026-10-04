---
id: software.seguranca.tranche17.001645
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#description", "https://docs.npmjs.com/cli/v11/using-npm/config#force"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `npm audit fix` e `--force`: diferenciar atualização compatível de mudança major

## Em uma frase
`npm audit fix` tenta aplicar remediações no grafo; quando a correção exige sair das faixas declaradas, `--force` pode permitir atualizações SemVer major.

## Por que importa
Uma correção de advisory pode alterar APIs e comportamento de runtime, por isso não deve ser aprovada apenas porque reduz o número de alertas.

## Como funciona
Gere um dry-run, examine manifestos e lockfile e teste a atualização em branch; reserve `--force` para mudanças major avaliadas explicitamente.

## Exemplo
Use primeiro `npm audit fix --dry-run --json --force` para inspecionar a proposta que sai das faixas declaradas; depois avalie separadamente a compatibilidade e só aplique a mudança major aprovada.

```text
npm audit fix --dry-run --json --force
```

## Limites e trade-offs
O próprio manual destaca que o comando executa uma instalação completa e que algumas vulnerabilidades exigem intervenção manual.

## Como verificar
Revise o diff e a versão de cada pacote, rode testes e repita `npm audit`; compare também a compatibilidade da API usada pelo produto.

## Conexões
- [[npm-audit-audit-level-limiar-nao-filtro-relatorio]] — `--audit-level` no npm: limiar do exit code, não filtro dos achados.
- [[npm-audit-omit-producao-devdependencies-escopo]] — Separar dependências de produção e desenvolvimento no `npm audit`.

## Fontes
- [npm CLI v11 — `npm audit fix`](https://docs.npmjs.com/cli/v11/commands/npm-audit#description) — remediação, `--dry-run` e efeitos de `--force` sobre as faixas SemVer; consultado em 2026-10-04.
- [npm CLI v11 — configuração `force`](https://docs.npmjs.com/cli/v11/using-npm/config#force) — efeito e alcance da flag `--force` em operações npm; consultado em 2026-10-04.
