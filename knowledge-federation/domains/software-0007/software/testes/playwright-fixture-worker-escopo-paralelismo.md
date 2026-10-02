---
id: software.testes.tranche08.000151
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/test-fixtures", "https://playwright.dev/docs/test-parallel"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: fixtures de worker e estado compartilhado

## Em uma frase
Use fixtures de worker apenas para dependências caras que possam ser compartilhadas sem contaminar dados de cada teste.

## Por que importa
Paralelizar com recursos compartilhados pode economizar tempo, mas um estado gravável comum cria interferência difícil de reproduzir.

## Como funciona
Separe o ciclo de vida do worker do ciclo de vida de teste. Gere namespaces por worker quando necessário e mantenha registros, carrinhos ou permissões particulares no escopo do teste.

## Exemplo
Um servidor local pode ser iniciado uma vez por worker, enquanto cada teste usa um prefixo próprio para filas ou objetos gravados nesse servidor.

## Limites e trade-offs
Uma fixture marcada como worker-scoped não garante concorrência segura; limites de conexão, quotas remotas e dados globais continuam sendo responsabilidades do sistema de teste.

## Como verificar
Aumente workers, repita a suíte e procure colisões. Compare logs de setup e teardown e confirme que workers diferentes não apagam recursos uns dos outros.

## Conexões
- [[playwright-paralelismo-dados-exclusivos]] — Veja também: Playwright: dados exclusivos para testes paralelos.
- [[playwright-fixture-ciclo-vida-isolamento]] — Veja também: Playwright: ciclo de vida de fixtures por teste.

## Fontes
- [Playwright — Fixtures](https://playwright.dev/docs/test-fixtures) — isolamento, ciclo de vida e composição de fixtures; consultado em 2026-10-02.
- [Playwright — Parallelism](https://playwright.dev/docs/test-parallel) — execução paralela, workers e dados independentes; consultado em 2026-10-02.
