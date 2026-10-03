---
id: software.testes.tranche24.001842
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/fuzzbench/master/README.md", "https://google.github.io/fuzzbench/getting-started/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Integração e aceite: do guia ao experimento

## Em uma frase
O README descreve o processo para participar: submeter seu fuzzer seguindo o "simple guide" de getting-started no site de documentação; quando a integração é aceita, "we will run a large-scale experiment using your fuzzer and generate a report comparing your fuzzer to others" — o relatório sample linkado é a demonstração do formato de saída.

## Por que importa
O ponto que torna o serviço viável é essa promessa de pipeline: o autor não precisa de cluster, corpus estatístico nem base de comparação — o serviço executa a parte custosa da avaliação e devolve o resultado comparado.

## Como funciona
Escrever a integração conforme o guia (a "easy API"), abrir a submissão, aguardar o aceite e então citar o relatório gerado como evidência comparativa — em vez de números caseiros de máquina única.

## Exemplo
O README usa a própria frase para qualificar o guia de submissão: "our simple guide" — o endereço getting-started do site oficial é o destino, linkado na seção de participação.

## Limites e trade-offs
A nota não descreve os critérios de aceite nem a fila de execução; o fluxo declarado termina em "we will run" — a governança editorial dos experimentos é decisão do serviço.

## Como verificar
A seção de participação do README oficial define os dois passos e o destino do resultado.

## Conexões
- [[fuzzbench-three-pieces]] — Veja também: Os três componentes oferecidos.
- [[fuzzbench-sample-scale]] — Veja também: A escala de referência do sample report.

## Fontes
- [FuzzBench — README oficial](https://raw.githubusercontent.com/google/fuzzbench/master/README.md) — README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.; consultado em 2026-10-03.
- [FuzzBench — Getting Started (documentação oficial)](https://google.github.io/fuzzbench/getting-started/) — Guia oficial Getting Started do FuzzBench para integração de fuzzers e execução de experimentos.; consultado em 2026-10-03.
