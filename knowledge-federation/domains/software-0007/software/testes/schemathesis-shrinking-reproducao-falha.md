---
id: software.testes.tranche10.000433
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

# Schemathesis: usar shrinking para reduzir caso que falha

## Em uma frase
Shrinking busca reduzir uma entrada que reproduz uma falha para um caso menor e mais diagnóstico.

## Por que importa
Contratos OpenAPI e GraphQL permitem gerar chamadas estruturadas, mas schema, dados de negócio e sequência de operações são dimensões distintas. Payloads gerados extensos podem ocultar o campo ou combinação mínima que aciona o defeito.

## Como funciona
Use checks nativos, ajuste fases e orçamento de geração e preserve autenticação e dados suficientes para reproduzir falhas. Preserve o caso e o comando de reprodução reportados, depois converta o resultado mínimo em teste de regressão quando apropriado.

## Exemplo
Uma falha de resposta reduz um objeto com muitos campos até permanecer somente a combinação necessária para reproduzir o status inesperado.

## Limites e trade-offs
Esta série segue a documentação stable consultada, incluindo mudanças da linha v4; compatibilidade e defaults devem ser conferidos por versão. Uma forma reduzida pode depender de estado ou sequência anterior; não remova contexto que seja necessário para reproduzir o bug.

## Como verificar
Execute a reprodução registrada contra ambiente controlado e compare o comportamento antes e depois da correção.

## Conexões
- [[schemathesis-valid-invalid-modes-contrato]] — Veja também: Schemathesis: usar modos válido e inválido com objetivo claro.
- [[schemathesis-stateful-links-sequencia-api]] — Veja também: Schemathesis: declarar OpenAPI Links para fluxos stateful específicos.

## Fontes
- [Schemathesis — Data generation](https://schemathesis.readthedocs.io/en/stable/explanations/data-generation/) — examples, coverage, fuzzing, modos válido/inválido, stateful e shrinking; consultado em 2026-10-02.
- [Schemathesis — Quick Start](https://schemathesis.readthedocs.io/en/stable/quick-start/) — inputs gerados de OpenAPI/GraphQL, checks e reprodução de falhas; consultado em 2026-10-02.
