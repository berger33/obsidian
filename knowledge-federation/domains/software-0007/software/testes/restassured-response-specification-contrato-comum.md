---
id: software.testes.tranche11.000452
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
fontes: ["https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html", "https://github.com/rest-assured/rest-assured/wiki/Usage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: compartilhar expectativas de resposta sem mascarar exceções

## Em uma frase
Uma response specification permite reutilizar assertions comuns para respostas de vários testes.

## Por que importa
Se cada cenário validar somente status, mudanças de Content-Type ou headers obrigatórios podem passar despercebidas; uma especificação genérica demais também pode impor expectativas sem relação com o caso.

## Como funciona
Defina um conjunto enxuto de invariantes comuns, como tipo de conteúdo ou header de segurança, e mantenha no teste as assertions específicas do endpoint.

## Exemplo
Vários GET validam application/json por specification comum, enquanto cada teste verifica seus próprios campos e semântica de status.

## Limites e trade-offs
A API e a forma de declarar a specification variam conforme a versão usada; não compartilhe uma specification que o teste modifica.

## Como verificar
Faça um teste de controle que remova cada header obrigatório e confirme que a expectativa compartilhada falha pelo motivo esperado.

## Conexões
- [[restassured-request-specification-reuso-isolado]] — Veja também: REST Assured: reutilizar request specification sem compartilhar mutações.
- [[restassured-path-query-parameters-distintos]] — Veja também: REST Assured: distinguir path parameters de query parameters.

## Fontes
- [REST Assured — ValidatableResponse API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html) — assertions encadeadas e validação de status, headers e corpo da resposta; consultado em 2026-10-02.
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
