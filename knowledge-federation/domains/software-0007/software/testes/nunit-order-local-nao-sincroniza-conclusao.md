---
id: software.testes.tranche11.000498
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.nunit.org/articles/nunit/writing-tests/attributes/order.html", "https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NUnit: usar Order para organização local, nunca como dependência temporal

## Em uma frase
Order organiza quando testes ou fixtures começam dentro da suite que os contém; não ordena globalmente nem aguarda término anterior.

## Por que importa
Testes que dependem de dados criados por outro método falham em paralelismo, filtro parcial ou nova execução.

## Como funciona
Transforme a sequência em um caso com setup explícito ou em fixtures independentes com estado reconstruível.

## Exemplo
Migration A e migration B são verificadas dentro de um teste que cria seu próprio banco, em vez de depender de [Order] entre methods.

## Limites e trade-offs
Testes com mesmo order ou sem atributo têm sequência indeterminada e paralelo pode sobrepor suas execuções.

## Como verificar
Execute filtro contendo apenas o segundo caso e paralelismo habilitado; o caso deve continuar válido sem predecessor.

## Conexões
- [[nunit-parallelizable-nao-e-limite-de-workers]] — Veja também: NUnit: distinguir Parallelizable de LevelOfParallelism.
- [[nunit-testcontext-diagnostico-por-escopo]] — Veja também: NUnit: ler TestContext no escopo de execução correto.

## Fontes
- [NUnit — Order attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/order.html) — ordem local de início e ausência de garantia de conclusão sequencial; consultado em 2026-10-02.
- [NUnit — Parallelizable attribute](https://docs.nunit.org/articles/nunit/writing-tests/attributes/parallelizable.html) — marcação de testes paralelizáveis e separação da configuração máxima de workers; consultado em 2026-10-02.
