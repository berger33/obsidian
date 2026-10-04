---
id: software.apis.problem-details-http.000001
tipo: conceito
dominio: software
subdominio: apis
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc9457.html", "https://www.rfc-editor.org/rfc/rfc9110.html"]
tags: [dominio/software, subdominio/apis, qualidade/candidata]
aliases: [RFC 9457, Problem Details, application/problem+json]
lote: software-seguranca-0003
---

# Problem Details (RFC 9457) para erros de APIs HTTP

## Em uma frase
RFC 9457 define um formato comum para transportar detalhes legíveis por máquina sobre um erro HTTP sem substituir o significado do código de status.

## Por que importa
Um `400` ou `503` comunica uma categoria geral, mas pode não explicar ao cliente qual problema ocorreu ou como apresentá-lo. Um formato estável evita que cada endpoint invente um envelope incompatível e permite que clientes tratem erros conhecidos sem interpretar texto livre. A especificação também reduz a tentação de atribuir a um status HTTP um significado diferente do definido pelo protocolo.

## Como funciona
Uma resposta JSON usa `Content-Type: application/problem+json`. Os membros padronizados incluem `type` (identificador URI do tipo de problema; se ausente, assume `about:blank`), `title` (resumo legível), `status` (cópia informativa do status HTTP), `detail` (explicação desta ocorrência) e `instance` (identificador da ocorrência). Membros de extensão podem transportar dados específicos da API. Se o corpo incluir `status`, o servidor ainda precisa enviar o mesmo código na linha de status HTTP; clientes genéricos podem nunca ler o JSON. `type` identifica a classe do problema, enquanto `instance` pode identificar um caso particular.

## Exemplo
Uma API pode responder a uma entrada semanticamente inválida com `422 Unprocessable Content`, `application/problem+json`, um `type` estável para “pedido inválido” e uma explicação curta. O mesmo tipo pode aparecer em ocorrências diferentes; `instance` e `detail` podem variar. Clientes podem tomar decisões sobre o tipo e o status, em vez de depender de uma frase traduzida.

## Limites e trade-offs
RFC 9457 padroniza o envelope, não as regras de negócio, a taxonomia de erros ou a compatibilidade de cada extensão. Não inclua stack traces, credenciais, dados pessoais desnecessários ou detalhes internos exploráveis em `detail`. Nem todo erro precisa desse formato; para uma representação de recurso normal, use o modelo próprio do recurso. Mudanças em membros de extensão ainda precisam de uma política de compatibilidade.

## Como verificar
Teste o status HTTP real, o media type, a estabilidade de `type` e o tratamento de campos ausentes e extensões desconhecidas. Compare a descrição publicada com os exemplos da implementação e confirme que respostas de erro não revelam dados internos. Validação de schema não substitui teste de comportamento.

## Conexões
- [[contrato-openapi-http]] — OpenAPI pode descrever respostas e schemas sem garantir o comportamento em execução.
- [[rate-limit-http-429]] — um limite excedido pode ser comunicado como 429 e descrito com Problem Details.
- [[timeouts-retries-backoff-jitter]] — o cliente precisa combinar códigos de erro com uma política segura de retry.

## Fontes
- [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) — membros do objeto, media type e relação com o status HTTP; acesso em 2026-10-01.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica dos status e mensagens HTTP; acesso em 2026-10-01.
