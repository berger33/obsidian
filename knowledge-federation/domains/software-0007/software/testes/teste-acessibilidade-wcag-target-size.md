---
id: software.testes.tranche07.000116
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html", "https://www.w3.org/TR/WCAG22/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste do tamanho mínimo de alvos WCAG 2.2", "Teste: Teste do tamanho mínimo de alvos WCAG 2.2"]
lote: software-testes-2000-0001
---

# Teste do tamanho mínimo de alvos WCAG 2.2

## Em uma frase
Meça os alvos de entrada por ponteiro e avalie o requisito mínimo de tamanho ou as exceções de espaçamento definidas no critério.

## Por que importa
Alvos pequenos ou próximos aumentam ativações acidentais e podem ser difíceis para pessoas com tremor, pouca destreza ou telas sensíveis ao toque.

## Como funciona
Para SC 2.5.8, verifique se o alvo comporta 24 por 24 CSS pixels ou se uma exceção documentada se aplica; entre as exceções está espaçamento suficiente entre alvos menores. Mapeie links, ícones e controles, inclusive em estados responsivos.

## Exemplo
Em uma lista de ações com ícones, meça cada área clicável no viewport móvel e avalie separação entre alvos menores usando a regra de círculo de 24 CSS pixels descrita pelo critério.

## Limites e trade-offs
Não confunda o mínimo AA da SC 2.5.8 com a recomendação mais estrita de 44 por 44 CSS pixels; critérios de exceção e controles determinados pelo agente do usuário precisam de análise contextual.

## Como verificar
Registre bounding boxes em CSS pixels, examine alvos adjacentes e documente a exceção usada; teste também a funcionalidade equivalente se a interface oferece outro controle maior.

## Conexões
- [[teste-acessibilidade-navegacao-teclado]] — aprofundamento relacionado.
- [[teste-acessibilidade-regressao-multimodal]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — critério 2.5.8: 24 por 24 CSS pixels ou exceção de espaçamento aplicável; consultado em 2026-10-01.
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/) — critérios testáveis de acessibilidade para conteúdo web; consultado em 2026-10-01.
