---
id: software.testes.tranche23.001702
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

# cargo fuzz init: o diretório fuzz dentro (ou fora) do workspace

## Em uma frase
O comando cargo fuzz init prepara o projeto de fuzzing para o seu crate; o README oficial destaca a decisão estrutural: por default o diretório fuzz gerado é parte do workspace existente — e para crates em workspace é preciso adicionar fuzz à lista workspace.members do Cargo.toml raiz — ou você declara workspace independente com cargo fuzz init --fuzzing-workspace=true.

## Por que importa
A escolha do workspace muda o build do repositório inteiro: como membro, o target entra no check de todo mundo que compila o repo; como workspace separado, o fuzzing fica fora do caminho crítico do build normal.

## Como funciona
O tutorial do Rust Fuzz Book mostra a convenção do resultante: source do target em fuzz/fuzz_targets/nome.rs, arquivos gerados pelo init recomendados no versionamento ("generally a good idea to check in the files"), e um target inicial já criado para você editar.

## Exemplo
Rode o init em um crate, compare o Cargo.toml raiz antes e depois e abra fuzz/fuzz_targets/ — confirme o target gerado e o cargo fuzz list listando-o, como o tutorial demonstra.

## Limites e trade-offs
O book fala de check-in dos arquivos gerados, não define política para artefatos e corpus de execução (fuzz/artifacts e fuzz/corpus) — a convenção de versionar ou não esses diretórios continua decisão da equipe, não prescrição do init.

## Como verificar
Abra a seção init no README oficial (parágrafo do workspace.members) e o primeiro quarto do tutorial do Rust Fuzz Book, com o comando init e o caminho fuzz_targets.

## Conexões
- [[cargofuzz-platform-limits]] — Veja também: Restrições de plataforma: sanitizers pedem x86-64/AArch64, Unix e nightly.
- [[cargofuzz-target-anatomy]] — Veja também: Anatomia de um fuzz target: no_main, macro e fatia de bytes.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
