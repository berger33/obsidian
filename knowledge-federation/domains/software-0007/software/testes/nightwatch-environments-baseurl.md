---
id: software.testes.tranche21.001463
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
fontes: ["https://nightwatchjs.org/guide/reference/settings.html", "https://nightwatchjs.org/guide/concepts/test-environments.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: baseUrl por ambiente

## Em uma frase
A propriedade baseUrl (também grafada base_url, launch_url ou launchUrl) fica disponível na API do teste e assume o valor do ambiente selecionado na execução.

## Por que importa
Sem baseUrl, cada teste precisaria conhecer o endereço exato do sistema sob teste, o que trava a suíte contra um único servidor.

## Como funciona
Declare o endereço de cada ambiente na configuração e navegue com browser.url(browser.baseUrl) em vez de hardcodar o host dentro do teste.

## Exemplo
Rodar com --env integration aponta o baseUrl para o servidor de homologação enquanto os mesmos arquivos de teste continuam intocados.

## Limites e trade-offs
Um baseUrl fixo local escondido em constantes de teste quebra a esteira assim que a suíte roda fora da máquina do autor.

## Como verificar
Imprima o baseUrl em dois ambientes diferentes e confirme que os valores acompanham a configuração de cada um.

## Conexões
- [[nightwatch-settings-basics]] — Veja também: Nightwatch: organização da configuração.
- [[nightwatch-capabilities-desired]] — Veja também: Nightwatch: desiredCapabilities e sessões.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — Ambientes de teste](https://nightwatchjs.org/guide/concepts/test-environments.html) — herança entre ambientes, baseUrl e globals; consultado em 2026-10-03.
