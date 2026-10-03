---
id: software.testes.tranche21.001535
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

# cargo-mutants: ver mutantes sem rodá-los

## Em uma frase
As opções --list, --diff e --json mostram os mutantes gerados sem executar nada: a primeira a enumeração, a segunda a substituição em diff e a terceira a forma legível por máquina.

## Por que importa
Enumerar antes de rodar dimensiona a corrida e permite revisar a política de mutação em pull request, não só depois do susto.

## Como funciona
Rode --list --diff para ler as trocas previstas e --json quando um script for filtrar funções candidatas.

## Exemplo
A saída em JSON do list alimenta um job que reporta quantos mutantes novas funções vão gerar.

## Limites e trade-offs
A lista espelha a heurística atual de geração: ela não mostra o que você gostaria de mutar, e sim o que a ferramenta sabe fazer.

## Como verificar
Compare a contagem do --list com o total executado numa corrida curta e confirme a coerência.

## Conexões
- [[cargo-mutants-result-vocabulary]] — Veja também: cargo-mutants: caught, not caught, check e build failed.
- [[cargo-mutants-skip-annotation]] — Veja também: cargo-mutants: marcar funções para pular.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
