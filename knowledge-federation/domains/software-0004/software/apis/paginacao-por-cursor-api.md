---
id: software.apis.paginacao-cursor.000001
tipo: tecnica
dominio: software
subdominio: apis
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://google.aip.dev/158", "https://docs.stripe.com/api/pagination"]
tags: [dominio/software, subdominio/apis, qualidade/candidata]
aliases: [Cursor pagination, Paginação por cursor, Paginação de API]
lote: software-dados-distribuidos-0004
---

# Paginação por cursor em APIs

## Em uma frase
Paginação por cursor devolve uma porção ordenada de uma coleção e um marcador que permite continuar a partir de uma posição, sem exigir que o cliente calcule um número de página.

## Por que importa
Coleções crescem e uma resposta sem limite pode consumir memória, tempo e banda. Cursors podem evitar o custo e a instabilidade que deslocamentos grandes causam em algumas consultas, mas sua eficácia depende de ordenação e implementação. A paginação também faz parte do contrato: clientes precisam saber como avançar, quando a coleção terminou e quais filtros manter.

## Como funciona
O servidor escolhe uma ordem determinística e retorna resultados junto a um token de continuação. O cliente envia esse token na solicitação seguinte, preservando os demais parâmetros de busca. Google AIP-158 recomenda tokens opacos, URL-safe e que não sejam interpretáveis pelo cliente; o token indica onde continuar, não concede autorização. A implementação deve revalidar autenticação e autorização em cada página. Stripe apresenta um exemplo específico em que `starting_after` e `ending_before` recebem IDs de objetos já listados; essa forma não é uma exigência universal para APIs.

## Exemplo
Uma listagem ordenada por `(created_at, id)` retorna 50 itens e um cursor derivado da última posição. A próxima solicitação carrega esse token com os mesmos filtros. O identificador secundário torna a ordem total quando vários registros têm o mesmo timestamp. Se o serviço retornar menos itens que o limite solicitado, o cliente deve seguir o indicador de continuação, não presumir que a coleção acabou apenas pelo tamanho da página.

## Limites e trade-offs
Um cursor não garante por si só um snapshot imutável enquanto a coleção muda; registros inseridos ou removidos podem influenciar páginas conforme a política do serviço. Tokens transparentes acoplam o contrato aos detalhes internos e podem expor dados; Base64 simples não é criptografia. Tokens não devem substituir autorização. Paginação por offset pode continuar adequada para coleções pequenas ou navegação direta a páginas numeradas.

## Como verificar
Teste coleção vazia, página parcial, última página, filtros alterados, limites máximos, cursores inválidos e registros com valores de ordenação repetidos. Verifique ausência de lacunas ou duplicatas no cenário que a API promete suportar, autorização em todas as páginas e expiração documentada se os tokens tiverem validade.

## Conexões
- [[indice-btree-multicolunas-postgresql]] — a ordem e os predicados do cursor podem orientar um índice composto.
- [[contrato-openapi-http]] — documente parâmetros, token de continuação e sinal de fim da coleção.
- [[rate-limit-http-429]] — clientes que percorrem muitas páginas precisam respeitar limites de taxa.

## Fontes
- [Google AIP-158 — Pagination](https://google.aip.dev/158) — tokens, parâmetros e autorização na paginação de APIs; acesso em 2026-10-01.
- [Stripe API — Pagination](https://docs.stripe.com/api/pagination) — exemplo concreto de cursores baseados em IDs de objetos; acesso em 2026-10-01.
