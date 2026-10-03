---
id: software.testes.tranche25.001931
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

# Como o gock funciona: RoundTripper, fila FIFO e modo de rede real opcional

## Em uma frase
A seção How it mocks explica o mecanismo em quatro passos numerados: (1) intercepta qualquer requisição HTTP de saída via http.DefaultTransport ou um http.Transport customizado usado por qualquer http.Client; (2) compara as requisições de saída contra um pool de expectativas de mock definidas em ordem FIFO de declaração; (3) se ao menos um mock casar, ele é usado para compor a resposta HTTP simulada; e (4) se nenhum mock casar, resolve a requisição com erro, a menos que o modo de rede real esteja habilitado, caso em que uma requisição HTTP real é realizada.

## Por que importa
Dois detalhes operacionais dessa lista evitam horas de depuração: a avaliação do pool segue estritamente a ordem FIFO em que os mocks foram declarados, e requisições não casadas falham imediatamente com erro por padrão (bloqueando tráfego acidental para fora do teste).

## Como funciona
Declare os mocks na ordem exata em que espera que sejam avaliados pelo pool FIFO e mantenha o modo padrão que retorna erro para requisições não casadas em testes unitários, habilitando o modo de rede real apenas em cenários híbridos.

## Exemplo
Se o código sob teste fizer uma chamada para uma URL não declarada em nenhum gock.New(...), o passo 4 do mecanismo devolve um erro imediato ao http.Client em vez de acessar a internet.

## Limites e trade-offs
Como o matching percorre a fila em ordem FIFO de declaração, um mock genérico declarado antes de um mock específico na mesma rota pode consumir a requisição antes que o mock específico seja testado.

## Como verificar
Conferi os quatro itens da seção How it mocks no README oficial do gock.

## Conexões
- [[gock-what-it-is]] — Veja também: gock: mocking HTTP versátil e sem dependências para clientes net/http em Go.
- [[gock-defer-off-and-isdone]] — Veja também: Ciclo de vida no teste: defer gock.Off() e verificação de pendências com gock.IsDone().

## Fontes
- [gock — README oficial](https://raw.githubusercontent.com/h2non/gock/master/README.md) — README oficial do gock com lista de features, funcionamento em quatro passos via http.RoundTripper e fila FIFO, dicas de defer gock.Off/concorrência/precedência/InterceptClient/RestoreClient e exemplos de código.; consultado em 2026-10-03.
- [gock — referência GoDoc oficial](https://godoc.org/github.com/h2non/gock) — Documentação de referência da API do pacote github.com/h2non/gock no GoDoc.; consultado em 2026-10-03.
