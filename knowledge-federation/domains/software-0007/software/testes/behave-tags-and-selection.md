---
id: software.testes.tranche20.001373
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://behave.readthedocs.io/en/stable/tag_expressions/", "https://behave.readthedocs.io/en/stable/behave/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Behave: selecionar cenários com etiquetas

## Em uma frase
Etiquetas podem ser aplicadas a funcionalidades e cenários, e a execução aceita expressões para incluir ou excluir grupos.

## Por que importa
A seleção por etiqueta permite rodar conjuntos específicos em cada etapa sem duplicar arquivos.

## Como funciona
Aplique etiquetas por tipo de verificação e por área, e escreva a expressão de seleção na configuração ou na linha de comando.

## Exemplo
A execução de revisão pode rodar apenas o conjunto rápido, deixando o conjunto completo para a execução periódica.

## Limites e trade-offs
Etiquetas inconsistentes quebram expressões, e excluir por etiqueta ampla demais deixa cenários relevantes fora sem aviso.

## Como verificar
Rode a seleção com uma etiqueta de exclusão e confirme que os cenários descartados são exatamente os previstos.

## Conexões
- [[behave-hooks]] — Veja também: Behave: preparar e limpar com ganchos.
- [[behave-fixtures]] — Veja também: Behave: usar fixtures para recursos.

## Fontes
- [Behave — Expressões de etiqueta](https://behave.readthedocs.io/en/stable/tag_expressions/) — seleção de cenários por expressões de etiqueta; consultado em 2026-10-03.
- [Behave — Uso da ferramenta](https://behave.readthedocs.io/en/stable/behave/) — argumentos de linha de comando e arquivos de configuração; consultado em 2026-10-03.
