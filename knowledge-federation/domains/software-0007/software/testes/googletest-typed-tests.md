---
id: software.testes.tranche18.001192
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

# GoogleTest: reutilizar casos entre tipos

## Em uma frase
Os testes por tipo permitem executar a mesma bateria sobre várias implementações que compartilham interface, e a suíte é instanciada para cada tipo.

## Por que importa
Contratos de interface verificados uma vez passam a valer para todas as implementações, revelando incompatibilidades entre elas.

## Como funciona
Agrupe os tipos a testar, declare a suíte parametrizada por tipo e registre a instanciação para cada implementação.

## Exemplo
O mesmo contrato de coleção pode ser verificado para a implementação em vetor e para a implementação em lista ligada.

## Limites e trade-offs
Diferenças de comportamento entre tipos exigem ramificações que reduzem o valor do compartilhamento e devem ser tratadas como exceção explícita.

## Como verificar
Remova um tipo da lista de instanciação e confirme que a bateria deixa de ser executada para ele.

## Conexões
- [[googletest-parameterized]] — Veja também: GoogleTest: variar entradas com testes parametrizados.
- [[googletest-mocks-integration]] — Veja também: GoogleTest: integrar dublês com a suíte.

## Fontes
- [GoogleTest — Advanced](https://google.github.io/googletest/advanced.html) — fixtures, parametrização, testes por tipo, filtros e asserções de morte; consultado em 2026-10-03.
- [GoogleTest — repositório oficial](https://github.com/google/googletest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
