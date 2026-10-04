---
id: software.testes.tranche13.000744
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
fontes: ["https://cmake.org/cmake/help/latest/prop_test/TIMEOUT.html", "https://cmake.org/cmake/help/latest/manual/ctest.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: limitar duração com propriedade TIMEOUT

## Em uma frase
Propriedade TIMEOUT define limite de parede por teste e impede processo travado de bloquear indefinidamente a suite.

## Por que importa
Um limite por cenário facilita diagnóstico e permite ao driver encerrar testes sem impor um único valor amplo a toda pipeline.

## Como funciona
Escolha prazo compatível com operação medida, registre timeout no teste lento e publique saída de falha com `--output-on-failure`.

## Exemplo
Teste de integração que sobe container pode ter limite maior que unit test puro, mas ainda encerra processo se readiness nunca chega.

## Limites e trade-offs
Timeout pode terminar um processo que deixa recurso externo ativo; mecanismo de cleanup do sistema sob teste precisa lidar com interrupção.

## Como verificar
Use um teste controlado que aguarda indefinidamente e confirme duração, status e log que CTest reporta.

## Conexões
- [[ctest-exit-code-will-fail]] — Veja também: CTest: usar WILL_FAIL só para processo com erro esperado.
- [[ctest-label-filter]] — Veja também: CTest: selecionar subconjunto por LABELS.

## Fontes
- [CMake — TIMEOUT](https://cmake.org/cmake/help/latest/prop_test/TIMEOUT.html) — wall-clock timeout behavior for an individual test; consultado em 2026-10-02.
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
