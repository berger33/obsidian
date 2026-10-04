---
id: software.testes.tranche07.000144
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
fontes: ["https://opensource.zalando.com/restful-api-guidelines/#pagination", "https://spec.openapis.org/oas/v3.1.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Teste de paginação por cursor e invariantes", "Teste: Teste de paginação por cursor e invariantes"]
lote: software-testes-2000-0001
---

# Teste de paginação por cursor e invariantes

## Em uma frase
Verifique que a navegação por cursor mantém ordem e cobertura previstas no contrato diante de limites, filtros e alterações concorrentes controladas.

## Por que importa
Páginas duplicadas ou com lacunas podem gerar resultados incompletos sem erro explícito, especialmente quando a coleção muda entre consultas.

## Como funciona
Use fixture com ordenação estável e valores empatados; percorra todas as páginas, teste limites zero/máximo, cursor inválido e filtros. Defina a semântica quando registros entram ou saem durante a paginação e valide tokens sem revelar estado sensível.

## Exemplo
Com 23 registros e tamanho de página 10, percorra os cursores e compare IDs ao conjunto esperado; insira novo registro entre páginas e confirme a regra de snapshot ou ordenação documentada.

## Limites e trade-offs
Cursor costuma ser opaco e específico da API; não presuma que permita salto aleatório ou que preserve snapshot sem contrato. Dataset mutável exige regra explícita.

## Como verificar
Confronte concatenação das páginas com conjunto e ordem esperados, verifique ausência de ciclos, duplicatas e lacunas e teste cursor expirado/adulterado conforme comportamento documentado.

## Conexões
- [[paginacao-por-cursor-api]] — aprofundamento relacionado.
- [[schema-based-api-testing-schemathesis-openapi]] — aprofundamento relacionado.

## Fontes
- [Zalando RESTful API Guidelines — Pagination](https://opensource.zalando.com/restful-api-guidelines/#pagination) — contrato de paginação, links e navegação entre páginas; consultado em 2026-10-01.
- [OpenAPI Specification 3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — descrição estruturada e validável do contrato HTTP; consultado em 2026-10-01.
