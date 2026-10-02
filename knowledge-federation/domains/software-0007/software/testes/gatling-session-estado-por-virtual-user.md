---
id: software.testes.tranche11.000531
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

# Gatling: manter atributos na Session do próprio usuário

## Em uma frase
Session representa o estado de um virtual user e carrega atributos ao longo das ações do scenario.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Guardar token ou id em variável global pode misturar usuários e gerar requests cruzadas durante concorrência.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Extraia valores para Session e leia-os na expressão seguinte do mesmo usuário, sem compartilhar atributo mutável entre cenários.

## Exemplo
Cada user extrai seu access token do login e usa esse token em request de perfil própria.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. No Gatling Session é imutável; uma transformação precisa devolver a nova Session para que a alteração continue no fluxo.

## Como verificar
Crie dois usuários com tokens distintos e confirme que cada request subsequente carrega somente seu próprio valor.

## Conexões
- [[gatling-scenario-exec-sequencia]] — Veja também: Gatling: construir workflow ordenado com exec.
- [[gatling-feeder-dados-variados-cache]] — Veja também: Gatling: alimentar usuários com registros distintos para workload.

## Fontes
- [Gatling — Session API](https://docs.gatling.io/concepts/session/api/) — estado de cada virtual user e propagação de atributos; consultado em 2026-10-02.
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
