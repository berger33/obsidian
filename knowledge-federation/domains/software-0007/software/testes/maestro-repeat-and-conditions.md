---
id: software.testes.tranche15.000907
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

# Maestro: repetir passos e tratar variações

## Em uma frase
O comando `repeat` executa um bloco por número de vezes ou enquanto uma condição for verdadeira, permitindo cobrir listas e tentativas sem duplicar comandos.

## Por que importa
Sem repetição, cenários com listas de tamanho variável dependem de cópia manual de passos e ficam presos a uma quantidade fixa de itens.

## Como funciona
Use repetição com condição de parada clara e combine com fluxos condicionais para tratar telas que aparecem apenas em algumas execuções.

## Exemplo
`- repeat: { times: 3, commands: [ { tapOn: "Adicionar" } ] }` cobre três interações e pode ser combinado com asserções a cada volta.

## Limites e trade-offs
Repetição sem limite ou com condição instável pode gerar laço longo e mascarar problema de navegação; o tempo máximo do fluxo continua sendo o limite de segurança.

## Como verificar
Registre quantas voltas ocorreram em uma execução típica e teste uma variação com mais itens para confirmar que o fluxo acompanha o dado.

## Conexões
- [[maestro-tags-and-filters]] — Veja também: Maestro: organizar fluxos com tags.
- [[maestro-screenshots-artifacts]] — Veja também: Maestro: registrar evidências da execução.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — runFlow](https://docs.maestro.dev/api-reference/commands/runflow) — reuso de fluxos, subflows, variáveis de ambiente e condições; consultado em 2026-10-02.
