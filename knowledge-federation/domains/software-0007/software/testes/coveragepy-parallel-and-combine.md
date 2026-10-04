---
id: software.testes.tranche16.000996
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

# coverage.py: consolidar dados de execuções paralelas

## Em uma frase
O modo paralelo faz cada processo gravar arquivo próprio, e os arquivos podem ser combinados antes da geração dos relatórios.

## Por que importa
Suítes distribuídas em vários trabalhadores ou trabalhos do pipeline produzem dados parciais, e medir apenas um deles subestima a cobertura real.

## Como funciona
Ative o modo paralelo no projeto, publique os arquivos como artefato de cada trabalho e combine tudo em uma etapa final antes do relatório.

## Exemplo
Um trabalho final baixa os dados de todos os executores, combina os arquivos e gera o relatório consolidado usado pela verificação.

## Limites e trade-offs
A combinação exige que os arquivos venham da mesma revisão e do mesmo conjunto de fontes; dados obsoletos no diretório elevam artificialmente o resultado.

## Como verificar
Compare a soma dos relatórios parciais com o relatório combinado e confirme que os totais de linhas e ramos coincidem.

## Conexões
- [[coveragepy-omit-and-exclude]] — Veja também: coverage.py: excluir o que não deve ser medido.
- [[coveragepy-fail-under]] — Veja também: coverage.py: falhar o build por limite de cobertura.

## Fontes
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
