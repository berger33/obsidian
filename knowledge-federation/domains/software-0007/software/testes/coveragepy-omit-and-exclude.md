---
id: software.testes.tranche16.000995
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

# coverage.py: excluir o que não deve ser medido

## Em uma frase
Padrões de omissão removem arquivos inteiros da medição, e comentários ou expressões de exclusão removem linhas específicas do cálculo.

## Por que importa
Código gerado, migrações e ramos de compatibilidade distorcem o percentual e desviam atenção do código que expressa regras de negócio.

## Como funciona
Prefira exclusões por padrão de caminho para artefatos gerados e use marcadores pontuais para blocos impossíveis de testar, sempre com justificativa.

## Exemplo
Um ramo que só existe para compatibilidade com versão antiga pode ser marcado individualmente, mantendo o restante do arquivo dentro da medição.

## Limites e trade-offs
Excluir demais produz número artificialmente alto, e a exclusão por linha esconde código que talvez devesse ter teste; ambas precisam de revisão periódica.

## Como verificar
Remova temporariamente uma exclusão e verifique quanto o percentual cai, avaliando se a decisão original continua adequada.

## Conexões
- [[coveragepy-config-files]] — Veja também: coverage.py: centralizar regras na configuração.
- [[coveragepy-parallel-and-combine]] — Veja também: coverage.py: consolidar dados de execuções paralelas.

## Fontes
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
- [coverage.py — Command line](https://coverage.readthedocs.io/en/6.5.0/cmd.html) — comandos run, combine, report, xml, json e html com suas opções; consultado em 2026-10-03.
