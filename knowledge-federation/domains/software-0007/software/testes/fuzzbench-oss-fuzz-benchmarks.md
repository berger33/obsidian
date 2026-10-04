---
id: software.testes.tranche24.001844
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

# Benchmarks herdados do OSS-Fuzz

## Em uma frase
A frase operacional do README: "FuzzBench can use any OSS-Fuzz project as a benchmark" — o acervo de alvos do serviço é o mesmo universo de projetos reais alimentados ao fuzzing contínuo do OSS-Fuzz, e novos benchmarks são pedidos como melhorias via issue ("new benchmarks" citado no canal de feedback).

## Por que importa
Escolher benchmark real-carregado-de-histórico em vez de alvos sintéticos decide a validade externa do experimento; herdar o corpus do programa de fuzzing de produção do ecossistema open source dá aos números do relatório a mesma base onde os bugs reais aparecem.

## Como funciona
Para propor um alvo novo ao FuzzBench, o caminho declarado é o GitHub issue do projeto (feedback sobre integrações e benchmarks); para entender o alvo, o projeto OSS-Fuzz correspondente já traz build e seeds.

## Exemplo
Uma comparação entre fuzzers sobre libpng, harfbuzz e família — todos residentes do OSS-Fuzz — chega com contexto de bugs reais, não com parsing de toy format.

## Limites e trade-offs
O README declara a capacidade (any OSS-Fuzz project), não a lista corrente de benchmarks habilitados; o acervo ativo é consultado no site de documentação/relatórios.

## Como verificar
A frase do any OSS-Fuzz benchmark e o canal de feedback com pedidos de benchmark vêm da seção de oferta e de feedback do README.

## Conexões
- [[fuzzbench-sample-scale]] — Veja também: A escala de referência do sample report.
- [[fuzzbench-reporting-library]] — Veja também: A biblioteca de reporting com estatística embutida.

## Fontes
- [FuzzBench — README oficial](https://raw.githubusercontent.com/google/fuzzbench/master/README.md) — README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.; consultado em 2026-10-03.
- [FuzzBench — Getting Started (documentação oficial)](https://google.github.io/fuzzbench/getting-started/) — Guia oficial Getting Started do FuzzBench para integração de fuzzers e execução de experimentos.; consultado em 2026-10-03.
