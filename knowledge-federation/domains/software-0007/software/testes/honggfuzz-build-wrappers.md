---
id: software.testes.tranche24.001796
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

# O build: make, hfuzz_cc e os wrappers de compilação

## Em uma frase
A compilação oficial é um "make" na raiz, que cria "compilation wrappers" em hfuzz_cc/; o passo 1 do uso é compilar o alvo com esses wrappers — hfuzz-clang para C e hfuzz-clang++ para C++ — para "automatically add instrumentation" ao binário.

## Por que importa
O modelo wrapper é o mesmo do AFL/libFuzzer que a comunidade conhece: você não muda o build system do alvo, troca o compilador; isso torna a instrumentação uma decisão reversível, controlável por variável de ambiente do CI sem tocar no Makefile da vítima.

## Como funciona
Rode make no checkout (após instalar as dependências do SO), e então "make CC=./hfuzz_cc/hfuzz-clang CXX=./hfuzz_cc/hfuzz-clang++" no projeto alvo para obter o binário instrumentado — a linha de compilação do README mostra o uso direto com -o alvo.

## Exemplo
./hfuzz_cc/hfuzz-clang -o my_target my_target.c é o exemplo literal do README para C; para C++, o par com hfuzz-clang++.

## Limites e trade-offs
O README documenta o wrapper como caminho padrão; targets em outros sistemas de build (CMake, Meson) seguem o mesmo princípio de trocar CC/CXX, que a nota menciona como prática sem afirmar que o README a descreva.

## Como verificar
Os comandos de build e de compilação do alvo são as listas literais das seções Build e Usage do README oficial.

## Conexões
- [[honggfuzz-platform-support]] — Veja também: Seis famílias de SO: do Linux ao Windows via Cygwin.
- [[honggfuzz-input-placeholder]] — Veja também: ___FILE___: o contrato do input por arquivo.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
