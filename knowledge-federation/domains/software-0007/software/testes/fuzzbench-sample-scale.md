---
id: software.testes.tranche24.001843
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
fontes: ["https://raw.githubusercontent.com/google/fuzzbench/master/README.md", "https://www.fuzzbench.com/reports/sample/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# A escala de referência do sample report

## Em uma frase
O README quantifica o sample report público: ele é "generated using 10 fuzzers against 24 real-world benchmarks, with 20 trials each and over a duration of 24 hours", e o raw data em formato CSV comprimido fica disponível no final do relatório — a própria estrutura do dataset é consultável.

## Por que importa
Esses quatro números (10×24×20×24h) definem a régua do que a comunidade chama de avaliação séria de fuzzer: trials múltiplos por benchmark porque fuzzing é estocástico, e o dataset aberto existe para a afirmação "statistically significant" ser conferível, não apenas legível.

## Como funciona
Antes de citar um resultado de fuzzer, pergunte se a configuração alcança a ordem de grandeza do sample (múltiplos trials por benchmark); um run único de uma hora não sustenta comparação, e o CSV do próprio FuzzBench permite calibrar a expectativa.

## Exemplo
O dado bruto no fim do relatório (compressed CSV) é o que permite reimplementar o teste estatístico de fora — a biblioteca de reporting facilita, mas não impõe opacidade.

## Limites e trade-offs
A nota usa a configuração do sample report declarado no README; relatórios periódicos e experimentos de submissão podem ter escalas diferentes que o próprio README não especifica.

## Como verificar
Os números do sample report constam da seção Overview/Sample Report do README oficial.

## Conexões
- [[fuzzbench-integration-flow]] — Veja também: Integração e aceite: do guia ao experimento.
- [[fuzzbench-oss-fuzz-benchmarks]] — Veja também: Benchmarks herdados do OSS-Fuzz.

## Fontes
- [FuzzBench — README oficial](https://raw.githubusercontent.com/google/fuzzbench/master/README.md) — README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.; consultado em 2026-10-03.
- [FuzzBench — Sample Report oficial](https://www.fuzzbench.com/reports/sample/index.html) — Relatório de exemplo oficial do FuzzBench com 10 fuzzers, 24 benchmarks, 20 trials de 24 horas e dados brutos em CSV.; consultado em 2026-10-03.
