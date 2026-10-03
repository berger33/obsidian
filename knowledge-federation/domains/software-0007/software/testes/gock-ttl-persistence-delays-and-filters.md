---
id: software.testes.tranche25.001939
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

# Recursos avançados da lista de Features: persistência/TTL, atrasos, filtros/maps e compatibilidade

## Em uma frase
A seção Features do README enumera capacidades além do mock unitário de uma chamada: suporte a mocks persistentes e voláteis limitados por TTL ("Supports persistent and volatile TTL-limited mocks"), simulação de atraso de rede e cancelamento/timeout ("Network timeout/cancelation delay simulation"), filtros e mapeadores de requisições HTTP ("Ability to filter/map HTTP requests for accurate mock matching"), regras de matching plugáveis e compatibilidade com qualquer cliente baseado em net/http, como o gentleman (github.com/h2non/gentleman), com referência completa da API no GoDoc e mais casos no diretório _examples.

## Por que importa
Por padrão, um mock volátil é consumido quando casa; poder torná-lo persistente ou limitado por TTL, injetar atrasos para testar context.Context/timeouts do cliente e aplicar filtros de requisição cobre cenários de resiliência e uso em runtime sem trocar de biblioteca.

## Como funciona
Consulte a referência GoDoc (godoc.org/github.com/h2non/gock) e a pasta _examples do repositório quando precisar configurar persistência/TTL de mocks, simular latência/timeout de rede ou registrar funções de filtro e mapeamento de requisições.

## Exemplo
Para testar se um cliente HTTP aborta corretamente quando o servidor demora mais que o deadline configurado, usa-se o recurso de simulação de delay/timeout listado nas Features do gock em vez de subir um servidor lento real.

## Limites e trade-offs
Esta nota resume as capacidades declaradas na lista Features do README e aponta os canais oficiais (_examples e GoDoc) onde a assinatura de cada método correspondente é detalhada.

## Como verificar
Conferi a seção Features, a seção API e o link da seção Examples no README oficial.

## Conexões
- [[gock-json-body-matching-and-reply]] — Veja também: Matching de payload e resposta JSON com Post, MatchType("json") e JSON(...).

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
