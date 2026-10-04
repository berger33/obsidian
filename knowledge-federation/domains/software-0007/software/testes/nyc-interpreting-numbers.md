---
id: software.testes.tranche16.001012
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
fontes: ["https://github.com/istanbuljs/nyc", "https://github.com/istanbuljs/istanbuljs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: interpretar as quatro métricas

## Em uma frase
Statements, branches, functions e lines medem dimensões distintas, e um arquivo pode estar integralmente coberto em uma delas e descoberto em outra.

## Por que importa
Ler apenas o total geral esconde um módulo com todas as funções exercitadas e nenhum ramo de erro verificado.

## Como funciona
Examine as quatro métricas por diretório, investigue divergências acentuadas e trate a métrica como indicação para revisão de casos.

## Exemplo
Um arquivo com linhas cobertas e ramos parciais indica tratamento de erro executado pela metade, apontando lacuna concreta de cenário.

## Limites e trade-offs
Percentuais altos convivem com asserções fracas, e comparar projetos distintos sem contexto de tamanho e criticidade leva a metas inadequadas.

## Como verificar
Escolha um arquivo com divergência entre métricas e proponha um caso que exercite o ramo ausente com verificação de resultado.

## Conexões
- [[nyc-excludes-and-generated-code]] — Veja também: nyc: excluir código gerado com critério.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [Istanbul — monorepo oficial](https://github.com/istanbuljs/istanbuljs) — instrumentação JavaScript, bibliotecas de cobertura e geradores de relatório; consultado em 2026-10-03.
