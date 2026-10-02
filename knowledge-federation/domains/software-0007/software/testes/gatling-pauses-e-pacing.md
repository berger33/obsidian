---
id: software.testes.tranche11.000537
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
fontes: ["https://docs.gatling.io/concepts/timings/", "https://docs.gatling.io/concepts/injection/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: distinguir pausa do usuário de arrival-rate injection

## Em uma frase
Pause modela intervalo entre ações do scenario; injection controla chegada/concorrência inicial de virtual users.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Aumentar pause pode reduzir requests por usuário sem necessariamente representar chegada pretendida de usuários novos.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Use pauses para think time dentro de workflow e ajuste injection profile para população e ritmo de chegada.

## Exemplo
Usuário lê página e espera antes de enviar formulário; teste de pico separado injeta perfis crescentes.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. Duração de resposta soma ao ciclo do usuário e afeta modelo fechado; pause não é garantia de RPS.

## Como verificar
Meça request rate e users ativos após variar pause e injection separadamente.

## Conexões
- [[gatling-groups-agregacao-por-jornada]] — Veja também: Gatling: nomear groups para separar estatísticas de jornada.
- [[gatling-protocol-config-comum]] — Veja também: Gatling: centralizar protocolo HTTP comum sem esconder overrides.

## Fontes
- [Gatling — Timings](https://docs.gatling.io/concepts/timings/) — pausas e temporização explícita dos fluxos simulados; consultado em 2026-10-02.
- [Gatling — Injection](https://docs.gatling.io/concepts/injection/) — modelos open/closed e perfis de usuários; consultado em 2026-10-02.
