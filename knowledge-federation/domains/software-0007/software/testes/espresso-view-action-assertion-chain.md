---
id: software.testes.tranche14.000790
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
fontes: ["https://developer.android.com/training/testing/espresso", "https://developer.android.com/training/testing/espresso/basics"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: explicitar alvo, ação e resultado

## Em uma frase
O fluxo central do Espresso separa a seleção de uma view, a ação do usuário e a assertion sobre o estado apresentado.

## Por que importa
Um teste que comunica essas três etapas é mais fácil de diagnosticar do que uma sequência de sleeps e consultas indiretas.

## Como funciona
Localize por identificador, texto ou matcher de view com `onView`, execute uma ação suportada e valide estado observável com `check(matches(...))`.

## Exemplo
Um fluxo de saudação seleciona o campo, digita um nome, clica no botão e verifica que a mensagem resultante aparece.

## Limites e trade-offs
Matchers genéricos podem localizar mais de uma view ou depender de texto instável, gerando ambiguidade em layouts complexos.

## Como verificar
Revise se o matcher identifica o elemento pretendido e se a assertion verifica resultado visível, não implementação interna.

## Conexões
- [[espresso-automatic-idle-boundary]] — Veja também: Espresso: reconhecer o limite da sincronização automática.

## Fontes
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
- [Android — Espresso basics](https://developer.android.com/training/testing/espresso/basics) — seleção de views, ações e verificações encadeadas em UI tests; consultado em 2026-10-02.
