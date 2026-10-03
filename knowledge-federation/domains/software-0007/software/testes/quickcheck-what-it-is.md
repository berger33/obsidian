---
id: software.testes.tranche25.001940
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

# quickcheck em Rust: testes baseados em propriedades e shrinking por busca binária

## Em uma frase
O README oficial apresenta a crate quickcheck como uma forma de fazer testes baseados em propriedades (property-based testing) usando entradas geradas aleatoriamente: a crate sabe gerar e encolher (shrink) inteiros, floats, tuplas, booleanos, listas, strings, options e results; quando uma propriedade falha (por erro em tempo de execução como index out-of-bounds ou por retornar falso), as entradas são encolhidas automaticamente para encontrar um contraexemplo menor.

## Por que importa
Escrever exemplos manuais raramente exercita combinações estranhas de listas vazias, números negativos e fronteiras; ao fornecer apenas uma função de propriedade, o quickcheck gera centenas de entradas aleatórias e, se achar uma falha, reduz a entrada por busca binária — a mesma estratégia usada no QuickCheck de Koen Claessen para Haskell.

## Como funciona
Escreva uma função que receba argumentos de tipos que implementam Arbitrary e retorne se a propriedade se manteve válida; deixe o quickcheck gerar as entradas e reduzir automaticamente qualquer falha encontrada.

## Exemplo
No exemplo inicial do README, a propriedade verifica que inverter um vetor duas vezes devolve o próprio vetor: xs == reverse(&reverse(&xs)) para xs: Vec<u32>.

## Limites e trade-offs
O README destaca na seção Alternative Rust crates que a crate proptest melhora o conceito de shrinking; se você tiver problemas ou frustrações com o shrinking baseado em tipos do quickcheck, o próprio autor recomenda experimentar o proptest.

## Como verificar
Conferi os dois parágrafos de abertura e a seção Alternative Rust crates no README oficial de BurntSushi/quickcheck.

## Conexões
- [[quickcheck-macro-vs-attribute]] — Veja também: Duas formas de declarar propriedades: a macro quickcheck! e o atributo #[quickcheck].

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
