---
id: software.seguranca.tranche17.001654
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
fontes: ["https://pnpm.io/cli/audit#--fix", "https://pnpm.io/settings/dependency-resolution#overrides"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `pnpm audit --fix`: remediar com `overrides` no arquivo de workspace

## Em uma frase
A opção `--fix` pode adicionar overrides em `pnpm-workspace.yaml` para forçar uma versão não vulnerável de uma dependência afetada.

## Por que importa
Um override alcança dependências transitivas, mas pode impor versão não prevista pelo consumidor e precisa de teste de compatibilidade.

## Como funciona
Revise o pacote pai, a faixa corrigida e o escopo da regra; prefira um pull request isolado e teste toda configuração que consome o override.

## Exemplo
Depois da auditoria, gere a sugestão, examine a alteração em `pnpm-workspace.yaml` e confirme que apenas o pacote vulnerável recebe a substituição necessária.

```text
pnpm audit --fix
```

## Limites e trade-offs
A ferramenta não garante compatibilidade semântica do override; uma atualização forçada pode ocultar dependência de API incompatível.

## Como verificar
Rode testes e `pnpm why` após a correção, confira a versão efetivamente instalada e repita auditoria para confirmar a remoção do advisory.

## Conexões
- [[pnpm-audit-json-patched-versions-null]] — `pnpm audit --json`: diferenciar advisories corrigíveis de sem versão corrigida.
- [[pnpm-audit-fix-update-lockfile-interativo]] — `pnpm audit --fix=update` e modo interativo: escolher a forma da remediação.

## Fontes
- [pnpm — `pnpm audit --fix`](https://pnpm.io/cli/audit#--fix) — criação de overrides para corrigir advisories; consultado em 2026-10-04.
- [pnpm — overrides](https://pnpm.io/settings/dependency-resolution#overrides) — escopo e semântica de overrides em `pnpm-workspace.yaml`; consultado em 2026-10-04.
