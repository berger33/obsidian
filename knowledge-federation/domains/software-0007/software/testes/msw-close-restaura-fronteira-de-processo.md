---
id: software.testes.tranche15.000925
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/guides/integrations/node", "https://mswjs.io/api/setup-server/listen"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: fechar a interceptação depois da suite

## Em uma frase
`server.close()` desabilita a camada de interceptação instalada para testes, por isso integrações Node costumam iniciar uma vez, resetar entre testes e fechar no teardown final.

## Por que importa
O lifecycle previne que mocks continuem afetando ferramentas ou código executado depois da suíte.

## Como funciona
A chamada é sincronizada na API do Node porque não há worker browser nem socket real para aguardar registro.

## Exemplo
Use `beforeAll(() => server.listen())`, `afterEach(() => server.resetHandlers())` e `afterAll(() => server.close())`, adaptando os hooks aos nomes do runner escolhido.

## Limites e trade-offs
Se vários módulos criam setupServer independentes, interceptadores duplicados podem competir e mascarar requests; mantenha uma instância comum no escopo do processo de teste.

## Como verificar
Adicione um teste que valida interceptação e um teardown que faz request controlada depois do fechamento, confirmando que o mock não continua ativo.

## Conexões
- [[msw-restore-handlers-nao-e-reset-handlers]] — Veja também: MSW: usar restoreHandlers para rearmar handlers de uso único.
- [[msw-boundary-isolar-state-por-contexto-async]] — Veja também: MSW: criar boundary quando handlers de runtime precisam de escopo assíncrono.

## Fontes
- [MSW — Node.js integration](https://mswjs.io/guides/integrations/node) — setupServer e ciclo listen/reset/close em testes; consultado em 2026-10-02.
- [MSW — listen()](https://mswjs.io/api/setup-server/listen) — início da interceptação e estratégias para frames sem handler; consultado em 2026-10-02.
