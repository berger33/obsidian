---
id: software.testes.tranche07.000141
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9110.html", "https://spec.openapis.org/oas/v3.1.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de semântica e idempotência de métodos HTTP", "Teste: Teste de semântica e idempotência de métodos HTTP"]
lote: software-testes-2000-0001
---

# Teste de semântica e idempotência de métodos HTTP

## Em uma frase
Verifique que métodos aceitos produzem os efeitos definidos pelo contrato HTTP, incluindo segurança, idempotência e resposta adequada a métodos não permitidos.

## Por que importa
Clientes, proxies e retries dependem da semântica do método; efeito colateral inesperado em GET ou repetição insegura pode causar perda ou duplicação de operações.

## Como funciona
Para cada recurso, registre métodos permitidos, estado inicial e efeito esperado. Repita PUT e DELETE conforme contrato para verificar idempotência de efeito, confira HEAD sem conteúdo de resposta e avalie 405/Allow quando método não é suportado.

## Exemplo
Crie recurso, envie duas atualizações PUT equivalentes e compare estado final; execute HEAD e verifique metadados sem corpo. Para ação financeira, não presuma que POST possa ser repetido sem chave idempotente.

## Limites e trade-offs
Idempotência refere-se ao efeito pretendido, não necessariamente a respostas byte a byte idênticas; logs e métricas podem mudar. A operação também pode ser parcialmente idempotente por regra de domínio.

## Como verificar
Compare estado de negócio antes/depois de chamadas repetidas e valide status, headers e corpo contra RFC 9110 e contrato publicado; inclua métodos inválidos sem causar alteração.

## Conexões
- [[idempotencia-http-api]] — aprofundamento relacionado.
- [[testes-consumer-idempotency-duplicates]] — aprofundamento relacionado.

## Fontes
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
- [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — descrição estruturada e validável do contrato HTTP; consultado em 2026-10-01.
