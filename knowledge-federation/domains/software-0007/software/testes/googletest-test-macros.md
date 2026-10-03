---
id: software.testes.tranche18.001187
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://google.github.io/googletest/primer.html", "https://github.com/google/googletest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: declarar casos e suítes

## Em uma frase
As macros declaram casos de teste com nome de suíte e nome do caso, gerando a função de entrada e o registro automático no executor.

## Por que importa
O registro automático dispensa código de chamada e mantém os casos descobertos pela execução sem configuração adicional.

## Como funciona
Nomeie a suíte pela classe ou comportamento e o caso pelo cenário verificado, mantendo nomes descritivos no relatório.

## Exemplo
Um caso pode verificar que a soma de dois números corresponde ao valor esperado, com nome que descreve a operação.

## Limites e trade-offs
Nomes genéricos dificultam localizar a falha no relatório, e casos que fazem coisas diferentes sob o mesmo nome escondem a intenção.

## Como verificar
Liste os testes disponíveis sem executá-los e confirme que os nomes correspondem ao comportamento descrito.

## Conexões
- [[googletest-assertions]] — Veja também: GoogleTest: escolher entre asserção fatal e não fatal.

## Fontes
- [GoogleTest — Primer](https://google.github.io/googletest/primer.html) — macros de caso, asserções, comparações e execução; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
