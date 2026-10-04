---
id: software.testes.tranche12.000612
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
fontes: ["https://rspec.info/features/3-13/rspec-core/hooks/around-hooks/", "https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: `around` como envelope de um exemplo

## Em uma frase
Um hook `around(:example)` recebe o objeto de exemplo e envolve a execução que ocorre em `example.run`.

## Por que importa
O bloco permite preparar e limpar recursos em torno do exemplo, inclusive quando a ordem de ações precisa permanecer explícita.

## Como funciona
Coloque preparação antes de `example.run` e finalize depois, preservando o fluxo de exceção sem executar o exemplo duas vezes.

## Exemplo
Um hook pode abrir uma transação antes do exemplo e fechá-la no bloco de saída depois que assertions terminarem.

## Limites e trade-offs
`around` não substitui hooks de contexto e uma implementação que não chama `run` pode impedir completamente a execução do exemplo.

## Como verificar
Registre marcadores antes e depois, force falha dentro do exemplo e confirme a ordem e a execução única do bloco recebido.

## Conexões
- [[rspec-include-vs-it-behaves-like]] — Veja também: RSpec 3.13: escolher a inclusão de exemplos compartilhados.
- [[rspec-before-after-scope]] — Veja também: RSpec 3.13: limitar hooks ao escopo necessário.

## Fontes
- [RSpec 3.13 — Around hooks](https://rspec.info/features/3-13/rspec-core/hooks/around-hooks/) — invocação de example.run e posição dos hooks em torno do exemplo; consultado em 2026-10-02.
- [RSpec 3.13 — Before and after hooks](https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/) — escopo e ordem de before/after hooks por exemplo e grupo; consultado em 2026-10-02.
