---
id: software.testes.tranche11.000539
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.gatling.io/concepts/session/api/", "https://docs.gatling.io/concepts/scenario/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: limitar logging e inspeção de Session fora da carga

## Em uma frase
Session pode ser inspecionada durante desenvolvimento para diagnosticar feeders, expressões e check failures.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Imprimir sessão em cada ação sob alta concorrência consome recursos do engine e pode expor token ou dados de usuário.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Ative logging em execução pequena e isolada, remova debug antes do benchmark e redija atributos sensíveis.

## Exemplo
Um teste de smoke imprime somente chave de fixture; a simulação de carga registra métricas sem despejar Session.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. Logging pode ainda afetar medição mesmo que a aplicação não mude; dados exportados exigem proteção.

## Como verificar
Compare RPS e uso de CPU com debug habilitado/desabilitado e procure valores secretos nos artifacts.

## Conexões
- [[gatling-protocol-config-comum]] — Veja também: Gatling: centralizar protocolo HTTP comum sem esconder overrides.

## Fontes
- [Gatling — Session API](https://docs.gatling.io/concepts/session/api/) — estado de cada virtual user e propagação de atributos; consultado em 2026-10-02.
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
