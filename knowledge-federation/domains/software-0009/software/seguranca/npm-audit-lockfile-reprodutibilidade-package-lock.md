---
id: software.seguranca.tranche17.001642
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#package-lock", "https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `package-lock.json` como entrada do `npm audit`: consistência e reprodutibilidade

## Em uma frase
Por padrão, npm requer `package-lock.json` ou `npm-shrinkwrap.json` para executar a auditoria e alerta que reconstruir o grafo pode alterar resultados entre execuções.

## Por que importa
Vincular a análise ao mesmo grafo resolvido pelo build reduz discrepâncias entre auditoria local, CI e dependências efetivamente empacotadas.

## Como funciona
Versione o lockfile da aplicação, audite o commit exato e trate `--no-package-lock` como modo que reconstrói a árvore e precisa de justificativa.

## Exemplo
No pull request, execute auditoria após a instalação determinística e publique o hash do lockfile usado ao lado da saída JSON.

```text
npm audit --json
```

## Limites e trade-offs
O lockfile descreve resolução, não prova que o pacote implantado seja idêntico; verifique também a cadeia de build e o artefato resultante.

## Como verificar
Compare o hash do lockfile antes e depois da tarefa e confirme que a CI não usa lockfile diferente do commit que será mesclado.

## Conexões
- [[npm-audit-descricao-dependencias-registry-privacidade]] — `npm audit`: envio da descrição de dependências ao registry configurado.
- [[npm-audit-bulk-advisory-endpoint-pacotes-versoes]] — Bulk Advisory Endpoint do npm: enviar nomes e versões resolvidas.

## Fontes
- [npm CLI v11 — `npm audit` e package-lock](https://docs.npmjs.com/cli/v11/commands/npm-audit#package-lock) — requisito padrão de lockfile e modo `--no-package-lock`; consultado em 2026-10-04.
- [npm CLI v11 — package-lock.json](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json) — papel do lockfile, árvore resolvida e instalação reprodutível; consultado em 2026-10-04.
