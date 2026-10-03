---
id: software.testes.tranche19.001265
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/reporters.md", "https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: escolher e combinar relatórios

## Em uma frase
A execução aceita múltiplos relatórios simultâneos, com saída legível para pessoas e formatos estruturados para integração.

## Por que importa
Combinar relatório humano e estruturado atende ao diagnóstico no terminal e ao consumo pelo pipeline sem segunda execução.

## Como funciona
Ative o relatório de console para desenvolvimento e o formato de intercâmbio para o pipeline, escolhendo destino em arquivo quando necessário.

## Exemplo
Uma execução pode gravar o resultado legível na tela e o arquivo estruturado consumido pela esteira de integração.

## Limites e trade-offs
Saídas volumosas sem destino definido poluem o registro do pipeline, e formatos escolhidos sem acordo com a ferramenta de acompanhamento geram retrabalho.

## Como verificar
Gere os dois formatos em uma única execução e confirme que a contagem de falhas coincide entre eles.

## Conexões
- [[catch2-floating-point]] — Veja também: Catch2: comparar números de ponto flutuante.
- [[catch2-command-line]] — Veja também: Catch2: selecionar e repetir execuções.

## Fontes
- [Catch2 — Reporters](https://github.com/catchorg/Catch2/blob/devel/docs/reporters.md) — relatórios embutidos, múltiplos destinos e relatórios próprios; consultado em 2026-10-03.
- [Catch2 — Command line](https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md) — filtros por nome e etiqueta, listagem, embaralhamento e semente; consultado em 2026-10-03.
