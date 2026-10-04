---
id: software.testes.tranche11.000457
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://github.com/rest-assured/rest-assured/wiki/Usage#filters", "https://github.com/rest-assured/rest-assured/wiki/Usage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: não confundir logging de filtro com captura exata no wire

## Em uma frase
Filters podem observar ou alterar request antes do envio e response antes das expectations; filtros também podem implementar logging ou autenticação.

## Por que importa
O log de uma especificação não é necessariamente a requisição final: cliente HTTP pode adicionar headers e filtros posteriores ainda podem modificá-la.

## Como funciona
Use filtros para comportamento transversal e diagnóstico; para prova do que chegou, observe o request em servidor controlado ou proxy de teste.

## Exemplo
Um teste confirma no servidor um header inserido por filtro posterior, em vez de inferir sua presença apenas pelo log pré-envio.

## Limites e trade-offs
Logs podem conter tokens, cookies e corpos pessoais; redija segredos e não os publique como artefato irrestrito.

## Como verificar
Compare log, ordem de filtros e request observado no stub e confira política de redaction antes de habilitar logging em CI.

## Conexões
- [[restassured-json-schema-validacao-opcional]] — Veja também: REST Assured: tratar JSON Schema como validação configurada.
- [[restassured-auth-por-caso-sem-credencial-em-log]] — Veja também: REST Assured: configurar autenticação por teste e proteger credenciais.

## Fontes
- [REST Assured — Filters](https://github.com/rest-assured/rest-assured/wiki/Usage#filters) — interceptação e alteração de request/response, logging e composição de filtros; consultado em 2026-10-02.
- [REST Assured — Usage (documentação do projeto)](https://github.com/rest-assured/rest-assured/wiki/Usage) — DSL given/when/then, parâmetros HTTP, validação de resposta, autenticação, filtros e exemplos do projeto; consultado em 2026-10-02.
