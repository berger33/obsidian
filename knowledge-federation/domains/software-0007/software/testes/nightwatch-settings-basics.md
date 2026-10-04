---
id: software.testes.tranche21.001462
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

# Nightwatch: organização da configuração

## Em uma frase
A configuração central do Nightwatch define src_folders para localizar os testes, test_settings para declarar ambientes e os objetos webdriver ou selenium para o transporte.

## Por que importa
Um único arquivo governa onde estão os testes, contra qual navegador cada ambiente roda e quais opções de sessão serão usadas, o que facilita a revisão em code review.

## Como funciona
Mantenha um ambiente default obrigatório e herde dele as variações, trocando apenas o que muda entre ambientes; escolha webdriver direto ou selenium conforme o destino.

## Exemplo
O ambiente default aponta para Chrome local, e um ambiente edge redefine apenas o navegador e o servidor de teste remoto.

## Limites e trade-offs
Ambientes que divergem do default por cópia inteira da configuração multiplicam a manutenção; a herança parcial existe para evitar isso.

## Como verificar
Alterne entre dois ambientes com --env e confirme que só as opções redefinidas mudam em relação ao default.

## Conexões
- [[nightwatch-browser-drivers]] — Veja também: Nightwatch: drivers por navegador.
- [[nightwatch-environments-baseurl]] — Veja também: Nightwatch: baseUrl por ambiente.

## Fontes
- [Nightwatch — Referência de Config Settings](https://nightwatchjs.org/guide/reference/settings.html) — chaves de configuração, ambientes, runner, workers e capturas; consultado em 2026-10-03.
- [Nightwatch — Ambientes de teste](https://nightwatchjs.org/guide/concepts/test-environments.html) — herança entre ambientes, baseUrl e globals; consultado em 2026-10-03.
