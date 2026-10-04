---
id: software.testes.tranche10.000387
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
fontes: ["https://jestjs.io/docs/ecmascript-modules", "https://jestjs.io/docs/jest-object"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: escolher API de mock conforme ESM ou CommonJS

## Em uma frase
O fluxo de mock de módulo depende do sistema de módulos e da ordem em que imports estáticos são avaliados.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Um jest.mock tradicional pode não substituir um import ESM estático que já foi resolvido antes do código de configuração.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Para ESM use a API de mock indicada pela versão e carregue o módulo dinamicamente depois da configuração; mantenha jest.mock para casos CommonJS compatíveis.

## Exemplo
O teste registra unstable_mockModule com factory e então faz await import do módulo antes de chamar o SUT.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. A API ESM marcada unstable e a compatibilidade com top-level await dependem do Node e do grafo de módulos.

## Como verificar
Rode um teste mínimo na versão exata do Node/Jest e valide qual implementação foi importada, sem depender só de um log.

## Conexões
- [[jest-fake-timers-timers-pendentes-recursivos]] — Veja também: Jest: controlar timers falsos sem drenar loops recursivos.
- [[jest-snapshot-revisao-antes-de-atualizar]] — Veja também: Jest: revisar mudança de snapshot antes de atualizar.

## Fontes
- [Jest 30.5 — ECMAScript modules](https://jestjs.io/docs/ecmascript-modules) — restrições e APIs de mock para módulos ESM e CommonJS; consultado em 2026-10-02.
- [Jest 30.5 — The Jest object](https://jestjs.io/docs/jest-object) — limpeza, reset, restauração e isolamento de módulos; consultado em 2026-10-02.
