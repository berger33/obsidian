---
id: software.testes.tranche15.000866
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
fontes: ["https://mswjs.io/docs/http/intercepting-requests", "https://mswjs.io/docs/defaults/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: casar URLs e extrair parâmetros

## Em uma frase
Padrões de URL podem incluir parâmetros de caminho como `:id`, curingas e expressões, e o resolver recebe os valores extraídos para montar a resposta.

## Por que importa
Comparar apenas parte da URL ou esquecer a base absoluta faz o handler não casar e a requisição cair em aviso ou rede real sem que o teste perceba.

## Como funciona
Prefira padrões estreitos o suficiente para não capturar rotas vizinhas e leia os parâmetros nomeados em vez de recortar a URL manualmente dentro do resolver.

## Exemplo
`http.get('/api/pedidos/:pedidoId', ({ params }) => HttpResponse.json({ id: params.pedidoId }))` responde de acordo com o identificador recebido.

## Limites e trade-offs
URLs relativas dependem do contexto de execução e exigem atenção especial em Node, e padrões amplos podem interceptar chamadas de terceiros que deveriam permanecer fora do mock.

## Como verificar
Registre a URL completa vista pelo handler e confirme o casamento para uma rota existente e a ausência de casamento para uma rota vizinha.

## Conexões
- [[msw-httpresponse-construction]] — Veja também: MSW: construir respostas com HttpResponse.
- [[msw-async-handler-and-body]] — Veja também: MSW: ler corpo de requisição em handler assíncrono.

## Fontes
- [MSW — Intercepting requests](https://mswjs.io/docs/http/intercepting-requests) — handlers por método e URL, parâmetros de caminho e resolução de requisições; consultado em 2026-10-02.
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
