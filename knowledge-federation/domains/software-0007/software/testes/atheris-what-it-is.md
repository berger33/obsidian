---
id: software.testes.tranche23.001750
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://github.com/google/atheris/blob/master/native_extension_fuzzing.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Atheris: fuzzer coverage-guided para Python que também encosta no nativo

## Em uma frase
O README oficial define: "Atheris is a coverage-guided Python fuzzing engine. It supports fuzzing of Python code, but also native extensions written for CPython", construído sobre o libFuzzer — e, ao fuzzar código nativo, combinável com AddressSanitizer ou UndefinedBehaviorSanitizer para pegar bugs adicionais.

## Por que importa
Fuzzers puros de linguagem alta perdem o que importa no CPython: quase toda lib de parsing veloz é uma extensão C. O Atheris existe para a mutação guiada por cobertura atravessar a fronteira Python/C sem trocar de ferramenta.

## Como funciona
O modelo de execução é o do libFuzzer vestido de Python: você exporta uma função TestOneInput(data: bytes), o motor chama repetidamente com inputs mutados, e a cobertura é coletada instrumentando bytecode Python — com os extras de sanitizer quando o alvo é nativo.

## Exemplo
Rode o exemplo mínimo da página (instrument_imports, um parse qualquer, Setup, Fuzz) contra um parser do seu projeto e veja a contagem de execuções subir no terminal, no formato libFuzzer que a engine imprime.

## Limites e trade-offs
A definição é de engine para scripts de fuzz, não de serviço gerenciado: orquestração, corpus em escala e triagem continuam seus (ou do OSS-Fuzz, notado na página) — o escopo do README é o ciclo dentro do seu processo.

## Como verificar
Abra a primeira frase do README oficial e confirme as três peças: coverage-guided, Python mais extensões nativas, base libFuzzer com sanitizers.

## Conexões
- [[atheris-install-platform]] — Veja também: Instalação: pip com libFuzzer embutido, LLVM novo quando há nativo.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [Atheris — Native Extension Fuzzing](https://github.com/google/atheris/blob/master/native_extension_fuzzing.md) — documento dedicado à instrumentação de extensões nativas; consultado em 2026-10-03.
