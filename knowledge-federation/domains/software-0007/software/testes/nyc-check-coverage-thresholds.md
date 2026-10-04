---
id: software.testes.tranche16.001006
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
fontes: ["https://github.com/istanbuljs/nyc", "https://www.npmjs.com/package/nyc"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nyc: reprovar por limites de cobertura

## Em uma frase
A verificação de cobertura compara cada métrica com o limite declarado e encerra com erro quando algum valor fica abaixo do mínimo.

## Por que importa
Limites por métrica capturam dimensões diferentes, e olhar apenas linhas deixa funções e ramos sem qualquer proteção.

## Como funciona
Declare limites para statements, branches, functions e lines, escolha valores alcançáveis e inclua a verificação na esteira obrigatória.

## Exemplo
Um projeto pode exigir percentual mais alto para linhas e mais baixo para ramos enquanto a suíte amadurece.

## Limites e trade-offs
Limites altos aplicados de uma vez produzem bloqueio geral e pressão para reduzir a regra, e limites por arquivo exigem configuração própria.

## Como verificar
Reduza o limite para um valor acima do medido e confirme que o comando termina com erro indicando a métrica afetada.

## Conexões
- [[nyc-reporters]] — Veja também: nyc: escolher relatórios e destino.
- [[nyc-temp-dir-and-merge]] — Veja também: nyc: consolidar dados de várias execuções.

## Fontes
- [nyc — repositório oficial](https://github.com/istanbuljs/nyc) — linha de comando, filtros, relatórios, limites e mesclagem de dados; consultado em 2026-10-03.
- [nyc — pacote npm](https://www.npmjs.com/package/nyc) — opções documentadas e exemplos de uso do publicador; consultado em 2026-10-03.
