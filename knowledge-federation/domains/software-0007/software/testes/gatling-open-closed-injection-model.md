---
id: software.testes.tranche11.000535
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
fontes: ["https://docs.gatling.io/concepts/injection/", "https://docs.gatling.io/concepts/scenario/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: escolher open ou closed conforme hipótese de carga

## Em uma frase
Perfis open injetam usuários por taxa de chegada; closed model define concorrência de usuários cuja duração influencia novas iterações.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Modelo fechado pode reduzir novas chegadas quando servidor fica lento e subestimar sobrecarga comparado a tráfego independente do tempo de resposta.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Declare se interesse é usuários concorrentes ou taxa de chegada e use injectOpen/injectClosed coerente com hipótese.

## Exemplo
API de ingestão testa chegada de eventos por segundo em modelo open; jornada com sessões concorrentes limitadas usa closed.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. Perfis e formas de injection variam por DSL e produto; não compare execuções sem registrar modelo.

## Como verificar
Inspecione virtual users ativos, taxa de chegada e response time durante degradação para validar dinâmica observada.

## Conexões
- [[gatling-assertions-criterios-de-simulacao]] — Veja também: Gatling: expressar pass fail com assertions de estatísticas.
- [[gatling-groups-agregacao-por-jornada]] — Veja também: Gatling: nomear groups para separar estatísticas de jornada.

## Fontes
- [Gatling — Injection](https://docs.gatling.io/concepts/injection/) — modelos open/closed e perfis de usuários; consultado em 2026-10-02.
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
