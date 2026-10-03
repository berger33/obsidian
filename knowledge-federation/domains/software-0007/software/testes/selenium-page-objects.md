---
id: software.testes.tranche17.001098
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
fontes: ["https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/", "https://github.com/SeleniumHQ/selenium"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Selenium: encapsular páginas e componentes

## Em uma frase
Um objeto de página expõe serviços da tela por métodos, escondendo localizadores e devolvendo outros objetos de página ou valores de negócio.

## Por que importa
Testes que espalham localizadores por todo o código quebram em vários pontos quando a interface muda, e o objeto de página concentra essa manutenção.

## Como funciona
Modele cada tela ou componente com uma classe, mantenha localizadores privados e faça os métodos representarem o que a pessoa usuária pode fazer.

## Exemplo
Um objeto de listagem pode devolver os produtos encontrados e um método de busca que retorna a tela de detalhe.

## Limites e trade-offs
Objetos que expõem elementos brutos perdem a proteção, e asserções dentro do objeto misturam responsabilidades com o teste.

## Como verificar
Renomeie um localizador dentro do objeto e confirme que nenhum arquivo de teste precisou ser alterado.

## Conexões
- [[selenium-explicit-waits]] — Veja também: Selenium: esperar condições com limite.
- [[selenium-actions-api]] — Veja também: Selenium: executar interações complexas.

## Fontes
- [Selenium — Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) — objetos de página e de componente e boas práticas de estruturação; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
