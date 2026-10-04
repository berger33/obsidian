---
id: software.testes.tranche17.001099
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://www.selenium.dev/documentation/webdriver/actions_api/", "https://github.com/SeleniumHQ/selenium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: executar interações complexas

## Em uma frase
A interface de ações permite encadear movimento do ponteiro, cliques, arrasto, digitação e combinações de teclas, liberando o conjunto de uma vez.

## Por que importa
Interações compostas com arrasto e atalhos não são reproduzíveis por cliques simples e exigem sequência coordenada de eventos.

## Como funciona
Monte a sequência com as ações necessárias, libere a execução e aguarde o efeito observável antes das verificações seguintes.

## Exemplo
Mover um cartão entre colunas pode exigir arrastar com pausa intermediária e soltar sobre o alvo correto.

## Limites e trade-offs
Ações dependem de o elemento estar visível e posicionado, e coordenadas fixas quebram quando o layout muda de largura.

## Como verificar
Repita a ação em duas resoluções diferentes e confirme que o efeito independe da posição absoluta do elemento.

## Conexões
- [[selenium-page-objects]] — Veja também: Selenium: encapsular páginas e componentes.
- [[selenium-frames-windows-alerts]] — Veja também: Selenium: alternar entre contextos.

## Fontes
- [Selenium — Actions API](https://www.selenium.dev/documentation/webdriver/actions_api/) — sequências de ponteiro, teclado, arrasto e liberação das ações; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
