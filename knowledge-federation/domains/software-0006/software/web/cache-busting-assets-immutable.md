---
id: software.web.cache-busting-immutable.000001
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
fontes: ["https://www.rfc-editor.org/rfc/rfc8246.html", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [Cache busting, Fingerprinted assets, Immutable HTTP response]
lote: software-cache-http-0006
---

# Cache busting e assets imutáveis

## Em uma frase
Publicar assets estáticos em URLs versionadas ou com fingerprint permite usar uma vida de cache longa sem servir silenciosamente uma versão nova sob a URL antiga.

## Por que importa
Uma folha de estilo ou script reutilizada rapidamente economiza tráfego, mas pode permanecer desatualizada após um deploy se o conteúdo mudar sem que a URL mude. Fingerprints vinculados ao conteúdo resolvem a atualização alterando o identificador no URL quando os bytes mudam. O cache pode então conservar a versão anterior enquanto páginas novas passam a referenciar a nova.

## Como funciona
Um build gera arquivos como `app.abc123.js`, cuja versão muda junto com o conteúdo. O servidor pode dar a esses recursos uma vida de frescor longa e usar `immutable`. A extensão definida pela RFC 8246 indica que o origin não atualizará a representação durante o período de frescor; clientes não precisam revalidar uma resposta ainda fresca apenas por um reload comum. A diretiva não elimina revalidação depois que a resposta fica stale. O HTML que referencia os assets costuma precisar de política mais curta ou validação para apontar aos novos nomes após a publicação.

## Exemplo
Uma implantação entrega `/assets/app.abc123.js` com `Cache-Control: public, max-age=31536000, immutable`. Quando o conteúdo muda, o build publica `/assets/app.def456.js` e altera a referência no HTML. O cliente pode manter o recurso antigo em cache, mas a página nova solicita outro URL.

## Limites e trade-offs
`immutable` é seguro apenas se o origin realmente não substituir a representação durante o período de frescor. Se arquivos diferentes forem publicados com o mesmo URL fingerprintado, caches podem servir conteúdo incoerente. Metadados de cache e HTML de entrada precisam ser implantados de forma coordenada; a diretiva não invalida caches remotamente nem corrige referências antigas já distribuídas.

## Como verificar
Compare hash/versão no nome do asset antes e depois de alterar bytes. Inspecione `Cache-Control`, faça reload normal e force reload para observar revalidação, e teste que o HTML novo aponta ao nome novo. Valide também que rollback do deploy restaura referências a assets que continuam disponíveis.

## Conexões
- [[freshness-age-cache-http]] — `max-age` define o período em que `immutable` pode dispensar revalidação.
- [[revalidacao-cache-etag-if-none-match]] — revalidação continua útil para recursos sem URL versionada.
- [[cache-control-diretivas-armazenamento-http]] — `public` e `max-age` têm papéis diferentes de `immutable`.

## Fontes
- [RFC 8246 — HTTP Immutable Responses](https://www.rfc-editor.org/rfc/rfc8246.html) — semântica e escopo de `immutable`; acesso em 2026-10-01.
- [MDN — Cache-Control header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) — padrão de cache de assets versionados; acesso em 2026-10-01.
