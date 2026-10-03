---
id: software.testes.tranche24.001846
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

# Como ler um relatório de fuzzers, segundo o próprio serviço

## Em uma frase
O README oferece duas recomendações explícitas de análise para quem lê relatórios: "Checking the strengths and weaknesses of a fuzzer against various benchmarks" e "Looking at aggregate results to understand the overall significance of the result" — micro antes, macro depois.

## Por que importa
O desempenho de um fuzzer raramente é uniforme: um motor excelente em binary-only pode perder em targets pequenos com feedback de cobertura fino; a recomendação de ler a disagregação antes do agregado existe porque números gerais escondem exatamente a estrutura que decide adoção no seu contexto.

## Como funciona
Na leitura do relatório: primeiro o per-benchmark (onde o candidato vence/perde e por margem), depois o agregado — e só então a decisão de usar, combinar ou ignorar o fuzzer para o workload local.

## Exemplo
Um fuzzer 2º colocado no agregado mas 1º nos alvos de rede pode ser a escolha certa para um projeto de protocolos — a ordem de leitura recomendada é o que torna esse trade-off visível.

## Limites e trade-offs
O README prescreve heurística de leitura, não método completo; profundidade estatística fica na biblioteca de reporting e nos documentos linkados do projeto.

## Como verificar
Os dois bullets de recomendação estão na seção Sample Report do README oficial.

## Conexões
- [[fuzzbench-reporting-library]] — Veja também: A biblioteca de reporting com estatística embutida.
- [[fuzzbench-periodic-reports]] — Veja também: Relatórios públicos e recorrentes.

## Fontes
- [FuzzBench — README oficial](https://raw.githubusercontent.com/google/fuzzbench/master/README.md) — README oficial do FuzzBench com definição do serviço gratuito, API de integração, benchmarks OSS-Fuzz, biblioteca de reporting e escala do sample report.; consultado em 2026-10-03.
- [FuzzBench — Sample Report oficial](https://www.fuzzbench.com/reports/sample/index.html) — Relatório de exemplo oficial do FuzzBench com 10 fuzzers, 24 benchmarks, 20 trials de 24 horas e dados brutos em CSV.; consultado em 2026-10-03.
