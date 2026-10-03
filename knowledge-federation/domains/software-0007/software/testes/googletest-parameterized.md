---
id: software.testes.tranche18.001191
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
fontes: ["https://google.github.io/googletest/advanced.html", "https://github.com/google/googletest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: variar entradas com testes parametrizados

## Em uma frase
O gerador de valores combinado com a macro de teste parametrizado cria um caso por valor, com nome derivado e relatório individual.

## Por que importa
Regras verificadas com várias entradas ficam concisas e cada valor aparece separadamente no relatório, facilitando localizar a falha.

## Como funciona
Defina a lista de valores com nome legível, declare o caso parametrizado e use o parâmetro para montar o valor esperado.

## Exemplo
Um caso pode verificar o mesmo cálculo para vários valores-limite, exibindo cada um deles no relatório.

## Limites e trade-offs
Listas longas tornam a leitura pesada, e valores sem nome dificultam identificar qual entrada falhou.

## Como verificar
Adicione um valor inválido à lista e confirme que o relatório aponta exatamente qual entrada produziu a falha.

## Conexões
- [[googletest-fixtures]] — Veja também: GoogleTest: compartilhar preparação com fixtures.
- [[googletest-typed-tests]] — Veja também: GoogleTest: reutilizar casos entre tipos.

## Fontes
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
