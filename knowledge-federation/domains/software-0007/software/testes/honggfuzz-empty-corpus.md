---
id: software.testes.tranche24.001793
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
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz/blob/master/docs/USAGE.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Começar do zero: corpus vazio que se auto-constrói

## Em uma frase
O README promete "Easy: Can start with an empty corpus and automatically build a valid input set" — a ferramenta é capaz de partir de um diretório de inputs vazio e construir sozinha um conjunto de entradas válidas.

## Por que importa
Para formatos com estrutura forte, a maioria dos fuzzers exige seeds que passem do primeiro parser; a promessa de corpus inicial zero reduz o atrito de começar a fuzzar um formato novo, transferindo para o motor o trabalho de descobrir entradas que exercitam código.

## Como funciona
Crie o diretório, deixe-o vazio e aponte "-i input_dir/" no comando; a evolução guiada por cobertura constrói o corpus — e o mesmo diretório continua recebendo os inputs interessantes descobertos.

## Exemplo
O exemplo canônico do README roda exatamente assim: ./honggfuzz -i input_dir/ -- ./my_target ___FILE___ com input_dir/ vazio.

## Limites e trade-offs
Para alvos complexos, seeds reais de corpus público aceleram muito; a nota registra a capacidade declarada de partir do zero, não a recomendação de fazê-lo sempre.

## Como verificar
A frase do empty corpus está na lista "Key Features" do README oficial, e o exemplo de uso confirma o diretório vazio.

## Conexões
- [[honggfuzz-persistent-mode]] — Veja também: Persistent fuzzing com 1M de iterações por segundo.
- [[honggfuzz-ptrace-monitoring]] — Veja também: ptrace: detectar sinais sequestrados e crashes escondidos.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
