---
id: software.testes.tranche24.001790
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
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Honggfuzz: fuzzer evolutivo orientado a feedback

## Em uma frase
O README oficial define o Honggfuzz como "a security-oriented, feedback-driven, evolutionary fuzzer", um fuzzer de propósito geral que usa cobertura de código — de software e de hardware — para encontrar bugs, com engine multi-processo, multi-thread e suporte a persistent fuzzing "for extreme speed".

## Por que importa
A combinação das três palavras do lema importa: security-oriented significa que o alvo declarado são vulnerabilidades exploráveis; feedback-driven que a evolução dos inputs é guiada por sinais de execução; e evolutionary que o corpus cresce por mutação e seleção, não por geração cega.

## Como funciona
O motor executa o binário instrumentado com inputs mutados, mede cobertura (inclusive via hardware), mantém e expande o conjunto de inputs interessantes e distribui o trabalho entre processos e threads para ocupar todas as CPUs.

## Exemplo
Comece pelo binário alvo instrumentado e "honggfuzz -i corpus/ -- ./alvo ___FILE___": sem nenhum input inicial, a ferramenta evolui o corpus do zero.

## Limites e trade-offs
O README é sucinto por design; o detalhamento de opções vive em docs/USAGE.md, referenciado como a doc de uso avançado que esta nota apenas endereça.

## Como verificar
A definição, os três adjetivos e o modelo multi-processo/thread estão no topo do README oficial.

## Conexões
- [[honggfuzz-hardware-coverage]] — Veja também: Cobertura de hardware: Intel BTS/PT como motor de feedback.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Repositório oficial google/honggfuzz](https://github.com/google/honggfuzz) — Repositório oficial do Honggfuzz no GitHub com código-fonte, wrappers hfuzz_cc, exemplos e documentação.; consultado em 2026-10-03.
