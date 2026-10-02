---
id: software.testes.tranche08.000156
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/network", "https://playwright.dev/docs/test-assertions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: distinguir erro HTTP de falha de transporte

## Em uma frase
Teste separadamente respostas HTTP de erro e falhas de transporte, pois elas representam caminhos diferentes para o cliente.

## Por que importa
Um status 500 é uma resposta recebida; timeout ou conexão recusada não trazem resposta HTTP e podem acionar tratamento distinto na aplicação.

## Como funciona
Use mocks separados para fulfill com status de erro e para abortar uma requisição. Observe o estado final apresentado ao usuário e evite depender apenas de eventos de rede.

## Exemplo
Uma linha cobre serviço que retorna 503 com código de erro; outra aborta a conexão e verifica mensagem de indisponibilidade sem assumir que houve status.

## Limites e trade-offs
Mocks demonstram o contrato do cliente, não reproduzem a causa física de uma queda ou a política de retry do balanceador real.

## Como verificar
Confirme no trace se houve resposta ou erro de request, e valide ambos os estados com assertions web-first sobre o comportamento observável.

## Conexões
- [[playwright-retries-flaky-diagnostico]] — Veja também: Playwright: retries como sinal de flakiness, não correção.
- [[playwright-mock-api-contrato-resposta]] — Veja também: Playwright: mocks de API alinhados ao contrato.

## Fontes
- [Playwright — Network](https://playwright.dev/docs/network) — interceptação, observação e alteração controlada de tráfego; consultado em 2026-10-02.
- [Playwright — Assertions](https://playwright.dev/docs/test-assertions) — expect web-first e estabilização de assertions; consultado em 2026-10-02.
