---
id: software.testes.tranche13.000746
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
fontes: ["https://cmake.org/cmake/help/latest/prop_test/FIXTURES_SETUP.html", "https://cmake.org/cmake/help/latest/prop_test/FIXTURES_REQUIRED.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: conectar setup e consumidor com fixtures

## Em uma frase
`FIXTURES_SETUP` marca um teste preparatório e `FIXTURES_REQUIRED` marca consumidores que precisam daquele recurso.

## Por que importa
A relação permite que CTest inclua setup quando apenas consumidor é selecionado e organize pré-requisito sem depender de posição textual no arquivo.

## Como funciona
Dê nome de fixture distinto de nome de teste, declare setup e consumo nas propriedades apropriadas e defina cleanup associado quando houver recurso para liberar.

## Exemplo
Selecionar um teste de integração que requer banco inclui automaticamente setup marcado, mesmo que filtro de seleção não tenha escolhido o setup diretamente.

## Limites e trade-offs
Setup de uma mesma fixture executa uma vez por run e falha impede consumidores, embora CTest ainda execute cleanup relacionado.

## Como verificar
Filtre somente consumidor, faça setup falhar e confirme inclusão automática, bloqueio dos casos dependentes e execução segura do cleanup.

## Conexões
- [[ctest-label-filter]] — Veja também: CTest: selecionar subconjunto por LABELS.
- [[ctest-parallel-processors]] — Veja também: CTest: declarar consumo para agendamento paralelo.

## Fontes
- [CMake — FIXTURES_SETUP](https://cmake.org/cmake/help/latest/prop_test/FIXTURES_SETUP.html) — setup ordering and automatic inclusion of fixture prerequisites; consultado em 2026-10-02.
- [CMake — FIXTURES_REQUIRED](https://cmake.org/cmake/help/latest/prop_test/FIXTURES_REQUIRED.html) — required setup, test behavior and cleanup on failure; consultado em 2026-10-02.
