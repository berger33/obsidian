---
id: software.testes.tranche15.000875
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/excluding.html", "https://coverage.readthedocs.io/en/latest/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: revisar como exclusões alteram statements e branches reportados

## Em uma frase
Padrões de exclusão mudam o denominador do relatório e podem também eliminar uma alternativa de branch, portanto a configuração faz parte da interpretação da métrica.

## Por que importa
`exclude_also` acrescenta padrões sem substituir exclusões padrão, enquanto `exclude_lines` substitui a lista e pode exigir reapresentar pragmas que a equipe quer manter.

## Como funciona
Se um ramo condicional é excluído, coverage.py deixa de tratá-lo como destino exigível naquele ponto.

## Exemplo
Antes de adicionar regex a `[report] exclude_also`, escreva um exemplo mínimo da linha ou bloco que deve sair da métrica e gere um relatório antes/depois para avaliar o efeito.

## Limites e trade-offs
Um padrão pode corresponder a mais código do que o pretendido, e excluir uma linha de definição pode remover o bloco inteiro; exclusões não devem servir para atingir um percentual alvo artificialmente.

## Como verificar
Revise relatório de linhas e de branches junto com a lista de padrões, teste um caso que corresponda e um semelhante que não deveria corresponder.

## Conexões
- [[coverage-py-branch-partial-e-pragma-no-branch]] — Veja também: coverage.py: usar pragma no branch para desvios estruturalmente parciais.
- [[coverage-py-source-detecta-arquivos-nao-executados]] — Veja também: coverage.py: declarar source para incluir módulos sem execução.

## Fontes
- [Coverage.py 7.16.2 — Excluding code](https://coverage.readthedocs.io/en/latest/excluding.html) — exclusões de linhas/blocos e efeito sobre branch coverage; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
