---
id: software.testes.tranche10.000434
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
fontes: ["https://schemathesis.readthedocs.io/en/stable/explanations/stateful/", "https://schemathesis.readthedocs.io/en/stable/reference/configuration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Schemathesis: declarar OpenAPI Links para fluxos stateful específicos

## Em uma frase
OpenAPI Links permite mapear explicitamente dados de uma resposta para parâmetros de outra operação e modelar relações stateful específicas.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Uma relação explícita ajuda quando a dependência de negócio não é inferida pela forma do schema ou precisa de controle preciso.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Declare operationId e o mapeamento do parâmetro, por exemplo com $response.body#/id; use Links para relações necessárias que a análise automática não represente.

## Exemplo
A resposta 201 de POST /users fornece body.id a userId de GET /users/{userId}; o fluxo pode então consultar e remover o mesmo recurso.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Links descrevem somente as relações modeladas e precisam acompanhar o contrato; relações inferidas continuam possíveis e não são desativadas por um Link explícito.

## Como verificar
Inspecione a sequência stateful gerada e confirme que o valor do próximo parâmetro veio da resposta anterior e corresponde à relação de negócio pretendida.

## Conexões
- [[schemathesis-shrinking-reproducao-falha]] — Veja também: Schemathesis: usar shrinking para reduzir caso que falha.
- [[schemathesis-stateful-sem-link-nao-presumir]] — Veja também: Schemathesis: links explícitos não são pré-requisito universal para stateful.

## Fontes
- [Schemathesis — Understanding Stateful Testing](https://schemathesis.readthedocs.io/en/stable/explanations/stateful/) — inferência por schema, aprendizado de Location no CLI, OpenAPI Links explícitos e sequências stateful; consultado em 2026-10-02.
- [Schemathesis — Configuration](https://schemathesis.readthedocs.io/en/stable/reference/configuration/) — algoritmos padrão de inferência stateful, limites por fase, rede e precedência de autenticação; consultado em 2026-10-02.
