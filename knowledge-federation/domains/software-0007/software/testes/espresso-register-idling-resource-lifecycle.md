---
id: software.testes.tranche14.000792
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
fontes: ["https://developer.android.com/training/testing/espresso/idling-resource", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: registrar idling resource antes da primeira ação

## Em uma frase
Os benefícios de sincronização começam quando Espresso consulta o recurso; registrar antecipadamente evita uma primeira ação que passe sem observá-lo.

## Por que importa
Ciclo de vida explícito reduz esperas implícitas e impede manter estado de teste ativo além do cenário que o usa.

## Como funciona
Registre no setup antes de `onView`, sinalize idle quando o trabalho termina e remova o recurso no teardown.

## Exemplo
Um `CountingIdlingResource` é incrementado ao iniciar duas tarefas e decrementado quando ambas concluem, ficando idle apenas quando a contagem zera.

## Limites e trade-offs
Atualização de estado após notificar transição para idle pode correr junto da assertion e criar condição de corrida.

## Como verificar
Faça teste com uma operação real assíncrona e confira que registro e remoção acontecem mesmo se o caso falhar.

## Conexões
- [[espresso-automatic-idle-boundary]] — Veja também: Espresso: reconhecer o limite da sincronização automática.
- [[espresso-intents-validate-outgoing]] — Veja também: Espresso-Intents: validar o intent que o app tentou enviar.

## Fontes
- [Android — Espresso idling resources](https://developer.android.com/training/testing/espresso/idling-resource) — registro, transições de idle e coordenação de operações assíncronas; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
