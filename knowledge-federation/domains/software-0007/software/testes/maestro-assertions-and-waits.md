---
id: software.testes.tranche15.000903
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
fontes: ["https://docs.maestro.dev/api-reference/commands", "https://docs.maestro.dev/api-reference/commands/runflow"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Maestro: afirmar visibilidade e esperar condição

## Em uma frase
`assertVisible` e `assertNotVisible` verificam o estado da tela, e `extendedWaitUntil` aguarda uma condição com tempo limite antes de seguir.

## Por que importa
Verificar apenas que a ação foi aceita não prova que a interface respondeu; sem espera explícita, telas lentas geram falha intermitente.

## Como funciona
Afirme o elemento que representa o resultado do fluxo e use espera estendida para operações que dependem de rede ou processamento demorado.

## Exemplo
`- extendedWaitUntil: { visible: "Pedido confirmado", timeout: 15000 }` aguarda o marco do fluxo antes de avaliar o restante.

## Limites e trade-offs
Espera longa demais mascara lentidão real e afirmação de texto exato quebra com pequenas mudanças de cópia; o ideal é afirmar um elemento com significado estável.

## Como verificar
Introduza um atraso artificial no aplicativo e confirme que a espera cobre o caso; remova o elemento e verifique se a falha indica a asserção correta.

## Conexões
- [[maestro-tapon-selectors]] — Veja também: Maestro: escolher alvos de toque.
- [[maestro-runflow-subflows]] — Veja também: Maestro: reutilizar fluxos com runFlow.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — runFlow](https://docs.maestro.dev/api-reference/commands/runflow) — reuso de fluxos, subflows, variáveis de ambiente e condições; consultado em 2026-10-02.
