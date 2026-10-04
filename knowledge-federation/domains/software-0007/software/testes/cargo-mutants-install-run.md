---
id: software.testes.tranche21.001531
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/sourcefrog/cargo-mutants", "https://crates.io/crates/cargo-mutants"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo-mutants: instalar e disparar

## Em uma frase
cargo install cargo-mutants publica o subcomando, e o trabalho começa com um simples cargo mutants na raiz do crate, sem tocar no código.

## Por que importa
A promessa de uso é custo zero de adoção: se a árvore bem testada não render achados, pelo menos não cobrou setup para isso.

## Como funciona
Instale o subcomando, entre na árvore Rust e deixe a corrida baseline-then-mutants acontecer; o resumo vem por função mutada.

## Exemplo
O resultado no terminal lista cada substituição com o nome do arquivo e a posição de origem, facilitando abrir direto na linha.

## Limites e trade-offs
A árvore precisa compilar e testar limpa antes; um baseline quebrado consome a corrida em erro, não em análise.

## Como verificar
Execute com --dir apontando para um projeto seu e confirme que o baseline roda antes do primeiro mutante.

## Conexões
- [[cargo-mutants-what-it-finds]] — Veja também: cargo-mutants: funções que ninguém testa de verdade.
- [[cargo-mutants-side-effects]] — Veja também: cargo-mutants: perigo de efeitos colaterais.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
