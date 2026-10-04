---
id: software.testes.tranche17.001065
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
fontes: ["https://docs.gatling.io/concepts/simulation/", "https://github.com/gatling/gatling"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: consumir relatórios e integrar ao pipeline

## Em uma frase
Ao final da execução a ferramenta publica relatório navegável com séries temporais, distribuição de latências e contagem de falhas por requisição.

## Por que importa
O relatório é a evidência da medição, e guardá-lo por revisão permite comparar tendências em vez de julgar um número isolado.

## Como funciona
Preserve o diretório de resultados como artefato, destaque as requisições com falha e vincule o relatório à mudança que motivou a execução.

## Exemplo
Um relatório com erro concentrado em um passo costuma apontar dependência específica, mais útil do que a média geral da simulação.

## Limites e trade-offs
O relatório descreve o que o gerador observou e não substitui a telemetria do serviço, que indica qual recurso saturou durante a carga.

## Como verificar
Execute a mesma simulação duas vezes e compare os relatórios para identificar variação de ambiente antes de atribuir diferença ao código.

## Conexões
- [[gatling-http-protocol]] — Veja também: Gatling: configurar o protocolo HTTP compartilhado.

## Fontes
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
- [Gatling — repositório oficial](https://github.com/gatling/gatling) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
