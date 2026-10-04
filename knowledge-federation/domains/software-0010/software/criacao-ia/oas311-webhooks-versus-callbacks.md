---
id: software.criacao_ia.tranche03.000298
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://spec.openapis.org/oas/v3.1.1.html#oas-webhooks", "https://spec.openapis.org/oas/v3.1.1.html#callback-object"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# OAS 3.1.1: escolher entre webhook top-level e callback de operação

## Em uma frase
`webhooks` descreve requests recebidas independentemente de outra chamada; um Callback Object descreve request associada a uma operação e a um runtime expression.

## Por que importa
Os dois recursos podem descrever chamadas iniciadas pelo provider, mas têm gatilhos diferentes. Colocar qualquer push do serviço em callback pode sugerir falsamente que uma request específica sempre o provoca, e representar um callback como webhook omite a URL derivada do contexto da operação.

## Como funciona
Use o campo top-level `webhooks` para incoming requests que o consumer pode implementar, inclusive eventos iniciados fora de uma chamada API anterior, como após registro out-of-band. Use `callbacks` no Operation Object quando a request do provider decorre daquela operação; a chave do callback pode ser uma expressão avaliada no request/response runtime para localizar a URL.

## Exemplo
Um provider envia avisos de conta depois que o consumer registrou endpoint fora de uma operação: descreva o formato em `webhooks`. Já uma operação `/subscribe` recebe `queryUrl` e por causa dela envia confirmação para aquele endereço: modele como callback com chave baseada em `$request.query.queryUrl`.

## Limites e trade-offs
Ambos descrevem o contrato da mensagem iniciada pelo provider, não provam que a entrega ocorrerá ou que a URL estará alcançável. A proteção SSRF, autenticação e política de retries do endpoint callback/webhook pertencem também à implementação e deployment.

## Como verificar
Inspecione o gatilho de cada mensagem: se depende de uma operação identificável, modele callback; se é independente de uma chamada, modele webhook. Teste a avaliação da expressão de URL com request que tem e que não tem o campo esperado.

## Conexões
- [[oas311-binary-contentencoding-vs-format]] — OAS 3.1.1: modelar binário com contentEncoding e contentMediaType.
- [[oas311-path-item-ref-conflitos]] — OAS 3.1.1 Path Item `$ref`: não sobrepor fields com o alvo.

## Fontes
- [OpenAPI Specification v3.1.1 — OpenAPI Object webhooks](https://spec.openapis.org/oas/v3.1.1.html#oas-webhooks) — define incoming webhooks top-level, fora de uma chamada API Consulta: 2026-10-04.
- [OpenAPI Specification v3.1.1 — Callback Object](https://spec.openapis.org/oas/v3.1.1.html#callback-object) — define requests out-of-band relacionadas à operação pai e suas runtime expressions Consulta: 2026-10-04.
