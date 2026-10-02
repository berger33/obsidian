# MOC — Cache HTTP

Notas autorais do lote `software-cache-http-0006`. O mapa é uma trilha de navegação, não validação factual.

## Política e duração
- [[cache-control-diretivas-armazenamento-http]] — armazenamento, reutilização e escopo privado/compartilhado.
- [[freshness-age-cache-http]] — frescor, idade, `max-age` e `s-maxage`.
- [[stale-while-revalidate-if-error]] — janelas explícitas para resposta stale.

## Identidade e validação
- [[revalidacao-cache-etag-if-none-match]] — revalidação condicional e resposta 304.
- [[variantes-cache-vary-http]] — seleção de representações com `Vary`.
- [[cache-respostas-autenticadas-shared]] — dados de identidade em caches compartilhados.

## Publicação e mutações
- [[cache-busting-assets-immutable]] — URLs versionadas e assets imutáveis.
- [[invalidacao-cache-metodos-unsafe]] — invalidação da URI-alvo em caches no caminho de métodos não seguros.

## Revisão
As 8 notas do lote 0006 tiveram revisão factual humana confirmada pelo usuário em 2026-10-02 e contam como válidas; o passe automático, isoladamente, não substitui essa revisão.
