---
id: software.testes.tranche15.000865
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
fontes: ["https://mswjs.io/docs/api/http-response/", "https://mswjs.io/docs/http/handling-requests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: construir respostas com HttpResponse

## Em uma frase
`HttpResponse` oferece métodos como `json`, `text`, `html` e `error` para compor status, cabeçalhos e corpo da resposta mockada de forma tipada.

## Por que importa
Respostas montadas como objeto solto esquecem cabeçalhos e formato, fazendo o código sob teste interpretar o corpo de maneira diferente do serviço real.

## Como funciona
Use o método correspondente ao tipo de conteúdo, informe status e cabeçalhos relevantes e mantenha os dados do corpo em fixtures reutilizáveis entre handlers.

## Exemplo
`HttpResponse.json({ erro: 'indisponivel' }, { status: 503, headers: { 'Retry-After': '30' } })` simula indisponibilidade com o mesmo contrato esperado pelo cliente.

## Limites e trade-offs
O helper não valida se o formato escolhido corresponde ao que o consumidor espera, e respostas simplificadas demais podem deixar de exercitar ramos importantes do código.

## Como verificar
Compare o corpo e os cabeçalhos recebidos pelo cliente com o contrato do serviço modelado, incluindo códigos de erro e tipos de conteúdo alternativos.

## Conexões
- [[msw-passthrough-real-response]] — Veja também: MSW: encaminhar requisições com passthrough.
- [[msw-url-patterns-and-params]] — Veja também: MSW: casar URLs e extrair parâmetros.

## Fontes
- [MSW — HttpResponse](https://mswjs.io/docs/api/http-response/) — construção de respostas com status, cabeçalhos e corpos tipados; consultado em 2026-10-02.
- [MSW — Handling requests](https://mswjs.io/docs/http/handling-requests) — resposta mockada, passthrough e handlers que não respondem; consultado em 2026-10-02.
