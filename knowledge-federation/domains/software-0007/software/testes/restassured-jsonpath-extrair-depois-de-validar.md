---
id: software.testes.tranche11.000455
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

# REST Assured: extrair valores JSON após validar a resposta

## Em uma frase
JsonPath permite selecionar valores do corpo JSON da resposta para assertions ou etapas posteriores do teste.

## Por que importa
REST Assured oferece uma DSL Java para enviar requisições HTTP e validar respostas, mas sua cobertura depende dos dados, do servidor e das assertions escritos no teste. Extrair um campo sem primeiro validar status e formato pode transformar uma resposta de erro em falha secundária confusa.

## Como funciona
Separe preparação da requisição, envio e verificação da resposta; reaproveite specifications somente para invariantes, forneça dados próprios por cenário e mantenha configuração, credenciais e logs controlados. Valide primeiro status e Content-Type; então extraia o campo relevante e compare seu valor ou use-o em uma chamada subsequente controlada.

## Exemplo
Um GET de pedido verifica status 200 e JSON antes de extrair o id para consultar uma rota de detalhe.

## Limites e trade-offs
Um teste do cliente não prova a correção do provedor nem o contrato completo da API. Mapeadores e validadores de schema dependem de módulos no classpath, e configuração estática compartilhada pode gerar interferência entre testes. JsonPath verifica caminhos e valores escolhidos, mas não prova que todos os campos ou a estrutura completa obedecem a um schema.

## Como verificar
Substitua o status de sucesso por erro e confirme que o teste falha na assertion de protocolo antes da extração do campo.

## Conexões
- [[restassured-object-mapping-dependencias-explícitas]] — Veja também: REST Assured: verificar dependências exigidas por object mapping.
- [[restassured-json-schema-validacao-opcional]] — Veja também: REST Assured: tratar JSON Schema como validação configurada.

## Fontes
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
- [REST Assured — ValidatableResponse API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/response/ValidatableResponse.html) — assertions encadeadas e validação de status, headers e corpo da resposta; consultado em 2026-10-02.
