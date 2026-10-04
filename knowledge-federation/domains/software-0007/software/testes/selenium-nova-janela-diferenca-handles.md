---
id: software.testes.tranche10.000356
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
fontes: ["https://www.selenium.dev/documentation/webdriver/interactions/windows/", "https://www.selenium.dev/documentation/webdriver/waits/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: identificar a nova janela pelo handle

## Em uma frase
WebDriver representa janelas e abas por handles únicos dentro da sessão e não distingue conceitualmente as duas formas.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. Assumir que a nova janela sempre estará no índice seguinte da lista torna o teste dependente da ordem do retorno.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Guarde o handle original, aguarde a quantidade esperada e encontre o handle que não existia antes.

## Exemplo
Após clicar em abrir recibo, o teste espera duas janelas, calcula a diferença de handles e valida o título da nova aba.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. Fechar a aba atual não retorna automaticamente o foco à original; faça a troca de volta de forma explícita.

## Como verificar
Execute o fluxo repetidamente e valide tanto o conteúdo da nova janela quanto a restauração e o encerramento dos handles.

## Conexões
- [[selenium-frame-trocar-e-restaurar-contexto]] — Veja também: Selenium: trocar para o frame antes de interagir.
- [[selenium-alert-wait-accept-dismiss]] — Veja também: Selenium: aguardar e tratar alertas JavaScript nativos.

## Fontes
- [Selenium — Windows and tabs](https://www.selenium.dev/documentation/webdriver/interactions/windows/) — handles, troca, criação e fechamento de janelas/abas; consultado em 2026-10-02.
- [Selenium — Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/) — condições de espera, readiness e a advertência sobre combinar esperas implícitas e explícitas; consultado em 2026-10-02.
