---
id: software.testes.tranche15.000867
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
fontes: ["https://mswjs.io/docs/http/handling-requests", "https://mswjs.io/docs/api/http-response/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: ler corpo de requisição em handler assíncrono

## Em uma frase
Ler o corpo com `await request.json()` exige um resolver assíncrono; um resolver síncrono que tenta aguardar o corpo devolve resultado indefinido.

## Por que importa
Handlers que aparentam funcionar, mas retornam `undefined`, geram respostas vazias e deslocam a investigação para o código consumidor, que não tem defeito algum.

## Como funciona
Declare o resolver como `async`, trate o corpo conforme o tipo de conteúdo e use `request.clone()` quando o mesmo corpo precisar ser lido mais de uma vez.

## Exemplo
`http.post('/login', async ({ request }) => { const dados = await request.json(); return HttpResponse.json({ ok: dados.usuario === 'ada' }); })` decide a resposta com base no conteúdo enviado.

## Limites e trade-offs
Consumir o corpo uma vez esgota o fluxo; sem clone, uma segunda leitura falha mesmo que a primeira tenha funcionado, e formatos diferentes de JSON exigem tratamento próprio.

## Como verificar
Envie um corpo conhecido, confirme que o handler reagiu ao conteúdo e tente ler o mesmo corpo duas vezes para verificar o comportamento com e sem clone.

## Conexões
- [[msw-url-patterns-and-params]] — Veja também: MSW: casar URLs e extrair parâmetros.
- [[msw-shared-handlers-across-environments]] — Veja também: MSW: compartilhar handlers entre testes, dev e Storybook.

## Fontes
- [MSW — Handling requests](https://mswjs.io/docs/http/handling-requests) — resposta mockada, passthrough e handlers que não respondem; consultado em 2026-10-02.
- [MSW — HttpResponse](https://mswjs.io/docs/api/http-response/) — construção de respostas com status, cabeçalhos e corpos tipados; consultado em 2026-10-02.
