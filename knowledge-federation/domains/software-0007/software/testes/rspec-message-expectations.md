---
id: software.testes.tranche17.001151
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://rspec.info/features/3-12/rspec-mocks/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: declarar expectativas de mensagem

## Em uma frase
Uma expectativa de mensagem configura o recebimento e falha o exemplo se a chamada não ocorrer, distinguindo-se da permissão simples.

## Por que importa
Verificar que a colaboração aconteceu cobre comportamento que a mudança de estado observada não revela sozinha.

## Como funciona
Declare expectativa apenas para a interação central do exemplo, combine com critérios de argumento e verifique ao final do exemplo.

## Exemplo
Um caso de confirmação de pedido pode exigir que o serviço de notificação receba a mensagem com o identificador correto.

## Limites e trade-offs
Expectativas em cada dependência transformam o teste em espelho da implementação, e argumentos fixos demais quebram com dados variáveis.

## Como verificar
Remova a chamada no código de produção e confirme que o exemplo falha com a mensagem indicando a interação não satisfeita.

## Conexões
- [[rspec-doubles-and-stubs]] — Veja também: RSpec: substituir dependências com dublês.
- [[rspec-argument-matchers]] — Veja também: RSpec: casar argumentos com critérios flexíveis.

## Fontes
- [RSpec — Mocks](https://rspec.info/features/3-12/rspec-mocks/) — dublês verificados, permissões de recebimento e expectativas de mensagem; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
