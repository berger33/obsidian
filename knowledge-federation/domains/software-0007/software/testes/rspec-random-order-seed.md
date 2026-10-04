---
id: software.testes.tranche12.000618
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://rspec.info/features/3-13/rspec-core/command-line/order/", "https://rspec.info/features/3-13/rspec-core/command-line/tag/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: reproduzir falhas de ordem aleatória

## Em uma frase
RSpec pode embaralhar grupos e exemplos usando uma seed que permite repetir a ordem de uma execução.

## Por que importa
Randomização encontra acoplamento oculto, enquanto a seed dá um caminho concreto para investigar o primeiro teste que deixou estado contaminado.

## Como funciona
Ative `--order rand` em uma execução de diagnóstico e preserve o número exibido; use `--order rand:SEED` ou `--seed SEED` para reproduzir.

## Exemplo
Uma falha que depende de configuração deixada por um exemplo anterior pode aparecer somente quando a ordem aleatória coloca os dois casos em sequência.

## Limites e trade-offs
A seed controla a ordem aleatória do RSpec, não outras fontes como relógio, rede ou aleatoriedade criada pela aplicação sem semear.

## Como verificar
Registre a seed no ticket de falha, repita no mesmo conjunto de arquivos e depois execute os testes isoladamente para localizar estado compartilhado.

## Conexões
- [[rspec-metadata-tag-selection]] — Veja também: RSpec 3.13: filtrar exemplos por metadata.
- [[rspec-let-let-bang-lazy]] — Veja também: RSpec 3.13: diferenciar `let` e `let!`.

## Fontes
- [RSpec 3.13 — Randomized order](https://rspec.info/features/3-13/rspec-core/command-line/order/) — randomização de grupos/exemplos e reprodução por seed; consultado em 2026-10-02.
- [RSpec 3.13 — Metadata filtering](https://rspec.info/features/3-13/rspec-core/command-line/tag/) — seleção e exclusão de exemplos por tags/metadata; consultado em 2026-10-02.
