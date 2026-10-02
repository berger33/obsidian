---
id: software.web.vary-cache-variantes.000001
tipo: conceito
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-4.1", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [Vary header, HTTP cache variants, Cache key]
lote: software-cache-http-0006
---

# Variantes de resposta e cabeçalho Vary

## Em uma frase
`Vary` informa quais cabeçalhos da solicitação influenciaram uma resposta, para que uma cache não reutilize uma variante incompatível.

## Por que importa
Uma URL pode produzir representações distintas, por exemplo conforme `Accept-Language` ou `Accept-Encoding`. Se uma cache identificar conteúdo apenas pela URL, pode entregar uma versão comprimida ou localizada a uma solicitação com cabeçalhos diferentes. `Vary` adiciona essas dimensões ao critério de correspondência da resposta armazenada.

## Como funciona
Quando uma resposta contém `Vary`, a cache só pode reutilizá-la sem revalidação quando os valores dos cabeçalhos nomeados na solicitação atual corresponderem aos valores da solicitação original que gerou a resposta. A lista de cabeçalhos, em conjunto com o alvo e método, ajuda a determinar a variante aplicável. Se `Vary` contiver `*`, a resposta armazenada não corresponde automaticamente a uma solicitação posterior. O cabeçalho deve ser consistente também em respostas 304 relacionadas à mesma representação.

## Exemplo
Um servidor que comprime conforme `Accept-Encoding` pode responder com `Vary: Accept-Encoding`. A cache guarda ou seleciona variantes separadas para pedidos que aceitam gzip e pedidos que não o aceitam. Para idioma negociado, `Vary: Accept-Language` expressa que a escolha de idioma depende daquele cabeçalho.

## Limites e trade-offs
`Vary` só lista campos de cabeçalho da solicitação; não é autorização e não deve ser usado para tornar dados privados seguros em uma cache compartilhada. Variar por um cabeçalho de alta cardinalidade, como um identificador individual, pode fragmentar a reutilização. Se a aplicação também depende de fatores não representados na solicitação, é preciso rever a arquitetura da cache, não presumir que `Vary` os detectará.

## Como verificar
Faça solicitações para a mesma URL com valores distintos nos cabeçalhos relevantes e inspecione `Vary` nas respostas. Confirme que a cache não cruza variantes e que 304 mantém o mesmo conjunto de dimensões. Teste também a resposta padrão e o caso `Vary: *`, além de avaliar a cardinalidade e o risco de incluir dados pessoais na chave.

## Conexões
- [[cache-respostas-autenticadas-shared]] — segmentação de cache não substitui política segura para respostas autenticadas.
- [[revalidacao-cache-etag-if-none-match]] — respostas variantes também podem ser revalidadas com validadores.
- [[cache-control-diretivas-armazenamento-http]] — `private` e `no-store` tratam escopo de armazenamento, não variantes.

## Fontes
- [RFC 9111 — HTTP Caching, seção 4.1](https://www.rfc-editor.org/rfc/rfc9111.html#section-4.1) — correspondência de cache keys segundo `Vary`; acesso em 2026-10-01.
- [MDN — Vary header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary) — propósito e comportamento de variantes; acesso em 2026-10-01.
