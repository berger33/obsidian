---
id: software.testes.tranche25.001933
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/h2non/gock/master/README.md", "https://github.com/h2non/gock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Dica de precedência: declarar mocks mais concretos antes dos genéricos

## Em uma frase
A subseção Define complex mocks first em Tips orienta que, ao definir vários mocks na mesma suíte de teste, recomenda-se declarar os mocks mais concretos primeiro e os genéricos depois, evitando que um mock genérico case por engano uma requisição que tinha cabeçalhos ou corpo específicos.

## Por que importa
Como o passo 2 de How it mocks avalia o pool de expectativas em ordem FIFO de declaração, um mock que exige apenas Get("/bar") sempre dará match em uma requisição GET /bar com cabeçalhos especiais se tiver sido registrado antes do mock que exige MatchHeader.

## Como funciona
Sempre que registrar mais de um mock para o mesmo host e caminho, coloque no topo as declarações com restrições adicionais (MatchHeader, MatchParam, JSON body) e deixe por último o mock de fallback mais amplo.

## Exemplo
Se você tem um mock para GET /items?page=2 e outro genérico para qualquer GET /items, declare o mock com MatchParam("page", "2") primeiro e o mock sem parâmetros depois.

## Limites e trade-offs
Ainda melhor do que depender apenas da ordem dentro de uma suíte longa é manter cada função de teste isolada com seu próprio defer gock.Off(), registrando apenas os mocks necessários para aquele cenário.

## Como verificar
Conferi a subseção Define complex mocks first na seção Tips do README oficial.

## Conexões
- [[gock-defer-off-and-isdone]] — Veja também: Ciclo de vida no teste: defer gock.Off() e verificação de pendências com gock.IsDone().
- [[gock-concurrency-and-race-conditions-caveat]] — Veja também: Concorrência e condições de corrida: declarar mocks antes de disparar goroutines.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [Repositório oficial h2non/gock](https://github.com/h2non/gock) — Repositório oficial do gock no GitHub com código-fonte sem dependências externas e diretório _examples.; consultado em 2026-10-03.
