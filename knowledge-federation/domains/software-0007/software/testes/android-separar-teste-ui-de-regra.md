---
id: software.testes.tranche08.000178
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
fontes: ["https://developer.android.com/training/testing/fundamentals", "https://developer.android.com/develop/ui/compose/testing"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: não concentrar regras de negócio em teste de UI

## Em uma frase
Mantenha regras determinísticas em testes locais e reserve testes de interface para contratos que dependem da UI Android.

## Por que importa
Uma falha de regra dentro de fluxo completo gera diagnóstico lento e custos de emulador sem aumentar confiança para cada combinação de entrada.

## Como funciona
Teste lógica pura com entradas e saídas, integração do repositório em sua fronteira, e UI para navegação, semântica e ciclo de vida. Compartilhe contratos, não setup pesado.

## Exemplo
Validação de faixa numérica roda localmente para valores de fronteira; um único teste de UI confirma que erro aparece no campo correto.

## Limites e trade-offs
A separação não deve ocultar interação real entre camadas; mantenha cenários integrados para riscos de composição que unit tests não exercitam.

## Como verificar
Relacione cada assertion à camada cuja falha ela detecta; confira se a mesma regra não é reexecutada em dezenas de fluxos instrumentados sem propósito.

## Conexões
- [[android-process-death-restauracao-estado]] — Veja também: Android: testar restauração após recriação do processo.
- [[android-test-pyramid-escopo-runner]] — Veja também: Android: escolher escopo e runner de teste.

## Fontes
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
- [Android — Compose testing](https://developer.android.com/develop/ui/compose/testing) — semântica, ações e assertions de UI Compose; consultado em 2026-10-02.
