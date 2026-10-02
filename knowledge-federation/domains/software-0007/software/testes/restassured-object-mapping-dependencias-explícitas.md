---
id: software.testes.tranche11.000454
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
fontes: ["https://github.com/rest-assured/rest-assured/wiki/Usage#object-mapping", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: verificar dependências exigidas por object mapping

## Em uma frase
REST Assured pode serializar objetos Java para JSON ou XML e desserializar respostas quando os mapeadores compatíveis estão disponíveis no classpath.

## Por que importa
REST Assured oferece uma DSL Java para enviar requisições HTTP e validar respostas, mas sua cobertura depende dos dados, do servidor e das assertions escritos no teste. Um teste que passa na máquina de desenvolvimento pode falhar no CI se o runtime não incluir o mapper ou se o Content-Type não selecionar o formato pretendido.

## Como funciona
Separe preparação da requisição, envio e verificação da resposta; reaproveite specifications somente para invariantes, forneça dados próprios por cenário e mantenha configuração, credenciais e logs controlados. Declare o módulo de mapper exigido pelo projeto, envie DTO representativo e indique o tipo de conteúdo esperado na request.

## Exemplo
O teste envia um DTO de criação como JSON e confirma que o servidor recebeu nomes e tipos coerentes com o modelo wire.

## Limites e trade-offs
Um teste do cliente não prova a correção do provedor nem o contrato completo da API. Mapeadores e validadores de schema dependem de módulos no classpath, e configuração estática compartilhada pode gerar interferência entre testes. O formato concreto depende dos mapeadores instalados e da configuração; DTO Java não comprova sozinho compatibilidade com schema externo.

## Como verificar
Execute com as mesmas dependências do CI e verifique o corpo serializado e o Content-Type no servidor de teste.

## Conexões
- [[restassured-path-query-parameters-distintos]] — Veja também: REST Assured: distinguir path parameters de query parameters.
- [[restassured-jsonpath-extrair-depois-de-validar]] — Veja também: REST Assured: extrair valores JSON após validar a resposta.

## Fontes
- [REST Assured — Object Mapping](https://github.com/rest-assured/rest-assured/wiki/Usage#object-mapping) — serialização e desserialização com mapeadores disponíveis no classpath; consultado em 2026-10-02.
- [REST Assured — RequestSpecification API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html) — configuração e composição de requests, parâmetros, corpos, headers, filtros e especificações reutilizáveis; consultado em 2026-10-02.
