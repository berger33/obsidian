---
id: software.web.invalidacao-cache-http.000001
tipo: conceito
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-4.4", "https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.1"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [HTTP cache invalidation, Unsafe method cache invalidation, Cache purge]
lote: software-cache-http-0006
---

# Invalidação de cache após métodos HTTP não seguros

## Em uma frase
Caches HTTP que recebem uma resposta não errônea a um método não seguro devem invalidar a URI-alvo armazenada localmente para reduzir o risco de reutilizar uma representação antiga.

## Por que importa
Uma operação `PUT`, `POST` ou `DELETE` pode alterar o estado associado a uma URI que também tem respostas `GET` armazenadas. Se uma cache intermediária mantiver a representação antiga, clientes que passem por ela podem receber conteúdo desatualizado. A regra do protocolo é uma proteção local, não uma invalidação global de todas as caches.

## Como funciona
A RFC 9111 exige que uma cache invalide a URI-alvo quando recebe status não errôneo como resposta a um método não seguro, inclusive método cuja segurança não conhece. Resposta não errônea, nesse contexto, significa status 2xx ou 3xx. Invalidação pode significar remover as respostas armazenadas daquela URI ou marcá-las como inválidas para exigir validação antes de reutilizar. A cache pode invalidar outras URIs relacionadas sob regras da RFC, mas o requisito obrigatório é a URI-alvo. A mudança só alcança as caches pelas quais a solicitação e a resposta transitaram.

## Exemplo
Depois de um `PUT /items/42` bem-sucedido, uma cache intermediária que recebeu a solicitação invalida sua resposta armazenada para `/items/42`. Isso não garante que outras CDNs, regiões ou caches fora do caminho também descartem cópias; sistemas gerenciados podem exigir purge próprio ou uma estratégia com URLs versionadas.

## Limites e trade-offs
A RFC não garante purga mundial nem invalidar automaticamente todas as representações relacionadas. Respostas de erro não acionam a exigência descrita. A semântica de método seguro deve seguir HTTP Semantics, não uma lista improvisada de verbos na aplicação. Uma cache que não viu a solicitação mutável não consegue aplicar essa invalidação a partir dela.

## Como verificar
Armazene uma resposta GET numa cache controlada, execute um método não seguro que receba status 2xx ou 3xx pelo mesmo caminho e repita GET. Confirme que a resposta não é reutilizada sem validação. Repita com resposta de erro e com cache que não participou do caminho; documente que esta última pode continuar retendo a cópia conforme sua política.

## Conexões
- [[revalidacao-cache-etag-if-none-match]] — depois de invalidada, validação pode atualizar uma representação armazenada.
- [[cache-busting-assets-immutable]] — URLs versionadas ajudam quando purge global não é uma garantia disponível.
- [[cache-control-diretivas-armazenamento-http]] — invalidação não é o mesmo que proibir armazenamento com `no-store`.

## Fontes
- [RFC 9111 — HTTP Caching, seção 4.4](https://www.rfc-editor.org/rfc/rfc9111.html#section-4.4) — invalidação de URIs armazenadas após métodos não seguros; acesso em 2026-10-01.
- [RFC 9110 — HTTP Semantics, seção 9.2.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.1) — definição de métodos seguros e não seguros; acesso em 2026-10-01.
