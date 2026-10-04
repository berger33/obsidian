---
id: software.testes.tranche21.001479
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/avajs/ava/blob/main/readme.md", "https://github.com/avajs/ava/blob/main/docs/05-command-line.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AVA: distribuição na CI e modo watch

## Em uma frase
O AVA detecta ambientes de CI com builds paralelas (via ci-parallel-vars) e executa em cada build um subconjunto diferente dos arquivos, cobrindo o total somado; o flag --watch reexecuta ao salvar.

## Por que importa
Dividir a suíte entre workers de CI não deveria ser projeto próprio; o executor já conhece as variáveis dos serviços mais comuns e fatia sozinho.

## Como funciona
Deixe o runner particionar os arquivos entre os jobs, habilite --watch durante o desenvolvimento local e mantenha o commit limpo com npm test padrão.

## Exemplo
Quatro jobs na GitHub Actions recebem quartis distintos dos arquivos de teste sem nenhuma lista manual de split.

## Limites e trade-offs
O particionamento depende de o CI anunciar paralelismo; um servidor próprio sem as variáveis esperadas roda tudo em um job só.

## Como verificar
Rode o subconjunto da CI em um job e confira que o relatório lista apenas os arquivos daquele quartil, e teste o --watch salvando um arquivo.

## Conexões
- [[ava-magic-assert-diffs]] — Veja também: AVA: diagnóstico de falha com magic assert.

## Fontes
- [AVA — README oficial](https://github.com/avajs/ava/blob/main/readme.md) — proposta, instalação e destaques do runner; consultado em 2026-10-03.
- [AVA — Guia Command line](https://github.com/avajs/ava/blob/main/docs/05-command-line.md) — flags do CLI, reporter TAP e modo watch; consultado em 2026-10-03.
