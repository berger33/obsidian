---
id: software.testes.tranche13.000678
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
fontes: ["https://webdriver.io/docs/retry", "https://webdriver.io/docs/configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: diagnosticar antes de ativar retry de spec

## Em uma frase
Configuração pode repetir um arquivo de spec que falhou até o limite `specFileRetries`.

## Por que importa
Retry temporário coleta sinal sobre flakiness, mas uma execução posterior não prova que o primeiro resultado foi falso nem que a causa foi corrigida.

## Como funciona
Ative retry com limite pequeno durante diagnóstico, registre a tentativa original e trate dados externos idempotentemente para não repetir uma operação irreversível.

## Exemplo
Um arquivo de leitura pode ser reexecutado depois de timeout e gerar relatório de ambas as tentativas, enquanto uma criação de cobrança exige idempotency key antes de qualquer retry.

## Limites e trade-offs
Retry de arquivo não equivale a nova assertion nem garante repetir apenas um teste; o escopo escolhido pode tornar o custo maior do que parece.

## Como verificar
Faça um teste controlado falhar uma vez, confira número de reexecuções e resultado reportado e depois remova o retry quando investigação terminar.

## Conexões
- [[webdriverio-capability-concurrency]] — Veja também: WebdriverIO: limitar workers pela capacidade disponível.
- [[webdriverio-group-spec-execution]] — Veja também: WebdriverIO: agrupar arquivos para controlar ordem necessária.

## Fontes
- [WebdriverIO — Retry Flaky Tests](https://webdriver.io/docs/retry) — spec-file retry configuration; consultado em 2026-10-02.
- [WebdriverIO — Configuration](https://webdriver.io/docs/configuration) — specs, capabilities, hooks and runner options; consultado em 2026-10-02.
