---
id: software.testes.tranche07.000145
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
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
fontes: ["https://www.rfc-editor.org/rfc/rfc6585.html", "https://www.rfc-editor.org/rfc/rfc9110.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de API para 429 e Retry-After", "Teste: Teste de API para 429 e Retry-After"]
lote: software-testes-2000-0001
---

# Teste de API para 429 e Retry-After

## Em uma frase
Valide a resposta à quota excedida e se clientes e caches respeitam o contrato de limitação de taxa sem retentar de forma agressiva.

## Por que importa
Uma API precisa comunicar limitação de tráfego e orientar espera; comportamento errado pode amplificar a carga ou esconder que requisições foram recusadas.

## Como funciona
Em ambiente de teste, exceda quota baixa e conhecida, confira 429, mensagem e Retry-After quando implementado. Verifique janela de reset, escopo de identidade/recurso, comportamento de cache e que cliente espera antes de uma tentativa subsequente.

## Exemplo
Após a quota sintética ser consumida, confirme que o pedido seguinte recebe 429 e que o cliente aguarda o intervalo indicado; depois da janela, uma nova chamada permitida volta a funcionar.

## Limites e trade-offs
RFC 6585 deixa ao servidor a política de identificação e contagem, e Retry-After é opcional em 429. Testes de alta frequência em produção podem consumir capacidade ou afetar usuários.

## Como verificar
Registre instante, quota, cabeçalho e resultado; prove que resposta 429 não é armazenada por cache e que outras identidades não são limitadas acidentalmente, se a política as separa.

## Conexões
- [[rate-limit-http-429]] — aprofundamento relacionado.
- [[testes-load-shedding-limites-sobrecarga]] — aprofundamento relacionado.

## Fontes
- [IETF RFC 6585 — Additional HTTP Status Codes](https://www.rfc-editor.org/rfc/rfc6585.html) — 429 Too Many Requests e 428 Precondition Required; consultado em 2026-10-01.
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
