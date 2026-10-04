---
id: software.testes.tranche14.000798
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
fontes: ["https://developer.android.com/training/testing/espresso/accessibility-checking", "https://developer.android.com/training/testing/espresso/basics"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Espresso: restringir supressões de findings de acessibilidade

## Em uma frase
O matcher de supressão deve identificar um finding específico, em vez de silenciar toda uma categoria ou tela.

## Por que importa
Supressões largas ocultam regressões novas e transformam uma exceção temporária em uma lacuna permanente de visibilidade.

## Como funciona
Combine tipo de verificação com elemento ou view identificável, anote o motivo e mantenha prazo de revisão para a exceção.

## Exemplo
Se um botão legado tem contraste conhecido, suprima apenas o finding de contraste daquele botão, não todos os checks da tela.

## Limites e trade-offs
O framework permite ignorar resultados enquanto se trabalha em correções, mas isso não os converte em conformidade.

## Como verificar
Remova cada supressão após corrigir o componente e confirme que um finding semelhante em outra view ainda aparece.

## Conexões
- [[espresso-accessibility-checks-at-actions]] — Veja também: Espresso: executar verificações de acessibilidade junto às ações.
- [[espresso-webview-testing-boundary]] — Veja também: Espresso-Web: testar WebView dentro de fluxo híbrido.

## Fontes
- [Android — Accessibility checking](https://developer.android.com/training/testing/espresso/accessibility-checking) — execução e supressão estreita de resultados de acessibilidade; consultado em 2026-10-02.
- [Android — Espresso basics](https://developer.android.com/training/testing/espresso/basics) — seleção de views, ações e verificações encadeadas em UI tests; consultado em 2026-10-02.
