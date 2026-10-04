---
id: software.testes.tranche17.001152
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

# RSpec: casar argumentos com critérios flexíveis

## Em uma frase
Nas expectativas e permissões é possível casar argumentos por expressão, inclusão parcial e padrão, em vez de exigir igualdade exata.

## Por que importa
Valores gerados pelo código sob teste impedem comparação literal e tornam a expectativa inútil quando exigem o valor exato.

## Como funciona
Use correspondência parcial para os campos relevantes e padrões para formatos, mantendo a expectativa restrita ao que o exemplo verifica.

## Exemplo
A expectativa de um log pode casar com expressão sobre o texto que descreve o incidente registrado.

## Limites e trade-offs
Correspondências amplas aceitam qualquer argumento e transformam a verificação em formalidade, então o critério precisa ser revisado como código.

## Como verificar
Altere o campo coberto pela correspondência e confirme que o exemplo passa a falhar no momento da verificação.

## Conexões
- [[rspec-message-expectations]] — Veja também: RSpec: declarar expectativas de mensagem.
- [[rspec-shared-examples]] — Veja também: RSpec: reutilizar comportamento com exemplos compartilhados.

## Fontes
- [RSpec — Mocks](https://rspec.info/features/3-12/rspec-mocks/) — dublês verificados, permissões de recebimento e expectativas de mensagem; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
