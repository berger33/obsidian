---
id: software.testes.tranche12.000610
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
fontes: ["https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/", "https://rspec.info/features/3-13/rspec-expectations/composing-matchers/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: shared examples como contrato comportamental

## Em uma frase
Shared examples guardam comportamentos que podem ser executados no contexto de diferentes example groups.

## Por que importa
Um contrato comum ajuda a comparar implementações sem duplicar cada expectativa, desde que os grupos consumidores forneçam contexto equivalente.

## Como funciona
Declare o bloco com `shared_examples`, exija-o antes dos arquivos consumidores e passe parâmetros ou helpers locais apenas quando eles fizerem parte da variação do contrato.

## Exemplo
A mesma coleção de exemplos pode verificar métodos de classes Array e Set com expectativas sobre tamanho, inclusão e iteração.

## Limites e trade-offs
Um exemplo compartilhado também pode ocultar diferenças de pré-condição entre implementações; dependência implícita de arquivos carregados causa falha de descoberta.

## Como verificar
Execute cada consumidor isoladamente e confirme que o arquivo compartilhado foi carregado antes de registrar os grupos que o usam.

## Conexões
- [[rspec-include-vs-it-behaves-like]] — Veja também: RSpec 3.13: escolher a inclusão de exemplos compartilhados.

## Fontes
- [RSpec 3.13 — Shared examples](https://rspec.info/features/3-13/rspec-core/example-groups/shared-examples/) — inclusão de grupos compartilhados, parâmetros, carregamento e escopo; consultado em 2026-10-02.
- [RSpec 3.13 — Composing matchers](https://rspec.info/features/3-13/rspec-expectations/composing-matchers/) — composição de matchers em estruturas aninhadas e valores parciais; consultado em 2026-10-02.
