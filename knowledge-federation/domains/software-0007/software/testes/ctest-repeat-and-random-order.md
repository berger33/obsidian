---
id: software.testes.tranche13.000748
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
fontes: ["https://cmake.org/cmake/help/latest/manual/ctest.1.html", "https://cmake.org/cmake/help/latest/prop_test/LABELS.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# CTest: repetir teste para investigar instabilidade

## Em uma frase
CTest oferece opções de repetição e ordem aleatória para exercitar casos várias vezes no mesmo run.

## Por que importa
Repetição ajuda revelar dependência de estado e intermitência, especialmente quando um caso só falha após setup ou ordem diferente.

## Como funciona
Use modo de repeat documentado, selecione um subconjunto pelo nome ou label e guarde output de cada tentativa para reproduzir condição encontrada.

## Exemplo
Uma suite suspeita pode ser repetida até falha durante investigação, sem alterar em definitivo o job rápido de pull request.

## Limites e trade-offs
Repetição não corrige teste flakey nem substitui seed reproduzível quando estado depende do sistema externo; aumentar duração pode mascarar incidente por carga.

## Como verificar
Rode com repeat limitado, registre qual tentativa falhou e depois execute isoladamente para descobrir se causa está dentro ou fora do processo.

## Conexões
- [[ctest-parallel-processors]] — Veja também: CTest: declarar consumo para agendamento paralelo.
- [[ctest-junit-preset-output]] — Veja também: CTest: versionar opções de run em Test Preset.

## Fontes
- [CMake — ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html) — selection, parallel scheduling, presets, repeat and output; consultado em 2026-10-02.
- [CMake — LABELS](https://cmake.org/cmake/help/latest/prop_test/LABELS.html) — label metadata and label-based selection; consultado em 2026-10-02.
