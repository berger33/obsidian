---
id: software.testes.tranche13.000747
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://cmake.org/cmake/help/latest/prop_test/PROCESSORS.html", "https://cmake.org/cmake/help/latest/prop_test/RESOURCE_GROUPS.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: declarar consumo para agendamento paralelo

## Em uma frase
CTest pode executar testes em paralelo, e propriedade PROCESSORS informa quantos slots cada caso consome.

## Por que importa
Agendamento consciente de capacidade evita iniciar simultaneamente mais testes pesados do que o agente suporta.

## Como funciona
Use `ctest -j` com limite real do worker e classifique testes multi-core pela propriedade PROCESSORS; declare `RESOURCE_GROUPS` quando precisar de recursos nomeados específicos.

## Exemplo
Teste de GPU pode reservar mais de um processador ou recurso por execução para que CTest não inicie outros jobs concorrentes além da capacidade.

## Limites e trade-offs
PROCESSORS é estimativa de escalonamento, não isolamento de CPU nem proteção de porta ou banco compartilhado.

## Como verificar
Compare jobs em agente ocioso, observe concorrência efetiva e confirme que limites combinados correspondem à configuração do executor.

## Conexões
- [[ctest-fixture-dependency-graph]] — Veja também: CTest: conectar setup e consumidor com fixtures.
- [[ctest-repeat-and-random-order]] — Veja também: CTest: repetir teste para investigar instabilidade.

## Fontes
- [CMake — PROCESSORS](https://cmake.org/cmake/help/latest/prop_test/PROCESSORS.html) — resource-aware scheduling under parallel test execution; consultado em 2026-10-02.
- [CMake — RESOURCE_GROUPS](https://cmake.org/cmake/help/latest/prop_test/RESOURCE_GROUPS.html) — named resource requirements and allocation groups for tests; consultado em 2026-10-02.
