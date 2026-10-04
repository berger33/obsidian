---
id: software.testes.tranche10.000357
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
fontes: ["https://www.selenium.dev/documentation/webdriver/interactions/alerts/", "https://www.selenium.dev/documentation/webdriver/waits/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: aguardar e tratar alertas JavaScript nativos

## Em uma frase
WebDriver expõe alertas, confirmações e prompts nativos por uma API específica após selecionar o alerta ativo.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. Um alerta modal interrompe interações normais da página e uma leitura feita antes de sua presença pode falhar.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Aguarde alertIsPresent, leia o texto e escolha accept ou dismiss; prompts também permitem enviar entrada antes de aceitar.

## Exemplo
Ao confirmar a exclusão, o teste valida a mensagem, escolhe dismiss no cenário de cancelamento e verifica que o item continua na lista.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. O alerta nativo é distinto de um modal HTML estilizado pela aplicação, que deve ser localizado no DOM.

## Como verificar
Cubra aceitação, rejeição e prompt com estado final observável e não deixe um alerta aberto contaminar o próximo caso.

## Conexões
- [[selenium-nova-janela-diferenca-handles]] — Veja também: Selenium: identificar a nova janela pelo handle.
- [[selenium-actions-sequencia-e-liberacao-input]] — Veja também: Selenium Actions API: compor ações e liberar o estado de entrada.

## Fontes
- [Selenium — JavaScript alerts, prompts and confirmations](https://www.selenium.dev/documentation/webdriver/interactions/alerts/) — espera, leitura, entrada, aceitação e rejeição de alertas nativos; consultado em 2026-10-02.
- [Selenium — Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/) — condições de espera, readiness e a advertência sobre combinar esperas implícitas e explícitas; consultado em 2026-10-02.
