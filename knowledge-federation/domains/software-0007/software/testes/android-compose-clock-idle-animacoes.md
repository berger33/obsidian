---
id: software.testes.tranche08.000174
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developer.android.com/develop/ui/compose/testing/synchronization", "https://developer.android.com/develop/ui/compose/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android Compose: controlar clock e animações em testes

## Em uma frase
Controle o tempo virtual de Compose quando animação ou recomposição assíncrona fizer parte do cenário.

## Por que importa
Aguardar wall-clock pode deixar testes lentos e frágeis; o clock de teste permite observar estados intermediários e finais de forma determinística.

## Como funciona
Sincronize o teste com o scheduler de Compose, avance tempo virtual apenas para transições necessárias e aguarde idleness antes de verificar resultado.

## Exemplo
Um teste avança o clock até o fim de uma animação de expansão e então confirma que o conteúdo passou a estar disponível.

## Limites e trade-offs
Avançar clock não simula desempenho de GPU ou sincronização física; nem todo trabalho externo participa automaticamente do relógio virtual.

## Como verificar
Teste estado inicial, intermediário e final; execute com animação desativada e confirme que espera do scheduler não fica bloqueada por tarefa real não registrada.

## Conexões
- [[android-instrumented-sincronizacao-sem-sleep]] — Veja também: Android: sincronizar testes instrumentados sem sleeps fixos.
- [[flutter-pumpandsettle-animacao-indefinida]] — Veja também: Flutter: evitar pumpAndSettle em animações sem fim.

## Fontes
- [Android — Compose synchronization](https://developer.android.com/develop/ui/compose/testing/synchronization) — idle resources, virtual clock e sincronização; consultado em 2026-10-02.
- [Android — Compose testing](https://developer.android.com/develop/ui/compose/testing) — semântica, ações e assertions de UI Compose; consultado em 2026-10-02.
