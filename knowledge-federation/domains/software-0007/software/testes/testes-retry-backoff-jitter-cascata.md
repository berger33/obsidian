---
id: software.testes.tranche07.000132
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md"
fontes: ["https://sre.google/sre-book/addressing-cascading-failures/", "https://www.rfc-editor.org/rfc/rfc9110.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de retries com backoff e jitter", "Teste: Teste de retries com backoff e jitter"]
lote: software-testes-2000-0001
---

# Teste de retries com backoff e jitter

## Em uma frase
Valide que novas tentativas são limitadas, espaçadas e seguras para a operação, evitando multiplicar a carga quando uma dependência falha.

## Por que importa
Retries sincronizados podem amplificar sobrecarga; repetir uma operação com efeito colateral sem idempotência pode duplicar cobranças ou gravações.

## Como funciona
Injete falhas transitórias e permanentes, registre contagem e intervalos de tentativas e confirme backoff exponencial com jitter quando apropriado. Verifique limite, deadline total, cancelamento e classificação de erros retryable; não repita indiscriminadamente respostas definitivas.

## Exemplo
Faça uma dependência falhar por alguns segundos e depois recuperar; confirme tentativas espaçadas, variação entre clientes e uma única reserva efetiva, com interrupção ao vencer deadline.

## Limites e trade-offs
A política depende de protocolo, operação e orçamento de latência. Jitter não substitui limite de tentativas, circuit breaker ou idempotency key, e timers podem tornar testes lentos ou flaky.

## Como verificar
Use relógio controlado ou tolerâncias de intervalo, valide distribuição sob muitos clientes sintéticos e compare carga de saída com carga de entrada durante a falha.

## Conexões
- [[timeouts-retries-backoff-jitter]] — aprofundamento relacionado.
- [[testes-consumer-idempotency-duplicates]] — aprofundamento relacionado.

## Fontes
- [Google SRE — Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga e falhas de dependência podem amplificar-se em cascata; consultado em 2026-10-01.
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
