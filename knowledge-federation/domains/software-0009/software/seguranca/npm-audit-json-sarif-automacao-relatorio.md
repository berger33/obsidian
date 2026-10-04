---
id: software.seguranca.tranche17.001647
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#description", "https://github.com/npm/cli/blob/latest/lib/commands/audit.js"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `npm audit --json`: preservar dados estruturados para triagem automatizada

## Em uma frase
O formato JSON entrega detalhes programáveis do relatório e permite que ferramentas de CI correlacionem advisories com versões e dependências.

## Por que importa
Texto formatado para terminal é frágil para parsing; manter saída estruturada ajuda a criar histórico e integrar achados sem perder identificadores.

## Como funciona
Armazene JSON associado ao commit, sanitize campos que possam conter dados internos e valide o formato contra a versão do npm usada.

## Exemplo
Um job pode anexar `npm audit --json` como artefato e extrair ID, severidade e caminho de dependência para criar ticket com contexto.

```text
npm audit --json
```

## Limites e trade-offs
O esquema e detalhes de saída podem variar entre versões; JSON não determina aplicabilidade nem deve ser tratado como substituto da análise humana.

## Como verificar
Rode o mesmo comando em uma fixture com achado conhecido, valide parsing e confirme que o pipeline preserva o código de saída original.

## Conexões
- [[npm-audit-omit-producao-devdependencies-escopo]] — Separar dependências de produção e desenvolvimento no `npm audit`.
- [[npm-audit-metavulnerabilidades-cadeia-transitiva]] — Metavulnerabilidades no npm: quando uma dependência pai só resolve para versão vulnerável.

## Fontes
- [npm CLI v11 — `npm audit` JSON](https://docs.npmjs.com/cli/v11/commands/npm-audit#description) — saída estruturada e códigos de saída documentados do comando; consultado em 2026-10-04.
- [npm CLI — implementação do comando audit](https://github.com/npm/cli/blob/latest/lib/commands/audit.js) — parser JSON, saída de relatório e propagação de status no CLI atual; consultado em 2026-10-04.
