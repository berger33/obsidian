---
id: software.testes.tranche25.001911
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md", "https://github.com/creusot-rs/creusot"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# A arquitetura de tradução: de Rust para Coma e a plataforma Why3

## Em uma frase
Ainda na seção About, o README explica como a ferramenta funciona por dentro: o Creusot traduz o código Rust para Coma, uma linguagem intermediária de verificação da plataforma Why3 (why3.org), permitindo que os usuários aproveitem todo o poder do Why3 para descarregar de forma (semi-)automática as condições de verificação (verification conditions), com detalhes técnicos adicionais em ARCHITECTURE.md.

## Por que importa
Construir um verificador dedutivo diretamente do MIR do Rust para um único solver SMT limitaria a automação de provas; ao compilar para a linguagem intermediária Coma sobre o Why3, o Creusot reutiliza um ecossistema maduro de geração de VCs, transformações de prova e múltiplos provadores automáticos e interativos.

## Como funciona
Escreva o código e as especificações em Rust, acione o Creusot para traduzir o programa para Coma e utilize a infraestrutura do Why3 para despachar as obrigações de prova aos solvers configurados; consulte ARCHITECTURE.md quando precisar entender os detalhes da tradução.

## Exemplo
Uma função Rust anotada é compilada pelo pipeline do Creusot para um módulo Coma, a partir do qual o Why3 gera as condições de verificação que provam ausência de overflow e respeito às pós-condições.

## Limites e trade-offs
Como o Creusot depende da plataforma Why3 e do ecossistema OCaml por baixo, o ambiente de instalação inclui o gerenciador de pacotes opam além do toolchain Rust.

## Como verificar
Conferi o segundo e o terceiro parágrafos da seção About no README oficial do Creusot.

## Conexões
- [[creusot-what-it-is]] — Veja também: Creusot: verificador dedutivo para código Rust.
- [[creusot-safety-vs-functional-correctness]] — Veja também: Dois degraus de verificação: ausência de panics/overflows e correção funcional por anotações.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
