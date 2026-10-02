---
id: software.testes.tranche11.000451
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
fontes: ["https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/RestAssured.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: reutilizar request specification sem compartilhar mutações

## Em uma frase
RequestSpecification agrupa dados de request que podem ser compostos e reaproveitados em várias chamadas.

## Por que importa
REST Assured oferece uma DSL Java para enviar requisições HTTP e validar respostas, mas sua cobertura depende dos dados, do servidor e das assertions escritos no teste. Duplicar base URI, headers comuns e autenticação em cada caso cria divergência; um objeto global mutável pode, por outro lado, vazar dados entre testes.

## Como funciona
Separe preparação da requisição, envio e verificação da resposta; reaproveite specifications somente para invariantes, forneça dados próprios por cenário e mantenha configuração, credenciais e logs controlados. Construa uma specification comum para invariantes e derive ou crie uma configuração por cenário quando parâmetros e headers mudarem.

## Exemplo
Uma specification base define host e Accept; cada teste cria sua própria cópia lógica com token e path parameter do usuário em teste.

## Limites e trade-offs
Um teste do cliente não prova a correção do provedor nem o contrato completo da API. Mapeadores e validadores de schema dependem de módulos no classpath, e configuração estática compartilhada pode gerar interferência entre testes. O merge de specifications tem regras próprias para campos sobrescritos e mesclados; não presuma que toda propriedade é acumulada.

## Como verificar
Execute os casos em paralelo e em ordem aleatória e confirme que host, autenticação e parâmetros permanecem associados ao cenário certo.

## Conexões
- [[restassured-given-when-then-fronteira]] — Veja também: REST Assured: separar preparação, chamada e assertions.
- [[restassured-response-specification-contrato-comum]] — Veja também: REST Assured: compartilhar expectativas de resposta sem mascarar exceções.

## Fontes
- [REST Assured — RequestSpecification API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html) — configuração e composição de requests, parâmetros, corpos, headers, filtros e especificações reutilizáveis; consultado em 2026-10-02.
- [REST Assured — RestAssured API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/RestAssured.html) — configuração de URI, especificações, parsers, filtros e valores estáticos padrão; consultado em 2026-10-02.
