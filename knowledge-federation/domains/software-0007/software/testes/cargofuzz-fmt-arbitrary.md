---
id: software.testes.tranche23.001706
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

# cargo fuzz fmt: o que aquele input arbitrário realmente é

## Em uma frase
O README oficial descreve o subcomando de inspeção: cargo fuzz fmt <target> <input> imprime a saída std::fmt::Debug de um test case, e destaca a utilidade quando o fuzz target aceita entrada Arbitrary — o tipo estruturado que o motor desserializa dos bytes crus.

## Por que importa
O gap entre o input binário do crash e o valor de alto nível que o target recebeu é o que atrasa triagens; o fmt fecha o gap sem regravar nada, mostrando a representação Debug do valor arbitrário reconstruído.

## Como funciona
O par natural é com os arquivos crash- da seção de artefatos: você pega o path gravado pelo run e passa como input ao fmt para ler o que o motor construiu a partir daqueles bytes.

## Exemplo
Depois de um crash em target Arbitrary, rode cargo fuzz fmt <alvo> fuzz/artifacts/<alvo>/crash-<hash> e compare o dump Debug com a asserção que falhou — a decisão de reproduzir com struct em vez de blob de bytes sai da leitura.

## Limites e trade-offs
O README define o fmt como impressão do Debug do test case, nada além disso — não documenta formatação custom nem consumo de stdin; fluxos fora do arquivo-para-Debug pedem --help do subcomando.

## Como verificar
Abra a entrada de seção fmt no README oficial (rust-fuzz/cargo-fuzz) e confirme a frase "Print the std::fmt::Debug output for a test case. Useful when your fuzz target takes an Arbitrary input!".

## Conexões
- [[cargofuzz-list-add]] — Veja também: cargo fuzz list e add: múltiplos alvos por crate.
- [[cargofuzz-tmin-cmin]] — Veja também: Minificação local e global: tmin para um caso, cmin para o corpus.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
