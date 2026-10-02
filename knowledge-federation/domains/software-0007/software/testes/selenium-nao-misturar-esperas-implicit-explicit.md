---
id: software.testes.tranche10.000351
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
fontes: ["https://www.selenium.dev/documentation/webdriver/waits/", "https://www.selenium.dev/documentation/webdriver/elements/locators/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: não misturar implicit waits e explicit waits

## Em uma frase
A espera implícita afeta buscas de elementos, enquanto a explícita aguarda uma condição específica definida pelo teste.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. A documentação alerta que combiná-las pode gerar tempos de espera imprevisíveis, especialmente quando uma condição explícita executa buscas repetidas.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Escolha um modelo de sincronização consistente e prefira waits explícitos para condições de interface que mudam dinamicamente.

## Exemplo
Configure a espera implícita como zero e aguarde explicitamente a visibilidade do botão que será acionado.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. A configuração global de timeout ainda precisa refletir o ambiente; remover a espera implícita não corrige uma condição mal escolhida.

## Como verificar
Inspecione a configuração de timeouts e execute a mesma espera sob diferentes latências para detectar soma inesperada de atrasos.

## Conexões
- [[selenium-explicit-wait-condicao-observavel]] — Veja também: Selenium: esperar a condição observável, não um intervalo fixo.
- [[selenium-locators-identidade-estavel]] — Veja também: Selenium: preferir locators únicos e estáveis.

## Fontes
- [Selenium — Waiting strategies](https://www.selenium.dev/documentation/webdriver/waits/) — condições de espera, readiness e a advertência sobre combinar esperas implícitas e explícitas; consultado em 2026-10-02.
- [Selenium — Locator strategies](https://www.selenium.dev/documentation/webdriver/elements/locators/) — estratégias de localização e seleção de elementos; consultado em 2026-10-02.
