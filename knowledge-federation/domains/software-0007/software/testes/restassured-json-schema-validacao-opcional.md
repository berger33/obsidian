---
id: software.testes.tranche11.000456
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
fontes: ["https://github.com/rest-assured/rest-assured/wiki/Usage#json-schema-validation", "https://github.com/rest-assured/rest-assured/wiki/Usage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: tratar JSON Schema como validação configurada

## Em uma frase
REST Assured oferece matcher para validar um corpo JSON contra um schema, disponível pela integração de validação correspondente.

## Por que importa
REST Assured oferece uma DSL Java para enviar requisições HTTP e validar respostas, mas sua cobertura depende dos dados, do servidor e das assertions escritos no teste. Verificar poucos campos pode deixar propriedades obrigatórias, tipos ou estruturas aninhadas incompatíveis com o contrato passar despercebidas.

## Como funciona
Separe preparação da requisição, envio e verificação da resposta; reaproveite specifications somente para invariantes, forneça dados próprios por cenário e mantenha configuração, credenciais e logs controlados. Inclua a dependência de JSON Schema Validator, carregue schema versionado e aplique o matcher à resposta que já teve status validado.

## Exemplo
A resposta de listagem é conferida contra schema que exige id e name em cada item e define o tipo de price.

## Limites e trade-offs
Um teste do cliente não prova a correção do provedor nem o contrato completo da API. Mapeadores e validadores de schema dependem de módulos no classpath, e configuração estática compartilhada pode gerar interferência entre testes. O schema precisa refletir a versão de contrato pretendida; matcher não verifica regras de negócio nem que o schema esteja correto.

## Como verificar
Altere um tipo obrigatório de resposta em um teste negativo e confirme que o matcher reporta o caminho do campo inválido.

## Conexões
- [[restassured-jsonpath-extrair-depois-de-validar]] — Veja também: REST Assured: extrair valores JSON após validar a resposta.
- [[restassured-filtros-logging-nao-e-wire-capture]] — Veja também: REST Assured: não confundir logging de filtro com captura exata no wire.

## Fontes
- [REST Assured — JSON Schema Validation](https://github.com/rest-assured/rest-assured/wiki/Usage#json-schema-validation) — matcher opcional para verificar resposta JSON contra schema; consultado em 2026-10-02.
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
