---
id: software.criacao_ia.tranche03.000278
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://playwright.dev/docs/test-timeouts", "https://playwright.dev/docs/test-configuration"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Playwright Test: diagnosticar timeouts por escopo

## Em uma frase
Timeout de teste, assertion, action, navigation, fixture e hooks são controles distintos, não uma única duração global.

## Por que importa
Aumentar timeout do teste não necessariamente permite que uma assertion aguarde mais; um actionTimeout sem limite também não protege a suíte contra um processo preso. Saber qual budget expirou direciona a correção ao lugar certo.

## Como funciona
O test timeout inclui corpo do teste, fixtures de setup e `beforeEach`; cleanup de fixtures e `afterEach` compartilha timeout separado do mesmo valor. `beforeAll` e `afterAll` têm orçamento próprio. Assertions retrying têm default de cinco segundos independente do teste; action e navigation timeouts podem ser configurados separadamente e globalTimeout limita toda a execução.

## Exemplo
Uma página carrega lentamente e a assertion expira em cinco segundos embora teste tenha 60 segundos. A equipe aumenta timeout da assertion específica ou corrige espera da aplicação, sem elevar todos os budgets nem ocultar um navigation timeout separado.

## Limites e trade-offs
Defaults e configurações podem mudar entre versões e config scopes. Elevar vários limites sem localizar a operação bloqueada tende a mascarar lentidão, fila de rede ou deadlock.

## Como verificar
Force timeout em corpo, assertion, fixture, `afterEach` e action separadamente. Confirme mensagem e budget consumido no call log e compare os valores da configuração com o cenário de CI.

## Conexões
- [[playwright-expect-poll-e-topass]] — Playwright assertions: escolher expect.poll ou expect.toPass.
- [[playwright-add-init-script-determinismo]] — Playwright addInitScript: preparar ambiente antes do código da página.

## Fontes
- [Playwright — Timeouts](https://playwright.dev/docs/test-timeouts) — lista timeouts e relações de compartilhamento entre testes, hooks e assertions Consulta: 2026-10-04.
- [Playwright — Test configuration](https://playwright.dev/docs/test-configuration) — documenta configuração central de timeouts da suíte Consulta: 2026-10-04.
