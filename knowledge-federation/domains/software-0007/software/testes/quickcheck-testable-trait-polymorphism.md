---
id: software.testes.tranche25.001945
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

# Por que propriedades são polimórficas: o trait Testable e a função quickcheck

## Em uma frase
Na seção Discarding test results (or, properties are polymorphic!), o README mostra a assinatura pub fn quickcheck<A: Testable>(f: A) e a definição pub trait Testable { fn result(&self, &mut Gen) -> TestResult; }: qualquer tipo que consiga produzir um TestResult a partir de uma fonte de aleatoriedade (&mut Gen) é testável, incluindo bool e funções cujos parâmetros implementam Arbitrary + Debug e cujo retorno também implementa Testable.

## Por que importa
Esse desenho polimórfico explica como a função quickcheck aceita funções com diferentes números de argumentos e diferentes tipos de retorno (bool ou TestResult) sem duplicar o motor de execução: cada camada de função consome um argumento Arbitrary + Debug do gerador Gen e delega ao retorno Testable.

## Como funciona
Use retorno bool quando todo valor do tipo de entrada for válido para a propriedade, e troque o tipo de retorno da função para TestResult quando precisar codificar mais informações sobre o desfecho do caso gerado (como descartar entradas fora do subconjunto desejado).

## Exemplo
A implementação base mostrada no README converte um booleano diretamente com impl Testable for bool { fn result(&self, _: &mut Gen) -> TestResult { TestResult::from_bool(*self) } }, enquanto impl Testable for TestResult apenas clona o resultado.

## Limites e trade-offs
Para que uma função seja aceita como Testable, todos os seus tipos de parâmetro precisam implementar tanto Arbitrary (para gerar e encolher valores) quanto Debug (para imprimir o contraexemplo em caso de falha).

## Como verificar
Conferi a explicação de pub fn quickcheck<A: Testable> e pub trait Testable na seção Discarding test results do README oficial.

## Conexões
- [[quickcheck-arbitrary-compatibility-caveat]] — Veja também: Compatibilidade SemVer: implementações de Arbitrary podem mudar e achar bugs novos.
- [[quickcheck-discarding-test-results]] — Veja também: Descartar entradas fora do subdomínio com TestResult::discard() e TestResult::from_bool.

## Fontes
- [quickcheck — README oficial](https://raw.githubusercontent.com/BurntSushi/quickcheck/master/README.md) — README oficial da crate quickcheck com property-based testing, shrinking por busca binária, macro quickcheck! e atributo #[quickcheck], RUST_LOG=quickcheck, política de MSRV 1.85.0, compatibilidade de Arbitrary e trait Testable com TestResult::discard.; consultado em 2026-10-03.
- [Crate quickcheck no docs.rs](https://docs.rs/quickcheck) — Documentação oficial da API da crate quickcheck no docs.rs.; consultado em 2026-10-03.
