---
id: software.testes.tranche10.000383
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
fontes: ["https://jestjs.io/docs/setup-teardown", "https://jestjs.io/docs/jest-object"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: tratar beforeAll como escopo do arquivo de teste

## Em uma frase
beforeAll executa uma vez antes dos testes do escopo atual, não como banco de estado universal entre arquivos.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Assumir compartilhamento global entre workers pode causar duplicação de setup, colisões de porta ou fixtures ausentes.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Use setup global somente para recursos de ambiente apropriados e prefira lifecycle local para estado que cada arquivo controla.

## Exemplo
Dois arquivos criam contas de teste isoladas em beforeAll e limpam seus dados sem depender da ordem de execução.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Setup compartilhado por worker ou ambiente tem regras de configuração próprias e não deve ser inferido do hook local.

## Como verificar
Execute arquivos em paralelo e confirme que cada fixture tem dono, namespace e rotina de limpeza independentes.

## Conexões
- [[jest-hooks-escopo-e-ordem]] — Veja também: Jest: alinhar setup hooks ao escopo describe.
- [[jest-mock-function-calls-results-context]] — Veja também: Jest: inspecionar chamadas e resultados de jest.fn.

## Fontes
- [Jest 30.5 — Setup and teardown](https://jestjs.io/docs/setup-teardown) — escopo e ordenação de hooks de preparação e limpeza; consultado em 2026-10-02.
- [Jest 30.5 — The Jest object](https://jestjs.io/docs/jest-object) — limpeza, reset, restauração e isolamento de módulos; consultado em 2026-10-02.
