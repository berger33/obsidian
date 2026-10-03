---
id: software.testes.tranche15.000922
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/api/setup-server/use", "https://mswjs.io/guides/best-practices/structuring-handlers"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: usar server.use para acrescentar overrides locais a um cenário

## Em uma frase
`server.use` adiciona handlers em runtime que podem sobrescrever a resposta base, permitindo representar erro ou estado específico no teste que precisa dele.

## Por que importa
Manter respostas de sucesso no conjunto inicial e variações locais perto do caso evita poluir o mapa central com todos os estados possíveis.

## Como funciona
Como o handler novo tem precedência, uma alteração sem reset pode afetar testes seguintes.

## Exemplo
No teste de falha, use `server.use(http.get('/user', () => new HttpResponse(null, { status: 500 })))` e valide como a interface reage à resposta.

## Limites e trade-offs
Override não simula qualquer comportamento de rede automaticamente; preserve método e URL corretos e limpe handlers no lifecycle do runner para não haver vazamento.

## Como verificar
Execute primeiro o teste de sucesso e depois o de erro em ordens diferentes, verificando que a resposta base retorna após o reset de estado.

## Conexões
- [[msw-listen-onunhandledframe-com-politica-explicita]] — Veja também: MSW: falhar ou avisar para frames de rede sem handler.
- [[msw-reset-handlers-restaura-lista-inicial]] — Veja também: MSW: distinguir resetHandlers sem argumentos de substituição da lista.

## Fontes
- [MSW — use()](https://mswjs.io/api/setup-server/use) — adição e precedência de runtime handlers; consultado em 2026-10-02.
- [MSW — Structuring handlers](https://mswjs.io/guides/best-practices/structuring-handlers) — handlers de sucesso, overrides e composição por domínio; consultado em 2026-10-02.
