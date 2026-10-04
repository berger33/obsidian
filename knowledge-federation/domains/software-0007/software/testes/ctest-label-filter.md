---
id: software.testes.tranche13.000745
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
fontes: ["https://cmake.org/cmake/help/latest/prop_test/LABELS.html", "https://cmake.org/cmake/help/latest/manual/ctest.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: selecionar subconjunto por LABELS

## Em uma frase
Propriedade `LABELS` classifica teste e CTest permite selecionar ou excluir rótulos sem renomear alvo.

## Por que importa
Labels deixam jobs de custo diferente executarem recortes reproduzíveis de uma mesma descoberta.

## Como funciona
Associe categorias como `unit`, `db` ou `slow` no diretório que cria o teste e configure filtros em preset ou CLI com contagem de resultados visível.

## Exemplo
Pull request pode rodar unit e smoke; nightly inclui também label database, mantendo seleção documentada no comando.

## Limites e trade-offs
Label é metadado de seleção, não medição de cobertura; um teste sem categoria pode ser omitido por filtro que seleciona só rótulos conhecidos.

## Como verificar
Liste casos incluídos por cada filtro e falhe job quando seleção obrigatória resultar em nenhum teste.

## Conexões
- [[ctest-timeout-failure-diagnostic]] — Veja também: CTest: limitar duração com propriedade TIMEOUT.
- [[ctest-fixture-dependency-graph]] — Veja também: CTest: conectar setup e consumidor com fixtures.

## Fontes
- [CMake — LABELS](https://cmake.org/cmake/help/latest/prop_test/LABELS.html) — label metadata and label-based selection; consultado em 2026-10-02.
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
