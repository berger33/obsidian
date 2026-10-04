---
id: software.testes.tranche10.000435
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

# Schemathesis: links explícitos não são pré-requisito universal para stateful

## Em uma frase
Schemathesis pode inferir conexões stateful por análise do schema OpenAPI, aprender relações de cabeçalhos Location no CLI e usar Links explícitos quando necessário.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Exigir Links em todo contrato omite sequências inferíveis; por outro lado, assumir que toda regra de negócio será descoberta pode deixar fluxos sem cobertura.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Revise as conexões detectadas e as opções stateful.inference.algorithms; acrescente OpenAPI Links para dependências não inferidas ou para controle explícito.

## Exemplo
Sem Link manual, a análise pode relacionar o id retornado por POST /users ao userId de GET /users/{userId}; no CLI, um Location observado nas fases anteriores também pode ensinar uma conexão.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Inferência depende da forma e qualidade do schema; aprendizado por Location depende das fases CLI que observam respostas e não deve ser presumido em execução isolada por pytest.

## Como verificar
Confira versão e algoritmos ativos, inspecione operações conectadas e sequências stateful e acrescente Link explícito quando a relação real não aparecer.

## Conexões
- [[schemathesis-stateful-links-sequencia-api]] — Veja também: Schemathesis: declarar OpenAPI Links para fluxos stateful específicos.
- [[schemathesis-checks-server-error-schema-status]] — Veja também: Schemathesis: classificar server errors e respostas fora do schema.

## Fontes
- [Schemathesis — Understanding Stateful Testing](https://schemathesis.readthedocs.io/en/stable/explanations/stateful/) — inferência por schema, aprendizado de Location no CLI, OpenAPI Links explícitos e sequências stateful; consultado em 2026-10-02.
- [Schemathesis — Configuration](https://schemathesis.readthedocs.io/en/stable/reference/configuration/) — algoritmos padrão de inferência stateful, limites por fase, rede e precedência de autenticação; consultado em 2026-10-02.
