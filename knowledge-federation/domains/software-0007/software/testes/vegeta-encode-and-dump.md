---
id: software.testes.tranche16.000976
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

# Vegeta: converter resultados em formatos analisáveis

## Em uma frase
Os subcomandos de codificação e descarga convertem o fluxo binário em formatos legíveis, como JSON e CSV, permitindo consumo por ferramentas de análise.

## Por que importa
O formato binário é eficiente para armazenar séries longas, mas não é inspecionável nem filtrável sem conversão.

## Como funciona
Converta para JSON quando precisar de processamento campo a campo e para CSV quando a planilha for o destino, mantendo o binário como registro original.

## Exemplo
Encadear a conversão com um filtro de texto permite acompanhar em tempo quase real o código e a latência de cada requisição durante o ataque.

## Limites e trade-offs
A conversão gera volume grande de dados e pode conter cabeçalhos sensíveis, exigindo cuidado com o que é publicado como artefato.

## Como verificar
Converta uma amostra pequena, confirme que os campos esperados existem e que os valores batem com o resumo agregado da mesma execução.

## Conexões
- [[vegeta-plot-timeline]] — Veja também: Vegeta: visualizar a latência ao longo do tempo.
- [[vegeta-rate-workers-connections]] — Veja também: Vegeta: distinguir taxa, trabalhadores e conexões.

## Fontes
- [Vegeta — repositório oficial](https://github.com/tsenart/vegeta) — manual de uso: attack, report, plot, encode, dump e opções de conexão; consultado em 2026-10-03.
- [Vegeta — biblioteca Go](https://pkg.go.dev/github.com/tsenart/vegeta/v12/lib) — API de taxa, atacante, alvos e métricas para uso programático; consultado em 2026-10-03.
