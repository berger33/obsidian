---
id: software.testes.tranche12.000615
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
fontes: ["https://rspec.info/features/3-13/rspec-mocks/verifying-doubles/", "https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec 3.13: doubles que verificam a interface

## Em uma frase
Verifying doubles checam se métodos configurados existem na classe ou objeto representado, reduzindo divergências entre mock e implementação.

## Por que importa
Um double permissivo pode continuar aceitando uma chamada depois que o método real foi renomeado, deixando o teste passar com uma interface fictícia.

## Como funciona
Use `instance_double` ou `class_double` associado à constante concreta e mantenha a definição da classe carregada quando o RSpec precisa validar a interface.

## Exemplo
Uma dependência de gateway pode ser representada por um instance double que rejeita uma expectativa para `chargee` quando a interface declara apenas `charge`.

## Limites e trade-offs
Verificação de método não prova que o comportamento do colaborador real está correto, e classes carregadas tardiamente podem limitar o que o double consegue checar.

## Como verificar
Renomeie um método da interface em uma cópia local e confirme que o teste acusa o double desatualizado antes da execução de produção.

## Conexões
- [[rspec-composable-matchers-estruturas]] — Veja também: RSpec 3.13: compor matchers para respostas estruturadas.
- [[rspec-message-argument-constraints]] — Veja também: RSpec 3.13: restringir argumentos de expectativas de mensagem.

## Fontes
- [RSpec 3.13 — Verifying doubles](https://rspec.info/features/3-13/rspec-mocks/verifying-doubles/) — double que valida métodos disponíveis na interface real; consultado em 2026-10-02.
- [RSpec 3.13 — Matching arguments](https://rspec.info/features/3-13/rspec-mocks/setting-constraints/matching-arguments/) — restrições de argumentos de expectativas e stubs de mensagens; consultado em 2026-10-02.
