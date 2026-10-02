---
id: software.testes.tranche08.000171
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
fontes: ["https://developer.android.com/training/testing/instrumented-tests/stability", "https://developer.android.com/training/testing/fundamentals"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: sincronizar testes instrumentados sem sleeps fixos

## Em uma frase
Espere condições observáveis ou idleness do app em vez de pausar por duração fixa antes de cada assertion.

## Por que importa
Sleep curto falha em dispositivos lentos e sleep longo desperdiça tempo; ambos deixam o teste dependente de timing não relacionado ao contrato.

## Como funciona
Use sincronização oferecida pelo framework e condições explícitas do estado esperado. Para trabalho assíncrono próprio, exponha mecanismo de sincronização que o runner possa acompanhar.

## Exemplo
Após iniciar carregamento, aguarde a lista de resultados ou o estado idle relevante, em vez de dormir dois segundos antes de buscar o item.

## Limites e trade-offs
Idleness declarada incorretamente pode encerrar cedo ou nunca ocorrer; a estratégia precisa incluir tarefas assíncronas relevantes e terminar com timeout diagnóstico.

## Como verificar
Varie velocidade e carga do emulador, repita execução e examine logs de sincronização. Confirme que nenhuma espera fixa é o único controle de corrida.

## Conexões
- [[android-compose-clock-idle-animacoes]] — Veja também: Android Compose: controlar clock e animações em testes.
- [[android-test-flakiness-reproducao-dispositivo]] — Veja também: Android: tornar falhas instrumentadas reproduzíveis.

## Fontes
- [Android — Big test stability](https://developer.android.com/training/testing/instrumented-tests/stability) — sincronização e redução de flakiness em testes grandes; consultado em 2026-10-02.
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
