---
id: software.testes.tranche15.000861
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/docs/api/setup-server/", "https://mswjs.io/docs/defaults/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: cumprir o ciclo listen, reset e close

## Em uma frase
O ciclo recomendado inicia a interceptação antes de todos os testes, remove handlers adicionados por cada caso e encerra o servidor ao final da suíte.

## Por que importa
Sem a etapa de reset, um handler criado em um teste vaza para os seguintes e produz resultados que dependem da ordem de execução.

## Como funciona
Registre `server.listen()` em `beforeAll`, `server.resetHandlers()` em `afterEach` e `server.close()` em `afterAll`, mantendo o mesmo arquivo de configuração para toda a suíte.

## Exemplo
Em Jest ou Vitest, o arquivo de setup chama `beforeAll(() => server.listen())` e o restante do ciclo, enquanto os testes apenas importam o servidor compartilhado.

## Limites e trade-offs
Encerrar o servidor é obrigatório para não deixar a interceptação ativa em processos que reutilizam ambiente, mas `close()` não é o mesmo que limpar handlers de um teste específico.

## Como verificar
Adicione um handler temporário em um caso, confirme que o caso seguinte não enxerga esse handler e que a última execução termina sem pendências.

## Conexões
- [[msw-setupserver-node-interception]] — Veja também: MSW: interceptar requisições em Node com setupServer.
- [[msw-onunhandledrequest-fail]] — Veja também: MSW: tratar requisição sem handler como falha.

## Fontes
- [MSW — setupServer](https://mswjs.io/docs/api/setup-server/) — interceptação em Node.js e ciclo de vida de listen, resetHandlers e close; consultado em 2026-10-02.
- [MSW — Default behaviors](https://mswjs.io/docs/defaults/) — fallthrough entre handlers, ordem de avaliação e sensibilidade à ordem; consultado em 2026-10-02.
