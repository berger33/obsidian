---
id: software.testes.tranche07.000142
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9457.html", "https://www.rfc-editor.org/rfc/rfc9110.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de contrato Problem Details em APIs", "Teste: Teste de contrato Problem Details em APIs"]
lote: software-testes-2000-0001
---

# Teste de contrato Problem Details em APIs

## Em uma frase
Valide que erros publicados com Problem Details respeitam mídia, semântica HTTP e estrutura prevista no contrato, sem expor detalhes internos.

## Por que importa
Clientes precisam distinguir tipo e status de um problema por campos estáveis em vez de analisar texto livre ou receber stack traces.

## Como funciona
Provoque classes representativas de erro e confira application/problem+json, type, title, status e extensões documentadas. A propriedade status no corpo deve refletir o status HTTP quando presente; teste negociação e evite informação confidencial em detail.

## Exemplo
Para recurso ausente, confirme 404 e corpo problem+json com URI de tipo estável; para erro interno, confirme mensagem pública segura e correlation ID sem stack trace ou segredo.

## Limites e trade-offs
RFC 9457 define formato, não exige que toda API o use nem determina taxonomia de todos os problemas. Campos opcionais e extensões dependem do contrato; texto legível não deve ser o único identificador.

## Como verificar
Compare resposta a schema e exemplos, teste 4xx/5xx relevantes, status/cabeçalhos e campos sensíveis; inclua cliente que não entende extensões para validar interoperabilidade básica.

## Conexões
- [[problem-details-rfc9457]] — aprofundamento relacionado.
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.

## Fontes
- [IETF RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) — formato application/problem+json e campos de detalhe de erro; consultado em 2026-10-01.
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
