---
id: software.testes.tranche21.001461
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
fontes: ["https://nightwatchjs.org/guide/overview/what-is-nightwatch.html", "https://nightwatchjs.org/gettingstarted/installation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: drivers por navegador

## Em uma frase
O controle dos navegadores acontece por serviços que implementam o protocolo WebDriver: GeckoDriver, ChromeDriver, Microsoft Edge Driver e SafariDriver.

## Por que importa
Cada navegador mantém seu próprio driver, e o teste só é confiável se a versão do driver corresponder à do navegador instalado na máquina.

## Como funciona
Instale o driver do navegador-alvo antes de rodar os testes; no macOS, o SafariDriver já vem como binário do sistema e dispensa instalação avulsa.

## Exemplo
Para cobrir Firefox e Chrome, mantenha GeckoDriver e ChromeDriver atualizados junto com as versões dos navegadores no parque de CI.

## Limites e trade-offs
Drivers desatualizados geram erros de sessão que não têm nada a ver com a aplicação; o Safari depende de configuração no próprio sistema da Apple.

## Como verificar
Rode a mesma especificação em dois navegadores e confirme que as duas sessões abrem e concluem sem erro de protocolo.

## Conexões
- [[nightwatch-integrated-framework]] — Veja também: Nightwatch: um framework integrado de testes.
- [[nightwatch-settings-basics]] — Veja também: Nightwatch: organização da configuração.

## Fontes
- [Nightwatch — O que é o Nightwatch](https://nightwatchjs.org/guide/overview/what-is-nightwatch.html) — proposta, arquitetura WebDriver e navegadores suportados; consultado em 2026-10-03.
- [Nightwatch — Instalação](https://nightwatchjs.org/gettingstarted/installation/) — drivers por navegador e preparação do ambiente; consultado em 2026-10-03.
