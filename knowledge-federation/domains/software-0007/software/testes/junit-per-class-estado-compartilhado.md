---
id: software.testes.tranche10.000363
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
fontes: ["https://docs.junit.org/6.1.3/writing-tests/test-instance-lifecycle.html", "https://docs.junit.org/6.1.3/writing-tests/parallel-execution.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: tratar PER_CLASS como estado compartilhado

## Em uma frase
O lifecycle padrão cria uma instância por método; PER_CLASS reutiliza uma instância para métodos da mesma classe.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Com estado mutável compartilhado, a ordem de execução pode alterar resultado e tornar a suíte não determinística.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Mantenha o padrão quando não precisar de estado compartilhado; se escolher PER_CLASS, inicialize e restaure explicitamente dados mutáveis.

## Exemplo
Dois testes modificam uma lista de fixture; cada método limpa a lista ou passa a usar uma instância isolada.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. PER_CLASS também muda requisitos para métodos de lifecycle e não deve ser habilitado só para remover static sem avaliar o estado.

## Como verificar
Execute métodos em ordem diferente e em paralelo quando possível, observando se um teste depende do valor deixado por outro.

## Conexões
- [[junit-dynamic-test-factory-nao-e-caso]] — Veja também: JUnit: distinguir a factory de seus dynamic tests.
- [[junit-parallel-opt-in-modos-e-sincronizacao]] — Veja também: JUnit: configurar paralelismo sem presumir concorrência automática.

## Fontes
- [JUnit 6.1.3 — Test instance lifecycle](https://docs.junit.org/6.1.3/writing-tests/test-instance-lifecycle.html) — ciclo de vida PER_METHOD/PER_CLASS e estado compartilhado; consultado em 2026-10-02.
- [JUnit 6.1.3 — Parallel execution](https://docs.junit.org/6.1.3/writing-tests/parallel-execution.html) — ativação, modos de execução e sincronização de testes paralelos; consultado em 2026-10-02.
