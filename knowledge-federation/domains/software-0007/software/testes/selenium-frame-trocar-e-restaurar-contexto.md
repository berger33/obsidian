---
id: software.testes.tranche10.000355
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
fontes: ["https://www.selenium.dev/documentation/webdriver/interactions/frames/", "https://www.selenium.dev/documentation/webdriver/waits/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: trocar para o frame antes de interagir

## Em uma frase
O driver procura elementos no contexto de navegação atualmente selecionado; conteúdo em iframe requer troca explícita para o frame.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. Uma busca feita a partir do documento superior pode não localizar elementos que existem apenas no documento incorporado.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Espere o frame ficar disponível, selecione-o, execute as interações necessárias e retorne ao contexto pai ou padrão quando apropriado.

## Exemplo
O teste aguarda e seleciona o iframe de pagamento, confirma um rótulo interno e volta ao documento principal antes de validar a confirmação.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. A troca de contexto não autentica o usuário nem elimina diferenças de origem, políticas do browser ou carregamento tardio.

## Como verificar
Execute uma busca antes e depois da troca e verifique explicitamente em qual contexto cada elemento está disponível.

## Conexões
- [[selenium-stale-element-relocalizar-apos-render]] — Veja também: Selenium: relocalizar elementos após uma nova renderização.
- [[selenium-nova-janela-diferenca-handles]] — Veja também: Selenium: identificar a nova janela pelo handle.

## Fontes
- [Selenium — Frames](https://www.selenium.dev/documentation/webdriver/interactions/frames/) — seleção e troca de contexto entre documento e frames; consultado em 2026-10-02.
- [Selenium — Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/) — condições de espera, readiness e a advertência sobre combinar esperas implícitas e explícitas; consultado em 2026-10-02.
