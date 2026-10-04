---
id: software.testes.tranche14.000796
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
fontes: ["https://developer.android.com/training/testing/espresso/lists", "https://developer.android.com/training/testing/espresso"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: usar RecyclerViewActions para itens reciclados

## Em uma frase
`RecyclerViewActions` oferece ações de lista para localizar e operar itens que podem não estar materializados na tela.

## Por que importa
A reciclagem de views impede assumir que todos os filhos do RecyclerView estejam presentes simultaneamente na árvore de UI.

## Como funciona
Localize o RecyclerView, use matcher de item e ação específica, como rolar até posição ou até view correspondente.

## Exemplo
Um teste pode rolar para o card identificado por seu título e clicar em um botão dentro daquele item.

## Limites e trade-offs
A posição só representa o mesmo dado se a ordenação for estável; use matcher semântico quando a lista muda.

## Como verificar
Inspecione a ação em lista vazia e longa, e valide que o item acionado corresponde ao identificador de domínio esperado.

## Conexões
- [[espresso-adapter-view-ondata-selection]] — Veja também: Espresso: localizar item de AdapterView com onData.
- [[espresso-accessibility-checks-at-actions]] — Veja também: Espresso: executar verificações de acessibilidade junto às ações.

## Fontes
- [Android — Espresso lists](https://developer.android.com/training/testing/espresso/lists) — interação com AdapterView por onData e RecyclerView por actions específicas; consultado em 2026-10-02.
- [Android — Espresso](https://developer.android.com/training/testing/espresso) — ações de UI, assertions, sincronização automática e pacotes do Espresso; consultado em 2026-10-02.
