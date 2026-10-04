---
id: software.testes.tranche25.001947
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
fontes: ["https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md", "https://docs.rs/quickcheck"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Como funciona o shrinking no quickcheck: busca binária sobre listas e números

## Em uma frase
Logo na abertura do README oficial, o autor explica que, quando uma propriedade falha (seja por um panic/erro em tempo de execução como index out-of-bounds, seja por retornar falso), as entradas são encolhidas ("shrunk") para encontrar um contraexemplo menor, e que as estratégias de shrinking para listas e números usam busca binária para cobrir o espaço de entradas rapidamente.

## Por que importa
Um vetor aleatório de 80 inteiros que provoca um bug é difícil de depurar no olho; o shrinking por busca binária corta fatias da lista e reduz a magnitude dos números em passos logarítmicos até entregar, por exemplo, um vetor de um ou dois elementos mínimos que ainda dispara a mesma falha.

## Como funciona
Ao escrever propriedades ou implementar Arbitrary para seus próprios tipos em Rust, forneça um método de shrink que produza candidatos progressivamente menores para que o motor do quickcheck possa minimizar falhas automaticamente.

## Exemplo
Se uma função faz panic apenas quando recebe um vetor contendo ao menos dois elementos negativos, o quickcheck reduz uma entrada grande sorteada até um par mínimo de números negativos pequenos.

## Limites e trade-offs
Como no modelo clássico do QuickCheck de Haskell o shrinking depende apenas do tipo do valor (via trait Arbitrary) e não de como o valor foi construído pelo gerador, transformações complexas podem encolher pior do que no modelo de estratégias do proptest — ponto que o próprio README destaca na comparação entre as duas crates.

## Como verificar
Conferi os dois primeiros parágrafos e a seção Alternative Rust crates no README oficial.

## Conexões
- [[quickcheck-discarding-test-results]] — Veja também: Descartar entradas fora do subdomínio com TestResult::discard() e TestResult::from_bool.
- [[quickcheck-vs-proptest-and-fuzzing-alternatives]] — Veja também: Quando escolher quickcheck, quando escolher proptest e quando ir para fuzzing.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
