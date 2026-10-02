---
id: software.testes.tranche10.000362
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
fontes: ["https://docs.junit.org/6.1.3/writing-tests/dynamic-tests.html", "https://docs.junit.org/6.1.3/writing-tests/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: distinguir a factory de seus dynamic tests

## Em uma frase
@TestFactory produz nós DynamicTest ou DynamicContainer em tempo de execução; a factory não é em si um caso de teste.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Interpretar a factory como uma asserção única esconde a quantidade e os nomes dos testes que ela realmente cria.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Gere DynamicTest com nomes diagnósticos e uma Executable por propriedade; use o modo dinâmico quando a lista de casos só puder ser montada em runtime.

## Exemplo
Uma factory lê amostras de um arquivo e cria um teste nomeado por código de produto para cada linha válida.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Dynamic tests são executados lazy e seu lifecycle difere do método @Test tradicional; não presuma setup individual por nó.

## Como verificar
Inspecione a árvore de execução e simule uma falha em um nó para confirmar nome, origem do dado e isolamento de recursos.

## Conexões
- [[junit-methodsource-ordem-argumentos]] — Veja também: JUnit: projetar MethodSource com argumentos explícitos.
- [[junit-per-class-estado-compartilhado]] — Veja também: JUnit: tratar PER_CLASS como estado compartilhado.

## Fontes
- [JUnit 6.1.3 — Dynamic tests](https://docs.junit.org/6.1.3/writing-tests/dynamic-tests.html) — fábricas, execução lazy e estrutura de testes dinâmicos; consultado em 2026-10-02.
- [JUnit 6.1.3 — Annotations](https://docs.junit.org/6.1.3/writing-tests/annotations.html) — semântica das anotações de teste e ciclo de vida; consultado em 2026-10-02.
