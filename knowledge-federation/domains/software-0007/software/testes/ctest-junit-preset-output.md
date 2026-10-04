---
id: software.testes.tranche13.000749
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
fontes: ["https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#test-preset", "https://cmake.org/cmake/help/latest/manual/ctest.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: versionar opções de run em Test Preset

## Em uma frase
Test Preset guarda opções de execução reutilizáveis e CTest pode gravar saída JUnit com `--output-junit`.

## Por que importa
Preset alinha execução local e CI e formato JUnit permite que outro serviço consuma resultados sem interpretar texto livre.

## Como funciona
Declare nome, configure preset de configuração associado e filtros de teste necessários; informe arquivo JUnit no comando ou configuração suportada pela versão alvo.

## Exemplo
Um preset de PR pode escolher labels unit e gerar `test-results.xml` para publicação como artifact da pipeline.

## Limites e trade-offs
`--output-junit` sobrescreve arquivo existente, então jobs concorrentes precisam de caminhos distintos; campos de preset dependem da versão de CMake.

## Como verificar
Valide `ctest --preset` e confirme versão mínima, caminho de output e importação do XML pelo consumidor da CI.

## Conexões
- [[ctest-repeat-and-random-order]] — Veja também: CTest: repetir teste para investigar instabilidade.

## Fontes
- [CMake — Test Presets](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#test-preset) — presets for repeatable test-run configuration; consultado em 2026-10-02.
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
