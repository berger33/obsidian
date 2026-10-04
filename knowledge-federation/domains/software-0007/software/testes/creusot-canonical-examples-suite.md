---
id: software.testes.tranche25.001913
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

# Os cinco exemplos de entrada na suíte oficial do repositório

## Em uma frase
Na seção Examples of Verification, o README convida o leitor a inspecionar cinco arquivos da suíte para ver como é um programa verificado com Creusot: Zeroing out a vector (examples/all_zero.rs), Binary search on Vectors (examples/binary_search.rs), Sorting a vector (examples/gnome_sort.rs), IterMut (examples/iterators/02_iter_mut.rs) e Normalizing If-Then-Else Expressions (examples/ite_normalize.rs), apontando ainda as pastas examples e tests/should_succeed para mais casos.

## Por que importa
Verificação dedutiva de empréstimos mutáveis (borrows) em Rust — como iteradores mutáveis e mutação in-place de vetores — é historicamente difícil em outras linguagens devido ao aliasing de ponteiros; o sistema de tipos de propriedade do Rust simplifica esse raciocínio, como demonstram all_zero.rs, gnome_sort.rs e 02_iter_mut.rs.

## Como funciona
Ao aprender a escrever invariantes no Creusot, siga a progressão sugerida pelos cinco exemplos oficiais: comece por all_zero.rs e binary_search.rs, avance para ordenação em gnome_sort.rs e mutação via iteradores em 02_iter_mut.rs, e use tests/should_succeed como catálogo de padrões idiomáticos.

## Exemplo
O exemplo examples/binary_search.rs mostra como especificar e provar busca binária sobre vetores Rust sem estouro de cálculo de ponto médio nem acesso fora dos limites.

## Limites e trade-offs
Os arquivos em examples/ e tests/should_succeed acompanham a versão do compilador e da biblioteca de especificação do próprio repositório; ao estudá-los, use a mesma revisão do checkout instalado.

## Como verificar
Conferi a seção Examples of Verification no README oficial do Creusot.

## Conexões
- [[creusot-safety-vs-functional-correctness]] — Veja também: Dois degraus de verificação: ausência de panics/overflows e correção funcional por anotações.
- [[creusot-real-world-projects-creusat-krabka]] — Veja também: Projetos reais verificados com Creusot: CreuSAT e Krabka.

## Fontes
- [Creusot — README oficial](https://raw.githubusercontent.com/creusot-rs/creusot/master/README.md) — README oficial do Creusot com verificação dedutiva para Rust, tradução para Coma na plataforma Why3, exemplos da suíte, projetos CreuSAT e Krabka, instalação via rustup/opam/./INSTALL, upgrade e publicação ICFEM'22.; consultado em 2026-10-03.
- [Repositório oficial creusot-rs/creusot](https://github.com/creusot-rs/creusot) — Repositório oficial do Creusot no GitHub com ARCHITECTURE.md, examples/, tests/should_succeed e CONTRIBUTING.md.; consultado em 2026-10-03.
