---
id: software.web.cache-autenticadas.000001
tipo: tecnica
dominio: software
subdominio: web
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [Caching authenticated HTTP responses, Shared cache authorization, Cache-Control private]
lote: software-cache-http-0006
---

# Respostas autenticadas em caches compartilhados

## Em uma frase
Uma resposta personalizada exige política de cache que impeça reutilização entre usuários, e autorização da aplicação continua necessária mesmo quando headers limitam o cache.

## Por que importa
Uma cache compartilhada pode servir a mesma representação a várias pessoas. Se um endpoint retorna dados ligados à identidade, armazenar uma resposta sem separar usuário e variante pode expor conteúdo de um cliente a outro. `Authorization`, cookies e headers de cache precisam ser avaliados junto à configuração real de proxy/CDN.

## Como funciona
A RFC 9111 estabelece que uma cache compartilhada não pode reutilizar uma resposta a uma solicitação com `Authorization` a menos que a resposta inclua uma diretiva que autorize o comportamento segundo a especificação, como `public`, `s-maxage` ou `must-revalidate`, observadas as demais regras. Uma resposta `private` não deve ser armazenada por uma cache compartilhada; uma cache privada do usuário pode armazená-la. `no-store` impede armazenamento conforme as regras do protocolo. Esses headers tratam do comportamento da cache, não verificam se o usuário pode acessar o recurso.

## Exemplo
Uma rota `/account` que retorna dados de cada usuário pode responder `Cache-Control: private, no-store` quando nenhuma cópia deve ser armazenada. Se uma resposta autenticada for deliberadamente compartilhável porque contém conteúdo idêntico para todos, isso exige revisão explícita de semântica, diretivas, chave de cache e configuração do intermediário; não basta remover o header `Authorization` do cache key.

## Limites e trade-offs
`private` não protege dados de um cliente que controla seu próprio browser/cache, e `no-store` não substitui autorização, controle de acesso ou proteção contra sistemas não conformes. `Vary: Authorization` pode particionar variantes, mas credenciais em chaves de cache trazem riscos e alta cardinalidade; não é solução automática para dados sensíveis. Caches gerenciadas podem ter regras específicas, que precisam ser testadas separadamente.

## Como verificar
Use duas identidades de teste com respostas distintas e percorra a mesma cache compartilhada. Confirme que Alice nunca recebe representação de Bob, inclusive após revalidação, expiração, erro e alteração de configuração. Inspecione `Cache-Control`, `Vary`, cache key real e política de autorização no origin; não valide apenas headers declarados.

## Conexões
- [[cache-control-diretivas-armazenamento-http]] — `private` e `no-store` têm semânticas diferentes.
- [[variantes-cache-vary-http]] — `Vary` define dimensões de seleção, mas não concede autorização.
- [[secrets-kubernetes-protecao-dados]] — proteção de credenciais também depende de escopo e controle de acesso.

## Fontes
- [RFC 9111 — HTTP Caching, seção 3.5](https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5) — regras para respostas associadas a `Authorization`; acesso em 2026-10-01.
- [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching) — diferenças entre cache privada e compartilhada e risco de personalização; acesso em 2026-10-01.
