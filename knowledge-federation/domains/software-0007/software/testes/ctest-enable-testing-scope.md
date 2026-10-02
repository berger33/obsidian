---
id: software.testes.tranche13.000740
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
fontes: ["https://cmake.org/cmake/help/latest/command/enable_testing.html", "https://cmake.org/cmake/help/latest/manual/ctest.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: habilitar descoberta no build tree

## Em uma frase
CTest executa testes descritos em `CTestTestfile.cmake`, que CMake gera quando testing foi habilitado no diretório apropriado.

## Por que importa
Declarar função de teste sem ativar descoberta pode deixar build compilável mas sem casos visíveis para `ctest`.

## Como funciona
Chame `enable_testing()` no escopo de topo necessário ou use módulo CTest que o habilite conforme `BUILD_TESTING`; confirme arquivo gerado no build directory.

## Exemplo
Um projeto pode desligar `BUILD_TESTING` para build de distribuição e habilitá-lo nos jobs de validação antes de rodar CTest.

## Limites e trade-offs
Configuração em subdiretório errado ou opção de build desativada pode excluir arquivo de teste do local que o driver examina.

## Como verificar
Configure projeto limpo, liste testes no build tree e confirme diferença quando `BUILD_TESTING` é falso.

## Conexões
- [[ctest-add-test-command]] — Veja também: CTest: registrar comando explícito com add_test NAME.

## Fontes
- [CMake — enable_testing](https://cmake.org/cmake/help/latest/command/enable_testing.html) — generation of testing support in build trees; consultado em 2026-10-02.
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
