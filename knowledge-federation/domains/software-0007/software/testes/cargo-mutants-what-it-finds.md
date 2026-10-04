---
id: software.testes.tranche21.001530
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

# cargo-mutants: funções que ninguém testa de verdade

## Em uma frase
A ferramenta substitui a implementação de funções candidatas por algo trivial e roda os testes: se tudo continua passando, a função não tem teste real.

## Por que importa
Cobertura conta o que foi alcançado; a mutação conta o que é asserido, e é a segunda pergunta que decide se um refactor seguro existe.

## Como funciona
Rode cargo mutants no diretório-fonte e trate cada NOT CAUGHT como buraco na suíte ou decisão documentada de pular a função.

## Exemplo
No exemplo do crate unix_mode, a função is_block_device sobreviveu porque ninguém testava o caso de bloco.

## Limites e trade-offs
Como a geração de mutantes é simples, falsos positivos e negativos convivem com os achados; o README assume essa fase com clareza.

## Como verificar
Mutar um módulo com teste de doctest e confirme que a contagem de pegos reflete os casos documentados.

## Conexões
- [[cargo-mutants-install-run]] — Veja também: cargo-mutants: instalar e disparar.

## Fontes
- [cargo-mutants — README oficial](https://github.com/sourcefrog/cargo-mutants) — proposta, resultados, skip e saída; consultado em 2026-10-03.
- [cargo-mutants — pacote no crates.io](https://crates.io/crates/cargo-mutants) — versões publicadas e metadados do pacote; consultado em 2026-10-03.
