---
id: software.testes.tranche24.001791
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

# Cobertura de hardware: Intel BTS/PT como motor de feedback

## Em uma frase
Entre os key features, o README lista "Feedback-Driven: Uses hardware (Intel BTS/PT) and software code coverage to evolve inputs" — o fuzzer aproveita os recursos de rastreamento de branch do hardware Intel (BTS/PT) além da instrumentação por software.

## Por que importa
Cobertura medida em hardware não depende de recompilar o alvo com instrumentação: abre caminho para fuzzar binários complexos com menos atrito de build e com menos distorção de performance, o que muda a taxa de execução efetiva em alvos grandes.

## Como funciona
Use a instrumentação por software (SanitizerCoverage via os wrappers) quando precisar de precisão de mapa; considere o caminho de hardware quando o alvo é caro de recompilar ou quando a sobrecarga do tracing por software compromete a vazão.

## Exemplo
Um binário compilado com o wrapper do próprio projeto já recebe cobertura de software; o modo hardware do README (BTS/PT) é o diferencial listado como capacidade nativa do motor.

## Limites e trade-offs
Os detalhes de quando cada fonte de cobertura é habilitada e os requisitos exatos de CPU não constam do README; a página USAGE.md linkada é o ponto de verificação.

## Como verificar
A linha de feedback do bloco "Key Features" do README oficial nomeia BTS/PT explicitamente.

## Conexões
- [[honggfuzz-what-it-is]] — Veja também: Honggfuzz: fuzzer evolutivo orientado a feedback.
- [[honggfuzz-persistent-mode]] — Veja também: Persistent fuzzing com 1M de iterações por segundo.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
