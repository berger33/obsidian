---
id: software.testes.tranche16.001000
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
fontes: ["https://coverage.readthedocs.io/en/6.5.0/config.html", "https://coverage.readthedocs.io/en/6.5.0/cmd.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: medir código executado em subprocessos

## Em uma frase
Processos filhos iniciados durante a execução só são medidos quando a instrumentação é propagada por configuração de ambiente ou por opção de simultaneidade.

## Por que importa
Muitos sistemas executam trabalho relevante fora do processo principal, e ignorá-lo produz relatório que descreve apenas a camada mais externa.

## Como funciona
Declare a forma de concorrência usada, inicie o processo de medição a partir da configuração de ambiente e combine os dados ao final.

## Exemplo
Um serviço que delega processamento a fila interna precisa que os processos trabalhadores também iniciem instrumentados para aparecer no relatório.

## Limites e trade-offs
A propagação depende do modo de criação dos processos e não cobre binários externos escritos em outra linguagem.

## Como verificar
Execute um cenário que cria subprocesso com e sem a propagação e compare o relatório para confirmar quais linhas entraram na medição.

## Conexões
- [[coveragepy-contexts]] — Veja também: coverage.py: separar medições por contexto.
- [[coveragepy-limits-and-quality]] — Veja também: coverage.py: tratar a métrica como indicação.

## Fontes
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
