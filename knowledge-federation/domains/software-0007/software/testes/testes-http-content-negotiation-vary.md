---
id: software.testes.tranche07.000140
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
fontes: ["https://www.rfc-editor.org/rfc/rfc9110.html", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de negociação de conteúdo e Vary", "Teste: Teste de negociação de conteúdo e Vary"]
lote: software-testes-2000-0001
---

# Teste de negociação de conteúdo e Vary

## Em uma frase
Verifique se o servidor escolhe uma representação compatível com Accept e outras preferências documentadas e se caches distinguem variantes quando necessário.

## Por que importa
Clientes podem solicitar formatos ou idiomas diferentes; resposta incorreta ou cache sem chave de variação adequada pode entregar representação incompatível.

## Como funciona
Envie combinações de Accept, Accept-Language e codificação suportada, incluindo preferências ponderadas e valor não suportado. Confira Content-Type, representação e comportamento 406/documentado; quando a seleção varia por cabeçalho, avalie Vary e cache.

## Exemplo
Solicite JSON e depois formato alternativo do mesmo recurso por meio do cache compartilhado; confirme tipo correto em ambas as respostas e que uma representação não é reutilizada para a preferência incompatível.

## Limites e trade-offs
Política para cabeçalho não suportado depende do contrato, e nem todo endpoint negocia múltiplos formatos. Teste com proxy/cache real se essa camada participa do sistema.

## Como verificar
Automatize tabela de combinações aceitas, rejeitadas e padrão; compare corpo e cabeçalhos e invalide cache entre casos para detectar vazamento de variantes.

## Conexões
- [[variantes-cache-vary-http]] — aprofundamento relacionado.
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.

## Fontes
- [IETF RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica de métodos, representação, negociação e precondições HTTP; consultado em 2026-10-01.
- [MDN — Content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content_negotiation) — cabeçalhos Accept, seleção de representação e Vary; consultado em 2026-10-01.
