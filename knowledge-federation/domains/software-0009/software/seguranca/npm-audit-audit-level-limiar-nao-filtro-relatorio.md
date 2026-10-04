---
id: software.seguranca.tranche17.001644
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#description", "https://docs.npmjs.com/cli/v11/using-npm/config#audit-level"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--audit-level` no npm: limiar do exit code, não filtro dos achados

## Em uma frase
A opção `--audit-level` define a severidade mínima que causa falha do comando, mas o manual afirma que ela não filtra o conteúdo do relatório.

## Por que importa
Confundir a política de saída com uma filtragem pode deixar times sem saber quais achados menores continuam presentes e precisam de triagem.

## Como funciona
Escolha o limiar como regra de bloqueio e processe o relatório completo separadamente; documente quando alertas abaixo do threshold serão tratados.

## Exemplo
Uma CI pode falhar a partir de `high`, enquanto ainda anexa o JSON integral para que severidades menores não desapareçam da fila de segurança.

```text
npm audit --audit-level=high
```

## Limites e trade-offs
Um exit code zero sob limiar elevado não significa que o projeto esteja livre de advisories; significa apenas que não houve achado acima do threshold.

## Como verificar
Introduza resultados de severidades diferentes em uma fixture e confirme que a saída mantém os itens enquanto o código de saída segue o limiar.

## Conexões
- [[npm-audit-bulk-advisory-endpoint-pacotes-versoes]] — Bulk Advisory Endpoint do npm: enviar nomes e versões resolvidas.
- [[npm-audit-fix-semver-force-risco-major]] — `npm audit fix` e `--force`: diferenciar atualização compatível de mudança major.

## Fontes
- [npm CLI v11 — `npm audit`](https://docs.npmjs.com/cli/v11/commands/npm-audit#description) — limiar de falha e distinção explícita entre threshold e conteúdo do relatório; consultado em 2026-10-04.
- [npm CLI v11 — configuração `audit-level`](https://docs.npmjs.com/cli/v11/using-npm/config#audit-level) — nível mínimo que altera o exit status; consultado em 2026-10-04.
