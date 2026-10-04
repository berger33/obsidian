---
id: software.testes.tranche10.000439
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
fontes: ["https://schemathesis.readthedocs.io/en/stable/reference/configuration/", "https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Schemathesis: limitar geração sem confundir orçamento e total de requests

## Em uma frase
`generation.max-examples` limita casos da fase fuzzing por operação e sequências stateful; examples e coverage adicionam seus próprios casos.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Um limite baixo demais reduz exploração, enquanto um limite aplicado como se cobrisse todas as fases subestima o tráfego real.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Configure `max-time`, `max-examples`, fases e rate limit separadamente para o alvo e para o job.

## Exemplo
Pull request limita o tempo total e casos de fuzzing; execução noturna habilita fases mais amplas e mede também os exemplos e casos de coverage.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. `max-examples` não limita o total de requests de todas as fases, e shrinking pode acrescentar chamadas durante a reprodução de falhas.

## Como verificar
Registre duração, operações, requests por fase, rate limit e casos de shrinking para confirmar o orçamento efetivo.

## Conexões
- [[schemathesis-pytest-parametrize-call-and-validate]] — Veja também: Schemathesis: integrar operações à suíte pytest.

## Fontes
- [Schemathesis — Configuration](https://schemathesis.readthedocs.io/en/stable/reference/configuration/) — algoritmos padrão de inferência stateful, limites por fase, rede e precedência de autenticação; consultado em 2026-10-02.
- [Schemathesis — Data generation](https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/) — examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking; consultado em 2026-10-02.
