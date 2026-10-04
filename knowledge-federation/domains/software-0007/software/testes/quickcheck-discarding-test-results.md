---
id: software.testes.tranche25.001946
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
fontes: ["https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md", "https://github.com/BurntSushi/quickcheck"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Descartar entradas fora do subdomínio com TestResult::discard() e TestResult::from_bool

## Em uma frase
Continuando na seção Discarding test results, o README resolve o problema de testar uma propriedade que só vale para um subconjunto das entradas possíveis: como retornar bool só permite aprovar ou reprovar, a função passa a retornar TestResult diretamente — retornando TestResult::discard() quando a entrada cai fora do subconjunto desejado e TestResult::from_bool(...) quando a entrada é válida.

## Por que importa
Se uma propriedade com pré-condição simplesmente retornasse true para entradas inválidas, o teste poderia "passar" gerando 100 entradas descartadas sem nunca exercitar a lógica real; TestResult::discard() instrui o quickcheck a registrar que aquele caso não conta nem como sucesso nem como falha e a tentar gerar outra entrada.

## Como funciona
Quando uma propriedade tiver uma pré-condição simples sobre a entrada gerada, declare o retorno da função como TestResult, retorne TestResult::discard() se a pré-condição não for satisfeita e conclua com TestResult::from_bool(condicao_da_propriedade).

## Exemplo
O exemplo completo do README (também em examples/reverse_single.rs) testa que reverter um vetor de tamanho 1 devolve o próprio vetor: fn prop(xs: Vec<isize>) -> TestResult { if xs.len() != 1 { return TestResult::discard() } TestResult::from_bool(xs == reverse(&xs)) }.

## Limites e trade-offs
Descartar entradas demais com uma condição muito restritiva (como xs.len() == 1 sobre vetores de tamanho aleatório) faz o gerador desperdiçar quase todas as tentativas; quando o subdomínio for muito estreito, é melhor gerar diretamente o tipo restrito do que depender de TestResult::discard().

## Como verificar
Conferi o exemplo de TestResult::discard() e a referência a examples/reverse_single.rs no README oficial.

## Conexões
- [[quickcheck-testable-trait-polymorphism]] — Veja também: Por que propriedades são polimórficas: o trait Testable e a função quickcheck.
- [[quickcheck-binary-search-shrinking]] — Veja também: Como funciona o shrinking no quickcheck: busca binária sobre listas e números.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Repositório oficial BurntSushi/quickcheck](https://github.com/BurntSushi/quickcheck) — Repositório oficial do quickcheck para Rust no GitHub com código-fonte, quickcheck_macros e examples/reverse_single.rs.; consultado em 2026-10-03.
