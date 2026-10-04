---
id: software.testes.tranche10.000361
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
fontes: ["https://docs.junit.org/6.1.3/writing-tests/parameterized-classes-and-tests.html", "https://docs.junit.org/6.1.3/extensions/overview.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: projetar MethodSource com argumentos explícitos

## Em uma frase
MethodSource fornece os argumentos de cada invocação a partir de uma factory method compatível.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Uma fonte opaca ou que dependa de estado oculto dificulta entender qual conjunto de parâmetros produziu a falha.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Use factory nomeada, retorne argumentos tipados e mantenha a ordem dos parâmetros indexed, aggregators e resolvers conforme o User Guide.

## Exemplo
Uma Stream de Arguments nomeados alimenta pares de locale e valor monetário e identifica cada invocação no resultado do runner.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Factories externas precisam ser estáticas; métodos locais seguem as regras de lifecycle e podem requerer PER_CLASS para não ser estáticos.

## Como verificar
Revise cada conjunto emitido e confirme que a ordem e os tipos correspondem à assinatura real do teste.

## Conexões
- [[junit-parametrized-test-casos-complementares]] — Veja também: JUnit: usar testes parametrizados para variação de dados.
- [[junit-dynamic-test-factory-nao-e-caso]] — Veja também: JUnit: distinguir a factory de seus dynamic tests.

## Fontes
- [JUnit 6.1.3 — Parameterized classes and tests](https://docs.junit.org/6.1.3/writing-tests/parameterized-classes-and-tests.html) — fontes, consumo de argumentos e natureza experimental de classes parametrizadas; consultado em 2026-10-02.
- [JUnit 6.1.3 — Extension model](https://docs.junit.org/6.1.3/extensions/overview.html) — pontos de extensão e integração com o ciclo de execução; consultado em 2026-10-02.
