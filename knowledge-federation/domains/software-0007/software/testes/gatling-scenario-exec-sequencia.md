---
id: software.testes.tranche11.000530
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
fontes: ["https://docs.gatling.io/concepts/scenario/", "https://docs.gatling.io/concepts/session/api/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: construir workflow ordenado com exec

## Em uma frase
Um ScenarioBuilder encadeia ações com exec; requests e funções executadas no cenário seguem a sequência declarada.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Request de checkout pode rodar sem autenticação se a etapa anterior foi omitida ou a cadeia não foi ligada ao scenario correto.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Divida jornadas reutilizáveis em chains pequenas e encadeie explicitamente login, leitura, ação e verificação.

## Exemplo
O virtual user busca carrinho, extrai id, adiciona item e conclui checkout em ações sucessivas.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. Uma sequência sintática correta não garante que o estado do serviço corresponda à precondição de cada passo.

## Como verificar
Inspecione order de requests e faça um teste pequeno que valide status e estado final antes de subir carga.

## Conexões
- [[gatling-session-estado-por-virtual-user]] — Veja também: Gatling: manter atributos na Session do próprio usuário.

## Fontes
- [Gatling — Scenario](https://docs.gatling.io/concepts/scenario/) — sequência de ações, exec, controles de fluxo e pausas; consultado em 2026-10-02.
- [Gatling — Session API](https://docs.gatling.io/concepts/session/api/) — estado de cada virtual user e propagação de atributos; consultado em 2026-10-02.
