---
id: software.testes.tranche10.000386
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
fontes: ["https://jestjs.io/docs/timer-mocks", "https://jestjs.io/docs/setup-teardown"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: controlar timers falsos sem drenar loops recursivos

## Em uma frase
Fake timers permitem avançar relógio JavaScript sem esperar o tempo real passar.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Debounce e backoff são lentos com espera real, mas drenar todos os timers pode entrar em recursão infinita.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Instale fake timers antes de agendar callbacks, avance somente o intervalo necessário e restaure o relógio real no cleanup.

## Exemplo
Um teste avança 300 milissegundos para disparar debounce e usa runOnlyPendingTimers quando callbacks agendam a próxima rodada.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Fake timers não avançam automaticamente relógio, rede ou timers executados fora do ambiente controlado.

## Como verificar
Valide quantas vezes o callback executa e rode cleanup mesmo quando uma assertion falha.

## Conexões
- [[jest-clear-reset-restore-mocks-diferencas]] — Veja também: Jest: distinguir limpar, resetar e restaurar mocks.
- [[jest-mock-modulos-esm-commonjs]] — Veja também: Jest: escolher API de mock conforme ESM ou CommonJS.

## Fontes
- [Jest 30.5 — Timer mocks](https://jestjs.io/docs/timer-mocks) — relógio falso, avanço de timers e timers encadeados; consultado em 2026-10-02.
- [Jest 30.5 — Setup and teardown](https://jestjs.io/docs/setup-teardown) — escopo e ordenação de hooks de preparação e limpeza; consultado em 2026-10-02.
