---
id: software.testes.tranche10.000352
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
fontes: ["https://www.selenium.dev/documentation/webdriver/elements/locators/", "https://www.selenium.dev/documentation/webdriver/elements/interactions/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: preferir locators únicos e estáveis

## Em uma frase
Locators traduzem uma propriedade observável do DOM em um alvo para interações WebDriver.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. Seletores frágeis acoplados à estrutura visual mudam com refatorações sem que o comportamento testado tenha regredido.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Prefira um identificador único e previsível quando disponível; na ausência dele, use CSS ou outro locator que represente claramente o elemento.

## Exemplo
Um formulário usa data-test ou id estável para localizar o campo de e-mail em vez de depender do terceiro div aninhado.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. Um locator correto não garante que o elemento esteja visível, habilitado ou disponível no contexto atual.

## Como verificar
Confirme unicidade do locator, revise mudanças de DOM e falhe com diagnóstico claro quando nenhum ou mais de um alvo for encontrado.

## Conexões
- [[selenium-nao-misturar-esperas-implicit-explicit]] — Veja também: Selenium: não misturar implicit waits e explicit waits.
- [[selenium-findelement-find-elements-ausencia]] — Veja também: Selenium: distinguir busca singular de busca plural.

## Fontes
- [Selenium — Locator strategies](https://www.selenium.dev/documentation/webdriver/elements/locators/) — estratégias de localização e seleção de elementos; consultado em 2026-10-02.
- [Selenium — Element interactions](https://www.selenium.dev/documentation/webdriver/elements/interactions/) — comandos de interação e condições de interatividade de elementos; consultado em 2026-10-02.
