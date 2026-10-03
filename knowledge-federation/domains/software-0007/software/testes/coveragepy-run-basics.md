---
id: software.testes.tranche16.000992
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

# coverage.py: medir a execução de um programa

## Em uma frase
O comando de execução instrumenta o interpretador, roda o módulo ou script indicado e grava os dados coletados em arquivo.

## Por que importa
Medir a partir da suíte real, e não por inspeção manual, permite identificar quais linhas a execução efetivamente alcançou.

## Como funciona
Execute o programa ou a suíte de testes pela ferramenta, informe o pacote de interesse e mantenha o arquivo de dados fora do controle de versão.

## Exemplo
Rodar a suíte com o módulo de teste sob instrumentação produz dados que servem de base para os relatórios seguintes.

## Limites e trade-offs
O arquivo de dados é binário e específico da execução, e misturar execuções de revisões diferentes sem combinar corretamente gera números incoerentes.

## Como verificar
Compare a contagem de arquivos do relatório com o conjunto que se esperava medir e verifique se algum pacote ficou de fora.

## Conexões
- [[coveragepy-branch-coverage]] — Veja também: coverage.py: habilitar cobertura de ramos.

## Fontes
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
