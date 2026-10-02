---
id: software.web.freshness-cache-http.000001
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9111.html#section-4.2", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching"]
tags: [dominio/software, subdominio/web, qualidade/candidata]
aliases: [HTTP freshness, Freshness lifetime, Age header, max-age, s-maxage]
lote: software-cache-http-0006
---

# Frescor e idade de respostas em cache HTTP

## Em uma frase
Uma resposta armazenada pode ser reutilizada sem validação enquanto sua vida de frescor exceder a idade calculada pelo cache.

## Por que importa
Frescor controla o equilíbrio entre reutilização eficiente e conteúdo atualizado. `max-age` não é necessariamente a idade real observada por cada cliente: uma resposta pode já ter passado por outra cache, e o campo `Age` comunica parte dessa história. A duração também pode variar entre caches privados e compartilhados.

## Como funciona
A RFC 9111 define resposta fresca quando `freshness_lifetime > current_age`. Para calcular a vida de frescor, um cache compartilhado usa `s-maxage` se presente; caso contrário, aplica `max-age`, depois `Expires` em relação a `Date`, e em certas situações pode usar frescor heurístico. O cálculo de idade considera a data da resposta, o `Age` recebido, o atraso da solicitação e o tempo que ela permaneceu armazenada. Quando a resposta deixa de ser fresca, ela não precisa ser apagada imediatamente: pode ser validada com o origin antes de reutilização ou, conforme diretivas aplicáveis, tratada de outra forma.

## Exemplo
Uma resposta com `Cache-Control: max-age=300` tem vida explícita de cinco minutos para uma cache privada. Se um cache compartilhado receber também `s-maxage=60`, ele usa a duração compartilhada de um minuto; o navegador e o CDN não precisam, portanto, tomar a mesma decisão de frescor.

## Limites e trade-offs
Frescor não significa que o conteúdo não mudou no origin; significa que o protocolo permite a reutilização segundo a política e idade calculada. Relógios desalinhados, idade herdada de outra cache e overrides específicos de CDN podem produzir resultados diferentes do que um cliente espera. Frescor heurístico é permitido em determinadas condições, então omitir headers não equivale universalmente a proibir cache.

## Como verificar
Capture `Date`, `Age`, `Cache-Control` e `Expires` em solicitações repetidas, tanto no origin quanto no intermediário. Compare o comportamento antes e depois do limiar de frescor e valide se `s-maxage` afeta apenas caches compartilhados. Não conclua que uma resposta veio do origin só porque recebeu status 200; consulte indicadores do cache e os headers observados.

## Conexões
- [[cache-control-diretivas-armazenamento-http]] — diretivas controlam armazenamento e reutilização.
- [[revalidacao-cache-etag-if-none-match]] — respostas stale podem ser revalidadas sem retransmitir o corpo.
- [[stale-while-revalidate-if-error]] — exceções explícitas permitem servir stale em janelas limitadas.

## Fontes
- [RFC 9111 — HTTP Caching, seção 4.2](https://www.rfc-editor.org/rfc/rfc9111.html#section-4.2) — vida de frescor, idade e resposta fresh/stale; acesso em 2026-10-01.
- [MDN — HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching) — explicação dos estados fresh/stale e tipos de cache; acesso em 2026-10-01.
