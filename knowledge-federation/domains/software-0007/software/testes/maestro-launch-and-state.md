---
id: software.testes.tranche15.000901
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

# Maestro: controlar estado do aplicativo entre passos

## Em uma frase
`launchApp` inicia o aplicativo, `clearState` remove dados persistidos e `stopApp` encerra a execução, permitindo controlar o estado inicial de cada cenário.

## Por que importa
Reaproveitar estado de um fluxo anterior cria dependência de ordem, enquanto limpar tudo indiscriminadamente apaga condições que o cenário precisa montar de propósito.

## Como funciona
Inicie cada fluxo com o estado que o caso exige, limpando dados quando o cenário parte de instalação nova e preservando-os quando testa continuidade.

## Exemplo
Uma sequência comum é `- clearState`, `- launchApp` e então a navegação, garantindo que nenhuma sessão anterior influencie o resultado.

## Limites e trade-offs
Limpar estado também remove caches e credenciais que poderiam acelerar a suíte; o custo e o efeito precisam ser considerados no tempo total de execução.

## Como verificar
Rode o mesmo fluxo duas vezes seguidas sem limpeza e depois com limpeza, comparando os resultados para identificar dependência de estado residual.

## Conexões
- [[maestro-flow-yaml-structure]] — Veja também: Maestro: estruturar um fluxo em YAML.
- [[maestro-tapon-selectors]] — Veja também: Maestro: escolher alvos de toque.

## Fontes
- [Maestro — Commands](https://docs.maestro.dev/api-reference/commands) — catálogo de comandos de interação, asserção, controle e espera; consultado em 2026-10-02.
- [Maestro — runFlow](https://docs.maestro.dev/api-reference/commands/runflow) — reuso de fluxos, subflows, variáveis de ambiente e condições; consultado em 2026-10-02.
