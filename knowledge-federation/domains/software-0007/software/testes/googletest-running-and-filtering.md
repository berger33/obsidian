---
id: software.testes.tranche18.001195
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://google.github.io/googletest/advanced.html", "https://google.github.io/googletest/primer.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: executar e filtrar casos

## Em uma frase
O executável aceita filtros por nome de suíte e de caso, repetição, ordem aleatória e saída em formatos consumíveis por ferramentas.

## Por que importa
Filtrar permite investigar um caso específico rapidamente e a ordem aleatória revela dependências ocultas entre testes.

## Como funciona
Use filtros para iterar durante o desenvolvimento, ative ordem aleatória na esteira e publique a saída estruturada como artefato.

## Exemplo
Um caso pode ser executado isoladamente por filtro enquanto se investiga uma falha intermitente no pipeline.

## Limites e trade-offs
Filtros permanentes escondem casos da execução completa, e a ordem aleatória sem semente fixa dificulta reproduzir uma sequência específica.

## Como verificar
Execute a suíte com ordem aleatória duas vezes e verifique se a semente registrada permite reproduzir a sequência.

## Conexões
- [[googletest-death-tests]] — Veja também: GoogleTest: verificar encerramentos esperados.
- [[googletest-reports-and-limits]] — Veja também: GoogleTest: interpretar relatórios e limites.

## Fontes
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — macros de caso, asserções, comparações e execução; consultado em 2026-10-03.
