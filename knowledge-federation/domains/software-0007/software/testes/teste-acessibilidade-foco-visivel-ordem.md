---
id: software.testes.tranche07.000111
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
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html", "https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Testes de foco visível e ordem lógica", "Teste: Testes de foco visível e ordem lógica"]
lote: software-testes-2000-0001
---

# Testes de foco visível e ordem lógica

## Em uma frase
Examine se o foco de teclado permanece visível e percorre uma sequência que preserva significado e operabilidade.

## Por que importa
Sem indicador perceptível, uma pessoa que navega por teclado pode perder a referência de onde as ações serão aplicadas; saltos inesperados tornam fluxos confusos.

## Como funciona
Percorra controles com teclado em diferentes estados, incluindo cabeçalho fixo, menus, validações e modais. Confira visibilidade do indicador, se não é ocultado por conteúdo sobreposto e se a sequência programática corresponde ao fluxo de trabalho.

## Exemplo
Abra um diálogo, avance até o botão de confirmação e feche-o; verifique que o foco entra no diálogo, segue controles relevantes, continua visível e retorna a um ponto adequado quando o diálogo fecha.

## Limites e trade-offs
A WCAG 2.2 SC 2.4.7 exige modo com foco visível, enquanto critérios adicionais tratam aparência/oclusão. A nota não interpreta SC 2.4.7 como um design visual específico nem afirma que scanner automático cobre todos os casos.

## Como verificar
Capture estado e sequência para cada fluxo crítico, teste zoom e viewport estreito e valide contrastes pertinentes do indicador contra fundos adjacentes.

## Conexões
- [[teste-acessibilidade-navegacao-teclado]] — aprofundamento relacionado.
- [[teste-acessibilidade-contraste]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) — indicador visível em ao menos um modo de operação por teclado; consultado em 2026-10-01.
- [W3C WAI — Understanding Focus Order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — sequência de foco preserva significado e operabilidade; consultado em 2026-10-01.
