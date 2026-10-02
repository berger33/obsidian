---
id: software.testes.tranche08.000185
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
fontes: ["https://docs.flutter.dev/cookbook/testing/widget/introduction", "https://docs.flutter.dev/testing/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Flutter: evitar pumpAndSettle em animações sem fim

## Em uma frase
Use pumpAndSettle apenas quando a árvore deve ficar ociosa; animação contínua pode impedir que a chamada termine.

## Por que importa
Loading infinito ou ticker contínuo mantém frames pendentes e torna o teste bloqueado ou dependente do limite de timeout.

## Como funciona
Avance frames ou duração controlada, aguarde uma condição observável e encerre animação quando o cenário permitir. Não use settle como sinônimo de sincronização universal.

## Exemplo
Para spinner de carregamento, teste presença durante espera e transição após completar Future, em vez de aguardar spinner se estabilizar.

## Limites e trade-offs
O relógio de widget test não valida cadência real ou desempenho de animação em hardware; teste visual/performance requer outra camada.

## Como verificar
Inclua uma animação repetitiva e confirme que cenário não depende de settle infinito; depois resolva Future e valide estado final.

## Conexões
- [[flutter-testwidgets-pump-microtasks]] — Veja também: Flutter: sincronizar pump e atualizações assíncronas.
- [[android-compose-clock-idle-animacoes]] — Veja também: Android Compose: controlar clock e animações em testes.

## Fontes
- [Flutter — Widget testing](https://docs.flutter.dev/cookbook/testing/widget/introduction) — testWidgets, pump, finders e matchers; consultado em 2026-10-02.
- [Flutter — Testing apps](https://docs.flutter.dev/testing/overview) — níveis unit, widget e integration com trade-offs; consultado em 2026-10-02.
