---
id: software.testes.tranche12.000611
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
fontes: ["https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/", "https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: escolher a inclusão de exemplos compartilhados

## Em uma frase
`include_examples` inclui o conteúdo no contexto corrente, enquanto `it_behaves_like` cria um grupo aninhado para o comportamento compartilhado.

## Por que importa
A diferença de escopo importa quando helpers ou `let` com o mesmo nome são definidos por mais de uma inclusão.

## Como funciona
Use inclusão direta quando o contexto não conflitar e prefira a forma aninhada quando parâmetros ou métodos compartilhados poderiam sobrescrever definições anteriores.

## Exemplo
Dois contratos de serialização podem fornecer `let(:payload)` diferentes; agrupá-los em contexts separados evita que a última definição altere exemplos do primeiro.

## Limites e trade-offs
Incluir várias vezes no mesmo escopo pode emitir warning e fazer a definição mais recente vencer, produzindo falha distante da inclusão original.

## Como verificar
Execute os exemplos com formato de documentação e investigue warnings de métodos duplicados antes de ignorá-los.

## Conexões
- [[rspec-shared-examples-contrato]] — Veja também: RSpec 3.13: shared examples como contrato comportamental.
- [[rspec-around-hook-envelope]] — Veja também: RSpec 3.13: `around` como envelope de um exemplo.

## Fontes
- [RSpec 3.13 — Shared examples](https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/) — inclusão de grupos compartilhados, parâmetros, carregamento e escopo; consultado em 2026-10-02.
- [RSpec 3.13 — Before and after hooks](https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/) — escopo e ordem de before/after hooks por exemplo e grupo; consultado em 2026-10-02.
