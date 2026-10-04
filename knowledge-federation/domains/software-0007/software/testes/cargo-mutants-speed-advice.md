---
id: software.testes.tranche21.001538
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

# cargo-mutants: acelerar builds para acelerar mutantes

## Em uma frase
Todo ganho de velocidade de cargo build e cargo test se multiplica na corrida, e o README cita o linker Mold no Linux por causa das ligações incrementais intensas.

## Por que importa
Mutação é um loop de build-teste-build-teste; o tempo de link é justamente o fator que mais degrada esse ciclo na prática.

## Como funciona
Meça o build antes de reclamar da corrida; considere Mold e mantenha os lints de aviso fora do caminho da mutação.

## Exemplo
O README recomenda não negar warnings estaticamente no código, deixando o RUSTFLAGS para quando o check específico interessar.

## Limites e trade-offs
Árvore com lint deny falha build contra mutantes e polui o resultado de check failed, sem nada dizer sobre os testes.

## Como verificar
Rode uma corrida curta com e sem flags de negação de warnings e confirme a diferença de destinos.

## Conexões
- [[cargo-mutants-output-directory]] — Veja também: cargo-mutants: o que há em mutants.out.
- [[cargo-mutants-hard-to-test]] — Veja também: cargo-mutants: funções de efeito difícil de testar.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
