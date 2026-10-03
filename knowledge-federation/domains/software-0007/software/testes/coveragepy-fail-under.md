---
id: software.testes.tranche16.000997
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
fontes: ["https://coverage.readthedocs.io/en/6.5.0/cmd.html", "https://coverage.readthedocs.io/en/6.5.0/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: falhar o build por limite de cobertura

## Em uma frase
A opção de limite mínimo faz o comando terminar com código de erro quando o total fica abaixo do valor definido, tanto na configuração quanto na linha de comando.

## Por que importa
Só existe proteção contra regressão quando a verificação interrompe a esteira, e um relatório sem consequência tende a ser ignorado.

## Como funciona
Defina o limite no arquivo versionado, use valor alcançável a partir da situação atual e inclua a verificação entre as etapas obrigatórias do pipeline.

## Exemplo
Um projeto com cobertura atual conhecida pode fixar limite um ponto abaixo do valor medido e elevá-lo conforme os testes crescem.

## Limites e trade-offs
O limite total esconde módulos descobertos dentro de um conjunto bem testado, e perseguir percentual alto incentiva testes superficiais.

## Como verificar
Reduza deliberadamente o limite a um valor acima do medido e confirme que a esteira falha com o código de saída previsto.

## Conexões
- [[coveragepy-parallel-and-combine]] — Veja também: coverage.py: consolidar dados de execuções paralelas.
- [[coveragepy-report-formats]] — Veja também: coverage.py: escolher formatos de saída.

## Fontes
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
