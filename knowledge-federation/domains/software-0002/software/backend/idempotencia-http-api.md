---
id: software.backend.idempotencia-api.000001
tipo: conceito
dominio: software
subdominio: backend
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: pendente
revisor: ""
fontes: ["https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2", "https://docs.stripe.com/api/idempotent_requests"]
tags: [dominio/software, subdominio/backend, qualidade/candidata]
aliases: [Idempotência em APIs]
---

# Idempotência em APIs HTTP

## Em uma frase
Uma operação é idempotente quando repetir a mesma intenção produz o mesmo efeito pretendido no recurso, mesmo que cada tentativa gere logs ou respostas diferentes.

## Por que importa
Uma conexão pode cair depois que o servidor aplicou uma alteração, mas antes de o cliente receber a resposta. O cliente não sabe se a operação aconteceu. Sem uma regra de repetição, uma segunda tentativa pode criar dois pedidos, duas cobranças ou duas tarefas. Idempotência torna esse tipo de recuperação previsível e é uma base para retries seguros.

## Como funciona
A RFC 9110 classifica métodos seguros e os métodos PUT e DELETE como idempotentes pela semântica pretendida. Isso não significa que todos os efeitos internos do servidor sejam idênticos: auditoria e contadores podem registrar cada chamada. POST não é idempotente por definição geral. Uma API pode, porém, oferecer uma chave de idempotência para uma operação POST. O comportamento depende da API: na Stripe, a documentação descreve armazenar o status e o corpo da primeira solicitação cuja execução começou, comparar os parâmetros em repetições e devolver o resultado armazenado para a mesma chave; erros de validação e conflitos anteriores ao início da execução não entram nesse registro. Escopo, retenção e tratamento de falhas não são regras universais.

## Exemplo
Ao criar um pagamento, o cliente gera uma chave aleatória para aquela intenção de compra e a reutiliza após timeout. Se o usuário alterar o carrinho e iniciar outra compra, a nova intenção recebe outra chave. O servidor também rejeita a reutilização da mesma chave com parâmetros incompatíveis.

## Limites e trade-offs
Idempotência não garante execução distribuída “exactly once”. A retenção da chave tem prazo, o registro precisa ser atômico com a operação local e efeitos em serviços externos exigem uma estratégia adicional, como outbox ou reconciliação. Não coloque dados pessoais na chave.

## Como verificar
Simule a perda da resposta após a gravação, repita a chamada com a mesma chave e confirme que existe um único efeito de negócio. Teste também chamadas concorrentes, parâmetros divergentes, expiração da chave e falhas antes do início da operação.

## Conexões
- [[timeouts-retries-backoff-jitter]] — limita quando repetir uma operação.
- [[contrato-openapi-http]] — descreve a superfície HTTP sem substituir a semântica do servidor.
- [[contract-testing-consumer-provider]] — verifica as interações que clientes realmente usam.

## Fontes
- [RFC 9110, seção 9.2.2 — Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.2) — semântica normativa de métodos HTTP; acesso em 2026-10-01.
- [Stripe API — Idempotent requests](https://docs.stripe.com/api/idempotent_requests) — exemplo de implementação específica de chaves, retenção e repetição; acesso em 2026-10-01.
