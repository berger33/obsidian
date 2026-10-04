---
id: software.testes.tranche12.000619
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
fontes: ["https://rspec.info/features/3-13/rspec-core/helper-methods/let/", "https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: diferenciar `let` e `let!`

## Em uma frase
`let` memoiza um helper quando ele é acessado pela primeira vez em cada exemplo, enquanto `let!` também agenda sua avaliação por um hook antes do exemplo.

## Por que importa
Escolher avaliação tardia ou imediata altera quando side effects de setup acontecem e pode explicar diferenças entre exemplos que parecem usar a mesma fixture.

## Como funciona
Use `let` para valores puros e baratos que o exemplo pode não precisar; reserve `let!` para preparação cujo efeito precisa ocorrer antes das assertions, mantendo sua dependência explícita.

## Exemplo
Um exemplo pode criar um usuário somente ao chamar `user`; outro usa `let!` quando callbacks precisam observar o usuário antes de a primeira linha do corpo rodar.

## Limites e trade-offs
Efeitos em getters tornam a ordem de leitura importante, e uma cadeia de `let!` pode esconder setup que seria mais claro em `before`.

## Como verificar
Adicione uma observação ao construtor da fixture e confira se ocorre antes do corpo do teste somente nas declarações que precisam desse efeito.

## Conexões
- [[rspec-random-order-seed]] — Veja também: RSpec 3.13: reproduzir falhas de ordem aleatória.

## Fontes
- [RSpec 3.13 — let and let!](https://rspec.info/features/3-13/rspec-core/helper-methods/let/) — memoização lazy por exemplo e avaliação de let! por hook; consultado em 2026-10-02.
- [RSpec 3.13 — Before and after hooks](https://rspec.info/features/3-13/rspec-core/hooks/before-and-after-hooks/) — escopo e ordem de before/after hooks por exemplo e grupo; consultado em 2026-10-02.
