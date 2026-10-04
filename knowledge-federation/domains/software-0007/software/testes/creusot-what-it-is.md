---
id: software.testes.tranche25.001910
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

# Creusot: verificador dedutivo para código Rust

## Em uma frase
A seção About do README oficial define o Creusot como um verificador dedutivo (deductive verifier) para código Rust: ele verifica que o código está livre de panics, overflows e falhas de asserção e, com a adição de anotações, permite ir além e provar que o código faz a coisa funcionalmente correta.

## Por que importa
Enquanto testes baseados em propriedades amostram entradas e model checkers limitados desenrolam laços até uma cota fixa, a verificação dedutiva prova teoremas matemáticos sobre o comportamento da função para entradas de tamanho arbitrário.

## Como funciona
Sem anotações extras de especificação, a análise já mira ausência de panics, estouros aritméticos e falhas de assert; adicionando contratos e invariantes na linguagem de especificação do Creusot (documentada em guide.creusot.rs e doc.creusot.rs/creusot_std), prova-se a correção funcional completa.

## Exemplo
Ao verificar uma rotina de busca ou ordenação em vetor, o Creusot prova não apenas que nenhum índice faz panic, mas também que o resultado retornado satisfaz a pós-condição de ordenação ou busca para qualquer tamanho válido de vetor.

## Limites e trade-offs
A verificação dedutiva é descrita pelo próprio README como "(semi)-automatically" descarregada no Why3: provas complexas exigem anotações de invariantes de laço e contratos escritas pelo desenvolvedor.

## Como verificar
Conferi a seção About e os badges de documentação no README oficial do repositório creusot-rs/creusot.

## Conexões
- [[creusot-coma-and-why3-pipeline]] — Veja também: A arquitetura de tradução: de Rust para Coma e a plataforma Why3.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
