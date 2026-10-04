---
id: software.testes.tranche15.000860
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
fontes: ["https://mswjs.io/docs/api/setup-server/", "https://mswjs.io/docs/http/intercepting-requests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: interceptar requisições em Node com setupServer

## Em uma frase
`setupServer` configura a interceptação de requisições no processo Node sem abrir porta ou servidor real, aplicando os mesmos handlers usados no navegador.

## Por que importa
Testes de integração precisam de respostas controladas sem depender de rede externa, e um servidor de verdade adicionaria latência, portas e estado compartilhado desnecessários.

## Como funciona
Importe `setupServer` de `msw/node`, forneça a lista de handlers, e mantenha o objeto do servidor em um módulo compartilhado para que cada suíte controle seu ciclo de vida.

## Exemplo
`const server = setupServer(http.get('/user', () => HttpResponse.json({ id: 1 })))` cria o interceptador, que passa a responder às chamadas feitas pelo código sob teste.

## Limites e trade-offs
A interceptação atua no processo e depende das APIs de rede do ambiente; contextos que não passam pelo módulo HTTP do Node podem exigir configuração adicional.

## Como verificar
Faça uma requisição real pelo código de produção e confirme que a resposta veio do handler, sem tráfego externo observável.

## Conexões
- [[msw-lifecycle-listen-reset-close]] — Veja também: MSW: cumprir o ciclo listen, reset e close.

## Fontes
- [MSW — setupServer](https://mswjs.io/docs/api/setup-server/) — interceptação em Node.js e ciclo de vida de listen, resetHandlers e close; consultado em 2026-10-02.
- [MSW — Intercepting requests](https://mswjs.io/docs/http/intercepting-requests) — handlers por método e URL, parâmetros de caminho e resolução de requisições; consultado em 2026-10-02.
