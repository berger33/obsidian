---
id: software.web.revalidacao-cache-etag.000001
tipo: tecnica
dominio: software
subdominio: web
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-4.3", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [Cache revalidation, If-None-Match, HTTP 304, Conditional GET]
lote: software-cache-http-0006
---

# Revalidação de cache com ETag e If-None-Match

## Em uma frase
Quando uma cópia HTTP fica stale, um cache pode perguntar ao origin se a representação mudou e reutilizar o corpo armazenado após uma resposta `304 Not Modified`.

## Por que importa
Uma resposta pode precisar de validação frequente, mas ainda ser útil manter uma cópia local para evitar retransmitir um corpo inalterado. Revalidação separa “posso reutilizar sem contatar o origin?” de “o conteúdo realmente mudou?”. Ela reduz tráfego em alguns cenários, mas ainda exige uma ida ao servidor para confirmar.

## Como funciona
O origin pode enviar um `ETag` opaco junto à representação. Ao validar uma cópia, cliente ou cache envia `If-None-Match` com esse validador. Para `GET` e `HEAD`, se a condição corresponder, o origin pode responder `304 Not Modified` sem o corpo; o cache mantém a representação armazenada e atualiza metadados de acordo com as regras HTTP. Se não corresponder, o servidor envia uma representação atual, normalmente com `200 OK`. Quando `If-None-Match` e `If-Modified-Since` estão presentes, o validador de entidade tem precedência conforme a semântica HTTP.

## Exemplo
Uma página HTML pode ser armazenada com `Cache-Control: no-cache` e um `ETag`. Cada reutilização exige validação, mas, se o conteúdo não mudou, o cliente recebe um `304` e reaproveita o corpo local em vez de baixá-lo novamente.

## Limites e trade-offs
`304` evita transferir novamente a representação, mas não evita a solicitação ao servidor nem o custo de validação. O ETag não é necessariamente um hash do conteúdo: pode ser um identificador de versão gerado pelo servidor. `If-None-Match` também tem semântica condicional para métodos diferentes de GET/HEAD; esta nota trata do caso de validação de cache, não de controle de escrita concorrente.

## Como verificar
Registre uma resposta inicial com ETag, force a resposta a ficar stale e repita a solicitação observando `If-None-Match`. Confirme que a versão inalterada recebe `304` e que uma mudança real recebe a representação nova. Verifique que cabeçalhos de cache presentes na resposta 304 atualizam corretamente os metadados guardados.

## Conexões
- [[freshness-age-cache-http]] — revalidação passa a ser relevante quando o frescor normal termina.
- [[concorrencia-otimista-etag-if-match]] — ETag/If-Match protege mutações concorrentes, enquanto If-None-Match valida representações.
- [[cache-control-diretivas-armazenamento-http]] — `no-cache` permite armazenar e exige validar antes da reutilização.

## Fontes
- [RFC 9111 — HTTP Caching, seção 4.3](https://www.rfc-editor.org/rfc/rfc9111.html#section-4.3) — solicitação de validação e atualização de respostas armazenadas; acesso em 2026-10-01.
- [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching) — validação condicional com ETag, If-None-Match e 304; acesso em 2026-10-01.
