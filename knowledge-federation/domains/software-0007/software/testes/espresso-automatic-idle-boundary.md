---
id: software.testes.tranche14.000791
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
fontes: ["https://developer.android.com/training/testing/espresso", "https://developer.android.com/training/testing/espresso/idling-resource"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: reconhecer o limite da sincronização automática

## Em uma frase
Espresso aguarda condições conhecidas da fila de UI e recursos de idling registrados, mas não entende automaticamente toda tarefa de background.

## Por que importa
Testes que presumem que uma chamada de rede ou executor arbitrário terminou podem observar a tela cedo demais.

## Como funciona
Se uma operação assíncrona afeta a próxima assertion, conecte-a a um idling resource e mantenha a espera vinculada ao estado do app.

## Exemplo
Após carregar itens em executor próprio, o teste espera a transição do recurso registrado antes de procurar o resultado no RecyclerView.

## Limites e trade-offs
Substituir toda assincronia por `Thread.sleep` aumenta duração e ainda falha em dispositivos mais lentos.

## Como verificar
Reproduza sob latência variável e verifique que a assertion só continua após a operação relevante chegar a idle.

## Conexões
- [[espresso-view-action-assertion-chain]] — Veja também: Espresso: explicitar alvo, ação e resultado.
- [[espresso-register-idling-resource-lifecycle]] — Veja também: Espresso: registrar idling resource antes da primeira ação.

## Fontes
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
- [Android — Espresso idling resources](https://developer.android.com/training/testing/espresso/idling-resource) — registro, transições de idle e coordenação de operações assíncronas; consultado em 2026-10-02.
