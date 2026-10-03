---
id: software.testes.tranche21.001460
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
fontes: ["https://nightwatchjs.org/guide/overview/what-is-nightwatch.html", "https://github.com/nightwatchjs/nightwatch"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Nightwatch: um framework integrado de testes

## Em uma frase
O Nightwatch é um framework completo, escrito em Node.js, para testes de ponta a ponta de sites em vários navegadores, usando a API W3C WebDriver.

## Por que importa
Concentrar testes de navegador, de unidade de serviços Node.js e de integração HTTP em uma única CLI evita montar e manter uma colagem de bibliotecas separadas.

## Como funciona
Declare os navegadores-alvo, aponte o CLI para as pastas de teste e deixe o Nightwatch abrir a sessão WebDriver, executar cada comando e fechar a sessão ao terminar.

## Exemplo
Um mesmo projeto pode cobrir o fluxo de checkout no Chrome e Firefox, um serviço interno e a API REST que os alimenta, com um só runner.

## Limites e trade-offs
O escopo amplo não elimina a necessidade de uma estratégia de testes: testes de unidade rápidos ainda pertencem a ferramentas específicas do idioma.

## Como verificar
Execute um teste mínimo com npx nightwatch e confirme que a sessão abre, navega e termina sem configuração de servidor externo.

## Conexões
- [[nightwatch-browser-drivers]] — Veja também: Nightwatch: drivers por navegador.

## Fontes
- [Nightwatch — O que é o Nightwatch](https://nightwatchjs.org/guide/overview/what-is-nightwatch.html) — proposta, arquitetura WebDriver e navegadores suportados; consultado em 2026-10-03.
- [Nightwatch — repositório oficial](https://github.com/nightwatchjs/nightwatch) — código-fonte, releases e documentação do projeto; consultado em 2026-10-03.
