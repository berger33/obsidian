---
id: software.testes.tranche17.001103
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

# Selenium: registrar evidências de falha

## Em uma frase
O driver permite capturar imagens da tela, e a captura costuma ser associada a ganchos que gravam artefato apenas quando o teste falha.

## Por que importa
Evidência visual acelera a análise de falha em integração contínua e reduz a necessidade de reproduzir o cenário localmente.

## Como funciona
Capture no gancho de falha, salve com nome que identifique o caso e publique o diretório como artefato do trabalho.

## Exemplo
Uma captura no momento da falha mostra o estado da página e a mensagem exibida, indicando se o problema é de dado ou de interface.

## Limites e trade-offs
Imagens podem conter informações sensíveis do ambiente, e o volume cresce rapidamente quando todas as execuções são preservadas.

## Como verificar
Provoque uma falha controlada e confirme que a imagem foi gravada e que o artefato do pipeline contém o arquivo correspondente.

## Conexões
- [[selenium-browser-options]] — Veja também: Selenium: configurar opções do navegador.
- [[selenium-flakiness-diagnosis]] — Veja também: Selenium: diagnosticar instabilidade.

## Fontes
- [Selenium — Page object models](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/) — objetos de página e de componente e boas práticas de estruturação; consultado em 2026-10-03.
- [Selenium — repositório oficial](https://github.com/SeleniumHQ/selenium) — código-fonte e documentação das ligações por linguagem; consultado em 2026-10-03.
