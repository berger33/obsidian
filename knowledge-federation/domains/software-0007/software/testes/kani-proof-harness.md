---
id: software.testes.tranche24.001784
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
fontes: ["https://raw.githubusercontent.com/model-checking/kani/main/README.md", "https://model-checking.github.io/kani/kani-tutorial.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O harness de prova: kani::any e assert

## Em uma frase
O exemplo central do README define o padrão de uso: uma função anotada com #[kani::proof] que cria uma entrada não-determinística via "let input: u8 = kani::any()", chama a função sob verificação e conclui com assert!(meets_specification(input, output)); a ferramenta então "tentará provar que todas as entradas válidas produzem saídas que satisfazem a especificação, sem panic ou comportamento inesperado".

## Por que importa
Esse formato inverte a economia do teste: em vez de adivinhar entradas interessantes, o autor declara o espaço inteiro (u8 aqui: 256 casos, mas o verificador opera em espaço de estados, não em loops) e a asserção vira contrato verificável; a entrada não-determinística é o ponto exato onde a especificação passa a ser checagem.

## Como funciona
Para uma função de um byte de entrada, anote a prova, use kani::any() com o tipo certo, chame o código real e afirme a propriedade; a mensagem de falha devolve o valor concreto de input que viola — um contraexemplo minimizado para reproduzir em teste de regressão.

## Exemplo
#[kani::proof] fn check_my_property() com input: u8 = kani::any() exatamente como o README; para validar a forma, compare com o tutorial oficial que o README recomenda para exemplos maiores.

## Limites e trade-offs
O README descreve o exemplo como "simples" e manda seguir o tutorial para o uso realista; harnesses de funções puras de um byte não exploram as dificuldades de estado, loops não limitados nem estruturas de dados grandes que o livro aborda.

## Como verificar
O esqueleto de código e a frase de objetivo da prova vieram copiados da seção "How to use Kani" do README oficial.

## Conexões
- [[kani-install]] — Veja também: Instalação: cargo install mais o setup explícito.
- [[kani-vs-testing]] — Veja também: Verificação com cara de teste, garantia de outra ordem.

## Fontes
- [Kani Rust Verifier — README oficial](https://raw.githubusercontent.com/model-checking/kani/main/README.md) — README oficial do Kani Rust Verifier com verificação de safety e correctness, instalação, harness #[kani::proof], GitHub Action, citação ASE 2026 e licenciamento.; consultado em 2026-10-03.
- [The Kani Rust Verifier — Tutorial oficial](https://model-checking.github.io/kani/kani-tutorial.html) — Documentação oficial do Kani Rust Verifier sobre harnesses de prova, undefined behavior, instalação e integração em CI.; consultado em 2026-10-03.
