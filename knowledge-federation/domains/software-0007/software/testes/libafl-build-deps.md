---
id: software.testes.tranche24.001806
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

# Dependências declaradas: LLVM 15–18, just e o toolchain certo

## Em uma frase
A seção de build especifica: Rust instalado direto de rust-lang.org (a recomendação é expressa: "not to use e.g. your Linux distribution package as this is likely outdated"), o mínimo suportado definido no Cargo.toml do crate libafl com rustup update stable como remédio, ferramentas LLVM "newer than LLVM 15.0.0 up to LLVM 18.1.3" (em Debian/Ubuntu, do apt.llvm.org) e o just para os fuzzers de fuzzers/; o build é cargo build --release, a API sale de cargo doc e o livro local roda com mdbook serve no diretório docs.

## Por que importa
A janela de LLVM com teto explícito (18.1.3) é informação de compatibilidade valiosa para imagens de CI: fora dela, o comportamento do build não é o que o projeto testou; e a MSRV por Cargo.toml é a consulta canônica em vez de tabela no README.

## Como funciona
Fixe no container de CI a versão de LLVM dentro da faixa do README, instale just, e antes de reclamar de erro de sintaxe verifique a MSRV corrente no Cargo.toml linkado — o README diz onde ela mora, não qual é.

## Exemplo
A sequência oficial: git clone do repositório, cargo build --release, cargo doc, cd docs && mdbook serve para o livro (marcado WIP).

## Limites e trade-offs
A janela de LLVM é a do momento do README; releases novas movem o teto — revalidar a faixa a cada upgrade é prática obrigatória que a nota assume como dinâmica.

## Como verificar
A seção "Building and installing" do README oficial lista as dependências e comandos citados.

## Conexões
- [[libafl-instrumentation-backends]] — Veja também: Quatro backends de instrumentação declarados.
- [[libafl-examples-first]] — Veja também: O caminho de partida: ler os exemplos, just run.

## Fontes
- [LibAFL — README oficial](https://raw.githubusercontent.com/AFLplusplus/LibAFL/main/README.md) — README oficial do LibAFL com conceitos centrais, LLMP, backends de instrumentação, no_std, dependências LLVM/Rust, exemplos em fuzzers/ e citação CCS '22.; consultado em 2026-10-03.
- [Repositório oficial AFLplusplus/LibAFL](https://github.com/AFLplusplus/LibAFL) — Repositório oficial do LibAFL no GitHub com crates modulares, exemplos em fuzzers/, livro mdBook e guias de depuração/contribuição.; consultado em 2026-10-03.
