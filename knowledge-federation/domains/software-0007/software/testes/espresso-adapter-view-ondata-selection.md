---
id: software.testes.tranche14.000795
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
fontes: ["https://developer.android.com/training/testing/espresso/lists", "https://developer.android.com/training/testing/espresso/basics"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: localizar item de AdapterView com onData

## Em uma frase
`onData()` procura o objeto de dados que alimenta uma `AdapterView` e pode rolar a lista até tornar a linha correspondente visível.

## Por que importa
Em listas virtualizadas, a view do item desejado pode ainda não existir na hierarquia atual e por isso `onView` direto não resolve o alvo.

## Como funciona
Construa matcher sobre o dado do adapter, refine pelo campo que identifica a linha e aplique a ação quando o Espresso a localizar.

## Exemplo
Um matcher de mapa seleciona a linha cujo valor `STR` é `item: 50` e clica nela mesmo quando ela está fora da tela.

## Limites e trade-offs
Matchers vagos podem coincidir com várias linhas; associar somente posição ordinal também tende a quebrar quando dados mudam.

## Como verificar
Use item de conteúdo distinguível, confira a rolagem automática e valide a reação da aplicação ao item escolhido.

## Conexões
- [[espresso-intents-stub-response]] — Veja também: Espresso-Intents: simular resposta externa com intending.
- [[espresso-recyclerview-actions]] — Veja também: Espresso: usar RecyclerViewActions para itens reciclados.

## Fontes
- [Android — Espresso lists](https://developer.android.com/training/testing/espresso/lists) — interação com AdapterView por onData e RecyclerView por actions específicas; consultado em 2026-10-02.
- [Android — Espresso basics](https://developer.android.com/training/testing/espresso/basics) — seleção de views, ações e verificações encadeadas em UI tests; consultado em 2026-10-02.
