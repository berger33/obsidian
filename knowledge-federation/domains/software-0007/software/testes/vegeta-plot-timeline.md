---
id: software.testes.tranche16.000975
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

# Vegeta: visualizar a latência ao longo do tempo

## Em uma frase
O subcomando de gráfico gera uma página com série temporal de latências, permitindo correlacionar picos com eventos ocorridos durante o ataque.

## Por que importa
Um resumo agregado esconde a forma da carga ao longo do tempo, enquanto a série revela aquecimento, degradação e recuperação.

## Como funciona
Gere o gráfico a partir do arquivo de resultados, combine vários arquivos para comparar execuções e observe a linha temporal junto do volume de requisições.

## Exemplo
Comparar dois arquivos de ataques com taxas diferentes na mesma página evidencia em que ponto a taxa maior começa a degradar as respostas.

## Limites e trade-offs
O gráfico reduz a quantidade de pontos para caber na tela, então detalhes finos podem ser suavizados; a leitura deve ser combinada com o relatório numérico.

## Como verificar
Gere o gráfico de uma execução conhecida e verifique se os picos visíveis correspondem aos momentos registrados no relatório.

## Conexões
- [[vegeta-report-metrics]] — Veja também: Vegeta: ler o relatório de resultados.
- [[vegeta-encode-and-dump]] — Veja também: Vegeta: converter resultados em formatos analisáveis.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
