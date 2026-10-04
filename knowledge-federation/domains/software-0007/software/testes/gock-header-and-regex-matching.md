---
id: software.testes.tranche25.001936
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
fontes: ["https://raw.githubusercontent.com/h2non/gock/master/README.md", "https://godoc.org/github.com/h2non/gock"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Matching de cabeçalhos com expressões regulares: MatchHeader e HeaderPresent

## Em uma frase
O exemplo TestMatchHeaders e a seção Features do README demonstram o pareamento de cabeçalhos HTTP com suporte a expressões regulares completas: gock.New("http://foo.com").MatchHeader("Authorization", "^foo bar$").MatchHeader("API", "1.[0-9]+").HeaderPresent("Accept").Reply(200).BodyString("foo foo").

## Por que importa
Clientes de API frequentemente enviam cabeçalhos dinâmicos ou versionados (como tokens, cabeçalhos de versão "1.0" ou "Accept" obrigatório); validar esses cabeçalhos com regex diretamente na expectativa do mock garante que o cliente não apenas chamou a URL certa, mas enviou os metadados de protocolo corretos.

## Como funciona
Encadeie MatchHeader(nome, padraoRegex) para validar o valor do cabeçalho (usando âncoras ^ e $ ou classes como [0-9]+) e HeaderPresent(nome) quando quiser exigir apenas que o cabeçalho exista na requisição.

## Exemplo
No exemplo TestMatchHeaders do README, a requisição monta req.Header.Set("Authorization", "foo bar"), req.Header.Set("API", "1.0") e req.Header.Set("Accept", "text/plain"), casando com as três regras declaradas no mock.

## Limites e trade-offs
Como MatchHeader interpreta o segundo argumento como expressão regular (por exemplo "1.[0-9]+"), metacaracteres de regex no valor esperado devem ser tratados como padrão regular ao escrever a expectativa.

## Como verificar
Conferi a seção Features e o exemplo TestMatchHeaders no README oficial do gock.

## Conexões
- [[gock-custom-http-client-intercept-and-restore]] — Veja também: Clientes customizados: gock.InterceptClient(client) uma vez e defer gock.RestoreClient(client).
- [[gock-query-params-matching]] — Veja também: Matching de parâmetros de URL com MatchParam.

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
