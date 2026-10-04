---
id: software.testes.tranche23.001704
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
fontes: ["https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html", "https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# cargo fuzz run: lendo a saída do libFuzzer até o crash

## Em uma frase
O subcomando cargo fuzz run alvo começa a fuzzagem; o tutorial oficial interpreta o output como gerado pelo libFuzzer e exemplifica as linhas de progresso: número de execução, marcador NEW, cov (borda de cobertura), corp (entradas e bytes do corpus), exec/s e o que mudou de mutação (MS: EraseBytes, CopyPart etc.) — o output "looks like" exatamente aquilo enquanto o motor encontra caminhos novos.

## Por que importa
A métrica que importa durante uma campanha é a de cobertura: cov crescendo significa corpus interessante, e o book liga o entendimento da saída à seção output da documentação do próprio libFuzzer, apontada nominalmente no tutorial.

## Como funciona
O book fecha o ciclo com um crash real documentado: após milhares de execuções, a thread panicou em host.rs do rust-url com índice fora de limites, o ERROR deadly signal do libFuzzer apareceu, e o input ofensor foi gravado em fuzz/artifacts/<alvo>/crash-<hash> com o prefixo artifact_prefix mostrado no log e a linha Base64 do caso.

## Exemplo
Deixe o run do exemplo do tutorial contra o commit com bug do rust-url e localize as três coisas: uma linha NEW, o SUMMARY da falha e o arquivo crash- escrito — o book indica inclusive o pull request que corrigiu o bug (servo/rust-url#108) como link para "causes a panic".

## Limites e trade-offs
O exemplo do tutorial depende do estado versionado do repositório-alvo (um commit específico com o bug), não é para reproduzir em master atual; e o book recomenda AddressSanitizer ou similar "for better crash reports" — sem sanitizer o relatório é rudimentar, como o próprio log nota.

## Como verificar
Abra a seção de saída do tutorial do Rust Fuzz Book e confira o bloco de log, a frase sobre libFuzzer, o caminho artifact_prefix e a nota de sinalização rudimentar.

## Conexões
- [[cargofuzz-target-anatomy]] — Veja também: Anatomia de um fuzz target: no_main, macro e fatia de bytes.
- [[cargofuzz-list-add]] — Veja também: cargo fuzz list e add: múltiplos alvos por crate.

## Fontes
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
