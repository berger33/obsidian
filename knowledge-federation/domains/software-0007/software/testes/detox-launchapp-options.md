---
id: software.testes.tranche16.000952
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://wix.github.io/Detox/docs/introduction/getting-started", "https://github.com/wix/Detox"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Detox: controlar o lançamento do aplicativo

## Em uma frase
A chamada de lançamento aceita opções como instância nova, permissões de sistema, argumentos e abertura por link, definindo o estado inicial do cenário.

## Por que importa
Cada cenário precisa de um ponto de partida conhecido, e reaproveitar processo com sessão anterior mistura dados de testes diferentes.

## Como funciona
Inicie com instância nova quando o caso exigir estado limpo, conceda ou negue permissões declarativamente e passe argumentos que o aplicativo reconheça.

## Exemplo
Um fluxo de notificações pode iniciar com permissão negada e depois reabrir o aplicativo para validar o caminho alternativo de configuração.

## Limites e trade-offs
Reabrir a instância existente é útil para testar retomada, mas esconde vazamentos de estado quando usado por padrão em toda a suíte.

## Como verificar
Execute o mesmo caso duas vezes seguidas e confirme que o resultado não depende de dados deixados pela execução anterior.

## Conexões
- [[detox-testid-selectors]] — Veja também: Detox: preferir identificadores de testabilidade.
- [[detox-reload-react-native]] — Veja também: Detox: recarregar o JavaScript entre casos.

## Fontes
- [Detox — Getting Started](https://wix.github.io/Detox/docs/introduction/getting-started) — sincronização automática, matchers, esperas explícitas, lançamento, recarga, ações de dispositivo e artefatos; consultado em 2026-10-03.
- [Detox — repositório oficial](https://github.com/wix/Detox) — visão geral do projeto, documentação complementar e exemplos; consultado em 2026-10-03.
