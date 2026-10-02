---
id: software.testes.tranche10.000432
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
fontes: ["https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/", "https://schemathesis.readthedocs.io/en/stable/quick-start/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Schemathesis: usar modos válido e inválido com objetivo claro

## Em uma frase
Modos de geração podem focar entradas conformes ou violadoras do schema para testar aceitação e rejeição.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Testar apenas valores válidos deixa sem evidência o comportamento de validação da API perante dados malformados.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Escolha a estratégia conforme o contrato e afirme rejeição com status e formato de erro documentados.

## Exemplo
O teste envia payload válido para criação e usa modo inválido em etapa separada para verificar resposta de validação.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Schema pode descrever apenas parte das regras; rejeição de entrada inválida precisa de especificação consistente e permissiva o bastante para expressar o caso.

## Como verificar
Compare cada falha com o contrato e confirme que o erro observado é violação real, não fixture inválida do teste.

## Conexões
- [[schemathesis-fases-coverage-fuzzing-stateful]] — Veja também: Schemathesis: distinguir fases de coverage, fuzzing e stateful.
- [[schemathesis-shrinking-reproducao-falha]] — Veja também: Schemathesis: usar shrinking para reduzir caso que falha.

## Fontes
- [Schemathesis — Data generation](https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/) — examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking; consultado em 2026-10-02.
- [Schemathesis — Quick Start](https://schemathesis.readthedocs.io/en/stable/quick-start/) — inputs gerados de OpenAPI/GraphQL, checks e reprodução de falhas; consultado em 2026-10-02.
