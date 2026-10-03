---
id: software.testes.tranche21.001464
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: desiredCapabilities e sessões

## Em uma frase
O objeto desiredCapabilities (ou capabilities) define as capacidades da sessão WebDriver, como o nome do navegador e opções de toleração de certificados.

## Por que importa
As capacidades são a interface oficial do W3C para negociar o comportamento da sessão, e centralizá-las por ambiente evita surpresas entre máquinas.

## Como funciona
Declare browserName e demais capacidades no ambiente; desde a v2.0 é possível passar um objeto de Capabilities do Selenium ou uma função que o construa.

## Exemplo
O ambiente pode retornar firefox.Options com uma extensão adicionada, e o Nightwatch usará o objeto como capacidades da sessão.

## Limites e trade-offs
Capacidades incompatíveis com o driver instalado derrubam a sessão antes do primeiro comando; nem toda opção do navegador tem equivalente padronizado.

## Como verificar
Force uma capacidade inválida e confirme que a falha de sessão aparece antes de qualquer passo do teste executar.

## Conexões
- [[nightwatch-environments-baseurl]] — Veja também: Nightwatch: baseUrl por ambiente.
- [[nightwatch-page-objects-path]] — Veja também: Nightwatch: página de objetos pelo caminho.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
