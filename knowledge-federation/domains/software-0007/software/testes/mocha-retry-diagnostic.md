---
id: software.testes.tranche13.000655
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
fontes: ["https://mochajs.org/running/cli/", "https://mochajs.org/features/parallel-mode/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mocha: usar retries como evidência de instabilidade

## Em uma frase
A opção `--retries` repete testes que falham até o limite configurado; por padrão, falhas não são repetidas.

## Por que importa
Uma repetição pode manter uma pipeline útil enquanto coleta evidência, mas um passe posterior não apaga a primeira falha nem identifica a causa da instabilidade.

## Como funciona
Configure retries de maneira explícita, preserve resultados e examine se o caso depende de tempo, ordem, rede ou limpeza incompleta. Evite elevar o limite para transformar comportamento não determinístico em sucesso silencioso.

## Exemplo
Um teste de integração pode ter uma repetição temporária durante investigação, com registro da tentativa original e alerta quando só uma tentativa posterior passa.

## Limites e trade-offs
Repetir pode esconder defeito real e aumentar carga sobre um serviço já degradado. A política de retries também precisa ser compatível com reporter e modo paralelo usados.

## Como verificar
Provoque uma falha determinística e confira quantas tentativas aparecem; depois remova a causa e confirme que a configuração não mascara outros testes.

## Conexões
- [[mocha-parallel-order-isolation]] — Veja também: Mocha: não depender de ordem global em modo paralelo.
- [[mocha-timeout-test-and-hook]] — Veja também: Mocha: dimensionar timeout de teste e hook.

## Fontes
- [Mocha — Command-Line Usage](https://mochajs.org/running/cli/) — grep, retries, timeouts, parallel flags and reporter options; consultado em 2026-10-02.
- [Mocha — Parallel Mode](https://mochajs.org/features/parallel-mode/) — workers, nondeterministic file order and parallel-mode limitations; consultado em 2026-10-02.
