---
id: software.testes.tranche10.000360
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://docs.junit.org/6.1.3/writing-tests/parameterized-classes-and-tests.html", "https://docs.junit.org/6.1.3/writing-tests/intro.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: usar testes parametrizados para variação de dados

## Em uma frase
@ParameterizedTest executa um método repetidamente com argumentos fornecidos por uma fonte declarada.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Vários exemplos copiados como métodos separados podem divergir na configuração e deixar limites de entrada sem cobertura.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Escolha uma fonte legível, atribua nomes claros às invocações e mantenha a mesma propriedade verificável para cada conjunto de dados.

## Exemplo
Um teste de normalização recebe espaços, caixa diferente e texto vazio, e cada invocação informa qual entrada falhou.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. A classe parametrizada é um recurso experimental no JUnit 6.1.3 e testes parametrizados exigem junit-jupiter-params.

## Como verificar
Confira no relatório todas as invocações produzidas e inclua valores que distinguem casos válidos, inválidos e de fronteira.

## Conexões
- [[junit-methodsource-ordem-argumentos]] — Veja também: JUnit: projetar MethodSource com argumentos explícitos.

## Fontes
- [JUnit 6.1.3 — Parameterized classes and tests](https://docs.junit.org/6.1.3/writing-tests/parameterized-classes-and-tests.html) — fontes, consumo de argumentos e natureza experimental de classes parametrizadas; consultado em 2026-10-02.
- [JUnit 6.1.3 — Writing tests](https://docs.junit.org/6.1.3/writing-tests/intro.html) — modelo de escrita e execução de testes Jupiter; consultado em 2026-10-02.
