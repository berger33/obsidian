---
id: software.testes.tranche10.000431
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
fontes: ["https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/", "https://schemathesis.readthedocs.io/en/stable/migration/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Schemathesis: distinguir fases de coverage, fuzzing e stateful

## Em uma frase
Data generation inclui estratégias e fases diferentes, como exemplos, coverage, fuzzing e execução stateful.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Uma execução curta pode não exercitar fronteiras ou sequências mesmo quando envia ao menos uma chamada por operação.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Revise fases habilitadas, ordem e orçamento e escolha combinações que respondam ao risco da API.

## Exemplo
Uma pipeline rápida roda exemplos e coverage; uma execução agendada amplia fuzzing e sequências stateful.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Defaults mudaram entre versões principais; a documentação v4 executa modos disponíveis por padrão, então não assuma o comportamento da v3.

## Como verificar
Registre versão e configuração efetiva e compare relatório por fase antes de atribuir diferença a uma mudança de aplicação.

## Conexões
- [[schemathesis-schema-inputs-e-checks]] — Veja também: Schemathesis: gerar chamadas a partir do contrato da API.
- [[schemathesis-valid-invalid-modes-contrato]] — Veja também: Schemathesis: usar modos válido e inválido com objetivo claro.

## Fontes
- [Schemathesis — Data generation](https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/) — examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking; consultado em 2026-10-02.
- [Schemathesis — Migration from v3](https://schemathesis.readthedocs.io/en/stable/migration/) — mudanças de comportamento entre versões principais; consultado em 2026-10-02.
