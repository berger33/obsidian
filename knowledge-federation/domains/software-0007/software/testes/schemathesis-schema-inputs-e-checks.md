---
id: software.testes.tranche10.000430
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://schemathesis.readthedocs.io/en/stable/quick-start/", "https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Schemathesis: gerar chamadas a partir do contrato da API

## Em uma frase
Schemathesis lê schema OpenAPI ou GraphQL para construir entradas e exercitar operações documentadas.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Dados escritos manualmente tendem a cobrir menos combinações de parâmetros do que geração orientada pelo contrato.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Carregue o schema correto, execute operações dentro do alvo autorizado e avalie checks de status, resposta e erros.

## Exemplo
A suíte lê OpenAPI publicado no ambiente de teste e gera chamadas para cada operação incluída no schema.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Rotas não documentadas ou regras de negócio ausentes no schema não são cobertas automaticamente.

## Como verificar
Compare operações descobertas com o catálogo da API e investigue falhas reproduzíveis antes de alterar exemplos do contrato.

## Conexões
- [[schemathesis-fases-coverage-fuzzing-stateful]] — Veja também: Schemathesis: distinguir fases de coverage, fuzzing e stateful.

## Fontes
- [Schemathesis — Quick Start](https://schemathesis.readthedocs.io/en/stable/quick-start/) — inputs gerados de OpenAPI/GraphQL, checks e reprodução de falhas; consultado em 2026-10-02.
- [Schemathesis — Data generation](https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/) — examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking; consultado em 2026-10-02.
