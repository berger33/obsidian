---
id: software.testes.tranche23.001708
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

# cargo fuzz coverage e onde a documentação real mora

## Em uma frase
O subcomando de medição declarada no README é cargo fuzz coverage <target>, que gera "coverage information on the fuzzed program"; a referência completa de flags fica em cargo fuzz --help, e o README aponta o Rust Fuzz Book em rust-fuzz.github.io como documentação de projeto — o book é o canônico, o README é o cartão de visita.

## Por que importa
Fuzzing sem leitura de cobertura é tiro no escuro: coverage mostra o que nunca foi alcançado e orienta o que o próximo alvo ou próximo corpus deve atacar — o subcomando existe para fechar o loop mutar-medir-escolher.

## Como funciona
O tutorial do book exemplifica a leitura de cobertura pelo log (o campo cov em cada linha NEW) como indicador de progresso do corpus; o coverage materializa a mesma contagem em forma navegável sobre o código-fonte.

## Exemplo
Abra o book na página do cargo-fuzz, siga a seção de coverage e compare com o campo cov das linhas NEW de um run seu — os números são o mesmo objeto visto ao vivo e post-mortem.

## Limites e trade-offs
O README descreve a saída como "coverage information" sem especificar formato (profraw, HTML, lcov); quem precisa integrar com ferramentas de visualização deve ler a página do book em vez de adivinhar flags a partir do one-liner.

## Como verificar
Abra a seção coverage do README oficial e a página do book a que ele encaminha (Documentation), confirmando a divisão de papel entre os dois documentos.

## Conexões
- [[cargofuzz-tmin-cmin]] — Veja também: Minificação local e global: tmin para um caso, cmin para o corpus.
- [[cargofuzz-trophy-license]] — Veja também: Troféus e licença: MIT mais Apache-2.0, bugs em crates famosos.

## Fontes
- [cargo-fuzz — README oficial](https://github.com/rust-fuzz/cargo-fuzz/blob/main/README.md) — instalação, plataformas, subcomandos, workspace e licenças; consultado em 2026-10-03.
- [Rust Fuzz Book — tutorial do cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) — init, alvo fuzz_target, saída, crash em artifacts e cargo fuzz list; consultado em 2026-10-03.
