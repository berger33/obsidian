---
id: software.testes.tranche16.001001
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://coverage.readthedocs.io/en/6.5.0/branch.html", "https://coverage.readthedocs.io/en/6.5.0/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: tratar a métrica como indicação

## Em uma frase
Percentual de linhas e ramos descreve o que foi executado, sem atestar que as asserções verificam o comportamento correto.

## Por que importa
Confundir execução com verificação leva a suíte extensa e frágil, com muitos caminhos percorridos e nenhuma afirmação sobre resultados.

## Como funciona
Combine a métrica com revisão dos casos, use a lista de trechos não executados para levantar perguntas e evite transformar o número em objetivo isolado.

## Exemplo
Um bloco de tratamento de erro executado sem verificação do efeito produz linha coberta e nenhuma garantia sobre o comportamento observado.

## Limites e trade-offs
Exclusões e ramos triviais alteram o percentual sem mudança correspondente na qualidade, e comparações entre projetos diferentes raramente são justas.

## Como verificar
Escolha um trecho coberto mas sem asserção significativa e proponha uma verificação que realmente distinga comportamento correto de incorreto.

## Conexões
- [[coveragepy-subprocesses]] — Veja também: coverage.py: medir código executado em subprocessos.

## Fontes
- [coverage.py — Branch coverage](https://coverage.readthedocs.io/en/6.5.0/branch.html) — medição de ramos, ramos parciais e ajuste de exclusões; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
