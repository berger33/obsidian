---
id: software.testes.tranche24.001805
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
fontes: ["https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md", "https://github.com/AFLplusplus/LibAFL"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Quatro backends de instrumentação declarados

## Em uma frase
A seção "Core concepts" lista os backends suportados para instrumentar o alvo: "SanitizerCoverage" (no crate libafl_targets), "Frida" (libafl_frida), "QEMU user-mode and system mode, including hooks for emulation" (libafl_qemu) e "TinyInst" (libafl_tinyinst, contribuído por elbiazo) — com a nota de que "it's easy to add custom instrumentation backends".

## Por que importa
Instrumentação é a fonte do sinal de cobertura; uma matriz de backends cobre do build com fontes (SanCov) ao binário fechado (Frida/QEMU), e o sistema de crates separados mantém cada backend substituível sem tocar no resto.

## Como funciona
Escolha por disponibilidade do alvo: fontes + clang para SanitizerCoverage; sem fontes, Frida in-process ou QEMU; Windows nativo, TinyInst — e um backend próprio cabe na mesma hierarquia de crates.

## Exemplo
O libafl_qemu tem até post de blog citado no README ("Hacking TMNF - Fuzzing the game server") sobre fuzzar um servidor de jogo binário — o caso real de backend sem código-fonte.

## Limites e trade-offs
A nota cobre os quatro nomes declarados; a maturidade relativa de cada backend muda por release — o README chama o libfuzzer_libpng de "best-tested", o que dimensiona o estado dos demais.

## Como verificar
A lista de backends e seus crates aparece na seção Core concepts do README oficial.

## Conexões
- [[libafl-no-std-embedded]] — Veja também: no_std: fuzzador dentro de firmware e hypervisor.
- [[libafl-build-deps]] — Veja também: Dependências declaradas: LLVM 15–18, just e o toolchain certo.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
