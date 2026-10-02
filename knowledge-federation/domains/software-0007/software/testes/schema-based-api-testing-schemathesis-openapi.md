---
id: software.testes.api-schema.000001
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://schemathesis.readthedocs.io/en/stable/quick-start/", "https://spec.openapis.org/oas/v3.1.1.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Schema-based API testing, OpenAPI-based testing, Teste de API baseado em schema]
lote: software-testes-2000-0001
---

# Teste de API baseado em schema com OpenAPI

## Em uma frase
Teste baseado em schema gera requisições a partir de uma descrição de API e verifica se respostas observadas respeitam os contratos e checks configurados.

## Por que importa
Escrever manualmente casos para todos os parâmetros e combinações de endpoints é trabalhoso e pode deixar fronteiras e entradas inválidas pouco exploradas. Uma descrição OpenAPI bem mantida pode apoiar documentação, clientes e geração de testes, ajudando a detectar respostas não documentadas, erros de servidor e divergências de schema.

## Como funciona
OpenAPI especifica uma interface descritiva, independente de linguagem, para HTTP APIs, permitindo que pessoas e ferramentas entendam operações e estruturas. Schemathesis lê descrições OpenAPI ou GraphQL, produz entradas de exemplo, valores de fronteira e dados gerados, executa requests e valida checks como status, erro de servidor e resposta contra o schema. A ferramenta também apresenta um comando reproduzível para falhas, útil para transformar descobertas em regressões.

## Exemplo
Para `POST /orders`, uma suíte gerada pode experimentar o objeto de pedido com valores válidos e próximos de limites declarados e conferir se status, headers e corpo correspondem à descrição. Se uma entrada viola restrições, teste também se o serviço a rejeita conforme o contrato. Uma resposta 500 gera um caso a investigar, mas não explica sozinha a causa.

## Limites e trade-offs
O gerador só conhece o que a descrição expressa e os checks ativados; schema incompleto, incorreto ou permissivo gera lacunas ou resultados enganosos. Propriedades de negócio, autorização contextual e sequências de estado podem não ser capturadas por uma chamada isolada. Testes gerados ainda precisam de ambiente, autenticação e dados controlados.

## Como verificar
Valide o schema e sua correspondência com o comportamento esperado antes de confiar nele como oráculo. Configure checks explicitamente, defina base URL, autenticação e limites de execução. Preserve IDs e comandos de reprodução; revise cada falha contra contrato e requisitos antes de alterar implementação ou schema.

## Conexões
- [[contrato-openapi-http]] — contrato descritivo serve também como fonte de casos gerados.
- [[property-based-testing-hypothesis]] — geração explora classes de entrada além de exemplos fixos.
- [[fuzzing-coverage-guided-libfuzzer]] — fuzzing e geração por schema exploram espaços diferentes de entradas.

## Fontes
- [Schemathesis — Quick Start](https://schemathesis.readthedocs.io/en/stable/quick-start/) — geração de dados e validação de respostas a partir de schemas; acesso em 2026-10-01.
- [OpenAPI Specification v3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — papel e estrutura da descrição de API; acesso em 2026-10-01.
