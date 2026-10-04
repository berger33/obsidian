---
id: software.seguranca.tranche17.001646
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#bulk-advisory-endpoint", "https://docs.npmjs.com/cli/v11/using-npm/config#omit"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Separar dependências de produção e desenvolvimento no `npm audit`

## Em uma frase
Opções como `--omit=dev` podem restringir o que é considerado no payload de auditoria, enquanto o lockfile ainda mantém dependências omitidas no grafo.

## Por que importa
A leitura de runtime ajuda a priorizar exposição de produção, mas dependências de build e desenvolvimento também podem executar em pipelines ou afetar releases.

## Como funciona
Gere relatórios distintos para dependências de produção e para o conjunto completo, explicando qual vista aciona bloqueio e qual alimenta backlog.

## Exemplo
Um pipeline pode publicar a visão `--omit=dev` para o artefato e outra auditoria completa para a cadeia de desenvolvimento.

```text
npm audit --omit=dev
```

## Limites e trade-offs
Omitir uma classe não prova que ela seja inofensiva; scripts de instalação e ferramentas de CI podem executar antes da aplicação entrar em produção.

## Como verificar
Compare os dois relatórios, confira os tipos de dependência omitidos e confirme que o inventário completo continua arquivado.

## Conexões
- [[npm-audit-fix-semver-force-risco-major]] — `npm audit fix` e `--force`: diferenciar atualização compatível de mudança major.
- [[npm-audit-json-sarif-automacao-relatorio]] — `npm audit --json`: preservar dados estruturados para triagem automatizada.

## Fontes
- [npm CLI v11 — `npm audit` Bulk Advisory](https://docs.npmjs.com/cli/v11/commands/npm-audit#bulk-advisory-endpoint) — efeito de `--omit` sobre o payload de pacotes enviado ao endpoint; consultado em 2026-10-04.
- [npm CLI v11 — configuração `omit`](https://docs.npmjs.com/cli/v11/using-npm/config#omit) — classes de dependências omitidas e efeito na árvore/payload; consultado em 2026-10-04.
