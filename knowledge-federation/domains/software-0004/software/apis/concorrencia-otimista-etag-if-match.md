---
id: software.apis.concorrencia-otimista-etag.000001
tipo: tecnica
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests"]
tags: [dominio/software, subdominio/apis, qualidade/candidata]
aliases: [ETag, If-Match, Controle otimista de concorrência HTTP]
lote: software-dados-distribuidos-0004
---

# Concorrência otimista com ETag e If-Match

## Em uma frase
Um cliente pode enviar o `ETag` que leu em `If-Match` para que o servidor só aplique uma alteração se a representação ainda corresponder à versão observada.

## Por que importa
Duas pessoas podem ler a mesma versão de um recurso, editar cópias diferentes e enviar mudanças quase ao mesmo tempo. Sem uma precondição, a segunda gravação pode sobrescrever silenciosamente a primeira. A validação condicional transforma essa corrida em conflito explícito, permitindo que o cliente atualize, compare ou combine as alterações.

## Como funciona
O servidor retorna um `ETag` associado à representação. Antes de uma operação de alteração, o cliente envia `If-Match` com a entidade-tag conhecida. A RFC 9110 exige comparação forte para `If-Match` e determina que o servidor avalie a condição antes de executar o método. Se ela for falsa, o método não deve ser aplicado; o servidor pode responder `412 Precondition Failed`. `If-Match: *` significa que existe uma representação atual do recurso, não que qualquer tag arbitrária seja aceita. ETag é um validador opaco para o cliente, não uma autorização.

## Exemplo
Dois clientes leem uma conta com `ETag: "v7"`. O primeiro atualiza saldo e o servidor passa a expor `"v8"`. O segundo envia a mudança baseada em `"v7"`; o servidor detecta que a versão não corresponde e recusa a mutação, permitindo que o cliente releia e reconcilie o estado.

## Limites e trade-offs
O servidor precisa gerar validadores coerentes com a representação e aplicar a comparação de forma atômica com a gravação; uma checagem separada da atualização recria a corrida. O cliente precisa tratar `412` como conflito e não reenviar cegamente a mesma alteração com um ETag novo. Nem toda API exige precondições em todos os recursos, então esse requisito deve estar documentado no contrato.

## Como verificar
Teste dois clientes com a mesma versão inicial. Confirme que a primeira mutação bem-sucedida invalida o ETag antigo, que a segunda não altera o recurso e que a resposta permite uma recuperação segura. Teste tags fortes, tags obsoletas, ausência de precondição quando ela é obrigatória e operações concorrentes na camada de persistência.

## Conexões
- [[contrato-openapi-http]] — documente a precondição e a resposta de conflito na descrição da operação.
- [[problem-details-rfc9457]] — Problem Details pode fornecer contexto legível por máquina para uma falha 412.
- [[idempotencia-http-api]] — precondição de versão e idempotência tratam problemas distintos em retries e concorrência.

## Fontes
- [RFC 9110, seção 13.1.1 — If-Match](https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1) — comparação forte e avaliação antes da aplicação do método; acesso em 2026-10-01.
- [MDN — HTTP conditional requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Conditional_requests) — uso de validadores para evitar atualizações perdidas; acesso em 2026-10-01.
