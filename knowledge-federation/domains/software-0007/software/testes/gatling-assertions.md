---
id: software.testes.tranche17.001063
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.gatling.io/concepts/assertions/", "https://docs.gatling.io/concepts/simulation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: reprovar a execução com asserções

## Em uma frase
As asserções comparam estatísticas globais ou por requisição com limites declarados e fazem a execução terminar com erro quando o critério não é atendido.

## Por que importa
Um teste de carga sem critério objetivo produz leitura subjetiva e deixa a regressão de desempenho passar como aceitável.

## Como funciona
Declare limites por percentil, taxa de sucesso ou contagem de falhas, com valores calibrados a partir de medições anteriores.

## Exemplo
Uma asserção pode exigir que o percentil alto fique abaixo de um limite e que a proporção de sucesso supere um patamar durante a rampa.

## Limites e trade-offs
Limites apertados geram falhas por variação do ambiente, enquanto limites frouxos tornam a verificação decorativa; a calibração exige histórico.

## Como verificar
Ajuste um limite para um valor que o sistema sabe violar e confirme que a execução termina com código de erro indicando a estatística afetada.

## Conexões
- [[gatling-pauses-and-pacing]] — Veja também: Gatling: representar o tempo de pensamento.
- [[gatling-http-protocol]] — Veja também: Gatling: configurar o protocolo HTTP compartilhado.

## Fontes
- [Gatling — Assertions](https://docs.gatling.io/concepts/assertions/) — limites por estatística e efeito no código de saída da execução; consultado em 2026-10-03.
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
