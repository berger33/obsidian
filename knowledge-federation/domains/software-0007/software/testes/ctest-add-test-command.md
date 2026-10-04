---
id: software.testes.tranche13.000741
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
fontes: ["https://cmake.org/cmake/help/latest/command/add_test.html", "https://cmake.org/cmake/help/latest/command/enable_testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: registrar comando explícito com add_test NAME

## Em uma frase
A assinatura nomeada de `add_test(NAME ... COMMAND ...)` associa identificador estável e comando ao teste executado por CTest.

## Por que importa
Nome descritivo aparece em filtros e resultados, enquanto argumentos explícitos revelam o que foi exercitado.

## Como funciona
Use target de executável quando possível para CMake resolver artefato gerado, escolha diretório de trabalho deliberado e coloque propriedade no diretório que criou o teste.

## Exemplo
`add_test(NAME parser_unit COMMAND parser_tests --filter=header)` mantém runner e filtro visíveis no arquivo de build.

## Limites e trade-offs
Test property só pode ser definida no diretório onde o teste foi criado; comando shell implícito pode funcionar local e falhar em outro generator.

## Como verificar
Gere build com dois generators suportados e confira comando resolvido, diretório atual e resultado do mesmo teste.

## Conexões
- [[ctest-enable-testing-scope]] — Veja também: CTest: habilitar descoberta no build tree.
- [[ctest-working-directory-contract]] — Veja também: CTest: fixar working directory para dados relativos.

## Fontes
- [CMake — add_test](https://cmake.org/cmake/help/latest/command/add_test.html) — test registration, command, working directory and target handling; consultado em 2026-10-02.
- [CMake — enable_testing](https://cmake.org/cmake/help/latest/command/enable_testing.html) — generation of testing support in build trees; consultado em 2026-10-02.
