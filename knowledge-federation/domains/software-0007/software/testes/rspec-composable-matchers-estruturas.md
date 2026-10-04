---
id: software.testes.tranche12.000614
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
fontes: ["https://rspec.info/features/3-13/rspec-expectations/composing-matchers/", "https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: compor matchers para respostas estruturadas

## Em uma frase
Matchers compostos permitem descrever partes importantes de uma estrutura aninhada sem exigir que todo valor coincida literalmente.

## Por que importa
Expectativas focadas nos campos do contrato resistem melhor a dados auxiliares que mudam sem alterar o comportamento relevante.

## Como funciona
Use `match`, `include` ou `contain_exactly` com matchers internos para validar tipos, faixas e valores parciais em hashes e coleções.

## Exemplo
Uma resposta pode exigir identificador inteiro e estado textual válido sem fixar timestamps ou metadados que variam por request.

## Limites e trade-offs
Composição não deve enfraquecer a assertion até aceitar respostas inválidas, nem transformar uma regra complexa em expressão impossível de diagnosticar.

## Como verificar
Faça uma cópia da resposta com um campo essencial incorreto e confira se a mensagem mostra qual matcher interno não foi satisfeito.

## Conexões
- [[rspec-before-after-scope]] — Veja também: RSpec 3.13: limitar hooks ao escopo necessário.
- [[rspec-verifying-doubles-interface]] — Veja também: RSpec 3.13: doubles que verificam a interface.

## Fontes
- [RSpec 3.13 — Composing matchers](https://rspec.info/features/3-13/rspec-expectations/composing-matchers/) — composição de matchers em estruturas aninhadas e valores parciais; consultado em 2026-10-02.
- [RSpec 3.13 — Matching arguments](https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/) — restrições de argumentos de expectativas e stubs de mensagens; consultado em 2026-10-02.
