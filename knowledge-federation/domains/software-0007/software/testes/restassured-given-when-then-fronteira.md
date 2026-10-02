---
id: software.testes.tranche11.000450
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
fontes: ["https://github.com/rest-assured/rest-assured/wiki/Usage", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: separar preparação, chamada e assertions

## Em uma frase
O padrão given/when/then organiza a especificação da requisição, a execução do HTTP e as expectativas sobre a resposta.

## Por que importa
Assertions distribuídas em helpers pouco claros podem ocultar qual entrada produziu um status ou corpo inesperado.

## Como funciona
Monte headers, parâmetros e corpo no given, faça a chamada identificável no when e valide status, headers e campos de resposta no then.

## Exemplo
Um teste POST configura JSON e token, envia a criação de pedido e verifica status 201, tipo de conteúdo e identificador devolvido.

## Limites e trade-offs
A DSL melhora leitura, mas não define por si só se a chamada é unitária, de integração ou contra um serviço externo.

## Como verificar
Compare o request construído com o contrato e verifique que cada assertion aponta para uma saída observável relevante.

## Conexões
- [[restassured-request-specification-reuso-isolado]] — Veja também: REST Assured: reutilizar request specification sem compartilhar mutações.

## Fontes
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
- [REST Assured — ValidatableResponse API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html) — assertions encadeadas e validação de status, headers e corpo da resposta; consultado em 2026-10-02.
