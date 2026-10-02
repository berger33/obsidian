---
id: software.testes.tranche07.000110
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
fontes: ["https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html", "https://www.w3.org/WAI/test-evaluate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de acessibilidade por navegação de teclado", "Teste: Teste de acessibilidade por navegação de teclado"]
lote: software-testes-2000-0001
---

# Teste de acessibilidade por navegação de teclado

## Em uma frase
Verifique se ações e conteúdo operáveis podem ser alcançados e acionados sem mouse, respeitando o comportamento esperado de cada controle.

## Por que importa
Pessoas que usam teclado, switch ou tecnologia assistiva dependem de foco e interação coerentes; mouse-only happy paths deixam barreiras importantes sem detecção.

## Como funciona
Execute o fluxo apenas com teclado, usando Tab e Shift+Tab para navegação e as teclas de ativação apropriadas ao tipo de controle. Verifique ordem lógica, interação com menus e diálogos, fechamento e ausência de armadilhas de foco.

## Exemplo
Em um formulário de compra, navegue até endereço, escolha método de entrega, corrija um erro e conclua a ação sem apontador; confirme que opções customizadas também respondem ao teclado.

## Limites e trade-offs
Automação de DOM não substitui a experiência real de teclado. A ordem ideal depende da estrutura e do fluxo; não imponha uma sequência visual fixa se a ordem programática mantém significado e operabilidade.

## Como verificar
Registre cada controle interativo, tecla usada, foco observado e resultado; teste entradas, diálogos e estados após validação, e corrija qualquer região sem rota de saída por teclado.

## Conexões
- [[teste-acessibilidade-automatizada-revisao-humana]] — aprofundamento relacionado.
- [[teste-acessibilidade-foco-visivel-ordem]] — aprofundamento relacionado.

## Fontes
- [W3C WAI — Understanding Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) — operabilidade por teclado sem exigir timings específicos; consultado em 2026-10-01.
- [W3C WAI — Easy Checks and Evaluation](https://www.w3.org/WAI/test-evaluate/) — avaliação combina verificações automáticas e exame manual; consultado em 2026-10-01.
