---
id: software.testes.tranche21.001534
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

# cargo-mutants: caught, not caught, check e build failed

## Em uma frase
Cada mutante recebe um de quatro destinos: pego por teste, não pego, verificação de tipos que falhou ou compilação quebrada, cada qual com seu significado de cobertura.

## Por que importa
Ler a lista sem distinguir os quatro destinos confunde mutante inviável com teste ausente e contamina a fila de trabalho.

## Como funciona
Trate not caught como trabalho, caught como confirmação, e os dois failures como material para a ferramenta ou configuração, não para o backlog.

## Exemplo
O README sugere abrir mutants.out e o log por mutante para ver quais testes falharam em cada caught.

## Limites e trade-offs
check failed é inconclusivo por natureza: a substituição não tipa, então nada se pode afirmar sobre a suíte a partir dele.

## Como verificar
Conte os estados no resumo e confirme que um check failed não aparece na lista de pendências de teste.

## Conexões
- [[cargo-mutants-baseline-first]] — Veja também: cargo-mutants: baseline verde antes de mutar.
- [[cargo-mutants-list-diff-json]] — Veja também: cargo-mutants: ver mutantes sem rodá-los.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
