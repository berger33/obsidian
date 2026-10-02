---
id: software.testes.tranche13.000742
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
fontes: ["https://cmake.org/cmake/help/latest/command/add_test.html", "https://cmake.org/cmake/help/latest/command/set_tests_properties.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: fixar working directory para dados relativos

## Em uma frase
`WORKING_DIRECTORY` define o diretório de execução do teste; quando omitido, CTest usa diretório binário atual.

## Por que importa
Fixtures por caminho relativo podem encontrar arquivo localmente e desaparecer sob outra configuração de build se diretório não estiver explícito.

## Como funciona
Configure propriedade para pasta de dados gerada ou forneça caminho absoluto calculado pelo teste; mantenha comportamento igual em multi-config.

## Exemplo
Um teste de parser pode receber fixture no build tree sem presumir que o processo iniciou na raiz do checkout.

## Limites e trade-offs
Diretório de trabalho não transfere arquivo entre máquinas e não deve apontar para artefato efêmero que outro job não publica.

## Como verificar
Execute pelo comando `ctest` fora da raiz do projeto e confirme que o teste lê somente os recursos previstos no build directory.

## Conexões
- [[ctest-add-test-command]] — Veja também: CTest: registrar comando explícito com add_test NAME.
- [[ctest-exit-code-will-fail]] — Veja também: CTest: usar WILL_FAIL só para processo com erro esperado.

## Fontes
- [CMake — add_test](https://cmake.org/cmake/help/latest/command/add_test.html) — test registration, command, working directory and target handling; consultado em 2026-10-02.
- [CMake — set_tests_properties](https://cmake.org/cmake/help/latest/command/set_tests_properties.html) — per-test properties such as timeout and labels; consultado em 2026-10-02.
