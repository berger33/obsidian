---
id: software.testes.tranche15.000909
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://docs.maestro.dev/api-reference/commands", "https://docs.maestro.dev/getting-started/installing-maestro"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: esperar animação e alcançar itens distantes

## Em uma frase
`waitForAnimationToEnd` aguarda a interface estabilizar e `scrollUntilVisible` rola a tela até o elemento aparecer, com limite de rolagem.

## Por que importa
Interagir durante animação produz toques perdidos, e elementos abaixo da dobra não existem para a asserção até que a tela seja rolada.

## Como funciona
Use a espera de animação após transições e a rolagem dirigida com seletor e limite para alcançar itens que não cabem na tela.

## Exemplo
`- scrollUntilVisible: { element: { id: "ultimo_item" }, direction: DOWN, timeout: 20000 }` percorre a lista até o alvo.

## Limites e trade-offs
Esperar toda animação pode mascarar animação infinita, e rolagem sem limite pode terminar em timeout silencioso quando o elemento nunca aparece.

## Como verificar
Meça o tempo da espera em execuções normais e provoque uma lista sem o elemento para confirmar que a falha aponta a rolagem sem sucesso.

## Conexões
- [[maestro-screenshots-artifacts]] — Veja também: Maestro: registrar evidências da execução.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — Installing Maestro](https://docs.maestro.dev/getting-started/installing-maestro) — instalação, requisitos e primeiros passos com a CLI; consultado em 2026-10-02.
