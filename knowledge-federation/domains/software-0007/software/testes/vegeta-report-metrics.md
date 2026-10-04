---
id: software.testes.tranche16.000974
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
fontes: ["https://github.com/tsenart/vegeta", "https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Vegeta: ler o relatório de resultados

## Em uma frase
O subcomando de relatório resume o fluxo de resultados com latências por percentil, taxa efetiva, volume de dados e proporção de sucesso.

## Por que importa
Percentuais altos descrevem a experiência nos piores casos e revelam contenção que a média esconde.

## Como funciona
Analise em conjunto latência mediana, cauda, taxa alcançada e proporção de sucesso, comparando sempre com uma linha de base registrada.

## Exemplo
Uma latência máxima muito acima do percentil 99 costuma indicar poucas requisições penalizadas por eventos isolados de coleta de lixo ou de contenção.

## Limites e trade-offs
A proporção de sucesso considera o resultado das chamadas e não a correção do conteúdo, de modo que uma resposta de erro da aplicação com código adequado ao teste continua contando como resposta recebida.

## Como verificar
Gere o relatório em formato texto e em formato estruturado e confirme que os totais coincidem entre as duas leituras.

## Conexões
- [[vegeta-targets-file]] — Veja também: Vegeta: descrever alvos com cabeçalhos e corpos.
- [[vegeta-plot-timeline]] — Veja também: Vegeta: visualizar a latência ao longo do tempo.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
