---
id: software.testes.tranche15.000904
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
fontes: ["https://kotest.io/docs/framework/sharedtestconfig.html", "https://kotest.io/docs/framework/testcaseconfig.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: configurar retries sem apagar o sinal de falha intermitente

## Em uma frase
A configuração compartilhada pode definir quantidade de retries e intervalo para testes de uma Spec, com possibilidade de sobrescrever a configuração em casos individuais.

## Por que importa
Repetir um caso instável pode reduzir ruído enquanto a equipe investiga, mas muda a política de resultado e aumenta duração.

## Como funciona
Registrar número de tentativas e manter visível a falha inicial é mais útil do que tratar qualquer sucesso tardio como evidência de determinismo.

## Exemplo
Defina `DefaultTestConfig(retries = 2, retryDelay = 20.milliseconds)` apenas no escopo que precisa da política e sobrescreva casos críticos com comportamento que falhe na primeira tentativa.

## Limites e trade-offs
Retry pode repetir escrita, e-mail ou chamada externa; limites de tentativas não limpam estado entre execuções nem substituem idempotência.

## Como verificar
Use um teste artificial que falha na primeira invocação e passa na seguinte; confirme número de tentativas, atraso e status final nos relatórios do runner.

## Conexões
- [[kotest-nomes-estaveis-para-linhas-de-dados]] — Veja também: Kotest 6.2: tornar nomes de casos de dados estáveis e legíveis.
- [[kotest-shared-test-config-com-defaults-locais]] — Veja também: Kotest 6.2: centralizar defaults sem impedir ajustes por caso.

## Fontes
- [Kotest 6.2 — Shared Test Config](https://kotest.io/docs/framework/sharedtestconfig.html) — defaults de teste, timeout, retry e precedência local; consultado em 2026-10-02.
- [Kotest 6.2 — Test Case Config](https://kotest.io/docs/framework/testcaseconfig.html) — tags, retries, extensões e configuração de caso; consultado em 2026-10-02.
