---
id: software.testes.tranche24.001792
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

# Persistent fuzzing com 1M de iterações por segundo

## Em uma frase
O README destaca "Persistent Fuzzing: Test APIs directly in-process with iteration speeds up to 1M/sec" — em vez de reiniciar o processo do alvo a cada input, o Honggfuzz exercita a API diretamente dentro do processo, e o modo é acionado com -P no comando do README.

## Por que importa
O gargalo clássico de fuzzing de processo único é o fork/exec por input; o modo in-process remove esse custo, e o número do próprio README (até 1 milhão/seg) dimensiona a diferença que isso faz em alvos de parsing pequeno.

## Como funciona
Compile o alvo com o wrapper (hfuzz-clang), exponha um ponto de entrada que leia o input em processo e rode "honggfuzz -P -i input_dir/ -- ./my_target"; sem -P, o modo clássico trata o input via placeholder de arquivo.

## Exemplo
O par de comandos do README mostra o contraste: modo básico com "___FILE___" substituído pelo caminho do arquivo, e modo persistente sem o placeholder porque o alvo lê pela API interna.

## Limites e trade-offs
"up to 1M/sec" é o teto anunciado, não uma garantia: depende do alvo, da instrumentação e da máquina; alvos com setup por iteração caem muito abaixo disso.

## Como verificar
A seção Usage do README lista os dois modos lado a lado, e o feature bloco quantifica a velocidade do persistente.

## Conexões
- [[honggfuzz-hardware-coverage]] — Veja também: Cobertura de hardware: Intel BTS/PT como motor de feedback.
- [[honggfuzz-empty-corpus]] — Veja também: Começar do zero: corpus vazio que se auto-constrói.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
