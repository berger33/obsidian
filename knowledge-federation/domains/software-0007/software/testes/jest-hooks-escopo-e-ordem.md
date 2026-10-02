---
id: software.testes.tranche10.000382
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
fontes: ["https://jestjs.io/docs/setup-teardown", "https://jestjs.io/docs/asynchronous"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: alinhar setup hooks ao escopo describe

## Em uma frase
beforeAll, beforeEach, afterEach e afterAll organizam setup e cleanup no escopo em que são declarados.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Um hook no nível do arquivo afeta testes além de um bloco aninhado e pode criar estado compartilhado inesperado.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Coloque fixtures locais dentro do describe correspondente e mantenha a limpeza no hook complementar com ordem fácil de inspecionar.

## Exemplo
Um bloco de testes de armazenamento cria banco em beforeAll e apaga seus registros em afterEach antes de cada exemplo.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Hooks de arquivo não são serviços globais compartilhados entre todos os arquivos e workers de Jest.

## Como verificar
Registre chamadas dos hooks em um teste pequeno e confirme a ordem para blocos aninhados na configuração da suíte.

## Conexões
- [[jest-rejeicoes-async-com-rejects]] — Veja também: Jest: testar rejeições com .rejects aguardado.
- [[jest-beforeall-nao-compartilha-estado-entre-arquivos]] — Veja também: Jest: tratar beforeAll como escopo do arquivo de teste.

## Fontes
- [Jest 30.5 — Setup and teardown](https://jestjs.io/docs/setup-teardown) — escopo e ordenação de hooks de preparação e limpeza; consultado em 2026-10-02.
- [Jest 30.5 — Testing asynchronous code](https://jestjs.io/docs/asynchronous) — promises, async/await, rejeições e garantia de que a asserção seja aguardada; consultado em 2026-10-02.
