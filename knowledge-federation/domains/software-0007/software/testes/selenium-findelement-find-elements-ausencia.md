---
id: software.testes.tranche10.000353
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
fontes: ["https://www.selenium.dev/documentation/webdriver/elements/locators/", "https://www.selenium.dev/documentation/webdriver/elements/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: distinguir busca singular de busca plural

## Em uma frase
findElement retorna um elemento correspondente e sinaliza ausência; findElements retorna uma lista, que pode estar vazia.

## Por que importa
Aplicações web mudam assincronamente; testes confiáveis precisam sincronizar o WebDriver com estado e contexto reais da página, não com uma duração presumida. Tratar uma lista vazia como erro de transporte confunde uma condição válida de interface com uma falha do driver.

## Como funciona
Use locators que expressem o alvo, uma condição observável e a troca explícita de contexto quando a interação sai do documento atual. Use busca singular quando a presença for pré-condição; use busca plural quando zero resultados fizer parte do estado esperado.

## Exemplo
Uma página sem avisos de validação verifica que a lista de alertas está vazia, enquanto o botão principal é buscado singularmente.

## Limites e trade-offs
A automação do browser não controla toda causa externa, e uma condição técnica satisfeita não garante que o fluxo de produto esteja correto. Uma busca plural vazia não explica por si só se o seletor está correto ou se a página ainda está carregando.

## Como verificar
Teste os estados com e sem resultados e valide o locator contra o DOM esperado para evitar sucesso por seletor incorreto.

## Conexões
- [[selenium-locators-identidade-estavel]] — Veja também: Selenium: preferir locators únicos e estáveis.
- [[selenium-stale-element-relocalizar-apos-render]] — Veja também: Selenium: relocalizar elementos após uma nova renderização.

## Fontes
- [Selenium — Locator strategies](https://www.selenium.dev/documentation/webdriver/elements/locators/) — estratégias de localização e seleção de elementos; consultado em 2026-10-02.
- [Selenium — Web elements](https://www.selenium.dev/documentation/webdriver/elements/) — busca, referência e comportamento de elementos WebDriver; consultado em 2026-10-02.
