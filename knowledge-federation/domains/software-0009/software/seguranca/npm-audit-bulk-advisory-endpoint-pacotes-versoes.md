---
id: software.seguranca.tranche17.001643
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#bulk-advisory-endpoint", "https://github.com/npm/cli/pull/7911"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bulk Advisory Endpoint do npm: enviar nomes e versões resolvidas

## Em uma frase
Desde npm 7, o CLI usa o Bulk Advisory endpoint para enviar nomes e versões do grafo; a implementação atual não recorre ao endpoint Quick legado quando Bulk falha, embora a página versionada v11 ainda descreva esse fallback.

## Por que importa
Saber o que o cliente envia ajuda a analisar privacidade, resposta de registry e diferenças entre ferramentas que usam endpoints de auditoria distintos.

## Como funciona
O cliente envia nomes e versões resolvidas ao endpoint bulk do registry configurado e calcula vulnerabilidades/metavulnerabilidades; desde a remoção do fallback legado, uma falha da consulta deve ser tratada como erro de serviço, não como fallback garantido.

## Exemplo
Ao depurar resultados diferentes de dois clients, compare versões do npm, registry e lockfile antes de atribuir divergência à base de vulnerabilidades.

```text
npm audit --json
```

## Limites e trade-offs
A página v11 do manual ainda descreve o Quick Audit fallback, mas o changelog/PR oficial registra sua remoção; trate o comportamento como dependente da versão do CLI e confirme o binário executado na CI.

## Como verificar
Registre a versão de npm e registry, teste uma resposta bulk válida e uma falha de consulta em ambiente isolado e compare a execução com o histórico oficial de remoção do fallback.

## Conexões
- [[npm-audit-lockfile-reprodutibilidade-package-lock]] — `package-lock.json` como entrada do `npm audit`: consistência e reprodutibilidade.
- [[npm-audit-audit-level-limiar-nao-filtro-relatorio]] — `--audit-level` no npm: limiar do exit code, não filtro dos achados.

## Fontes
- [npm CLI v11 — Bulk Advisory endpoint](https://docs.npmjs.com/cli/v11/commands/npm-audit#bulk-advisory-endpoint) — payload de nomes/versões, endpoint bulk e comportamento descrito na documentação versionada; consultado em 2026-10-04.
- [npm CLI — remoção do fallback de audit](https://github.com/npm/cli/pull/7911) — PR oficial que removeu o fallback para o endpoint Quick legado; consultado em 2026-10-04.
