---
id: software.testes.tranche14.000793
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md"
fontes: ["https://developer.android.com/training/testing/espresso/intents", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso-Intents: validar o intent que o app tentou enviar

## Em uma frase
`intended()` verifica se um intent de saída que corresponde ao matcher foi registrado pelo Espresso-Intents.

## Por que importa
A verificação cobre a integração do app com uma atividade ou aplicação externa sem precisar executar essa dependência real.

## Como funciona
Inicialize Espresso-Intents no escopo do teste, execute a ação da UI e passe matcher específico a `intended()`.

## Exemplo
Um botão de ajuda pode ser acionado e a assertion confirma um `ACTION_VIEW` apontando para o URI esperado.

## Limites e trade-offs
Validar um intent não fornece automaticamente o resultado da atividade externa; inspeção da saída e resposta simulada são operações distintas.

## Como verificar
Verifique action, data e categoria relevantes e assegure que a infraestrutura de intents foi encerrada após o caso.

## Conexões
- [[espresso-register-idling-resource-lifecycle]] — Veja também: Espresso: registrar idling resource antes da primeira ação.
- [[espresso-intents-stub-response]] — Veja também: Espresso-Intents: simular resposta externa com intending.

## Fontes
- [Android — Espresso-Intents](https://developer.android.com/training/testing/espresso/intents) — correspondência, verificação e stubbing de intents de saída; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
