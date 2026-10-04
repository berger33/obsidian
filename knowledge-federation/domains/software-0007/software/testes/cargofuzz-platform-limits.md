---
id: software.testes.tranche23.001701
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
fontes: ["https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md", "https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Restrições de plataforma: sanitizers pedem x86-64/AArch64, Unix e nightly

## Em uma frase
O README lista as dependências duras do subcomando com franqueza: o libFuzzer precisa de suporte a sanitizers LLVM, então funciona apenas em x86-64 e Aarch64, apenas em sistemas Unix-like (Windows não), e exige um compiler nightly porque usa flags de linha de comando instáveis; adicionalmente, um compilador C++ com suporte a C++11 é necessário.

## Por que importa
Essas quatro linhas eliminam metade dos bugs de "por que não compila" no CI: jobs de fuzzing em Windows ou stable toolchain falham antes de qualquer teste, e a causa é projeto declarado, não configuração.

## Como funciona
A nota sobre C++ vem da necessidade de linkar runtime do sanitizer; as flags instáveis citadas são as do próprio rustc/cargo que o wrapper passa — por isso o pin em nightly — e a arquitetura lista cobre o suporte de instrumentação do compiler-rt, não o da linguagem Rust.

## Exemplo
Rode cargo fuzz run em um target simples numa toolchain stable e observe a recusa de compilação; repita com +nightly numa máquina Linux x86-64 e confirme que a mesma compilação passa.

## Limites e trade-offs
O README documenta as restrições no tempo do snapshot da página; suporte a mais plataformas depende do upstream LLVM/compiler-rt e não tem cronograma publicado pelo projeto — trate a lista como recorte atual, não sentença permanente.

## Como verificar
Confirme o parágrafo "Note: libFuzzer needs LLVM sanitizer support..." no README oficial, com as arquiteturas, o veto a Windows, a exigência de nightly e o C++11.

## Conexões
- [[cargofuzz-what-it-is]] — Veja também: cargo fuzz: o subcomando do cargo para libFuzzer.
- [[cargofuzz-init-workspace]] — Veja também: cargo fuzz init: o diretório fuzz dentro (ou fora) do workspace.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
