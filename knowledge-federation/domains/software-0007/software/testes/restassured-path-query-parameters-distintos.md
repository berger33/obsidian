---
id: software.testes.tranche11.000453
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
fontes: ["https://github.com/rest-assured/rest-assured/wiki/Usage", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: distinguir path parameters de query parameters

## Em uma frase
Path parameters substituem segmentos nomeados do caminho; query parameters são enviados na parte de consulta da URL.

## Por que importa
REST Assured oferece uma DSL Java para enviar requisições HTTP e validar respostas, mas sua cobertura depende dos dados, do servidor e das assertions escritos no teste. Usar ambos como um único texto de URL dificulta variar identificadores e filtros e pode produzir encoding ou ordenação frágil.

## Como funciona
Separe preparação da requisição, envio e verificação da resposta; reaproveite specifications somente para invariantes, forneça dados próprios por cenário e mantenha configuração, credenciais e logs controlados. Declare o identificador de recurso como path parameter e filtros ou paginação como query parameters, sem concatenar valores manualmente.

## Exemplo
O teste faz GET em /orders/{orderId} com orderId dinâmico e envia status=pending como parâmetro de consulta independente.

## Limites e trade-offs
Um teste do cliente não prova a correção do provedor nem o contrato completo da API. Mapeadores e validadores de schema dependem de módulos no classpath, e configuração estática compartilhada pode gerar interferência entre testes. Convenções de encoding e valores repetidos dependem da configuração e do contrato HTTP esperado pelo servidor.

## Como verificar
Inspecione a URL efetivamente recebida pelo servidor de teste para validar caminho, nomes, multiplicidade e encoding de parâmetros.

## Conexões
- [[restassured-response-specification-contrato-comum]] — Veja também: REST Assured: compartilhar expectativas de resposta sem mascarar exceções.
- [[restassured-object-mapping-dependencias-explícitas]] — Veja também: REST Assured: verificar dependências exigidas por object mapping.

## Fontes
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
- [REST Assured — RequestSpecification API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html) — configuração e composição de requests, parâmetros, corpos, headers, filtros e especificações reutilizáveis; consultado em 2026-10-02.
