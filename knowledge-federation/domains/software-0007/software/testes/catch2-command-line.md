---
id: software.testes.tranche19.001266
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
fontes: ["https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md", "https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Catch2: selecionar e repetir execuções

## Em uma frase
A linha de comando permite filtrar por nome e etiqueta, listar casos, embaralhar a ordem e repetir a execução fixando a semente.

## Por que importa
Filtrar acelera o ciclo durante o desenvolvimento, e a semente registrada torna reproduzível a ordem que revelou uma falha.

## Como funciona
Use filtros para o conjunto em trabalho, embaralhe na esteira para expor dependências de ordem e registre a semente das execuções que falham.

## Exemplo
Uma falha que só aparece em determinada ordem pode ser reproduzida executando novamente com a semente anotada.

## Limites e trade-offs
Filtrar por etiqueta ampla pode excluir casos relevantes por engano, e depender da ordem padrão esconde acoplamentos entre testes.

## Como verificar
Execute com embaralhamento e semente fixa duas vezes e confirme que a ordem e o resultado se repetem.

## Conexões
- [[catch2-reporters]] — Veja também: Catch2: escolher e combinar relatórios.
- [[catch2-integration-limits]] — Veja também: Catch2: integrar ao build e reconhecer limites.

## Fontes
- [Catch2 — Command line](https://github.com/catchorg/Catch2/blob/devel/docs/command-line.md) — filtros por nome e etiqueta, listagem, embaralhamento e semente; consultado em 2026-10-03.
- [Catch2 — Tutorial](https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md) — primeiros passos, casos de teste, seções e asserções; consultado em 2026-10-03.
