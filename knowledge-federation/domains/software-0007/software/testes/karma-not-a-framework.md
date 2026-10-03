---
id: software.testes.tranche23.001662
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/karma-runner/karma/blob/master/README.md", "https://karma-runner.github.io/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karma não é framework de teste nem biblioteca de asserção

## Em uma frase
A doc oficial esclarece um equívoco comum: "Karma is not a testing framework, nor an assertion library"; ele apenas lança o servidor HTTP e gera o test runner HTML, deixando a definição de casos para o framework que você escolher.

## Por que importa
Como o runner é agnóstico, a equipe não precisa trocar de linguagem de teste para trocar de executor de navegador; Jasmine, Mocha e QUnit continuam válidos como camadas de caso de teste.

## Como funciona
O encaixe acontece via plugins adaptadores publicados no npm: karma-jasmine, karma-mocha e karma-qunit são os oficiais citados no README, e a busca por keyword karma-adapter revela muitos outros; sem adaptador para o seu framework, o README incentiva escrever um.

## Exemplo
Configure frameworks: [jasmine] no arquivo de configuração e instale karma-jasmine; o Karma cuida de empacotar os arquivos e coletar resultados no navegador, sem introduzir uma nova API de asserção.

## Limites e trade-offs
Escrever um adaptador próprio é descrito como "not that hard" pelo mantenedor, mas é trabalho de plugin com contrato interno — não é a integração trivial que a lista de opções sugere.

## Como verificar
Compare a seção "But I still want to use _insert testing library_" do README com a lista de links de adaptadores e confirme que o Karma delega asserções ao framework escolhido.

## Conexões
- [[karma-deprecated-officially]] — Veja também: Karma está descontinuado: só correções de segurança.
- [[karma-init-wizard]] — Veja também: karma init: um assistente que escreve o arquivo de configuração.

## Fontes
- [Karma — README oficial](https://github.com/karma-runner/karma/blob/master/README.md) — proposta, descontinuação, adaptadores e quando usar; consultado em 2026-10-03.
- [Karma — página inicial da documentação](https://karma-runner.github.io/latest/index.html) — destaques: real devices, remote control, frameworks, CI; consultado em 2026-10-03.
