---
id: software.testes.tranche13.000673
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://webdriver.io/docs/api/expect-webdriverio/", "https://webdriver.io/docs/configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: acumular falhas independentes com soft assertions

## Em uma frase
`expect.soft()` coleta falhas sem interromper imediatamente o teste e as reporta juntas ao final quando o serviço correspondente está ativo.

## Por que importa
Uma tela com vários campos independentes pode produzir diagnóstico completo em uma execução, sem parar na primeira diferença de texto.

## Como funciona
Use soft assertion apenas para verificações que continuam seguras após falha, instale `SoftAssertionService` e mantenha o auto-assert no fim habilitado ou chame `expect.assertSoftFailures()` manualmente.

## Exemplo
Um smoke test pode checar título, preço e disponibilidade da página e mostrar os três problemas de conteúdo no mesmo relatório.

## Limites e trade-offs
Falha de pré-condição que invalida leituras seguintes ainda deve interromper o teste; o serviço não é suportado com Jasmine usando a importação global e configuração importa.

## Como verificar
Force duas expectativas a falhar e confirme que ambas aparecem no final; remova uma para provar que o status do teste continua refletindo a outra.

## Conexões
- [[webdriverio-wait-displayed-state]] — Veja também: WebdriverIO: esperar visibilidade sem presumir presença.
- [[webdriverio-local-worker-isolation]] — Veja também: WebdriverIO: entender isolamento do Local Runner.

## Fontes
- [WebdriverIO — expect-webdriverio](https://webdriver.io/docs/api/expect-webdriverio/) — browser-aware matcher API; consultado em 2026-10-02.
- [WebdriverIO — Configuration](https://webdriver.io/docs/configuration) — specs, capabilities, hooks and runner options; consultado em 2026-10-02.
