---
id: software.testes.tranche22.001655
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/manpage.html", "https://gcovr.com/en/stable/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: configuração em arquivo, chave por opção

## Em uma frase
Cada opção sensata da CLI declara na referência o seu config key homônimo (filter, exclude, gcov-filter, exclude-unreachable-branches...), e o guia mantém uma página "Configuration Files" dedicada a esse modo.

## Por que importa
Flags de cobertura enterradas em shell script de CI não sobrevivem a refactor; um gcovr.cfg no repositório viaja com o código e vale para IDE, CI e local igualmente.

## Como funciona
O padrão é a chave levar o nome longo da opção sem os dois traços, permitindo escrever filter = src/ e excluir discussões de quoting por linha de comando.

## Exemplo
A mesma doc oferece --line-reference-format análogo em espírito: preferências de formato que cabem melhor em arquivo do que em flags repetidas.

## Limites e trade-offs
Nem toda flag nova ganha config key no mesmo release, e a página de changelog é o lugar de conferir antes de migrar um setup inteiro de flags para arquivo.

## Como verificar
Converta seu one-liner atual de gcovr em gcovr.cfg e compare os dois relatórios --txt para provar equivalência.

## Conexões
- [[gcovr-exclusions]] — Veja também: gcovr: excluir linha, branch e função.
- [[gcovr-gcov-parser]] — Veja também: gcovr: o parser do gcov por trás do número.

## Fontes
- [gcovr — Command Line Reference](https://gcovr.com/en/stable/manpage.html) — filtros, exclusões, config keys e --no-markers; consultado em 2026-10-03.
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
