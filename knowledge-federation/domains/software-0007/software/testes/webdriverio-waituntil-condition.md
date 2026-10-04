---
id: software.testes.tranche13.000671
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
fontes: ["https://webdriver.io/docs/api/browser/waitUntil/", "https://webdriver.io/docs/timeouts"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# WebdriverIO: modelar condição temporal com waitUntil

## Em uma frase
`browser.waitUntil()` consulta uma condição até que ela retorne valor truthy ou ultrapasse o timeout configurado.

## Por que importa
Uma espera por condição representa um estado observável da aplicação melhor que um `sleep` que presume quanto tempo o sistema precisa.

## Como funciona
Defina condição idempotente, limite de duração, intervalo entre verificações e mensagem de timeout com contexto que ajude a explicar o estado final.

## Exemplo
Após salvar um perfil, o teste pode aguardar que o texto exibido mude para o nome confirmado pelo servidor.

## Limites e trade-offs
A condição pode rodar repetidamente; não coloque nela uma ação que cria novos registros ou dispara efeitos a cada polling.

## Como verificar
Faça a condição tornar-se verdadeira no tempo limite e depois nunca verdadeira; confira retorno booleano e mensagem no segundo caso.

## Conexões
- [[webdriverio-auto-wait-interactable]] — Veja também: WebdriverIO: confiar no auto-wait para interação.
- [[webdriverio-wait-displayed-state]] — Veja também: WebdriverIO: esperar visibilidade sem presumir presença.

## Fontes
- [WebdriverIO — browser.waitUntil](https://webdriver.io/docs/api/browser/waitUntil/) — truthy condition polling, timeout, interval and timeout messages; consultado em 2026-10-02.
- [WebdriverIO — Timeouts](https://webdriver.io/docs/timeouts) — framework, implicit, script and command timeout types; consultado em 2026-10-02.
